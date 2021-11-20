from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("400x400")

label1 = Label(window, text = "선택된 파일 이름")
label1.pack()

saveFP = asksaveasfile(parent = window, mode = "w",
                           defaultextension = ".jpg",
                           filetypes = (("JPG 파일", "*.jpg;*.jpeg"),
                                        ("모든 파일", "*.*")))

label1.configure(text = saveFP)
saveFP.close()
window.mainloop()