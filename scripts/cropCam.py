from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop

def main(inputFile, OutputFile):
    clip = VideoFileClip(inputFile)
    (w, h) = clip.size
    y_center = (305 / 2) + 25  # Move the cropping area down by 25 pixels
    x_center = w - (407 / 2)

    cropped_clip = crop(clip, width=407, height=255, x_center=x_center, y_center=y_center)
    cropped_clip.write_videofile(OutputFile)

    clip.close()


if __name__ == "__main__":
    main("vidShort.mp4", "outputCam.mp4")