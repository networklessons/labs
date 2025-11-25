#!/usr/bin/env python3

import os
import re

def count_labs(directory, extensions=('yaml', 'yml')):
    """Count lab files in a directory"""
    count = 0
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.endswith(f'.{ext}') for ext in extensions):
                    count += 1
    return count

def get_lab_stats(base_dir):
    """Get lab stats for a directory and its subdirectories"""
    stats = {}
    total = 0
    
    if os.path.exists(base_dir):
        for item in sorted(os.listdir(base_dir)):
            item_path = os.path.join(base_dir, item)
            if os.path.isdir(item_path):
                count = count_labs(item_path)
                if count > 0:
                    stats[item] = count
                    total += count
    
    return total, stats

def generate_markdown_table(title, total, stats):
    """Generate a markdown table for lab stats"""
    lines = [
        f"**Total {title}: {total}**",
        "",
        "| Category | Labs |",
        "|----------|------|"
    ]
    
    for category, count in sorted(stats.items()):
        lines.append(f"| {category} | {count} |")
    
    return "\n".join(lines)

def update_readme():
    """Update README.md with lab counts"""
    readme_path = "README.md"
    
    # Count CML labs
    cml_total = count_labs("cml")
    cml_direct_total, cml_stats = get_lab_stats("cml")
    
    # Count Containerlab labs
    containerlab_total = count_labs("containerlab")
    containerlab_direct_total, containerlab_stats = get_lab_stats(os.path.join("containerlab", "labs"))
    
    # Generate CML stats
    cml_content = generate_markdown_table("CML Labs", cml_total, cml_stats)
    cml_stats_block = f"<!-- CML_STATS_START -->\n{cml_content}\n<!-- CML_STATS_END -->"
    
    # Generate Containerlab stats
    containerlab_content = generate_markdown_table("Containerlab Labs", containerlab_total, containerlab_stats)
    containerlab_stats_block = f"<!-- CONTAINERLAB_STATS_START -->\n{containerlab_content}\n<!-- CONTAINERLAB_STATS_END -->"
    
    # Read README
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    # Replace CML stats block
    readme_content = re.sub(
        r'<!-- CML_STATS_START -->.*?<!-- CML_STATS_END -->',
        cml_stats_block,
        readme_content,
        flags=re.DOTALL
    )
    
    # Replace Containerlab stats block
    readme_content = re.sub(
        r'<!-- CONTAINERLAB_STATS_START -->.*?<!-- CONTAINERLAB_STATS_END -->',
        containerlab_stats_block,
        readme_content,
        flags=re.DOTALL
    )
    
    # Write README
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    print("README.md updated successfully")
    print(f"CML Labs: {cml_total}")
    print(f"Containerlab Labs: {containerlab_total}")

if __name__ == "__main__":
    update_readme()
