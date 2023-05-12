================
常用的数据类型
================

数字
==========

**数字：整数、浮点数和复数等。** 例如：

.. code-block:: python3

    # 整数
    x = 42
    y = -13

    # 浮点数
    pi = 3.14
    e = 2.718

    # 复数
    z = 2 + 3j

字符串
=======

**由字符组成的序列。** 例如：

.. code-block:: python3

    # 单引号字符串
    s1 = 'Hello, world!'

    # 双引号字符串
    s2 = "Python is awesome!"

    # 三引号字符串
    s3 = '''This is a
    multi-line string.'''

列表
======

**由值组成的有序序列。** 例如：

.. code-block:: python3

    # 创建一个列表
    fruits = ['apple', 'banana', 'cherry']

    # 访问列表元素
    print(fruits[0])    # 输出'apple'
    print(fruits[1])    # 输出'banana'
    print(fruits[2])    # 输出'cherry'

    # 修改列表元素
    fruits[1] = 'orange'
    print(fruits)       # 输出['apple', 'orange', 'cherry']

元组
==========

**由值组成的有序序列，但是元组是不可变的。** 例如：

.. code-block:: python3

    # 创建一个元组
    colors = ('red', 'green', 'blue')

    # 访问元组元素
    print(colors[0])    # 输出'red'
    print(colors[1])    # 输出'green'
    print(colors[2])    # 输出'blue'

集合
==========

**由唯一值组成的无序集合。** 例如：

.. code-block:: python3

    # 创建一个集合
    numbers = {1, 2, 3, 4, 5}

    # 添加元素到集合
    numbers.add(6)
    print(numbers)      # 输出{1, 2, 3, 4, 5, 6}

    # 从集合中删除元素
    numbers.remove(3)
    print(numbers)      # 输出{1, 2, 4, 5, 6}


字典
=========

**由键值对组成的无序集合。** 例如：

.. code-block:: python3

    # 创建一个字典
    person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

    # 访问字典元素
    print(person['name'])    # 输出'Alice'
    print(person['age'])     # 输出25
    print(person['city'])    # 输出'New York'

    # 修改字典元素
    person['age'] = 26
    print(person)            # 输出{'name': 'Alice', 'age': 26, 'city': 'New York'}

布尔值
=========

**表示真或假的值。** 例如：

.. code-block:: python3

    # 创建一个布尔值
    x = True
    y = False

    # 使用布尔值进行逻辑运算
    print(x and y)    # 输出False
    print(x or y)     # 输出True
    print(not x)      # 输出False