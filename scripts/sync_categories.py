"""同步类别

projects.yaml → .github/ISSUE_TEMPLATE/01_suggest-project.yml
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from typing import TYPE_CHECKING

from ruamel.yaml import YAML


if TYPE_CHECKING:
    from typing import Generator


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="同步类别",
        epilog="从 source 读取类别，替换 destination 中"
        "“# sync-categories: start”与“# sync-categories: end”之间的内容。",
    )
    parser.add_argument("source", type=Path, help="projects.yaml")
    parser.add_argument(
        "destination", type=Path, help=".github/ISSUE_TEMPLATE/01_suggest-project.yml"
    )
    return parser


def interlude(projects_yaml: dict, *, tab: str) -> Generator[str, None, None]:
    return (f"{tab}- {c['title']}" for c in projects_yaml["categories"])


def transform(issue_template: str, projects_yaml: dict) -> str:
    original_rows = issue_template.splitlines()

    rows = []
    in_interlude = False
    for r in original_rows:
        if not in_interlude and r.strip() == "# sync-categories: start":
            rows.append(r)

            tab = r[: r.index("#")]
            rows.extend(interlude(projects_yaml, tab=tab))
            in_interlude = True

        elif in_interlude and r.strip() == "# sync-categories: end":
            rows.append(r)
            in_interlude = False

        elif not in_interlude:
            rows.append(r)

    return "\n".join(rows)


if __name__ == "__main__":
    args = build_parser().parse_args()
    src: Path = args.source
    dst: Path = args.destination

    yaml = YAML(typ="safe")
    projects_yaml = yaml.load(src.read_text(encoding="utf-8"))
    issue_template = dst.read_text(encoding="utf-8")

    dst.write_text(transform(issue_template, projects_yaml), encoding="utf-8")
