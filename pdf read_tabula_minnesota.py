import tabula
import sys
import os
import pandas as pd
import csv

input_path = r"C:\Users\sagar\Documents\Content Grabber 2\Agents\temasek_warn_minnesota\Debug\Files\mass-layoff-warn-report-april-2020_tcm1045-430922.pdf"
output_file_name = os.path.basename(input_path).replace(".pdf", ".csv")
output_dir_path = os.path.dirname(input_path)
output_path = output_dir_path + "\\" + output_file_name

df = tabula.read_pdf(input_path, pages ='all', guess = False, lattice=True)
list_df = []
for idx_number, chuked_df in enumerate(df):
    print(idx_number,chuked_df)