# n = int(input("Enter the no: "))
# s = True
# for i in range(2,n):
#     if n % i == 0:
#         s = False
# if s == True:
#     print("The no is prime!!!")
# else:
#     print("The no is not prime")

# min = int(input("Enter the start range: "))
# max = int(input("Enter the end range: "))
# for i in range(min,max+1):
#     for j in range(2,i):
#         if i % j == 0:
#             print(f"The no {i} is not prime")
#             break
#     else:
#         print(f"The no {i} is prime!!")

l = [1,2,3,5,6,8,9,4]
for i in l:
    for j in range(2,i):
        if i % j == 0:
            print(f"The no {i} is not prime")
            break
    else:
        print(f"The no {i} is prime!!")