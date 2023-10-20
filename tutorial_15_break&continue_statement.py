for i in range(20):
    print("3 X " , i ,"= ", 3*(i+1))
    if(i==10):
        break
print("break lag gya")



for i in range(20):
    if(i==10):
        print("skip the iteration")
        continue
    print("3 X " , i ,"= ", 3*(i))
    