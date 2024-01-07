set dotenv-load
python := env_var_or_default('PYTHON','python')

# 列出可用任务
@default:
    just --list

# 安装、升级依赖
bootstrap:
    {{ python }} -m pip install --upgrade ruamel.yaml

# 同步类别
sync-categories *ARGS:
    {{ python }} ./scripts/sync_categories.py ./projects.yaml ./.github/ISSUE_TEMPLATE/01_suggest-project.yml {{ ARGS }}

# 列出项目添加请求
list-project-suggestions:
    gh issue list --label add-project

# 从 issue 添加项目
add-project ISSUE_NUMBER:
    gh issue view {{ ISSUE_NUMBER }} --json body | {{ python }} ./scripts/add_project.py ./projects.yaml

# 用`README.md`构建可用于`pandoc --from gfm`的`build/index.md`
build-for-pandoc:
    #!/usr/bin/env bash
    set -euxo pipefail

    rm -rf build
    mkdir -p build
    cd build

    # Write metadata
    cat > index.md <<- "EOF"
    ---
    title: best-of-BITs (bytes)
    lang: zh-CN
    header-includes: |
        <style>
        details {
            margin-top: 1em;
        }
        li {
            margin-top: 0.2em;
        }
        .note {
            border-left: 0.25em solid #004daa;
            padding-left: 1em;
        }
        .note > .title {
            color: #004daa;
        }
        </style>
    ---
    EOF

    # Delete `<h1>` and unnecessary buttons
    cat ../README.md \
        | sed '1,5d' \
        | grep --invert-match '<a href="#contents">.* alt="Back to top"></a>' \
        >> index.md
