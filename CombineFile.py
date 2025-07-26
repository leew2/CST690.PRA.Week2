import pandas as pd
import glob
import time
import os

# CombineFile.py
# Wang Lee
# This script is designed to combine multiple files into a single file.

def main():
    file_count, data = 0, 0
    path = "data/"                                               # your path to the files
    all_files = glob.glob(path + "*.xlsx")
    df_list = []
    print("File Name : Data Count")
    for file in all_files:                                              # loop through all files in the directory
        df = pd.read_excel(file)
        df_list.append(df)                                              # print the data in the file
        datacollection(df.values, "data", os.path.basename(file))       # data collection for metrics
        file_count += 1                                                 # data collection for metrics
    combined_df = pd.concat(df_list, ignore_index=True)                 # combine them
    combined_df.sort_values(by=combined_df.columns[0], inplace=True)
    combined_df.to_excel("main.xlsx", index=False)               # save them to file "...path.../main.xlsx"
    
# Metrics --------------------------------------------------------------
    datacollection(combined_df.values, "list", "Main.xlsx")
    print("--------------------------------------------------------")
    print("All files combined into main.xlsx")
# End of Metrics -------------------------------------------------------

def datacollection(passlist, type, name):
    data = 0
    for point in passlist:
        data += 1
    if type == "list":
        print(f"'{name}': {data}")
    elif type == "data":
        print(f"'{name}': {data}")

if __name__ == "__main__":
    time_start = time.process_time()                                    # data collection for metrics   
    main()
    time_end = time.process_time()                                      # data collection for metrics
    print(f"Time taken: {time_end - time_start} seconds")
