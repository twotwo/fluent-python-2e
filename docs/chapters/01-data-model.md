# 01. Python 数据模型

我们可以将数据模型视为对 Python 作为框架的描述。它规范了语言本身的构建块（例如序列、函数、迭代器、协程、类、上下文管理器等）的接口。

使用框架时，我们会花费大量时间编写由框架调用的方法。当我们利用 Python 数据模型构建新的类时，情况也是如此。Python 解释器会调用特殊方法来执行基本的对象操作，这通常由特殊的语法触发。这些特殊方法的名称始终以双下划线开头和结尾。例如，语法 `obj[key]` 由 `__getitem__` 特殊方法支持。为了实现 `my_collection[key]`，解释器会调用 `my_collection.__getitem__(key)`。

当我们希望我们的对象支持和与以下基本语言结构进行交互时，我们会实现特殊方法：

* 集合
* 属性访问 (Attribute access，类似 my_collection.key)
* 迭代 (包括使用async for进行异步迭代)
* 运算符重载
* 函数和方法调用
* 字符串表示和格式化
* 使用 await 进行异步编程
* 对象的创建和销毁 (Object creation and destruction)
* 使用 with 或 async with 语句进行管理的上下文

## 1.1 A Pythonic Card Deck

代码见 chapters/01-data-model/frenchdeck.py

    通过 实现 `__getitem__` 方法，让对象可被迭代；

    接着实现 `__len__` 方法，对象可用被排序；

    额外实现 `__getattr__` 方法，对象中字典实例可用通过属性方式调用：`assert deck[12] == deck.sa`

chapters/01-data-model/frenchdeck.doctest

    `python -m doctest <doctest file> -v` 或者在 pytest 中执行

    `pytest --doctest-modules <python file with doctest code>`

    ```python
    >>> for card in deck:  # doctest: +ELLIPSIS
    ...   print(card)
    Card(rank='2', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='spades')
    ...
    ```
