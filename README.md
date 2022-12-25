# Youtube Content Loudness Scanner

If you run the compiled version you do not need to install anything.

To run the python file you need r128gain.
```
pip install r128gain
```

To compile you need r128gain and pyinstaller.
```
pip install r128gain
pip install pyinstaller
pyinstaller -F .\ycls.py
```

Usage:
```
ycls -i <inputFile>
```

Alternatively, you can run the file and it will prompt you with an input file.
```
ycls
Input File: <inputFile>