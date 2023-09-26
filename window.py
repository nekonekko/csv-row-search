import PySimpleGUI as sg

from search import search_row_in_csv

def main():
    sg.theme("BlueMono")

    layout = [
        [
            sg.Text("Search word", size=(20, 1)),
            sg.InputText(
                key="-SEARCH-WORD-",
            ),
        ],
        [
            sg.Text("Folder to search", size=(20, 1)),
            sg.InputText(
                "",
                key="-FOLDER-INPUT-",
                enable_events=True,
            ),
            sg.FolderBrowse(button_text="Select", key="-FOLDER-BROWSE-"),
        ],
        [
            sg.Text("File to write search result", size=(20, 1)),
            sg.InputText(
                "",
                key="-FILE-INPUT-",
                enable_events=True,
            ),
            sg.FileBrowse(button_text="Select", key="-FILE-BROWSE-"),
        ],
        [sg.Submit()],
    ]

    window = sg.Window("CSVRowSearch", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Submit":
            search_word = values["-SEARCH-WORD-"]
            folder_input = values["-FOLDER-INPUT-"]
            file_input = values["-FILE-INPUT-"]
            if len(search_word) == 0 or len(folder_input) == 0 or len(file_input) == 0:
                sg.popup("Some fields are not filled!")
                continue
            is_completed = search_row_in_csv(
                search_word,
                folder_input,
                file_input,
            )
            if is_completed:
                sg.popup("Search completed!")
            else:
                sg.popup("Could not complete successfully!")

    window.close()


if __name__ == "__main__":
    main()
