#!/usr/bin/env python3
"""Update a Docker Hub repository's full description from a local README file."""

import argparse
import json
import re
import urllib.request

DOCKERHUB_API = "https://hub.docker.com/v2"
SHORT_DESC_MAX = 100


def _json_request(method: str, url: str, payload: dict, token: str | None = None) -> dict:
    data = json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def login(username: str, password: str) -> str:
    result = _json_request("POST", f"{DOCKERHUB_API}/users/login", {"username": username, "password": password})
    return result["token"]


def complete_urls(content: str, base_url: str) -> str:
    """Rewrite relative markdown image/link URLs to absolute ones."""
    base_url = base_url.rstrip("/")

    def make_absolute(match: re.Match) -> str:
        prefix, url, suffix = match.group(1), match.group(2), match.group(3)
        if re.match(r"https?://|#|mailto:", url):
            return match.group(0)
        return f"{prefix}{base_url}/{url.lstrip('/')}{suffix}"

    content = re.sub(r"(!?\[[^\]]*\]\()([^)]+)(\))", make_absolute, content)
    content = re.sub(r'((?:src|href)=")([^"]+)(")', make_absolute, content, flags=re.IGNORECASE)
    return content


def update_repo(token: str, repository: str, full_description: str, short_description: str | None) -> None:
    namespace, name = repository.split("/", 1)
    payload: dict = {"full_description": full_description}
    if short_description:
        payload["description"] = short_description[:SHORT_DESC_MAX]
    _json_request("PATCH", f"{DOCKERHUB_API}/repositories/{namespace}/{name}/", payload, token)


def main() -> None:
    parser = argparse.ArgumentParser(description="Push a README file to a Docker Hub repository description.")
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--repository", required=True, help="namespace/name")
    parser.add_argument("--readme-filepath", required=True)
    parser.add_argument("--short-description", default=None)
    parser.add_argument("--readme-base-url", default=None)
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
