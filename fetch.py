import os
import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.iconbitmap('./media/icon.ico')
root.title("Fetch")
root.geometry("300x300")


frame = tkinter.Frame(root, width=300, height=300)

screen = tkinter.Entry(frame, width=50, borderwidth=5, font=("Helvetica", 12), bg='white', fg='black')
screen.insert(0, "Enter YouTube link")
screen.bind('<FocusIn>', lambda args: screen.delete('0', 'end'))
screen.pack()

name = os.getlogin()
download_path = f'C:\\Users\\{name}\\Downloads'

def download_video():
    confirmation = tkinter.Label(root, text=f'Saving to {download_path}', bg='white', fg='black')
    no_link_label = tkinter.Label(frame, text='No link inserted!', bg='white', fg='red', font=("Helvetica", 24))
    def close():
        frame.after(2000, no_link_label.destroy())
        frame.after(2000, confirmation.destroy())
        
    def download_start():
        
        confirmation.pack()
        close()
        
    def download_complete():
        complete_lablel = tkinter.Label(frame, text="Download Complete & saved in %s" %download_path)
        complete_lablel.pack()
        close()
        
    try:
        video = screen.get()
        YouTube(video, on_progress_callback=download_start() , on_complete_callback=download_complete()).streams.get_highest_resolution().download(str(download_path))
        
    except:  
        no_link_label.pack()
        close()
        
def download_audio():
        
    def close():
        no_link_label = tkinter.Label(frame, text='No link inserted!', bg='grey', fg='black', font=("Helvetica", 8))
        no_link_label.pack()
        frame.after(2000, no_link_label.destroy())
        
    def download_start():
        confirmation = tkinter.Label(root, text=f'Saving to {download_path}', bg='white', fg='black')
        confirmation.pack()
        close()
        
    def download_complete():
        complete_lablel = tkinter.Label(frame, text="Download Complete & saved in %s" %download_path)
        complete_lablel.pack()
        close()
        
        
        try:
            audio = screen.get()
            YouTube(audio, on_progress_callback=download_start(), on_complete_callback=download_complete()).streams.get_audio_only(subtype="mp3").download(str(download_path))
        except:
            close()
        
downloadvid_button = tkinter.Button(frame, relief='raised', borderwidth=5, command=download_video, text="Download Video", highlightcolor="red", width=20, height=2)
downloadvid_button.pack()
downloadaud_button = tkinter.Button(frame, relief='raised', borderwidth=5, command=download_audio, text="Download Audio", highlightcolor="red", width=20, height=2)
downloadaud_button.pack()
footnote = tkinter.Label(root, text="Made by Engineer Chiwara", bg='black', fg='grey', font=("Helvetica", 8))
footnote.pack(side=tkinter.BOTTOM)
frame.pack()
root.wm_attributes("-transparentcolor", "white")
root.wm_attributes("-alpha", 0.9)





root.mainloop()