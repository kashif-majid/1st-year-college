import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
mainwindow = tkinter.Tk()

mainwindow.title("hello world")
mainwindow.geometry("640x480+8+400")
mainwindow.mainloop()