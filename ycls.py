import r128gain
import argparse
import readchar

parser = argparse.ArgumentParser(description="An analyser")
parser.add_argument("-i", type=str)

args = parser.parse_args()

inputFile = args.i
inputLUFS = None
cmdMode = None

if not inputFile == None:
    inputLUFS = r128gain.get_r128_loudness([inputFile])[0]
    cmdMode = True
else:
    inputFile = input("Input File: ").replace('"','')
    inputLUFS = r128gain.get_r128_loudness([inputFile])[0]
    cmdMode = False

print(f"File LUFS: {inputLUFS}")

ContentLoudness = round(inputLUFS + 14, 1)

print(f"Youtube Content Loudness: {ContentLoudness}dB")

if cmdMode == False:
    print("Press Any Key To Exit")
    readchar.readchar()