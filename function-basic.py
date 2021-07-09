# -*- coding: utf-8 -*-
# 定意函式
# 函式內部的程式碼，若是沒有做函式呼叫，就不會執行
# def multiply(n1,n2):
#     # print(n1*n2)
#     return n1*n2
# # 呼叫函式
# value=multiply(8,3)+multiply(3,6)
# print(value)
# multiply(10,3)
# multiply(5,4)

# 韓式可用來做程式的包裝: 同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

calculate(10)
calculate(20)