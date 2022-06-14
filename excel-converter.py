import pandas as pd
import sys

myFile = sys.argv[1]

if myFile.lower().endswith(".xls"):
    df = pd.read_excel(myFile, engine="xlrd")
    newFile = myFile + "x"
    with pd.ExcelWriter(newFile, engine="openpyxl") as writer:
        df.to_excel(writer)
else:
    print("Invalid file format")