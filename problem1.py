''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n=int(input())
    x=list(map(int, input().split())) 
    y=list(map(int, input().split()))
    li=[]
    for i in range(n):
        d=y[i]//x[i]
        li.append(d)
    print(min(li))    
main()
