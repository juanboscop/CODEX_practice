import os
import argparse
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import ffmpeg

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

def main():
    parser = argparse.ArgumentParser(description="Create video with karaoke subtitles")
    parser.add_argument('--audio', required=True, help='Path to audio mp3 file')
    parser.add_argument('--subtitles', required=True, help='Path to ASS subtitle file')
    parser.add_argument('--images', required=True, help='Directory containing images')
    parser.add_argument('--output', default='output.mp4', help='Output video file')
    args = parser.parse_args()

    image_list = get_images(args.images)
    tmp_video = 'temp_video.mp4'
    create_slideshow(image_list, args.audio, tmp_video)
    add_subtitles(tmp_video, args.subtitles, args.output)
    os.remove(tmp_video)

if __name__ == '__main__':
    main()
