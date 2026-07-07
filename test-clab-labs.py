#!/usr/bin/env python3
"""
Script to test containerlab deployments from gns3vault-archive.

Workflow for each lab:
1. cd into the lab directory
2. sudo clab deploy -t <labfile>
3. Record success if exit code is 0
4. sudo clab destroy -t <labfile>
5. Repeat for next lab
"""

import os
import subprocess
import time
from pathlib import Path
from datetime import datetime

# Configuration
# The script runs from standard location, looking for gns3vault-archive subdir
REPO_ROOT = Path(".")
SEARCH_DIR = REPO_ROOT / "gns3vault-archive"
SUCCESS_FILE = REPO_ROOT / "successful_labs.txt"
FAILED_FILE = REPO_ROOT / "failed_labs.txt"
LOG_FILE = REPO_ROOT / "deployment_log.txt"

# ANSI color codes for better CLI output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def log_message(message, color=None, console_only=False):
    """Write message to log file and print to console with optional color."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    
    # Console output with color
    if color:
        print(f"{color}{log_entry}{Colors.ENDC}")
    else:
        print(log_entry)
    
    # File output (no color codes)
    if not console_only:
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry + '\n')

def print_separator(char="=", length=80, color=None):
    """Print a separator line."""
    line = char * length
    if color:
        print(f"{color}{line}{Colors.ENDC}")
    else:
        print(line)

def load_successful_labs():
    """Load the list of labs that have already been successfully deployed."""
    if SUCCESS_FILE.exists():
        with open(SUCCESS_FILE, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def load_failed_labs():
    """Load the dictionary of failed labs with their error messages."""
    failed_labs = {}
    if FAILED_FILE.exists():
        with open(FAILED_FILE, 'r') as f:
            current_lab = None
            for line in f:
                line = line.rstrip('\n')
                if line and not line.startswith('  '):  # Lab path
                    current_lab = line
                    failed_labs[current_lab] = []
                elif line.startswith('  ') and current_lab:  # Error detail
                    failed_labs[current_lab].append(line)
    return failed_labs

def save_successful_lab(lab_path_str):
    """Add a lab to the successful labs list."""
    with open(SUCCESS_FILE, 'a') as f:
        f.write(lab_path_str + '\n')

def save_failed_lab(lab_path_str, error_msg):
    """Add a lab to the failed labs list with error message."""
    with open(FAILED_FILE, 'a') as f:
        f.write(f"{lab_path_str}\n")
        f.write(f"  Error: {error_msg}\n")
        f.write(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

def remove_from_failed(lab_path_str):
    """Remove a lab from the failed labs file if it now succeeds."""
    if not FAILED_FILE.exists():
        return
    
    failed_labs = load_failed_labs()
    if lab_path_str in failed_labs:
        del failed_labs[lab_path_str]
        
        # Rewrite the file
        with open(FAILED_FILE, 'w') as f:
            for lab, errors in failed_labs.items():
                f.write(f"{lab}\n")
                for error in errors:
                    f.write(f"{error}\n")
                f.write("\n")

def find_clab_files():
    """Find all .clab.yml files in gns3vault-archive directory."""
    clab_files = []
    if not SEARCH_DIR.exists():
        log_message(f"ERROR: Directory '{SEARCH_DIR}' not found. Are you running this from the 'labs' root?", Colors.RED)
        return clab_files
    
    # Recursive search
    for clab_file in SEARCH_DIR.rglob("*.clab.yml"):
        clab_files.append(clab_file)
    
    return sorted(clab_files)

def run_destroy(filename, directory):
    """
    Runs clab destroy. 
    We pass the directory and only the filename to mimic running it from inside the folder.
    """
    log_message(f"      🧹 Cleaning up...", Colors.DIM, console_only=True)
    destroy_cmd = ["sudo", "clab", "destroy", "-t", filename]
    
    try:
        subprocess.run(
            destroy_cmd,
            cwd=str(directory),
            capture_output=True,
            text=True,
            timeout=120
        )
    except Exception as e:
        log_message(f"      ⚠️  Warning during cleanup: {str(e)[:100]}", Colors.YELLOW)

def test_lab(clab_file):
    """
    Orchestrates the deploy -> wait -> destroy cycle.
    Returns (success: bool, error_msg: str or None)
    """
    directory = clab_file.parent
    filename = clab_file.name
    
    log_message(f"      📂 Directory: {directory.relative_to(REPO_ROOT)}", Colors.DIM, console_only=True)

    # 1. DEPLOY
    deploy_cmd = ["sudo", "clab", "deploy", "-t", filename]
    
    deploy_success = False
    error_msg = None
    
    try:
        log_message(f"      🚀 Deploying...", Colors.CYAN, console_only=True)
        
        result = subprocess.run(
            deploy_cmd,
            cwd=str(directory),
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.returncode == 0:
            log_message(f"      ✅ Deploy successful!", Colors.GREEN, console_only=True)
            deploy_success = True
        else:
            # Extract meaningful error message
            err_output = result.stderr or result.stdout or "No error output captured"
            # Get last few lines of error
            error_lines = err_output.strip().split('\n')
            error_msg = ' | '.join(error_lines[-3:])  # Last 3 lines
            
            log_message(f"      ❌ Deploy failed!", Colors.RED, console_only=True)
            log_message(f"      Error: {error_msg[:200]}", Colors.RED)
            deploy_success = False

    except subprocess.TimeoutExpired:
        error_msg = "Deployment timeout (>10 minutes)"
        log_message(f"      ⏱️  {error_msg}", Colors.RED)
        deploy_success = False
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        log_message(f"      💥 {error_msg[:200]}", Colors.RED)
        deploy_success = False

    # 2. DESTROY
    run_destroy(filename, directory)
    
    return deploy_success, error_msg

def print_status_summary(total, skipped_success, remaining):
    """Print a nice status summary."""
    print()
    print_separator("─", color=Colors.CYAN)
    print(f"{Colors.BOLD}📊 Status Summary{Colors.ENDC}")
    print_separator("─", color=Colors.CYAN)
    print(f"  Total labs found:        {Colors.BOLD}{total}{Colors.ENDC}")
    print(f"  {Colors.GREEN}✓{Colors.ENDC} Previously successful:  {Colors.DIM}{skipped_success}{Colors.ENDC}")
    print(f"  {Colors.CYAN}▶{Colors.ENDC} Remaining to test:      {Colors.BOLD}{remaining}{Colors.ENDC}")
    print_separator("─", color=Colors.CYAN)
    print()

def main():
    print()
    print_separator("=", color=Colors.HEADER)
    print(f"{Colors.BOLD}{Colors.HEADER}🧪 Containerlab Sequential Deployment Tests{Colors.ENDC}")
    print_separator("=", color=Colors.HEADER)
    log_message(f"Search Path: {SEARCH_DIR}", Colors.BLUE)
    print_separator("=", color=Colors.HEADER)
    
    successful_labs = load_successful_labs()
    # No longer loading failed labs for skipping
    # failed_labs = load_failed_labs()
    clab_files = find_clab_files()
    
    total = len(clab_files)
    if total == 0:
        log_message("❌ No labs found.", Colors.RED)
        return

    skipped_success = 0
    passed = 0
    failed = 0
    
    # Filter out ONLY already successful labs (not failed ones)
    labs_to_test = []
    for clab_file in clab_files:
        clab_path_str = str(clab_file)
        if clab_path_str in successful_labs:
            skipped_success += 1
        else:
            # Test this lab regardless of whether it previously failed
            labs_to_test.append(clab_file)
    
    remaining = len(labs_to_test)
    
    # Print summary (removed skipped_failed parameter)
    print_status_summary(total, skipped_success, remaining)
    
    if remaining == 0:
        log_message("✨ All labs have been tested! Nothing to do.", Colors.GREEN)
        return
    
    # Test remaining labs
    for idx, clab_file in enumerate(labs_to_test, 1):
        clab_path_str = str(clab_file)
        
        print()
        print_separator("─", 80, Colors.BLUE)
        log_message(f"[{idx}/{remaining}] {Colors.BOLD}{clab_file.name}{Colors.ENDC}", Colors.BLUE, console_only=True)
        log_message(f"[{idx}/{remaining}] Testing: {clab_file.name}")
        print_separator("─", 80, Colors.BLUE)
        
        # Run the test
        success, error_msg = test_lab(clab_file)
        
        if success:
            save_successful_lab(clab_path_str)
            remove_from_failed(clab_path_str)  # Remove from failed if it was there
            passed += 1
            log_message(f"      ✅ {Colors.GREEN}PASSED{Colors.ENDC}", Colors.GREEN, console_only=True)
        else:
            save_failed_lab(clab_path_str, error_msg or "Unknown error")
            failed += 1
            log_message(f"      ❌ {Colors.RED}FAILED{Colors.ENDC}", Colors.RED, console_only=True)
        
        # Breathing room between labs
        time.sleep(1)

    # Final summary (removed skipped_failed)
    print()
    print_separator("=", color=Colors.HEADER)
    print(f"{Colors.BOLD}{Colors.HEADER}📋 Test Run Complete{Colors.ENDC}")
    print_separator("=", color=Colors.HEADER)
    print(f"  Total Found:     {total}")
    print(f"  {Colors.DIM}Skipped (Success): {skipped_success}{Colors.ENDC}")
    print(f"  {Colors.GREEN}✓ Passed:          {passed}{Colors.ENDC}")
    print(f"  {Colors.RED}✗ Failed:          {failed}{Colors.ENDC}")
    print_separator("=", color=Colors.HEADER)
    
    if failed > 0:
        print(f"\n{Colors.YELLOW}💡 Failed labs logged to: {FAILED_FILE}{Colors.ENDC}")
    if passed > 0:
        print(f"{Colors.GREEN}✨ Successful labs logged to: {SUCCESS_FILE}{Colors.ENDC}")
    print()

if __name__ == "__main__":
    main()
