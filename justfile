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
