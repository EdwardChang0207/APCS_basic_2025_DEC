'''
print(123)
print('abc')
print(123+345, end = ' ')
print(123, 456, 789, sep = ',')
#分隔符號 seprate -> sep 結尾符號 end 換行->'\n'

input('請輸入姓名') #提示文字 烤箱
import sys
for i in sys.stdin:
    i = int(i)
    print(i)
'''

#'10 20 30' -> ['10','20','30']
# [int(i) for i in input().split()]
# list(map(int, input().split()))

'''
1 2 3
4 5 6
7 8 9
'''

# [list(map(int, input().split())) for _ in range(3)]
