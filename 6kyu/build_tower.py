#  n integer determines the rows
#
# [
#  '  *  ', 
#  ' *** ', 
#  '*****'
# ]
# 1 row =  1 on the bottom
# 2 rows = 3 on the bottom
# 3 rows = 5 on the bottom
# 4 rows = 7 on the bottom
# 5 rows = 9 on the bottom
# 6 rows = 11 on the bottom
# 7 rows = 13 on the bottom

def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

print(tower_builder(10))
    