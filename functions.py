def multiply_and_greet(*number, **student):
    mul=1
    for num in number:
        mul*=num
        print(mul)  
    print(f"Hello {student} ")