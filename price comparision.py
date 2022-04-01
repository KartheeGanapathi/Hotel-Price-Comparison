from tkinter import *  # importing everything from tkinter
import pandas as pd  # importing pandas


windows = Tk()        # creating the new window
windows.title("SOME APP")  # setting the title of windows
windows.geometry("2000x1080")  # setting the dimensions of windows
windows.configure(bg="black")  # setting the background colour of windows


def close_window():
    windows.destroy()  # function to close the main window and its derived windows


# function to create the next window and moving on
def starter():
    # function to display the results for the selected city
    def select():
        # printing a city user have selected
        lbl.config(text="\n\nYOU HAVE SELECTED : " + listbox.get(ANCHOR), bg="black", fg="lime", font=("ink free", 14))
        top2 = Toplevel()
        top2.geometry("2000x1080")
        top2.configure(bg="black")
        top2.title("RESULTS")

        if listbox.get(ANCHOR) == "GOA":
            # opening the results of GOA using pandas if GOA is selected from list
            df = pd.read_csv(r"C:\Users\GANAPATHI M\PycharmProjects\pythonProject\projects\GOAF.csv")

        elif listbox.get(ANCHOR) == "COORGE":
            # opening the results of COORGE using pandas if COORGE is selected from list
            df = pd.read_csv(r"C:\Users\GANAPATHI M\PycharmProjects\pythonProject\projects\COORGF.csv")

        elif listbox.get(ANCHOR) == "KOCHI":
            # opening the results of KOCHI using pandas if KOCHI is selected from list
            df = pd.read_csv(r"C:\Users\GANAPATHI M\PycharmProjects\pythonProject\projects\KOCHIF.csv")

        else:
            # opening the results of KODAIKANAL using pandas if KODAIKANAL is selected from list
            df = pd.read_csv(r"C:\Users\GANAPATHI M\PycharmProjects\pythonProject\projects\KODAIKANALF.csv")

        k = df.to_string(index=False)  # statement so not to print the index
        pd.set_option("display.expand_frame_repr", False)  # print all columns completely
        # to print all rows and columns in single line
        pd.set_option("display.max_rows", None, "display.max_columns", None)

        # printing the result for selected city
        label3 = Label(top2, text=k, bg="black", fg="lime", font=("ink free", 12))
        label3.pack()

        # leaving a blank line
        label4 = Label(top2, text="\n", bg="black", fg="lime", font=("ink free", 12))
        label4.pack()

        # leaving a blank line
        label4 = Label(top2, text="\n", bg="black", fg="lime", font=("ink free", 12))
        label4.pack()

        # close button to close all the open windows
        close_button2 = Button(top2, width=25, text="CLOSE", bg="black", fg="lime", padx=50, command=close_window, font=("ink free", 12))
        close_button2.pack()

        top2.mainloop()

    top = Toplevel()  # opening the second window "TOP"
    top.title("WINDOW TO ENTER THE CREDENTIALS")  # setting the title for TOP
    top.geometry("2000x1080")  # setting the dimension for TOP
    top.configure(bg="black")  # setting the background colour for TOP

    listbox = Listbox(top)  # making the list of cities
    label2 = Label(top, text="\nSELECT THE CITY : \n\n", bg="black", fg="lime", font=("ink free", 14))
    label2.pack()

    listbox.pack(padx=50, pady=20)  # placing list in "top" window
    # inserting the city names to the list
    listbox.insert(END, "GOA")
    listbox.insert(END, "COORGE")
    listbox.insert(END, "KOCHI")
    listbox.insert(END, "KODAIKANAL")
    # making a button to select the city and moving to next page
    button2 = Button(top, text="SELECT", bg="black", fg="lime", padx=50, command=select, font=("ink free", 12))
    button2.pack()

    # dummy label to print the selected city
    lbl = Label(top, text="", bg="black", fg="lime", font=("ink free", 14))
    lbl.pack()


# label to print the title
label = Label(windows, text="\nWELCOME TO ROOM RESERVATION VIA THIS APP\n", bg="black", fg="lime", font=("ink free", 16))
label.pack()
# button to get started
start_button = Button(width=25, text="GET STARTED", bg="black", fg="lime", padx=50, command=starter, font=("ink free", 12))
start_button.pack()
# leaving some blank lines
label = Label(windows, text="\n\n\n", bg="black", fg="lime")
label.pack()

# close button to close all the open windows
close_button = Button(width=25, text="CLOSE", bg="black", fg="lime", padx=50, command=close_window, font=("ink free", 12))
close_button.pack()

windows.mainloop()  # mainloop to keep the windows open.
