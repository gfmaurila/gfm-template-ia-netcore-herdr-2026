#!/usr/bin/env python3
"""Valida a integridade estrutural do template (documentacao e agentes).

Nao valida runtime de ferramentas: apenas arquivos, frontmatter, links,
adaptadores, JSON e YAML. Uso: python scripts/validate-template.py
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

ROLES = [
    "architect",
    "implementer",
    "tester",
    "reviewer",
    "security-reviewer",
    "devops",
    "docs-writer",
    "orchestrator",
]

SKILLS = [
    "spec-writing",
    "adr-writing",
    "task-decomposition",
    "dotnet-clean-architecture",
    "testcontainers-integration",
    "code-review",
    "security-review",
    "docker-compose-local",
    "github-actions-ci",
    "documentation-style",
    "herdr-orchestration",
]

REQUIRED = [
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    "prompts.md",
    "ai/registry.yaml",
    "ai/agents/README.md",
    "ai/rules/README.md",
    "ai/prompts/README.md",
    "ai/skills/README.md",
    "ai/workflows/README.md",
    "tasks/TASK-TEMPLATE.md",
    "templates/README.md",
    "governance/README.md",
    ".herdr/README.md",
    ".herdr/scripts/install-templates.ps1",
    ".opencode/opencode.json",
]

LINK_ROOTS = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "prompts.md",
    "ai",
    "templates",
    "tasks",
    "governance",
    "docs",
    ".herdr",
]

errors: list[str] = []
warnings: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def check_required() -> None:
    for item in REQUIRED:
        if not (ROOT / item).is_file():
            errors.append(f"arquivo obrigatorio ausente: {item}")


def check_agents() -> None:
    for role in ROLES:
        path = ROOT / "ai" / "agents" / f"{role}.md"
        if not path.is_file():
            errors.append(f"agente canonico ausente: {rel(path)}")
            continue
        meta = frontmatter(path.read_text(encoding="utf-8"))
        if not meta.get("name"):
            errors.append(f"frontmatter sem name: {rel(path)}")
        if not meta.get("role"):
            errors.append(f"frontmatter sem role: {rel(path)}")


def check_prompts() -> None:
    files = sorted((ROOT / "ai" / "prompts").glob("PRM-*@*.md"))
    if len(files) != 14:
        errors.append(f"prompts esperados=14 encontrados={len(files)}")
    for path in files:
        text = path.read_text(encoding="utf-8")
        if not re.match(r"PRM-\d{3}@\d+\.\d+\.\d+", path.name):
            errors.append(f"nome de prompt fora do padrao: {rel(path)}")
        if text.count("```") < 2:
            warnings.append(f"prompt sem bloco delimitado: {rel(path)}")


def check_skills() -> None:
    for skill in SKILLS:
        path = ROOT / "ai" / "skills" / skill / "SKILL.md"
        if not path.is_file():
            errors.append(f"skill ausente: {rel(path)}")
            continue
        meta = frontmatter(path.read_text(encoding="utf-8"))
        if meta.get("name") != skill:
            errors.append(f"skill name divergente: {rel(path)}")
        if not meta.get("description"):
            errors.append(f"skill sem description: {rel(path)}")
    for adapter in (".opencode/skills", ".claude/skills"):
        base = ROOT / adapter
        found = {p.name for p in base.iterdir() if p.is_dir()} if base.is_dir() else set()
        missing = set(SKILLS) - found
        extra = found - set(SKILLS)
        if missing:
            errors.append(f"{adapter} sem skills: {sorted(missing)}")
        if extra:
            warnings.append(f"{adapter} com skills extras: {sorted(extra)}")


def adapter_files(base: Path, suffix: str) -> set[str]:
    if not base.is_dir():
        return set()
    names = set()
    for path in base.glob(f"*{suffix}"):
        stem = path.name[: -len(suffix)]
        names.add(stem)
    return names


def check_adapters() -> None:
    expected = set(ROLES)
    checks = [
        (ROOT / ".opencode/agents", ".md", "opencode agents"),
        (ROOT / ".claude/agents", ".md", "claude agents"),
        (ROOT / ".codex/prompts", ".md", "codex prompts"),
        (ROOT / ".github/agents", ".agent.md", "copilot agents"),
    ]
    for base, suffix, label in checks:
        found = adapter_files(base, suffix)
        missing = expected - found
        if missing:
            errors.append(f"{label} sem papeis: {sorted(missing)}")


def check_herdr() -> None:
    base = ROOT / ".herdr" / "templates"
    files = sorted(base.glob("gfm-*.md"))
    if len(files) != len(ROLES):
        errors.append(f"templates herdr esperados={len(ROLES)} encontrados={len(files)}")
    for path in files:
        meta = frontmatter(path.read_text(encoding="utf-8"))
        if meta.get("name") != path.stem:
            errors.append(f"template herdr name divergente: {rel(path)}")
        if not meta.get("command"):
            errors.append(f"template herdr sem command: {rel(path)}")


def check_json() -> None:
    for path in ROOT.rglob("*.json"):
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"JSON invalido: {rel(path)}: {exc}")


def check_yaml() -> None:
    path = ROOT / "ai" / "registry.yaml"
    try:
        import yaml  # type: ignore
    except ImportError:
        if os.environ.get("REQUIRE_YAML") == "1":
            errors.append("PyYAML ausente e REQUIRE_YAML=1")
        else:
            warnings.append("PyYAML ausente: validacao de YAML ignorada")
        return
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"YAML invalido: {rel(path)}: {exc}")
        return
    if not isinstance(data, dict) or "roles" not in data:
        errors.append(f"registry.yaml sem chave roles: {rel(path)}")


def check_links() -> None:
    for item in LINK_ROOTS:
        base = ROOT / item
        paths = [base] if base.is_file() else sorted(base.rglob("*.md"))
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for match in re.finditer(r"\]\(([^)\s]+)\)", text):
                target = match.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = unquote(target.split("#", 1)[0])
                if not target:
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    errors.append(f"link quebrado: {rel(path)} -> {target}")


def main() -> int:
    check_required()
    check_agents()
    check_prompts()
    check_skills()
    check_adapters()
    check_herdr()
    check_json()
    check_yaml()
    check_links()

    for warning in warnings:
        print(f"AVISO: {warning}")
    for error in errors:
        print(f"ERRO: {error}")

    if errors:
        print(f"FALHOU: {len(errors)} erro(s), {len(warnings)} aviso(s)")
        return 1

    print(f"OK: validacao concluida ({len(warnings)} aviso(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
