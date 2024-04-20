
def check(ss):

    par=True

    x_flag=[]
    x_buffer=[]
    
    for i in range(len(ss)):
        k=ss[i]
        if k=="(":
         x_flag.append(i)
        if k=="*":
         x_buffer.append(i)
        if k==")":        
            if len(x_flag)>0:
                x_flag.pop()
            elif (len(x_flag)==0) and(len(x_buffer)>0):
                    x_buffer.pop() 
            else:
                par=False
                break
    while (len(x_buffer)>0) and (len(x_flag)>0):
        if x_buffer[-1]<=x_flag[-1]:
            x_buffer.pop()
        elif x_buffer[-1]>x_flag[-1]:
            x_buffer.pop()
            x_flag.pop()

    if len(x_flag)>0:   
        par=False

    return par

s=str(input())
print(check(s))