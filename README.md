# marcStats

This repository contains a small Python script to gather basic statistics from MARC files.

The script `stats003.py` accepts MARC XML files (`.xml`) or binary MARC files (`.mrc`).
For each supplied file, a report is produced listing the number of occurrences of each
MARC field. The report is saved to a file named `reportYYYYMMDD-HHMMSS.txt`.

## Requirements
* Python 3
* [pymarc](https://pypi.org/project/pymarc/)

Install dependencies with:

```bash
pip install pymarc
```

## Usage
Run the script from the command line providing one or more MARC files:

```bash
python stats003.py records.mrc another.xml
```

A report file will be created in the current directory summarizing the field counts
for each supplied file.
## An adaptation to a script originally designed by Ed Summers.

