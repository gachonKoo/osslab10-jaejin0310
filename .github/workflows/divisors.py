import sys

number = int(sys.argv[1])

for i in range(1,number):
    if i % number == 0:
        print(i,end=" ")

print()
