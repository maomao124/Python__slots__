"""
 * Project name(项目名称)：Python__slots__
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 13:46
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def display(self):
        print(self.name, self.sex, self.age)


class C1:
    __slots__ = ('name', 'sex', 'age')

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def display(self):
        print(self.name, self.sex, self.age)


class C2:
    __slots__ = ('name')

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def display(self):
        print(self.name, self.sex, self.age)


if __name__ == '__main__':
    c = C("张三", "男", 22)
    c.display()
    c.no = 111
    print(c.no)

    c1 = C1("张三", "男", 24)
    c1.display()
    # c1.no = 222
    # print(c1.no)

    # c2 = C2("张三", "男", 24)
