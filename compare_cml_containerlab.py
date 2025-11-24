#!/usr/bin/env python3
"""
Script to find CML labs that don't have containerlab equivalents.
Outputs a list showing:
- CML topology folder+file
- Suggested containerlab folder+file
"""

from pathlib import Path
from typing import Set, Dict, List, Tuple

# Base paths - relative to script location
SCRIPT_DIR = Path(__file__).parent
CML_BASE = SCRIPT_DIR / "cml"
CONTAINERLAB_BASE = SCRIPT_DIR / "containerlab" / "labs"


def normalize_name(name: str) -> str:
    """Normalize a topology name for comparison."""
    # Remove file extension
    name = name.replace('.yaml', '').replace('.clab.yml', '')
    # Convert to lowercase for case-insensitive comparison
    name = name.lower()
    # Remove common prefixes/suffixes that might differ
    name = name.replace('.virl', '')
    return name


def get_cml_topologies() -> Dict[str, List[Tuple[str, str]]]:
    """
    Get all CML topology files.
    Returns: dict mapping normalized name to list of (folder, filename) tuples
    Note: Some CML labs have duplicate names in different folders
    """
    topologies = {}
    
    for yaml_file in CML_BASE.rglob("*.yaml"):
        # Get relative path from CML_BASE
        rel_path = yaml_file.relative_to(CML_BASE)
        folder = str(rel_path.parent)
        filename = yaml_file.name
        
        # Normalize the name for comparison
        normalized = normalize_name(filename)
        
        # Handle duplicates by storing in a list
        if normalized not in topologies:
            topologies[normalized] = []
        topologies[normalized].append((folder, filename))
    
    return topologies


def get_containerlab_topologies() -> Set[str]:
    """
    Get all containerlab topology names (normalized).
    Returns: set of normalized topology names
    """
    topologies = set()
    
    for clab_file in CONTAINERLAB_BASE.rglob("*.clab.yml"):
        # Get the topology name (filename without .clab.yml)
        filename = clab_file.name
        normalized = normalize_name(filename)
        topologies.add(normalized)
    
    return topologies


def suggest_containerlab_path(cml_folder: str, cml_filename: str) -> str:
    """
    Suggest a containerlab path based on CML structure.
    """
    # Get the base filename without extension
    base_name = cml_filename.replace('.yaml', '').replace('.virl.yaml', '')
    
    # Convert folder name to lowercase for containerlab path
    # CML uses category folders like "BGP", "OSPF", etc.
    folder_lower = cml_folder.lower().replace(' ', '-')
    
    # Containerlab structure is: labs/category/cisco/topology-name/topology-name.clab.yml
    # For now, assume cisco vendor as most CML labs are Cisco
    suggested_path = f"labs/{folder_lower}/cisco/{base_name}/{base_name}.clab.yml"
    
    return suggested_path


def main():
    """Main function to compare and output results."""
    print("=" * 80)
    print("CML Labs without Containerlab Equivalents")
    print("=" * 80)
    print()
    
    # Get topologies
    cml_topologies = get_cml_topologies()
    containerlab_names = get_containerlab_topologies()
    
    # Calculate total CML files (including duplicates)
    total_cml_files = sum(len(topology_list) for topology_list in cml_topologies.values())
    
    # Find CML labs without containerlab equivalents
    missing_in_containerlab = []
    
    for normalized_name, topology_list in cml_topologies.items():
        if normalized_name not in containerlab_names:
            # Handle multiple CML files with the same normalized name
            for folder, filename in topology_list:
                cml_path = f"cml/{folder}/{filename}"
                suggested_clab_path = f"containerlab/{suggest_containerlab_path(folder, filename)}"
                missing_in_containerlab.append((cml_path, suggested_clab_path))
    
    # Sort by CML path
    missing_in_containerlab.sort(key=lambda x: x[0])
    
    # Print results
    print(f"Found {len(missing_in_containerlab)} CML labs without containerlab equivalents")
    print(f"(out of {total_cml_files} total CML lab files)")
    print()
    print("-" * 80)
    print(f"{'CML Topology':<50} {'Suggested Containerlab Path':<50}")
    print("-" * 80)
    
    for cml_path, suggested_clab_path in missing_in_containerlab:
        print(f"{cml_path:<50} {suggested_clab_path:<50}")
    
    print()
    print("=" * 80)
    print(f"Total: {len(missing_in_containerlab)} labs need containerlab versions")
    print("=" * 80)
    
    # Also save to a file for easier reference
    output_file = SCRIPT_DIR / "cml_without_containerlab.txt"
    with open(output_file, 'w') as f:
        f.write("CML Labs without Containerlab Equivalents\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Found {len(missing_in_containerlab)} CML labs without containerlab equivalents\n")
        f.write(f"(out of {total_cml_files} total CML lab files)\n\n")
        f.write("-" * 80 + "\n")
        f.write(f"{'CML Topology':<50} {'Suggested Containerlab Path':<50}\n")
        f.write("-" * 80 + "\n")
        
        for cml_path, suggested_clab_path in missing_in_containerlab:
            f.write(f"{cml_path:<50} {suggested_clab_path:<50}\n")
        
        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write(f"Total: {len(missing_in_containerlab)} labs need containerlab versions\n")
        f.write("=" * 80 + "\n")
    
    print(f"\nOutput also saved to: {output_file}")


if __name__ == "__main__":
    main()
