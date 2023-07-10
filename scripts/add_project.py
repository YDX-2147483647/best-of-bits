"""从 issue 添加项目

    python add_project.py --help
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlparse

from ruamel.yaml import YAML

if TYPE_CHECKING:
    from typing import Callable, TypeAlias


if TYPE_CHECKING:
    Transformer: TypeAlias = Callable[[str], dict[str, str]]
    """original_value ⇒ { key: value }
    
    `value`将直接出现在 YAML 中，后续不会转义，例如`{ "key": "123"}`会变成`key: 123`，值是数字。
    """


def url_to_id(url: str) -> dict[str, str]:
    u = urlparse(url.strip())
    match u.netloc:
        case "github.com" | "gitee.com":
            key = f"{u.netloc.removesuffix('.com')}_id"
            return {key: u.path.removeprefix("/").removesuffix("/")}
        case "greasyfork.org":
            m = re.match(R"^/scripts/(?P<id>\d+)-", u.path)
            assert m is not None, f"Fail to parse Greasy Fork URL path: {u.path}"
            return {"greasy_fork_id": m.group("id")}
        case _:
            raise Exception(f"Cannot recognize URL netloc “{u.netloc}”: {url}")


def build_transformers(project_yaml: str) -> dict[str, Transformer]:
    """
    @param project_yaml: content of `project.yaml`
    @return transformers: { original_key: original_value ⇒ { key: value} }
    """
    yaml = YAML(typ="safe")

    categories = yaml.load(project_yaml)["categories"]

    return {
        "名称": lambda v: {"name": v.strip()},
        "URL": url_to_id,
        # GitHub URL 已被替换为 URL，仅为兼容而保留，#45, #68, #70 全部解决后可删除
        "GitHub URL": lambda v: {
            "github_id": v.strip()
            .removeprefix("https://github.com/")
            .removesuffix("/"),
        },
        "类别": lambda v: {
            "category": next(c["category"] for c in categories if c["title"] == v)
        },
        "许可证": lambda v: {"license": v.strip()},
        "包管理器": lambda value: {
            f"{k}_id": str(v).strip() for k, v in yaml.load(value).items()
        },
    }


def parse_issue_body(body: str, transformers: dict[str, Transformer]) -> dict[str, str]:
    # 忽略补充信息
    body = body[: body.index("### 补充信息")]

    # 分段
    sections = body.removeprefix("### ").replace("\r\n", "\n").split("\n\n### ")
    pairs = (s.split("\n\n", maxsplit=1) for s in sections)

    # 转换
    project = {}
    for k, v in pairs:
        if v.strip() != "_No response_":
            project |= transformers[k](v)
    return project


def dump(project: dict[str, str], project_yaml: str) -> str:
    last_line = project_yaml.splitlines()[-1]
    tab = re.match(R"^(\s*)  ", last_line).group(1)
    return f"{tab}- " + f"\n{tab}  ".join(f"{k}: {v}" for k, v in project.items())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Append a project from stdin to project.yaml",
        epilog=f"""This script does not request GitHub API. Use it with GitHub CLI.

    gh issue view … --json body | python {__file__} ./project.yaml""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_yaml", type=Path, help="Path to project.yaml")
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    project_yaml_path: Path = args.project_yaml
    project_yaml = project_yaml_path.read_text(encoding="utf-8")

    project = parse_issue_body(
        body=json.loads(input())["body"],
        transformers=build_transformers(project_yaml),
    )

    patch = dump(project, project_yaml)
    print(patch)
    with project_yaml_path.open("a", encoding="utf-8") as f:
        f.write(f"\n{patch}\n")
