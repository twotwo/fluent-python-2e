# 项目结构

## 运行环境

### Base line of Python & Poetry

```bash
$ python -V # pyenv shell 3.11.4
Python 3.11.4
$ poetry -V # python -m pip install --upgrade poetry
Poetry (version 1.6.1)
```

Use correct poetry version:

```bash
# use installed poetry version after poetry shell
$ cp `which poetry` `poetry env info -p`/bin
```

[Adds source configuration to the project](https://python-poetry.org/docs/cli/#source-add)

```bash
$ poetry source add pypi-aliyun https://mirrors.aliyun.com/pypi/simple
$ poetry source add --priority=explicit pypi
$ poetry source show
 name      : pypi-aliyun
 url       : https://mirrors.aliyun.com/pypi/simple
 priority  : primary                                

 name      : PyPI
 priority  : explicit
```

Add Dev Dependencies

```bash
# 添加开发依赖库
$ poetry add --group=dev pytest="^7.4" black="^23.9" pre-commit="^3.4" isort="^5.12" autoflake="^2.2" flake8-pyproject="^1.2" mypy="^1.5"
$ poetry show --tree
```

Run scripts

```bash
$ poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: fluent-python-2e (0.1.0)
$ poetry run cli
This is fluent-python-2e. Let's build some cool python apps!
```

## 目录结构
