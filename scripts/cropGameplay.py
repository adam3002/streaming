import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop

def main(inputFile, OutputFile):
    clip = VideoFileClip(inputFile)
    (w, h) = clip.size
    cropped_clip = crop(clip, width=720, height=697.5, x_center=w/2, y_center=h/2)
    # cropped_clip = crop(clip, width=480, height=415, x_center=w/2, y_center=h/2)
    cropped_clip.write_videofile(OutputFile)
    clip.close()
    os.remove(inputFile)


if __name__ == "__main__":
    main("vidShort.mp4", "output gameplay.mp4")