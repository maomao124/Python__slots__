"""
 * Project name(项目名称)：Python__slots__
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 13:37
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    __slots__ = ('info')
    # __slots__ = ('info','info4')
    pass


# 下面定义了一个实例方法
def info(self):
    print("正在调用实例方法")


# 下面定义了一个实例方法
def info4(self):
    print("正在调用实例方法4")


# 下面定义了一个类方法
@classmethod
def info2(cls):
    print("正在调用类方法")


# 下面定义个静态方法
@staticmethod
def info3():
    print("正在调用静态方法")


if __name__ == '__main__':
    c1 = C()
    c1.info = info
    # c1.info4 = info4
    # 必须手动为 self 传值
    c1.info(c1)
    # c1.info4(c1)
