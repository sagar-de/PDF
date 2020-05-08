import tabula
import sys
import os
import pandas as pd
import csv

input_path = sys.argv[1]
output_file_name = os.path.basename(input_path).replace(".pdf", ".csv")
output_dir_path = os.path.dirname(input_path)
output_path = output_dir_path + "\\" + output_file_name

df = tabula.read_pdf(input_path, pandas_options={'header': None}, pages ='all', guess = True, lattice=True)

list_df = []
val_to_search = 'company name'
for idx_number, chuked_df in enumerate(df):
    #if (idx_number == 3):
    if isinstance(chuked_df, pd.DataFrame):
        chuked_df.columns = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7']
        company_name = chuked_df.loc[chuked_df['Col1'].astype(str).str.lower().str.contains("company name"), 'Col3'].iloc[0]
        type_of_event = chuked_df.loc[chuked_df['Col5'].astype(str).str.lower().str.contains("type of event"), 'Col7'].iloc[0]

        list_df.append({'company_name': company_name, 'event type': type_of_event})


valid_df = pd.DataFrame(list_df)

valid_df.to_csv(output_path, encoding='utf-8', index=False, quoting=1)

