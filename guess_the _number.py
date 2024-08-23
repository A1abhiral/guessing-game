import random
num = random.randint(1,100)
n = 1
while(n<=5):
    num_in=int(input("Guess the number(1-100):"))

    if(num_in<num):
        print("higher")
    elif(num_in>num):
        print("lower")
    else:
        print("you have won")
        break
    n +=1

print("you have lost")
