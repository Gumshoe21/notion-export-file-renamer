# Notion Export File Renamer

## The Problem

When you export files from Notion, the name of each exported file and folder is appended with an ugly GUID (yuck!):

![Notion Export - Raw Output](./Notion%20Export%20-%20Raw%20Output.png)

## The Solution:

1. Place the folder containing your newly exported Notion files into a folder that contains only the 'notion-export-file-renamer.py' script. The folder containing your exported Notion files will be named something like this:

```
Export-95fc3bc8-a529-4c39-b414-16d278c7d197
```

Your working directory folder structure should look like this:

```
root/
├─ Export-95fc3bc8-a529-4c39-b414-16d278c7d197/
├─ notion-export-file-renamer.py
```

2.  Run this script from the root dir - again, this script should be placed in the same folder as the folder containing your exported Notion files.

```shell
python3 notion-export-file-renamer.py
```

3.  ???
4.  Profit! Your output should look like this:

![Notion Files - Renamed Output](./Notion%20Export%20-%20Renamed%20Output.png)

## Enjoy!
