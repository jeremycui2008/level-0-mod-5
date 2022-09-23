"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user for a number

    number=simpledialog.askinteger(None, prompt='give me a number and I will determine whether it is prime or not')
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    is_prime=True

    for i in range(number):
        print(i)
        if i > 1 and number % i == 0:
            is_prime=False
            break
    if is_prime:
        messagebox.showinfo(None, message='you got a prime')
    else:
        messagebox.showinfo(None, message="it's not a prime" )
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass
