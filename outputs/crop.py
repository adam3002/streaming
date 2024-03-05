import math
import argparse
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def cropVideo(filename, end, seconds):
    tempFilename = "1" + filename
    clip = VideoFileClip(filename)
    video_duration = math.floor(clip.duration)

    if (end ==True):
        # Crop end of vid
        clip = clip.subclip(0,  video_duration - int(seconds))
    else:
        # Crop start of vid
        clip = clip.subclip(int(seconds), video_duration)

    clip.write_videofile(tempFilename)
    clip.close()
    # Delete original file and rename new file to original filename
    os.remove(filename)
    os.rename(tempFilename, filename)


def main():
    # parser = argparse.ArgumentParser(description="Add flags to help define what you want to crop")
    # parser.add_argument("filename", help="Name of file")
    # parser.add_argument("end", help="s for start or e for end")
    # parser.add_argument("seconds", help="Number of seconds you want to crop by")
    # args = parser.parse_args()

    filename = input("What is the name of the file")
    end = input("Do you want to crop the start or end the clip")
    seconds = input("Number of seconds  you want to crop by")


    end = True
    if (end.lower() == 's' or end.lower() == 'start'):
        end = False

    cropVideo(filename, end, seconds)

if __name__ == "__main__":
    main()
