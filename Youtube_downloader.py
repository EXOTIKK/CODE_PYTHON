import tkinter as tk
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    video_quality = quality_var.get()

    try:
        youtube = YouTube(video_url)
        video = youtube.streams.get_by_resolution(video_quality)
        video.download()
        status_label.config(text="Download completed!")
    except Exception as e:
        if 'rental' in str(e):
            status_label.config(text="This video is restricted.")
        else:
            status_label.config(text="Error during download.")

# Créer une fenêtre Tkinter
window = tk.Tk()

# Ajouter des widgets à la fenêtre
url_label = tk.Label(window, text="Video URL:")
url_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

quality_label = tk.Label(window, text="Video Quality:")
quality_label.pack()

quality_var = tk.StringVar(window)
quality_var.set("720p")

quality_dropdown = tk.OptionMenu(window, quality_var, "144p", "240p", "360p", "480p", "720p", "1080p")
quality_dropdown.pack()

download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

# Lancer la boucle principale Tkinter
window.mainloop()
