# TurnerSubs

TurnerSubs creates a slideshow video from a set of images, an audio narration and an ASS subtitle file containing karaoke effects. The resulting MP4 highlights the lyrics as the narration plays.

## Usage

```bash
python -m turnersubs.main \
    --audio voice.mp3 \
    --subtitles karaoke.ass \
    --images images_directory \
    --output final.mp4
```

The images directory should contain numbered image files (png or jpg). They will be shown in order for equal slices of the audio duration.
