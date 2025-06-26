# TurnerSubs

TurnerSubs creates a slideshow video from a set of images, an audio narration and an ASS subtitle file containing karaoke effects. The resulting MP4 highlights the lyrics as the narration plays.

## Installation

Install the Python dependencies and ensure `ffmpeg` is available on your system:

```bash
pip install moviepy ffmpeg-python
```

`ffmpeg` itself must also be installed and in your `PATH`.

## Usage

```bash
python -m turnersubs.main \
    --audio voice.mp3 \
    --subtitles karaoke.ass \
    --images images_directory \
    --output final.mp4
```

The images directory should contain numbered image files (png or jpg). They will be shown in order for equal slices of the audio duration.

## GUI

A minimal graphical interface is available and can be launched with:

```bash
python -m turnersubs.gui
```

Use the browse buttons to select the audio file, subtitle file, image directory
and output location, then click **Create Video**.
