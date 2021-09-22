import tkinter  # Imported to use Tkinter and make GUI applications
from PIL import Image, ImageTk  # PIL = Python Imaging Library. Used to perform operations involving images in the UI
import random  # imports to generated random numbers

# main window
root = tkinter.Tk()  # function helps to display the root window and manages all the other components of hte tkinter
# application.
root.geometry('500x500')  # the dimensions of the window
root.title('The Dice of Fate')  # the title of the window
# Note: must call mainloop once when ready for application to run. mainloop is an infinite loop. the tkinter window
# will refuse to open without there being a mainloop function.Must be Placed in the end of code

# label in window
BL = tkinter.Label(root, text="")  # text is the text that will be displayed
BL.pack()  # put a widget inside a frame, and have it fill the entire frame. used to pack the widget onto the root
# window

# formatting label

HL = tkinter.Label(root, text="This is the Dice Master of Fate",
                   fg="white",  # fg - color of hte font used for HL
                   bg="black",  # bg - color of the background of HL
                   font="Times 16 bold italic")  # font of letters
HL.pack()

# adding images to the dice

dice = ['one.png', 'two.png', 'three.png', 'four.png', 'five.png', 'six.png']
DI = ImageTk.PhotoImage(Image.open(random.choice(dice)))  # PhotoImage is used to add the user-defined images to the
# application. image.open() opens and identifies the given image file

# label for widget image

IL = tkinter.Label(root, image=DI)  # shows image in the widget
IL.image = DI  # place images to working directory in order for the images to be used

# packing

IL.pack(expand=True)  # tells the manager to assign additional space to the widget box


# adding button

def rolling():
    DI = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # image update
    IL.configure(image=DI)  # .configure() used to access an object's attributes after its initialisation.
    # keep reference
    IL.image = DI


# adding buttons and commands

button = tkinter.Button(root, text='Roll the Dice',  # button is used to add button in the application
                        fg='dark green',
                        command=rolling)  # the command calls the function when the button is clicked

# packing
button.pack(expand=True)

# calls the mainloop of Tk and keeps window open

root.mainloop()
