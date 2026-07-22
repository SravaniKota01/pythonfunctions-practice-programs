from turtle import shape
def add(a,b):
    return a+b
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
print(add(a,b))
def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = int(input('Enter another number: '))
print(max(a,b,c))
def evenorodd(a,b):
    if a%2==0:
        return a
    else:
        return b
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
print(evenorodd(a,b))
def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    return fac
print(factorial(5))
def prime(n):
    count = 0
    for i in range(2,n):
        if n % i == 0:
            count = count + 1
    if count == 0:
        return "prime"
    else:
        return "not prime"
print(prime(5))
def reverse(text):
    return text[::-1]
print(reverse("hello"))
def vowel(s):
    count = 0
    for i in s:
        if i in 'aeiou':
            count = count + 1
    return count
print(vowel("hello"))
def list_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
nums = [10, 20, 30, 40]
print(list_sum(nums))
def palindrom(text):
    p= text[::-1]
    if p == text:
        return "palindrom"
    else:
        return "not palindrom"
t = input("Enter a string: ")
print(palindrom(t))
def find(shape):

    def square():
        choice = input("Enter area or perimeter: ").lower()
        s = float(input("Enter side: "))

        if choice == "area":
            return s * s
        else:
            return 4 * s
    def rectangle():
        choice = input("Enter area or perimeter: ").lower()
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        if choice == "area":
            return l * w
        else:
            return 2 * (l + w)
    def circle():
        choice = input("Enter area or perimeter: ").lower()
        r = float(input("Enter radius: "))
        if choice == "area":
            return 3.14 * r * r
        else:
            return 2 * 3.14 * r
    def triangle():
        choice = input("Enter area or perimeter: ").lower()
        if choice == "area":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            return 0.5 * b * h
        else:
            b = float(input("Enter base: "))
            s1 = float(input("Enter side1: "))
            s2 = float(input("Enter side2: "))
            return b + s1 + s2
    if shape == "square":
        return square()
    elif shape == "rectangle":
        return rectangle()
    elif shape == "circle":
        return circle()
    elif shape == "triangle":
        return triangle()
    else:
        return "Invalid Shape"
shape = input("Enter shape (square/rectangle/circle/triangle): ").lower()
result = find(shape)
print("Result =", result)



