===============
数据类型
===============

编程的过程中最主要的任务之一就是把数据进行分类，定义自己程序所需要的数据类型，然后根据数据类型进行数据处理。

自定义类型：namedtuple
=======================

根据您的查询，您似乎想了解Python中的namedtuple类型。实际上，namedtuple是Python中的一个内置类型，用于创建具有命名字段的元组。

非常适合我们从数据库中读取每一条记录。

以下是一个使用namedtuple类型的示例：

.. code-block:: python3

    from collections import namedtuple

    # 创建一个名为Person的新namedtuple类型
    Person = namedtuple('Person', ['name', 'age', 'gender'])

    # 创建一个Person对象
    person1 = Person('Alice', 25, 'female')

    # 输出Person对象的属性
    print(person1.name)    # 输出'Alice'
    print(person1.age)     # 输出25
    print(person1.gender)  # 输出'female'

在此示例中，我们首先使用namedtuple()函数创建一个名为Person的新namedtuple类型，该类型具有三个命名字段（name、age和gender）。

然后，我们使用Person()函数创建一个名为person1的新Person对象，并使用字符串'Alice'、整数25和字符串'female'填充对象的属性。

最后，我们使用print()函数输出person1对象的属性，以验证它们已成功填充。

自定义类型：enum(枚举)
===========================

根据您的查询，您似乎想了解Python中的enum类型。实际上，enum是Python中的一个内置模块，用于创建枚举类型。

适合一个字段有多个取值的情况，每一种值代表不一样的意思的适合。

以下是一个使用enum模块创建枚举类型的示例：

.. code-block:: python3

    from enum import Enum

    # 创建一个名为Color的新枚举类型
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    # 输出枚举类型的成员
    print(Color.RED)    # 输出'Color.RED'
    print(Color.GREEN)  # 输出'Color.GREEN'
    print(Color.BLUE)   # 输出'Color.BLUE'

    # 输出枚举类型的值
    print(Color.RED.value)    # 输出1
    print(Color.GREEN.value)  # 输出2
    print(Color.BLUE.value)   # 输出3

在此示例中，我们首先使用class关键字创建一个名为Color的新类，并将其继承自Enum类。

然后，我们在类中定义三个枚举成员（RED、GREEN和BLUE），并为每个成员分配一个唯一的值。

最后，我们使用print()函数输出枚举成员和它们的值，以验证它们已成功创建。