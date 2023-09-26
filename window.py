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
            is_completed = search_row_in_csv(
                values["-SEARCH-WORD-"],
                values["-FOLDER-INPUT-"],
                values["-FILE-INPUT-"],
            )
            if is_completed:
                sg.popup("Search completed!")
            else:
                sg.popup("Could not complete successfully!")

    window.close()


if __name__ == "__main__":
    main()
