#!/usr/bin/env python3

import os
import re


def extract_description(readme_path):
    """Extract the first meaningful description line from a README.md."""
    if not os.path.exists(readme_path):
        return ""

    standalone_link_re = re.compile(r"^\s*\[.*?\]\(.*?\)\s*$")

    with open(readme_path, "r") as f:
        for line in f:
            line = line.rstrip()
            # Skip empty lines
            if not line:
                continue
            # Skip headings
            if line.startswith("#"):
                continue
            # Skip blockquotes (warnings, notes)
            if line.startswith(">"):
                continue
            # Skip standalone markdown links
            if standalone_link_re.match(line):
                continue
            # Strip inline markdown links: [text](url) -> text
            line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
            # Strip bold/italic markers
            line = re.sub(r"\*+([^*]+)\*+", r"\1", line)
            # Strip trailing colon or period
            line = line.rstrip(":.")
            return line.strip()

    return ""


def get_containers(containers_dir):
    """Return sorted list of container folder names that contain a Dockerfile."""
    containers = []
    for entry in sorted(os.listdir(containers_dir)):
        entry_path = os.path.join(containers_dir, entry)
        if os.path.isdir(entry_path) and os.path.exists(
            os.path.join(entry_path, "Dockerfile")
        ):
            containers.append(entry)
    return containers


def generate_table(containers, containers_dir):
    """Generate the markdown table for all containers."""
    lines = [
        "| Container | Description | Docker Hub |",
        "|-----------|-------------|------------|",
    ]
    for name in containers:
        readme_path = os.path.join(containers_dir, name, "README.md")
        description = extract_description(readme_path)
        docker_hub_url = f"https://hub.docker.com/r/networklessons/{name}"
        lines.append(
            f"| [{name}]({name}/) | {description} | [networklessons/{name}]({docker_hub_url}) |"
        )
    return "\n".join(lines)


def update_readme(containers_dir):
    """Update containers/README.md with the auto-generated table."""
    readme_path = os.path.join(containers_dir, "README.md")

    containers = get_containers(containers_dir)
    table = generate_table(containers, containers_dir)

    new_block = f"<!-- CONTAINERS_TABLE_START -->\n{table}\n<!-- CONTAINERS_TABLE_END -->"

    with open(readme_path, "r") as f:
        content = f.read()

    start_marker = "<!-- CONTAINERS_TABLE_START -->"
    end_marker = "<!-- CONTAINERS_TABLE_END -->"

    if start_marker not in content or end_marker not in content:
        raise ValueError(
            f"Markers '{start_marker}' and '{end_marker}' not found in {readme_path}. "
            "Please add them to mark the auto-generated table section."
        )

    updated = re.sub(
        r"<!-- CONTAINERS_TABLE_START -->.*?<!-- CONTAINERS_TABLE_END -->",
        new_block,
        content,
        flags=re.DOTALL,
    )

    with open(readme_path, "w") as f:
        f.write(updated)

    print(f"containers/README.md updated with {len(containers)} container(s):")
    for name in containers:
        print(f"  - {name}")


if __name__ == "__main__":
    update_readme("containers")
