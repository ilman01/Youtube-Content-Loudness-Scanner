import r128gain
import argparse
import readchar

parser = argparse.ArgumentParser(description="An analyser")
parser.add_argument("-i", type=str)

args = parser.parse_args()

inputFile = args.i
inputLUFS = None
inputPEAK = None
cmdMode = None

if not inputFile == None:
    inputLUFS = r128gain.get_r128_loudness([inputFile])[0]
    inputPEAK = r128gain.scale_to_gain(r128gain.get_r128_loudness([inputFile])[1])
    cmdMode = True
else:
    inputFile = input("Input File: ").replace('"','')
    inputLUFS = r128gain.get_r128_loudness([inputFile])[0]
    inputPEAK = r128gain.scale_to_gain(r128gain.get_r128_loudness([inputFile])[1])
    cmdMode = False

print(f"File Loudness: {inputLUFS} LUFS")

print(f"Peak Loudness: {round(inputPEAK, 1)} dBFS")

ContentLoudness = round(inputLUFS + 14, 1)

print(f"Youtube Content Loudness: {ContentLoudness} dB")

if cmdMode == False:
    print("Press Any Key To Exit")
    readchar.readchar()