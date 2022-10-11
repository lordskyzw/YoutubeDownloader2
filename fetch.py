import os
import tkinter
from pytube import YouTube
import tkinter

root = tkinter.Tk()
root.iconbitmap('./media/icon.ico')
root.title("Fetch")
root.geometry("500x500")

screen = tkinter.Entry(root, width=50)
screen.insert(0, "Enter the link of the video you want to download")
screen.bind('<FocusIn>', lambda args: screen.delete('0', 'end'))
screen.pack()

def downloadd():
    name = os.getlogin()
    download_path = f'C:\\Users\\{name}\\Downloads'
    try:
        video = screen.get()
        YouTube(video).streams.get_highest_resolution().download(str(download_path))
        confirmation = tkinter.Label(root, text=f'Saving to {download_path}')
        confirmation.pack()
    except:
        tkinter.Label(root, text='No link inserted!', bg='white', fg='red', font=("Helvetica", 24)).pack()
    
download_button= tkinter.Button(root, command=downloadd, text="Download", highlightcolor="red", width=20, height=2)
download_button.pack()
footnote = tkinter.Label(root, text="Made by Engineer Chiwara")
footnote.pack()


root.mainloop()