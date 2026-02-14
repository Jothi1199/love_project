import os
from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout

# Duration per image (seconds)
IMAGE_DURATION = 4

def create_section(folder_path):
    clips = []
    for img in sorted(os.listdir(folder_path)):
        if img.endswith((".jpg", ".jpeg", ".png")):
            clip = ImageClip(os.path.join(folder_path, img)) \
                .set_duration(IMAGE_DURATION) \
                .resize(height=720) \
                .fx(fadein, 1) \
                .fx(fadeout, 1)
            clips.append(clip)
    return clips

# Load all sections
college = create_section("video_project/assets/college")
couple = create_section("video_project/assets/couple")
marriage = create_section("video_project/assets/marriage")
baby = create_section("video_project/assets/baby")

all_clips = college + couple + marriage + baby

# Combine
final_video = concatenate_videoclips(all_clips, method="compose")

# Add music
audio = AudioFileClip("video_project/assets/music/music.mpeg").subclip(0, final_video.duration)
final_video = final_video.set_audio(audio)

# Export
final_video.write_videofile("Our_Love_Story.mp4", fps=24)
