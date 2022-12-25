# Youtube Content Loudness Scanner

If you run the compiled version you do not need to install anything.

To run the python file you need to install the requirements.
```
pip install -r requirements.txt
```

To compile you need the requirements and pyinstaller.
```
pip install -r requirements.txt
pip install pyinstaller
pyinstaller -F -i NONE .\ycls.py
```

Usage:
```
ycls -i <inputFile>
```

Alternatively, you can run the file and it will prompt you with an input file.
```
ycls
Input File: <inputFile>