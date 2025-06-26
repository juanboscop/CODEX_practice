import os
import tkinter as tk
from tkinter import filedialog, messagebox
from .main import get_images, create_slideshow, add_subtitles


tmp_video_name = "_temp_gui_video.mp4"


class TurnerSubsGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("TurnerSubs")

        self.audio_var = tk.StringVar()
        self.subtitles_var = tk.StringVar()
        self.images_var = tk.StringVar()
        self.output_var = tk.StringVar(value="output.mp4")

        self._build()

    def _build(self):
        row = 0
        # audio
        tk.Label(self.root, text="Audio file:").grid(row=row, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.audio_var, width=40).grid(row=row, column=1)
        tk.Button(self.root, text="Browse", command=self._browse_audio).grid(row=row, column=2)
        row += 1

        # subtitles
        tk.Label(self.root, text="Subtitles (ASS):").grid(row=row, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.subtitles_var, width=40).grid(row=row, column=1)
        tk.Button(self.root, text="Browse", command=self._browse_subtitles).grid(row=row, column=2)
        row += 1

        # images
        tk.Label(self.root, text="Images directory:").grid(row=row, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.images_var, width=40).grid(row=row, column=1)
        tk.Button(self.root, text="Browse", command=self._browse_images).grid(row=row, column=2)
        row += 1

        # output
        tk.Label(self.root, text="Output mp4:").grid(row=row, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.output_var, width=40).grid(row=row, column=1)
        tk.Button(self.root, text="Browse", command=self._browse_output).grid(row=row, column=2)
        row += 1

        tk.Button(self.root, text="Create Video", command=self._run).grid(row=row, column=0, columnspan=3, pady=10)

    def _browse_audio(self):
        path = filedialog.askopenfilename(filetypes=[("Audio", "*.mp3"), ("All", "*.*")])
        if path:
            self.audio_var.set(path)

    def _browse_subtitles(self):
        path = filedialog.askopenfilename(filetypes=[("ASS", "*.ass"), ("All", "*.*")])
        if path:
            self.subtitles_var.set(path)

    def _browse_images(self):
        path = filedialog.askdirectory()
        if path:
            self.images_var.set(path)

    def _browse_output(self):
        path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4", "*.mp4")])
        if path:
            self.output_var.set(path)

    def _run(self):
        audio = self.audio_var.get()
        subtitles = self.subtitles_var.get()
        images_dir = self.images_var.get()
        output = self.output_var.get()

        if not (audio and subtitles and images_dir and output):
            messagebox.showerror("Error", "Please provide all inputs")
            return

        try:
            images = get_images(images_dir)
            if not images:
                raise RuntimeError("No images found")
            create_slideshow(images, audio, tmp_video_name)
            add_subtitles(tmp_video_name, subtitles, output)
            messagebox.showinfo("Done", f"Video created at {output}")
        except Exception as exc:
            messagebox.showerror("Failed", str(exc))
        finally:
            if os.path.exists(tmp_video_name):
                os.remove(tmp_video_name)


def main():
    root = tk.Tk()
    TurnerSubsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
