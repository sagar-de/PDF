import tabula
import sys
import os
import pandas as pd
import csv


input_path = sys.argv[1]#r"C:\Users\sagar\Documents\Content Grabber 2\Agents\temasek_warn_west virginia_test\Debug\Files\WV_WARN_Notices_3-1-11_to_4-7-20.pdf"
output_file_name = os.path.basename(input_path).replace(".pdf", ".csv")
output_dir_path = os.path.dirname(input_path)
output_path = output_dir_path + "\\" + output_file_name

df = tabula.read_pdf(input_path, pandas_options={'header': None}, pages ='all', guess = True, lattice=True)

list_df = []

val_to_search = 'address'

def create_df(input_text, previous_column):
    text_to_find = [
        "company", "address", "contact information", "region", "county",
        "date of notice", "projected date", "closure/mass layoff", "number affected"
    ]
    for idx, a in enumerate(text_to_find):
        if input_text.lower().startswith(a):
            try:
                return a, " ".join(input_text.split("###")[1:]), a
            except:
                return a, input_text, a

        if idx == 8:
            return previous_column, input_text, previous_column


for idx_number, chuked_df in enumerate(df):
    #if (idx_number == 1):
    if isinstance(chuked_df, pd.DataFrame):
        replaced_df = chuked_df.replace('\\r',' ', regex=True).replace('\\n',' ', regex=True)
        rec_dic = {}
        previous_column = ""
        for ifx, row in replaced_df.iterrows():
            try:
                concat_row = row.astype(str).str.cat(sep="###")
                concat_row = concat_row.replace("nan###", "").replace("###nan", "")
            except:
                print (row)
                continue

            key_colum, key_value, previous_column = create_df(concat_row, previous_column)
            if key_colum != "":
                rec_dic[key_colum] = (rec_dic.get(key_colum, " ") + " " + key_value).strip()

        list_df.append(rec_dic)

valid_df = pd.DataFrame(list_df)
valid_df.dropna(inplace=True)

valid_df.to_csv(output_path, encoding='utf-8', index=False, quoting=1)
print(output_path)