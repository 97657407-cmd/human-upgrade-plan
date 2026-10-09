#!/usr/bin/env python3
"""Read-only hygiene check for the public human-upgrade-plan package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ALLOWED_RELATIVE = {
    ".gitignore",
    "README.md",
    "skills/human-upgrade-plan/SKILL.md",
    "skills/human-upgrade-plan/agents/openai.yaml",
    "skills/human-upgrade-plan/assets/profile-template.md",
    "skills/human-upgrade-plan/assets/training-log-template.md",
    "skills/human-upgrade-plan/references/athlete-profile.md",
    "skills/human-upgrade-plan/references/decision-protocol.md",
    "skills/human-upgrade-plan/references/device-data.md",
    "skills/human-upgrade-plan/references/event-frameworks.md",
    "skills/human-upgrade-plan/references/output-patterns.md",
    "skills/human-upgrade-plan/references/recent-training.md",
    "skills/human-upgrade-plan/references/recovery-working-athletes.md",
    "skills/human-upgrade-plan/references/training-knowledge-system.md",
    "skills/human-upgrade-plan/references/wiki-maintenance.md",
    "skills/human-upgrade-plan/scripts/check_public.py",
}

# Evidence cards grow over time; allow any markdown under references/evidence/.
ALLOWED_PREFIXES = (
    "skills/human-upgrade-plan/references/evidence/",
)

BLANK_TEMPLATES = {
    "skills/human-upgrade-plan/assets/profile-template.md",
    "skills/human-upgrade-plan/assets/training-log-template.md",
}

DEFAULT_DENY_PATTERNS = [
    re.compile(r"/Users/[^\s)'\"`]+"),
    re.compile(r"/home/[^\s)'\"`]+"),
    re.compile(r"C:\\Users\\", re.I),
    re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    re.compile(r"(?<!\d)(?:\+?86[-\s]?)?1[3-9]\d{9}(?!\d)"),
]


def iter_files(root: Path) -> list[Path]:
    skip_dir_names = {".git", "__pycache__"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in skip_dir_names for part in path.parts):
            continue
        if path.is_file() and path.name != ".DS_Store":
            files.append(path)
    return sorted(files)


def check_whitelist(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    rels = {str(p.relative_to(root)).replace("\\", "/") for p in files}

    def allowed(rel: str) -> bool:
        if rel in ALLOWED_RELATIVE:
            return True
        return any(rel.startswith(prefix) and rel.endswith(".md") for prefix in ALLOWED_PREFIXES)

    unexpected = sorted(rel for rel in rels if not allowed(rel))
    missing = sorted(ALLOWED_RELATIVE - rels)
    for item in unexpected:
        errors.append(f"unexpected file: {item}")
    for item in missing:
        errors.append(f"missing required file: {item}")
    return errors


def check_blank_templates(root: Path) -> list[str]:
    errors: list[str] = []
    filled_markers = [
        re.compile(r"用户代号：[ \t]*\S"),
        re.compile(r"建档日期[^\n]*：[ \t]*\d"),
        re.compile(r"主目标[^\n]*：[ \t]*\S"),
    ]
    for rel in BLANK_TEMPLATES:
        text = (root / rel).read_text(encoding="utf-8")
        for pattern in filled_markers:
            if pattern.search(text):
                errors.append(f"template may contain filled data: {rel} ({pattern.pattern})")
    return errors


def check_skill_frontmatter(root: Path) -> list[str]:
    path = root / "skills/human-upgrade-plan/SKILL.md"
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        errors.append("SKILL.md frontmatter must start at byte 0")
        return errors
    closing = text.find("\n---", 4)
    if closing == -1:
        errors.append("SKILL.md frontmatter is not closed")
        return errors
    header = text[4:closing]
    for required in ("name:", "description:", "metadata:", "version:"):
        if required not in header:
            errors.append(f"SKILL.md frontmatter missing {required}")
    return errors


def extract_md_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)


def check_relative_links(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for link in extract_md_links(text):
            target = link.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"link escapes package root in {path.relative_to(root)}: {link}")
                continue
            if not resolved.exists():
                errors.append(f"broken relative link in {path.relative_to(root)}: {link}")
    return errors


def check_deny_terms(root: Path, files: list[Path], extra_terms: list[str]) -> list[str]:
    errors: list[str] = []
    patterns = list(DEFAULT_DENY_PATTERNS)
    for term in extra_terms:
        term = term.strip()
        if term:
            patterns.append(re.compile(re.escape(term)))
    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(root)).replace("\\", "/")
        if rel.endswith("scripts/check_public.py"):
            # Checker encodes deny patterns; skip self-scan.
            continue
        for pattern in patterns:
            for match in pattern.finditer(text):
                snippet = match.group(0)
                if snippet.startswith(("https://", "http://")):
                    continue
                errors.append(f"deny match in {rel}: {snippet}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="public package root")
    parser.add_argument(
        "--deny-term",
        action="append",
        default=[],
        help="extra identifying term; repeatable; do not commit personal terms",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"root is not a directory: {root}", file=sys.stderr)
        return 2

    files = iter_files(root)
    errors: list[str] = []
    errors.extend(check_whitelist(root, files))
    errors.extend(check_skill_frontmatter(root))
    errors.extend(check_blank_templates(root))
    errors.extend(check_relative_links(root, files))
    errors.extend(check_deny_terms(root, files, args.deny_term))

    if errors:
        print(f"check_public FAILED ({len(errors)} issue(s))")
        for item in errors:
            print(f"- {item}")
        return 1

    print(f"check_public OK ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
