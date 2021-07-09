# -*- coding: utf-8 -*-
# str() 若兩個變數結合，字串與變數結合需使用str()

# break 的簡易範例
# n=0

# while n<5:
#     if n==3:
#         break
#     print(n) # 印出迴圈中的n
#     n+=1
# print("最後的 n: " + str(n)) # 印出迴圈結束後的n

# continue 的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # x 是偶數
#         continue
#     print(x)
#     n+=1
# print("最後的 n: " + str(n)) # 印出迴圈結束後的n

# else 的簡易範例
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) # 印出 0+1+2+...+10 的結果

# 綜合範例：找出整數平方根
# 輸入 9. 得到3
# 輸入 11. 得到『沒有』整數的平方根
n=input("輸入一個正整數：")
n=int(n) # 轉換輸入成數字
for i in range(n): # i 從 0 ~ n-1
    if i*i==n:
        print("整數平方根: " + str(i))
        break # 用 break 強制結束回圈時，不會執行else區塊
else:
    print("沒有整數平方根")
