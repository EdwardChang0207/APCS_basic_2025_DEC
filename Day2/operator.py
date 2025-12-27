#運算子:Operator, 運算:Operatee
'''
-優先序高到低排列-
括號 ()

1.數學運算
(1)負號[-]
(2)指數[**]
(3)乘除[*,/,**,//,%]
(4)加減[+,-]

2.邏輯運算(同等)
[>,<,>=,<=,==,!=]
special: [in]
l = [1, 2, 3]
print(4 in l)

3.布林運算
(1)not 反閘
    周杰倫：哎呦不錯喔
    不(not)錯(False) -> True
    錯  -> False

    不(not)行(True) -> False
    行  -> True
(2)and 且閘
    Hw and 打掃 -> :)
    T       F       F
    F       T       F
    T       T       T
    F       F       F
(3)xor (excursive or) 斥或閘
    珍奶 xor 烏龍 -> :)
    T       F       T
    F       T       T
    T       T       F
    F       F       F
    [1] not, and, or 
    -> whitelist and blacklist 
    -> (a or b)  and not(a and b)
    [2] binary
(4)or 或閘
    Math or English -> 3000
    T       F           T
    F       T           T
    T       T           T
    F       F           F(真值表 truth table)

4.Assign[=]
'''

a, b = False, False
print(f'a or b: {a or b} \na and b: {a and b}')
print(f'a xor b: {(a or b) and not(a and b)}')

c, d = True, False
print(f'ver1. a xor b: {(c or d) and not(c and d)}')
print(f'ver2. a xor b: {c^d}')

e = a**2
