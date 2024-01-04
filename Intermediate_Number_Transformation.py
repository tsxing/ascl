# let me know if wrong

for _ in range(5):
    n, p = map(int, input().split())
    n = list(str(n))
    pth = int(n[len(n)-p])
    ans = [0]*len(n)
    ans[len(n)-p] = pth
    
    for i in range(len(n)):
        if i < (len(n)-p):
            if int(n[i])+pth>9:
                ans[i]=(int(n[i])+pth)%10
            else:
                ans[i]=(int(n[i])+pth)
        if i> (len(n) -p):
            ans[i] = (abs(int(n[i])-pth))
    print(int(''.join(map(str, ans))))
