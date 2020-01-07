def addBinary(a: str, b: str) -> str:
    res = ''
    l1,l2 = len(a),len(b)
    l = l1
    if l1 < l2:
        for t in range(l2-l1):
            l = l2
            a = '0' + a
    else:
        for t in range(l1-l2):
            l = l1

            b = '0' + b
    carry = 0
    print(a,b,l,carry)
    for i in range(l-1, -1, -1):
        print('carry',carry,res)
        n1 = a[i]
        n2 = b[i]
        if carry ==0:
            if n1 == n2 == '1':
                carry = 1
                res = '0' + res
            elif n1 == n2 == '0':
                res = '0' + res
            else:
                res = '1' + res
        else:
            if n1 == n2 == '1':
                res = '1' + res
            elif n1 == n2 == '0':
                carry = 0
                res = '1' + res
            else:
                res = '0' + res
        print(carry)
    if carry == 1:
        print(res)
        res = '1' + res
    return res

res = addBinary('1010','1011')
print('res', res)