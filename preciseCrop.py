import math
import argparse
from scripts import cropCam, cropGameplay, getFileName, join
from moviepy.video.io.VideoFileClip import VideoFileClip

def cropVideo(filename, time, length, outputFile):
    clip = VideoFileClip(filename)
    video_duration = math.floor(clip.duration)

    minutes, seconds = str(time).split('.')
    time = (int(minutes) * 60) + int(seconds)
    clip = clip.subclip(int(time), int(time) + int(length))

    clip.write_videofile(outputFile)
    clip.close()


def main():
    # parser = argparse.ArgumentParser(description="Add flags to help define what you want to crop")
    # parser.add_argument("filename", help="Name of file")
    # parser.add_argument("time", help="Time you want to start the clip at e.g 12.30 (12 minutes and 30 seconds)")
    # parser.add_argument("seconds", help="Number of seconds you want the clip to be")
    # args = parser.parse_args()

    filename = input("What is the name of the file ")
    time = input("Time you want to start the clip at e.g 12.30 (12 minutes and 30 seconds) ")
    seconds = input("Number of seconds you want the clip to be ")

    batchNumber = getFileName.run()

    cropOutput = "outputCrop.mp4"
    camOutput = "outputCam.mp4"
    gameplayOutput = "outputGameplay.mp4"
    outputFile = "outputs/" + batchNumber + "-" + str(1) + ".mp4"

    # cropVideo(args.filename, args.time, args.seconds, cropOutput)
    cropVideo(filename, time, seconds, cropOutput)
    cropCam.main(cropOutput, camOutput)
    cropGameplay.main(cropOutput, gameplayOutput)
    join.main(camOutput, gameplayOutput, outputFile)

if __name__ == "__main__":
    main()
