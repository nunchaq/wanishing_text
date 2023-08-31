from tkinter import Tk, Text, Label, END

TIME_TO_CLEAR = 10
timer = 0
current_text = ''
app_title = "Wanishing text"
root = Tk()
root.title(app_title)
root.geometry('600x400')


def start_timer():
    global timer, current_text

    if len(text_area.get('1.0', END)) and text_area.get('1.0', END) == current_text:

        if timer == 0:
            text_area.delete('1.0', END)
            root.after(1000, start_timer)
        else:
            root.after(1000, start_timer)
            timer -= 1
    else:
        current_text = text_area.get('1.0', END)
        timer = TIME_TO_CLEAR
        root.after(1000, start_timer)


title = Label(root, text=app_title, font=('Arial', 20, 'bold'))
title.pack()

text_area = Text(root, height=20, width=52)
text_area.pack()

if __name__ == "__main__":
    start_timer()
    root.mainloop()
