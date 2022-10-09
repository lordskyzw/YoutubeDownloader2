from pytube import YouTube
import tkinter

root = tkinter.Tk()
root.title("Tarmica's Youtube Downloader")
root.geometry("500x500")

screen = tkinter.Entry(root, width=50)
screen.insert(0, "Enter the link of the video you want to download")
screen.pack()

def downloadd():
    download_path = r'C:\Users\Tarmica\Downloads'
    try:
        video = screen.get()
        YouTube(video).streams.get_highest_resolution().download(output_path=download_path)
        tkinter.Label(root, text=f'Saving to {download_path}').pack()
    except:
        tkinter.Label(root, text='No link inserted')
    
download_button= tkinter.Button(root, command=downloadd, text="Download", highlightcolor="red", width=20, height=2)
download_button.pack()


root.mainloop()