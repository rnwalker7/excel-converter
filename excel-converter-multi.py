import pandas as pd
import os
import sys

myDir = sys.argv[1]

for file in os.listdir(myDir):
    if file.lower().endswith(".xls"):
        df = pd.read_excel(file, engine="xlrd")
        newFile = file + "x"
        with pd.ExcelWriter(newFile, engine="openpyxl") as writer:
            df.to_excel(writer)
