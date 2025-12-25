def lists():
    numbers = input("Enter a list of numbers:").split(',')
    for i in numbers:
        print(int(i)**2)

lists()