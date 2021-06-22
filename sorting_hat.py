import os
import smtplib
import imghdr
from email.message import EmailMessage
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.constants import E, LEFT, RIGHT, W
from typing import Text

LARGEFONT = ("Verdana", 35)
SIMPLETEXT = ("Verdana", 12)


def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


def send_email(email):
    sender, password = read_creds()

    msg = EmailMessage()
    msg["Subject"] = "FINAL DESICION OF THE SORTING HAT!"
    msg["From"] = sender
    msg["To"] = email

    msg.set_content("This is a plain text email")

    msg.add_alternative(
        """\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">You are a ravenclaw!!</h1>
        </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6, Page7):

            frame = F(container, self)

            # initializing frame of that object from
            # StartPage, Page1, Page2, Page3, Page4, Page5, Page6, Page7 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Get sorted for Hogwarts!", font=LARGEFONT)
        label1 = ttk.Label(
            self,
            text="Welcome, I'm the Sorting Hat",
            font=SIMPLETEXT,
        )

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, padx=10, pady=10)
        label1.grid(row=1, column=0, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="To start, I need to know your name",
            command=lambda: controller.show_frame(Page1),
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=2, column=0, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="Tell me your name son, in the box I magically inserted below",
            font=SIMPLETEXT,
        )
        label.grid(row=1, column=0, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2

        name = tk.StringVar()
        nameEntered = ttk.Entry(self, width=40, textvariable=name)
        nameEntered.grid(column=0, row=2)

        button1 = ttk.Button(
            self,
            text="Enter",
            command=lambda: controller.show_frame(Page2),
        )
        button1.grid(row=3, column=0, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="Adorn the Sorting Hat to be placed into your rightful Hogwarts house. The Sorting Hat's decision is final",
            font=SIMPLETEXT,
        )
        label.grid(row=0, column=0, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="Ok, lets begin", command=lambda: controller.show_frame(Page3)
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=0, padx=10, pady=10)


# fourth
class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="What are you most looking forward to learning at Hogwarts?",
            font=SIMPLETEXT,
        )
        label.grid(row=0, column=0, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="All about magical creatures, and how to befriend/care for them",
            command=lambda: controller.show_frame(Page4),
        )

        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="Apparition and Disapparition (being able to materialize and dematerialize at will)",
            command=lambda: controller.show_frame(Page4),
        )

        button2.grid(row=2, column=0, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="Secrets about the castle",
            command=lambda: controller.show_frame(Page4),
        )

        button3.grid(row=3, column=0, padx=10, pady=10)

        button4 = ttk.Button(
            self,
            text="Transfiguration (turning one object into another object)",
            command=lambda: controller.show_frame(Page4),
        )

        button4.grid(row=4, column=0, padx=10, pady=10)


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="Four goblets are placed before you. Which would you choose to drink?",
            font=SIMPLETEXT,
        )
        label.grid(row=0, column=0, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums",
            command=lambda: controller.show_frame(Page5),
        )

        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions",
            command=lambda: controller.show_frame(Page5),
        )

        button2.grid(row=2, column=0, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds",
            command=lambda: controller.show_frame(Page5),
        )

        button3.grid(row=3, column=0, padx=10, pady=10)

        button4 = ttk.Button(
            self,
            text="The golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room.",
            command=lambda: controller.show_frame(Page5),
        )

        button4.grid(row=4, column=0, padx=10, pady=10)


class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="Which of the following would you most hate people to call you?",
            font=SIMPLETEXT,
        )
        label.grid(row=0, column=0, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="Ignorant",
            command=lambda: controller.show_frame(Page6),
        )

        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="Selfish",
            command=lambda: controller.show_frame(Page6),
        )

        button2.grid(row=2, column=0, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="Ordinary",
            command=lambda: controller.show_frame(Page6),
        )

        button3.grid(row=3, column=0, padx=10, pady=10)

        button4 = ttk.Button(
            self,
            text="Cowardly",
            command=lambda: controller.show_frame(Page6),
        )

        button4.grid(row=4, column=0, padx=10, pady=10)


class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="Which road tempts you most?",
            font=SIMPLETEXT,
        )
        label.grid(row=0, column=0, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="The twisting, leaf-strewn path through woods",
            command=lambda: controller.show_frame(Page7),
        )

        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="The wide, sunny, grassy lane",
            command=lambda: controller.show_frame(Page7),
        )

        button2.grid(row=2, column=0, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="The narrow, dark, lantern-lit alley",
            command=lambda: controller.show_frame(Page7),
        )

        button3.grid(row=3, column=0, padx=10, pady=10)

        button4 = ttk.Button(
            self,
            text="The cobbled street lined with ancient buildings",
            command=lambda: controller.show_frame(Page7),
        )

        button4.grid(row=4, column=0, padx=10, pady=10)


class Page7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="The Sorting Hat is ready to make its decision",
            font=LARGEFONT,
        )
        label.grid(row=0, column=0, padx=10, pady=10)

        label = ttk.Label(
            self,
            text="Enter your email please:",
            font=SIMPLETEXT,
        )
        label.grid(row=1, column=0, padx=10, pady=10)

        name = tk.StringVar()
        nameEntered = ttk.Entry(self, width=40, textvariable=name)
        nameEntered.grid(column=0, row=2)

        button1 = ttk.Button(
            self,
            text="PREPARE YOURSELF FOR THE MAGIC TO HAPPEN!",
            command=lambda: send_email(name.get()),
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=3, column=0, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
