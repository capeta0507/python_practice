# -*- coding: utf-8 -*-
# import sys

# sys.path.append("geometry") # 在模組的搜尋路徑列表中【新增路徑】
# 主程式

import geometry.point
result=geometry.point.distance(3,4)
print("距離 " + str(result))

import geometry.line
result=geometry.line.slope(1,1,3,4)
print("斜率 " + str(result))

# import point
# result=point.distance(3,4)
# print("距離 " + str(result))
# import line
# result=line.slope(1,1,3,4)
# print("斜率 " + str(result))