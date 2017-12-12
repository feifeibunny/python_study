# 顺序结构 washer01

#洗衣流程
print('注水20L')
print('搅拌30min')
print('放水')

#甩干流程
print('注水30L')
print('搅拌5min')
print('甩干')

# 分支结构 washer02

print('请选择水位：h/l')
level=input()

#洗衣流程
if level=='l':
    print('加水20L')
    print('搅拌30min')
elif level=='h':
    print('加水50L')
    print('搅拌60min')
print('放水')

#甩干流程
print('注水30L')
print('搅拌5min')
print('甩干')

# 循环结构 washer03

print('请选择水位：h/l')
level=input()

#洗衣流程

if level=='l':
    print('加水20L')
    print('搅拌30min')
elif level=='h':
    print('加水50L')
    print('搅拌60min')
print('放水')

#甩干流程

print('请输入甩干次数')
times= int(input())

print('注水30L')
print('搅拌5min')
print('甩干')
