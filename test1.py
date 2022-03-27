"""
 * Project name(项目名称)：Python__slots__
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 13:33
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    pass


# 下面定义了一个实例方法
def info(self):
    print("正在调用实例方法")


# 下面定义了一个类方法
@classmethod
def info2(cls):
    print("正在调用类方法")


# 下面定义个静态方法
@staticmethod
def info3():
    print("正在调用静态方法")


if __name__ == '__main__':
    # 类可以动态添加以上 3 种方法，会影响所有实例对象
    C.info = info
    C.info2 = info2
    C.info3 = info3
    c = C()
    # 如今，c 具有以上 3 种方法
    c.info()
    c.info2()
    c.info3()
    # 类实例对象只能动态添加实例方法，不会影响其它实例对象
    c1 = C()
    c1.info = info
    # 必须手动为 self 传值
    c1.info(c1)
    c1.info2()
    c1.info3()
