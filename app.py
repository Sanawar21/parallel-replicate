from src.utils import status, start_vps, close_vps, restore_dirs, paths
from src import video
from moviepy.editor import VideoFileClip
import os


def generate():
    # try:
    video.generate_video()
    status.set(status.enhancing_video)
    video.enhance_video()
    video.merge_audio_and_video(video=VideoFileClip(str(paths.enhanced_video)))
    return status.done
    # except Exception as e:
    #     return e
