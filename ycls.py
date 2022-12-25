import r128gain
import argparse

parser = argparse.ArgumentParser(description="An analyser")
parser.add_argument("-i", type=str)

args = parser.parse_args()

inputFile = args.i
inputLUFS = ""

if not inputFile == None:
    inputLUFS = r128gain.get_r128_loudness([inputFile])[0]
else:
    inputFile = input("Input File: ").replace('"','')
    inputLUFS = r128gain.get_r128_loudness([inputFile])[0]

print(f"File LUFS: {inputLUFS}")

ContentLoudness = round(inputLUFS + 14, 1)

print(f"Youtube Content Loudness: {ContentLoudness}dB")