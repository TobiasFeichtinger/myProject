def largest_square_number (n):
    q = 0
    x = 0
    while n >= q:
        x = x + 1
        q = x * x
    q = (x-1) * (x-1)
    print(q)

largest_square_number(int(input("Enter a number: ")))