# -*- coding: utf-8 -*-
# 參數的預設資料
# def power(base,exp=0):
#     print(base**exp)
# power(3,2)
# power(4)

# 使用參數名稱應對
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

# 無限/不定 參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum / len(ns)) # len長度 round() 計算小數點
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)