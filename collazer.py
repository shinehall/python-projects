#this is a Collatz queue compute game

def collazer(number):
    # is an even
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print("give me a number")
num = int(input())
print("ok! the number is " + str(num))
while(num != 1):
    num = collazer(num)
    print("after change the number is " + str(num))
print("collaz done!")
