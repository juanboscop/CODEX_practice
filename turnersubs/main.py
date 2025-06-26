import os
import argparse
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import ffmpeg
import tkinter as tk
from tkinter import filedialog, messagebox

def get_images(directory):
    """Return a sorted list of image file paths in directory."""
    images = [os.path.join(directory, f) for f in os.listdir(directory)
              if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    return sorted(images)

def create_slideshow(images, audio_file, tmp_video):
    """Create a slideshow video from images and audio."""
    audio = AudioFileClip(audio_file)
    duration = audio.duration
    if not images:
        raise ValueError("No images provided")
    each_duration = duration / len(images)
    clips = [ImageClip(img).set_duration(each_duration) for img in images]
    video = concatenate_videoclips(clips, method="compose").set_audio(audio)
    video.write_videofile(tmp_video, fps=24)


def add_subtitles(input_video, subtitles, output_video):
    """Use ffmpeg to overlay subtitles."""
    (
        ffmpeg
        .input(input_video)
        .filter('subtitles', subtitles)
        .output(output_video, codec='libx264', acodec='copy', movflags='faststart')
        .overwrite_output()
        .run()
    )


def run_slideshow(audio, subtitles, images, output):
    """Helper to create slideshow and add subtitles."""
    image_list = get_images(images)
    tmp_video = 'temp_video.mp4'
    create_slideshow(image_list, audio, tmp_video)
    add_subtitles(tmp_video, subtitles, output)
    os.remove(tmp_video)


def launch_gui():
    """Open a simple Tkinter interface for TurnerSubs."""
    root = tk.Tk()
    root.title("TurnerSubs")

    audio_var = tk.StringVar()
    sub_var = tk.StringVar()
    img_var = tk.StringVar()
    out_var = tk.StringVar(value="output.mp4")

    def browse_audio():
        path = filedialog.askopenfilename(title="Select Audio", filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")])
        if path:
            audio_var.set(path)

    def browse_sub():
        path = filedialog.askopenfilename(title="Select Subtitles", filetypes=[("ASS files", "*.ass"), ("All files", "*.*")])
        if path:
            sub_var.set(path)

    def browse_images():
        path = filedialog.askdirectory(title="Select Images Directory")
        if path:
            img_var.set(path)

    def browse_output():
        path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if path:
            out_var.set(path)

    tk.Label(root, text="Audio MP3:").grid(row=0, column=0, sticky="e")
    tk.Entry(root, textvariable=audio_var, width=40).grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_audio).grid(row=0, column=2)

    tk.Label(root, text="Subtitles ASS:").grid(row=1, column=0, sticky="e")
    tk.Entry(root, textvariable=sub_var, width=40).grid(row=1, column=1)
    tk.Button(root, text="Browse", command=browse_sub).grid(row=1, column=2)

    tk.Label(root, text="Images Dir:").grid(row=2, column=0, sticky="e")
    tk.Entry(root, textvariable=img_var, width=40).grid(row=2, column=1)
    tk.Button(root, text="Browse", command=browse_images).grid(row=2, column=2)

    tk.Label(root, text="Output MP4:").grid(row=3, column=0, sticky="e")
    tk.Entry(root, textvariable=out_var, width=40).grid(row=3, column=1)
    tk.Button(root, text="Browse", command=browse_output).grid(row=3, column=2)

    def run():
        try:
            run_slideshow(audio_var.get(), sub_var.get(), img_var.get(), out_var.get())
            messagebox.showinfo("Success", f"Video saved to {out_var.get()}")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    tk.Button(root, text="Create Video", command=run).grid(row=4, column=1, pady=10)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Create video with karaoke subtitles")
    parser.add_argument('--gui', action='store_true', help='Launch graphical interface')
    parser.add_argument('--audio', help='Path to audio mp3 file')
    parser.add_argument('--subtitles', help='Path to ASS subtitle file')
    parser.add_argument('--images', help='Directory containing images')
    parser.add_argument('--output', default='output.mp4', help='Output video file')
    args = parser.parse_args()

    if args.gui:
        launch_gui()
        return

    if not all([args.audio, args.subtitles, args.images]):
        parser.error('audio, subtitles and images are required unless --gui is used')

    run_slideshow(args.audio, args.subtitles, args.images, args.output)

if __name__ == '__main__':
    main()
