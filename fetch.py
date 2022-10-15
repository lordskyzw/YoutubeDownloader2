import os
import tkinter
from pytube import YouTube

name = os.getlogin()
download_path = f'C:\\Users\\{name}\\Downloads'

root = tkinter.Tk()
root.iconbitmap('./media/icon.ico')
root.title("Fetch")
root.geometry("300x300")




screen = tkinter.Entry(root, width=50, borderwidth=5, font=("Helvetica", 12), bg='white', fg='black')
screen.insert(0, "Enter YouTube link")
screen.bind('<FocusIn>', lambda args: screen.delete('0', 'end'))
screen.pack()



def download_video():
    confirmation = tkinter.Label(root, text=f'Saving to {download_path}', bg='white', fg='black')
    no_link_label = tkinter.Label(root, text='No link inserted!')
    complete_lablel = tkinter.Label(root, text="Download Complete & saved in %s" %download_path)
    def close():
        root.after(2000, no_link_label.destroy())
        root.after(2000, confirmation.destroy())
        root.after(2000, complete_lablel.destroy())
        
    def download_start():
        confirmation.pack()
        close()
        
        
    def download_complete():
        complete_lablel.pack()
        close()
        
    try:
        video = screen.get()
        YouTube(video, on_progress_callback=download_start , on_complete_callback=download_complete).streams.get_highest_resolution().download(str(download_path))
        
    except:  
        no_link_label.pack()
        close()
        
def download_audio():
    confirmation = tkinter.Label(root, text=f'Saving to {download_path}', bg='white', fg='black')
    no_link_label = tkinter.Label(root, text='No link inserted!', bg='grey', fg='black', font=("Helvetica", 8))
    complete_lablel = tkinter.Label(root, text="Download Complete & saved in %s" %download_path)
        
    def close():
        root.after(2000, confirmation.destroy())
        root.after(2000, no_link_label.destroy())
        
    def download_start():
        confirmation.pack()
        close()
        
    def download_complete():
        complete_lablel.pack()
        close()
        
        
    try:
        audio = screen.get()
        YouTube(audio, on_progress_callback=download_start, on_complete_callback=download_complete).streams.get_audio_only(subtype="mp3").download(str(download_path))
    except:
        no_link_label.pack()
        close()
        
downloadvid_button = tkinter.Button(root, relief='raised', borderwidth=5, command=download_video, text="Download Video", highlightcolor="red", width=20, height=2)
downloadvid_button.pack()
downloadaud_button = tkinter.Button(root, relief='raised', borderwidth=5, command=download_audio, text="Download Audio", highlightcolor="red", width=20, height=2)
downloadaud_button.pack()
footnote = tkinter.Label(root, text="Made by Engineer Chiwara", bg='black', fg='grey', font=("Helvetica", 8))
footnote.pack(side=tkinter.BOTTOM)


root.wm_resizable(width=False, height=False)

#root.wm_attributes("-transparentcolor", "white")
root.wm_attributes("-alpha", 0.9)
root.mainloop()