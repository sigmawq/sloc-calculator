# SLOC calculator
Tool for calculating SLOC

Usage:
```
sloc.py [-h] [--fe FE [FE ...]] [--de DE [DE ...]] [--d] [--debug] location

positional arguments:
  location              Location to calculate SLOC count in

optional arguments:
  -h, --help            show this help message and exit
  
  --fe FE [FE ...], --files-exclude FE [FE ...]
                        File types to exclude
                        
  --de DE [DE ...], --dir-exclude DE [DE ...]
                        Directories to exclude
                        
  --d                   Show detailed output
  --debug               Show debug info

```



**Example**:

Calculate SLOC of files in current folder and subfolders, recursively

In:
```
python3 sloc.py ./
```
Out:
```
225517 SLOC
```



There are a lot of other things in my project that I don't want to calculate, so let's things we don't need:

In:
```
python3 sloc.py ./ --de __pycache__ test_folder venv .git .idea --fe .gitignore .txt
```
Out:
```
126 SLOC
```
`--fe` specifies file types to be ignored
`--de` specifies directories to be ignored


Let's see info regarding every file in SLOC calculation:

In:
```
python3 sloc.py ./ --de __pycache__ test_folder venv .git .idea --fe .gitignore .txt --d
```
Out:
```
126 SLOC
./sloc.py : 36
./SlocCalculator.py : 90
```
