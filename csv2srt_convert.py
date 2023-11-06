"""
SRTMaker
Requirement : Python3 , Pandas Library

This script uses python3 to convert excel file into .srt file (used for subtitle in videos)
excel file should be in following format
Column 1: Text
Column 2: start timing in (hh:mm:ss) format
Column 3: milliseconds
Column 4: end timing in (hh:mm:ss) format
Column 5: milliseconds

Start from first row - first column (A1) WITHOUT headers
"""
import pandas as pd
import os
import pysrt
import sys

input_file = r"d:\youtuber\dongjiang\ep31_古竹到观音阁_沥口电站\ep31_subtitles.csv"

column_names = ["Start Time", "End Time", "Transcript"]
df = pd.read_csv(input_file)
counter = 1

base, ext = os.path.splitext(input_file)
output_file = base + ".srt"
# subs = pysrt.open(output_file)
# sys.exit()
# with open(output_file, "w", encoding="UTF-8") as file:
with open(output_file, "w", encoding="utf-8-sig") as file:
    for index, row in df.iterrows():
        if pd.isna(row["Transcript"]):
            continue
        text = row["Transcript"]
        start_time = row["Start Time"]
        end_time = row["End Time"]
        milli1 = "{:03d}".format(int(int(start_time.split(":")[-1]) / 30 * 1000))
        milli2 = "{:03d}".format(int(int(end_time.split(":")[-1]) / 30 * 1000))
        start_time = start_time[:-3]
        end_time = end_time[:-3]
        print(
            "%d\n%s,%s --> %s,%s\n%s\n"
            % (counter, start_time, milli1, end_time, milli2, text),
            file=file,
        )
        counter += 1
