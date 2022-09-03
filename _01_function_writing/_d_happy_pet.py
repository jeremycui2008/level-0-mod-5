"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


def walk(cyanide):
    if cyanide=='fish':
        messagebox.showinfo(None, message='you killed it')
        exit()
    if cyanide=='dog':
        messagebox.showinfo(None, message='they are more more happy now')
    if cyanide=='cat':
        messagebox.showinfo(None, message='they are happier now')


if __name__ == '__main__':
# TODO)
#   1. Ask the user to enter the type of pet they want (give them a few
#      choices).
    window = Tk()
    window.withdraw()
    happiness=10
    cyanide=simpledialog.askstring(None, prompt='which pet do you want (cat,dog,fish)')
    slavery=True
    while slavery:
        what=simpledialog.askstring(None, prompt='what you wanna do with the pet')
        if what=='walk':
            walk(cyanide)
            happiness+=5;
        if happiness==100:
            messagebox.showinfo(None, message='your pet might be a bit too excited, you should let it calm down.')
        if happiness>100:
            messagebox.showinfo(None, message='your pet got too excited and died')
            exit()









    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
