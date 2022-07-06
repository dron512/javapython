def returnResult(n1,n2):
    num1=0
    num2=0
    if n1 is None :
        num1 = 0
    else:    
        num1 = int(n1)
    if n2 is None :
        num2 = 0
    else:        
        num2 = int(n2)
    if( num1 > num2):
        num1,num2 = num2,num1
    result = 0
    for i in range(num1,num2):
        result +=i
    return result