import glob
import re
import os

import PySimpleGUI as sg
import pandas as pd


def search_row_in_csv(search_word, search_folder_path, result_excel_path):
    search_word = search_word.lower()
    
    csv_path_list = []
    for file_path in glob.glob("**", recursive=True, root_dir=search_folder_path):
        if re.search("\.csv$", file_path):
            csv_path_list.append(file_path)

    layout = [
        [
            sg.ProgressBar(
                len(csv_path_list), orientation="h", size=(30, 10), key="-PROG-"
            )
        ],
        [sg.Text(key="-CURRENT-FILE-NAME-")],
    ]
    window = sg.Window("Progress", layout)

    result_list = []
    for i, csv_path in enumerate(csv_path_list):
        event, _ = window.read(timeout=10, timeout_key="-READ-NEXT-FILE-")

        if event == sg.WIN_CLOSED:
            window.close()
            return False
        elif event == "-READ-NEXT-FILE-":
            window["-CURRENT-FILE-NAME-"].update(csv_path)

            df = pd.read_csv(os.path.join(search_folder_path, csv_path), dtype=str)
            df.fillna("", inplace=True)
            match_index_set = set()
            for i_col in range(len(df.columns)):
                ser_str = df.iloc[:, i_col]
                ser_matched = ser_str.str.lower().str.contains(search_word)
                for match_index in ser_str[ser_matched].index:
                    match_index_set.add(match_index)
            result_list += df.loc[list(match_index_set)].values.tolist()
            window["-PROG-"].update(i + 1)

    pd.DataFrame(result_list).to_excel(result_excel_path, index=False, header=False)

    window.close()
    return True
