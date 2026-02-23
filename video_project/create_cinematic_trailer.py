
from moviepy.config import change_settings

change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-13-Q16-HDRI\magick.exe"
})

import os
import numpy as np
from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout
from PIL import Image, ImageDraw, ImageFont, ImageOps
from moviepy.editor import ImageClip

IMAGE_DURATION = 5
W, H = 1280, 720

def ken_burns_effect(clip):
    return clip.resize(lambda t: 1 + 0.05 * t)
'''
def create_section(folder):
    clips = []
    for img in sorted(os.listdir(folder)):
        if img.lower().endswith((".jpg", ".png", ".jpeg")):
            clip = ImageClip(os.path.join(folder, img)) \
                .set_duration(IMAGE_DURATION) \
                .resize((W, H)) \
                .fx(ken_burns_effect) \
                .fx(fadein, 1.5) \
                .fx(fadeout, 1.5)
            clips.append(clip)
    return clips

def create_section(folder):
    clips = []
    for img in sorted(os.listdir(folder)):
        if img.lower().endswith((".jpg", ".png", ".jpeg")):

            clip = ImageClip(os.path.join(folder, img))

            # Resize to fit inside 1280x720 WITHOUT cropping
            clip = clip.resize(height=720)

            # Center it on black background
            background = ColorClip((1280, 720), color=(0, 0, 0)).set_duration(5)
            clip = clip.set_position("center").set_duration(5)

            final = CompositeVideoClip([background, clip])

            # Very soft cinematic zoom (optional)
            final = final.resize(lambda t: 1 + 0.02 * t)

            clips.append(final.fadein(1).fadeout(1))

    return clips

'''
def create_section(folder):
    clips = []

    for img in sorted(os.listdir(folder)):
        if img.lower().endswith((".jpg", ".png", ".jpeg")):

            img_path = os.path.join(folder, img)

            # 🔧 FIX ROTATION USING EXIF DATA
            pil_img = Image.open(img_path)
            pil_img = ImageOps.exif_transpose(pil_img)  # <-- Fix rotation

            np_img = np.array(pil_img)

            # Create clip from corrected image
            clip = ImageClip(np_img)

            # Resize to fit inside 1280x720
            clip = clip.resize(height=720)

            # Black background
            background = ColorClip((1280, 720), color=(0, 0, 0)).set_duration(5)

            clip = clip.set_position("center").set_duration(5)

            final = CompositeVideoClip([background, clip])

            # Soft zoom
            final = final.resize(lambda t: 1 + 0.02 * t)

            clips.append(final.fadein(1).fadeout(1))

    return clips

def text_clip(text, duration=5):
    W, H = 1280, 720

    img = Image.new("RGB", (W, H), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()

    bbox = draw.multiline_textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((W - text_width) / 2, (H - text_height) / 2)

    draw.multiline_text(position, text, font=font, fill="white", align="center")

    np_img = np.array(img)

    clip = ImageClip(np_img).set_duration(duration).fadein(1).fadeout(1)

    return clip


# Intro text
intro = text_clip("Some love stories are written by destiny...\n\nOurs began in 2016...", 6)

# Sections
college = create_section("video_project/assets/college")
couple = create_section("video_project/assets/couple")
marriage = create_section("video_project/assets/marriage")
baby = create_section("video_project/assets/baby")

# Special text moments
marriage_text = text_clip("On 16.11.2024... Our forever began.\nOn 17.11.2024... We became one soul.", 6)
baby_text = text_clip("On 23.10.2025... Our little miracle arrived.\nOur greatest blessing.", 6)

# Final message
ending = text_clip("From 2016... to forever.\nI would choose you.\nAgain. And again. And again.", 8)

# Combine all

#all_clips = [intro] + college + couple  + [marriage_text] + marriage + [baby_text] + baby  + [ending]
all_clips= [intro]
final_video = concatenate_videoclips(all_clips, method="compose")

# Add music
audio = AudioFileClip("video_project/assets/music/music.mpeg")
audio = audio.subclip(0, final_video.duration)
final_video = final_video.set_audio(audio)

# Export
final_video.write_videofile("one.mp4", fps=24)
