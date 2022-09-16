"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk

#:)
def walk(cyanide):
    if cyanide=='fish':
        messagebox.showinfo(None, message='you killed it')
        exit()
    if cyanide=='dog':
        messagebox.showinfo(None, message='they are more more happy now')
    if cyanide=='cat':
        messagebox.showinfo(None, message='they are happier now')

def feed(cyanide):
    if cyanide=='fish':
        messagebox.showinfo(None, message='they are more well fed now')
    if cyanide=='dog':
        messagebox.showinfo(None, message='they are more more well fed now')
    if cyanide=='cat':
        messagebox.showinfo(None, message='they are more well fed now')

def nothing(cyanide):
    if cyanide=='fish':
        messagebox.showinfo(None, message='they are more chill now')
    if cyanide=='dog':
        messagebox.showinfo(None, message='they are more more chill now')
    if cyanide=='cat':
        messagebox.showinfo(None, message='they are more chill now')

def kill(cyanide):
    if cyanide=='fish' or 'dog' or 'cat':
        messagebox.showinfo(None, message='you monster')
        exit()

if __name__ == '__main__':
# TODO)
#   1. Ask the user to enter the type of pet they want (give them a few
#      choices).
    window = Tk()
    window.withdraw()
    happiness=10
    hunger=3
    cyanide=simpledialog.askstring(None, prompt='which pet do you want (cat,dog,fish)')
    slavery=True
    while slavery:
        what=simpledialog.askstring(None, prompt='what you wanna do with the pet')
        if what=='walk':
            walk(cyanide)
            happiness+=5;
            hunger-=2
        if what=='feed':
            feed(cyanide)
            hunger+=2;
        if what=='nothing':
            nothing(cyanide)
            happiness-=5
            hunger-=1
        if what== 'kill':
            kill(cyanide)
        if happiness==100:
            messagebox.showinfo(None, message='your pet might be a bit too excited, you should let it calm down.(seriously)')
        elif happiness==5:
            messagebox.showinfo(None, message='hes close to depression...')
        elif happiness==0:
            messagebox.showinfo(None, message='depression')
            slavery=False
        elif happiness>100:
            messagebox.showinfo(None, message='your pet got too excited and died')
        if hunger==1:
            messagebox.showinfo(None, message='your pets getting real hungry there maybe you should do something about it?')
        elif hunger==9:
            messagebox.showinfo(None, message='your pet is getting extra large, maybe cut back on the food.')
        elif hunger==0:
            messagebox.showinfo(None, message='starvation')
            slavery=False
        elif hunger==10:
            messagebox.showinfo(None, message='over fed')
            slavery=False









    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
