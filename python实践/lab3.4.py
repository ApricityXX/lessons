import math
# 海伦公式计算三角形面积
def TriangleArea(*, a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print("面积为："+str(area))

TriangleArea(a=3, b=4, c=5)

