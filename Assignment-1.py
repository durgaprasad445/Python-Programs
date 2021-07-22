n = int(input('Enter Any Value: '))
m = input('Please Enter Your Name: ')
for i in range(1,n):
    if i % 3 == 0 and i % 5 == 0:
        print(m)
    elif i % 3 == 0:
        print('3n')
    elif i % 5 == 0:
        print('5n')
    else:
        print(False)
