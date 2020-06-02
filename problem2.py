''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def main():
    t=int(input())
    while t>0:
        cnt=0
        n=int(input())
        g=list(map(int,input().split()))
        o=list(map(int,input().split()))
        g.sort(reverse=True)
        o.sort(reverse=True)
        p=0
        for i in range(n):
            for j in range(p,n):
                if g[i]>o[j]:
                    p=j+1
                    cnt+=1
                    break
        print(cnt)
        t-=1


main()
