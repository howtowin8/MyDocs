=====================
数据库数据的表现形式
=====================

表
============

可以把一个表的记录条数看作一个对象，把所有对象放进一个列表中，把一个表的主键看做一个字典的key,记录看做值。

每一种数据结构都有其最优的使用时机。

学生表的记录

=== ========== ========== ======== =============
ID  学号       姓名        年龄     性别
=== ========== ========== ======== =============
1   08L0900    王大海     26        女
2   08L0901    李铁锤     34        男
3   08L0902    张天翼     23        男
=== ========== ========== ======== =============

.. code-block:: python3

    student = namedtuple('student', ['ID', 'classId', 'name', 'age','gender'])

    STUDENTS_DICT={'08L0900':student(1,08L0900,'王大海','26','女'),
        '08L0901':student(2,'08L0901','李铁锤','34','男'),
        '08L0902':student(3,'08L0901'),'张天翼','男'} 


.. tip::

    上面的这中组织数据的形式比较适合于数据的查找，当给一个 ``classId`` 的时候，能够很方便的找到这条记录。
    适用于数据查找

.. code-block:: python3

    STUDENTS_list=[student(1,08L0900,'王大海','26','女'),
        student(2,'08L0901','李铁锤','34','男'),
        student(3,'08L0901','张天翼','男')]

.. tip::

    上面的这种组织数据的形式比较适合于数据的展示，能够很方便的查看数据的总数量，有哪些记录。
    适用于数据展示


metaclass=Singleton
=====================

根据您的查询，您似乎想了解Python中的元类和单例模式。实际上，元类是一种高级编程概念，用于创建类的类。单例模式是一种设计模式，用于确保类只有一个实例，并提供全局访问点。

以下是一个使用元类和单例模式创建单例类的示例：

.. code-block:: python3

    class Singleton(type):
        _instances = {}

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]

    class MyClass(metaclass=Singleton):
        def __init__(self, name):
            self.name = name

    # 创建两个实例
    a = MyClass('Instance A')
    b = MyClass('Instance B')

    # 输出实例名称
    print(a.name)    # 输出“Instance A”
    print(b.name)    # 输出“Instance A”

在此示例中，我们首先定义了一个名为Singleton的元类，

该元类包含一个名为 ``_instances`` 的类变量，该变量用于存储类的实例。

然后，我们定义了一个名为 ``MyClass``的类，并将  ``Singleton``元类分配给它的  ``metaclass`` 属性。

这将确保 ``MyClass`` 只有一个实例，并且该实例可以通过全局访问点访问。

接下来，我们创建了两个  ``MyClass`` 实例a和b，并将它们分别命名为 “Instance A”和“Instance B”。

由于 ``MyClass``是单例类，因此a和b实际上是同一个实例。最后，我们使用  ``print()`` 函数输出每个实例的名称，以证明它们是相同的。

