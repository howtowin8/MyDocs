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


自定义类型：class 类
======================

根据您的查询，您似乎想了解如何在Python中创建一个包括属性和方法的类。实际上，
类是Python中的一个重要概念，用于 **创建对象和实现面向对象编程**。在类中， **属性是类的数据成员，而方法是类的函数成员**。

以下是一个使用类创建包括属性和方法的示例：

.. code-block:: python3

    # 定义一个名为Person的新类
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def say_hello(self):
            print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # 创建一个Person对象
    person1 = Person('Alice', 25)

    # 输出Person对象的属性
    print(person1.name)    # 输出'Alice'
    print(person1.age)     # 输出25

    # 调用Person对象的方法
    person1.say_hello()    # 输出'Hello, my name is Alice and I am 25 years old.'


在此示例中，我们首先使用class关键字创建一个名为Person的新类。然后，我们在类中定义一个名为 ``__init__()`` 的特殊方法，
该方法用于初始化新对象的属性。在 ``__init__()`` 方法中，我们使用self关键字引用新对象，并使用name和age参数填充对象的属性。
接下来，我们在类中定义一个名为 ``say_hello()`` 的方法，该方法用于输出对象的属性。
在 ``say_hello()`` 方法中，我们使用self关键字引用对象的属性，并使用 ``print()`` 函数输出一条包含属性的消息。
最后，我们使用 ``Person()`` 函数创建一个名为person1的新Person对象，并使用字符串 ``'Alice'`` 和整数25填充对象的属性。
最后，我们使用 ``print()`` 函数输出person1对象的属性，并使用 ``person1.say_hello()`` 调用对象的方法，以验证它们已成功创建。

基类
=======

根据您的查询，您似乎想了解Python中的基类。实际上，在Python中，基类是一个类，其他类可以从中继承属性和方法。

基类也称为 **超类或父类**。

以下是一个使用基类创建子类的示例：

.. code-block:: python3

    # 定义一个名为Animal的基类
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            raise NotImplementedError("Subclass must implement abstract method")

    # 定义一个名为Dog的子类
    class Dog(Animal):
        def speak(self):
            return "Woof!"

    # 定义一个名为Cat的子类
    class Cat(Animal):
        def speak(self):
            return "Meow!"

    # 创建一个Dog对象并调用其方法
    dog1 = Dog("Fido")
    print(dog1.name)      # 输出'Fido'
    print(dog1.speak())   # 输出'Woof!'

    # 创建一个Cat对象并调用其方法
    cat1 = Cat("Whiskers")
    print(cat1.name)      # 输出'Whiskers'
    print(cat1.speak())   # 输出'Meow!'

在此示例中，我们首先使用class关键字创建一个名为Animal的基类。

然后，我们在类中定义一个名为 ``__init__()`` 的特殊方法，该方法用于初始化新对象的属性。

在 ``__init__()`` 方法中，我们使用self关键字引用新对象，并使用name参数填充对象的属性。

接下来，我们在类中定义一个名为 ``speak()`` 的方法，该方法用于输出对象的声音。

在 ``speak()`` 方法中，我们使用 ``raise`` 语句引发一个名为 ``NotImplementedError`` 的异常，以确保子类实现该方法。

然后，我们使用class关键字创建一个名为Dog的子类，并将其继承自Animal基类。

在Dog子类中，我们重写了Animal基类的 ``speak()`` 方法，并返回字符串 ``'Woof!'`` 。

接下来，我们使用class关键字创建一个名为Cat的子类，并将其继承自Animal基类。

在Cat子类中，我们重写了Animal基类的 ``speak()`` 方法，并返回字符串 ``'Meow!'``。

最后，我们使用 ``Dog()`` 函数创建一个名为dog1的新Dog对象，并使用字符串'Fido'填充对象的属性。

然后，我们使用 ``print()``  函数输出dog1对象的属性，并使用 ``dog1.speak()`` 调用对象的方法，以验证它们已成功创建。

接下来，我们使用 ``Cat()`` 函数创建一个名为cat1的新Cat对象，并使用字符串 ``'Whiskers'`` 填充对象的属性。

然后，我们使用 ``print()`` 函数输出cat1对象的属性，并使用 ``cat1.speak()`` 调用对象的方法，以验证它们已成功创建。

ABC基类
======================

根据您的查询，您似乎想了解Python中的ABC基类。实际上，ABC（Abstract Base Class）是Python中的一个内置模块，用于创建抽象基类。

**抽象基类是一种特殊的类， 不能直接实例化，而是用于定义其他类的接口和行为。**

以下是一个使用ABC模块创建抽象基类的示例：

.. code-block:: python3

    from abc import ABC, abstractmethod

    # 定义一个名为Shape的抽象基类
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

    # 定义一个名为Rectangle的子类
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    # 创建一个Rectangle对象并调用其方法
    rect1 = Rectangle(5, 10)
    print(rect1.area())         # 输出50
    print(rect1.perimeter())    # 输出30

在此示例中，我们首先使用from关键字导入ABC和 ``abstractmethod`` 类。然后，我们使用 ``class`` 关键字创建一个名为 ``Shape`` 的抽象基类，并在类中定义两个抽象方法（ ``area()和perimeter()`` ）。

在每个抽象方法中，我们使用 **@abstractmethod装饰器** 将方法标记为抽象，并使用 ``pass`` 语句占位符来指示子类必须实现该方法。

接下来，我们使用 ``class`` 关键字创建一个名为Rectangle的子类，并将其继承自Shape抽象基类。

在Rectangle子类中，我们重写了Shape抽象基类的 ``area()和perimeter()`` 方法，并返回矩形的面积和周长。

最后，我们使用 ``Rectangle()`` 函数创建一个名为rect1的新Rectangle对象，并使用整数5和10填充对象的属性。

然后，我们使用 ``print()`` 函数输出rect1对象的属性，并使用 ``rect1.area()和rect1.perimeter()`` 调用对象的方法，以验证它们已成功创建。

