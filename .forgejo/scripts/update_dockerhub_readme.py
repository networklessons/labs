#!/usr/bin/env python3
"""Update a Docker Hub repository's full description from a local README file."""

import argparse
import re
import sys

import requests

DOCKERHUB_API = "https://hub.docker.com/v2"
SHORT_DESC_MAX = 100


def login(username: str, password: str) -> str:
    resp = requests.post(
        f"{DOCKERHUB_API}/users/login",
        json={"username": username, "password": password},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["token"]


def complete_urls(content: str, base_url: str) -> str:
    """Rewrite relative markdown image/link URLs to absolute ones."""
    base_url = base_url.rstrip("/")

    def make_absolute(match: re.Match) -> str:
        prefix, url, suffix = match.group(1), match.group(2), match.group(3)
        if re.match(r"https?://|#|mailto:", url):
            return match.group(0)
        return f"{prefix}{base_url}/{url.lstrip('/')}{suffix}"

    # ![alt](url) and [text](url)
    content = re.sub(r"(!?\[[^\]]*\]\()([^)]+)(\))", make_absolute, content)
    # <img src="url"> and <a href="url">
    content = re.sub(
        r'((?:src|href)=")([^"]+)(")',
        make_absolute,
        content,
        flags=re.IGNORECASE,
    )
    return content


def update_repo(
    token: str,
    repository: str,
    full_description: str,
    short_description: str | None,
) -> None:
    namespace, name = repository.split("/", 1)
    payload: dict = {"full_description": full_description}
    if short_description:
        payload["description"] = short_description[:SHORT_DESC_MAX]

    resp = requests.patch(
        f"{DOCKERHUB_API}/repositories/{namespace}/{name}/",
        headers={"Authorization": f"Bearer {token}"},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Push a README file to a Docker Hub repository description."
    )
    parser.add_argument("--username", required=True, help="Docker Hub username")
    parser.add_argument("--password", required=True, help="Docker Hub password or PAT")
    parser.add_argument(
        "--repository", required=True, help="Docker Hub repository (namespace/name)"
    )
    parser.add_argument("--readme-filepath", required=True, help="Path to README file")
    parser.add_argument("--short-description", default=None, help="Short description (max 100 chars)")
    parser.add_argument(
        "--readme-base-url",
        default=None,
        help="Base URL for resolving relative links (e.g. https://github.com/owner/repo/raw/main)",
    )
    args = parser.parse_args()

    with open(args.readme_filepath, encoding="utf-8") as fh:
        content = fh.read()

    if args.readme_base_url:
        content = complete_urls(content, args.readme_base_url)

    token = login(args.username, args.password)
    update_repo(token, args.repository, content, args.short_description)
    print(f"Updated Docker Hub description for {args.repository}")


if __name__ == "__main__":
    main()
