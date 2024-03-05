import math
import random
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop

def main(inputFile, outputFile, videoLength):
    clip = VideoFileClip(inputFile)
    video_duration = math.floor(clip.duration)
    start_time = random.randint(0, video_duration - videoLength)
    clip = clip.subclip(start_time, start_time + videoLength)
    clip.write_videofile(outputFile)
    clip.close()


if __name__ == "__main__":
    main("vid.mp4", "cropLength.mp4", 30)