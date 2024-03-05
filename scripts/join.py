import os
from moviepy.editor import VideoFileClip, clips_array
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop

def main(inputFile1, inputFile2, outputFile):
    # Load the two video clips
    clip1 = VideoFileClip(inputFile1)
    clip2 = VideoFileClip(inputFile2)
    
    # Resize the clips to have the same width
    w, _ = clip1.size
    clip2 = clip2.resize(width=w)
    
    # Stack the clips vertically
    final_clip = clips_array([[clip1], [clip2]])
    
    # Write the final clip to the output file
    final_clip.write_videofile(outputFile)
    
    # Close the original clips
    clip1.close()
    clip2.close()

    os.remove(inputFile1)
    os.remove(inputFile2)


if __name__ == "__main__":
    main("output cam.mp4", "output gameplay.mp4", "output join.mp4")