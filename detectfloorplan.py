import tkinter
from tkinter import filedialog
from catchword import captch_ex

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    captch_ex(filename)
main=tkinter.Tk()
main.title('Floorplandetect')
main.geometry("500x500")
button = tkinter.Button(main, text='Open', command=UploadAction)


button.pack()
main.mainloop()
