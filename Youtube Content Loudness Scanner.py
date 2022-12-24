import r128gain

inputFile = input("Enter File: ")

inputLUFS = r128gain.get_r128_loudness([inputFile])[0]
print(f"File LUFS: {inputLUFS}")

ContentLoudness = round(inputLUFS + 14, 1)

print(f"Youtube Content Loudness: {ContentLoudness}dB")

input("Press Enter to Continue: ")