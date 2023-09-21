# fluent-python-2e

[流畅的 python](http://wiki.li3huo.com/book/Fluent_Python) 第二版读书笔记及示例代码

## 安装

本项目使用 `poetry` 进行依赖管理。更多 Poetry 帮助参见 [official docs](https://python-poetry.org/docs/#installation)。

1. Fork(如果尚不确定需要提交代码，请选择克隆)
2. Clone your new repository to your local computer

    ```bash
    git https://github.com/twotwo/fluent-python-2e.git
    cd fluent-python-2e
    ```

3. Install project depenencies.

    ```bash
    poetry install
    ```

4. Install pre-commit hooks

    ```bash
    poetry run pre-commit install
    ```

You are ready to rock.

## 使用

接下来可以阅读我的读书笔记或运行实力代码了。以下是一些可用的命令：

```bash
mkdocs serve --dirtyreload
```

查看更多文档。

```bash
poetry run cli
```

这是一个 poetry 的脚本化命令。

```bash
poetry run pytest
```

运行单元测试。

```bash
poetry run doctest
```

运行 doctest。
