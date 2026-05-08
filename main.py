import customtkinter as ctk
from tkinter import messagebox
import threading
import yt_dlp


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def download_mp3(url):
    if not url.strip():
        messagebox.showwarning("Fehler", "Bitte einen YouTube-Link eingeben.")
        return

    status_label.configure(text="Download läuft...")

    ydl_opts = {
        "format": "bestaudio/best",

        #Gebe hier zwischen den speicher pfade bitte an
        # muster Beispiel     C:\Users\Muster\Musik\Muster\
        "outtmpl": r"C:\Users\lucas\Music\YouTube\%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "keepvideo": False,
        "postprocessor_args": ["-vn"],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.configure(text="Fertig! MP3 wurde gespeichert.")
        messagebox.showinfo("Fertig", "Die MP3 wurde erfolgreich heruntergeladen.")

    except Exception as e:
        status_label.configure(text="Fehler beim Download.")
        messagebox.showerror("Fehler", f"Fehler:\n{e}")


def start_download():
    url = url_entry.get()
    url_entry.delete(0, "end")

    thread = threading.Thread(target=download_mp3, args=(url,))
    thread.start()


app = ctk.CTk()
app.title("YouTube MP3 Downloader")
app.geometry("620x360")
app.resizable(False, False)

frame = ctk.CTkFrame(app, corner_radius=20)
frame.pack(padx=30, pady=30, fill="both", expand=True)

title = ctk.CTkLabel(
    frame,
    text="YouTube MP3 Downloader",
    font=("Arial", 28, "bold")
)
title.pack(pady=(30, 10))

subtitle = ctk.CTkLabel(
    frame,
    text="Füge einen YouTube-Link ein und speichere ihn als MP3.",
    font=("Arial", 14),
    text_color="gray"
)
subtitle.pack(pady=(0, 25))

url_entry = ctk.CTkEntry(
    frame,
    width=480,
    height=42,
    placeholder_text="YouTube-Link hier einfügen..."
)
url_entry.pack(pady=10)

download_button = ctk.CTkButton(
    frame,
    text="MP3 herunterladen",
    width=220,
    height=42,
    corner_radius=12,
    command=start_download
)
download_button.pack(pady=15)

status_label = ctk.CTkLabel(
    frame,
    text="Bereit für einen Link.",
    font=("Arial", 13),
    text_color="gray"
)
status_label.pack(pady=10)


app.mainloop()



