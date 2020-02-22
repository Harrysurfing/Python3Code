#Hacker rank list 

#takes in N lines of commands and eval commands

'''
sample input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''


if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        line = input().split()
        cmd = line[0]
        values = line[1:]
        if cmd == 'print':
            print(l)
        else:
            eval('l.{0}{1}'.format(cmd,tuple(map(int,values))))
