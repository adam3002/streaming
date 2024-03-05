from scripts import cropCam, cropGameplay, cropLength, getFileName, join
import argparse

batchNumber = getFileName.run()
parser = argparse.ArgumentParser(description="Type name of file you want to crop")
parser.add_argument("cropfile", nargs='?', default=None, help="Name of file you want to use")
args = parser.parse_args()

numOfVids = input("How many videos do you want to generate? ")

for i in range(int(numOfVids)):
    if (args.cropfile != None):
        cropfile =  args.cropfile
    else:
        cropfile = "vid.mp4" # Edit this line with the name of the file you want to crop

    cropOutput = "outputCrop.mp4"
    camOutput = "outputCam.mp4"
    gameplayOutput = "outputGameplay.mp4"
    outputFile = "outputs/" + batchNumber + "-" + str(i + 1) + ".mp4"
    videoLength = 35 #SECONDS

    cropLength.main(cropfile, cropOutput, videoLength)
    cropCam.main(cropOutput, camOutput)
    cropGameplay.main(cropOutput, gameplayOutput)
    join.main(camOutput, gameplayOutput, outputFile)
