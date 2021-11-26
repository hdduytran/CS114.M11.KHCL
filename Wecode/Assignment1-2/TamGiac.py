a = [None]*3
for i in range(3):
    a[i] = int(input())

def dientich(a):
    p = sum(a)/2.0
    s = p
    for i in a:
        s*=p-i
    s = s**(1/2)
    return s

a = sorted(a,reverse=True)
if a[0]**2 == a[1]**2+a[2]**2:
    loai = 'vuong'
    s = a[1]*a[2]/2.0
elif len(set(a)) == 1:
    loai = 'deu'
    s = dientich(a)
elif len(set(a)) == 2 and a[0]<a[1]+a[2]:
    loai = 'can'
    s = dientich(a)
elif a[0]<a[1]+a[2]:
    loai = 'thuong'
    s = dientich(a)
else:
    loai = None

if loai:
    s = round(s,2)
    if int(s) == s:
        s = int(s)
    print(f'Tam giac {loai}, dien tich = {s:g}')
else:
    print('Khong phai tam giac')