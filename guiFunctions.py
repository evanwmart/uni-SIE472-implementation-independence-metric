import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

colTitles = ['Categories', 'Components', 'Uniqueness Score']


def genWindow(bgColor):
    root = tk.Tk()
    root.configure(bg=bgColor)
    root.attributes('-fullscreen', True)  # make the window full-screen
    root.attributes('-topmost', True)  # make the window always on top
    root.attributes('-alpha', 1.0)  # set the window opacity to 100%
    # quit on Escape key press
    root.bind('<Escape>', lambda event: toggle_fullscreen(event, root))
    return root


def toggle_fullscreen(event, root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))


def genTable(window, rows, cols, gridColor, bgColor):
    table = tk.Frame(window, bg=bgColor, bd=2,
                     relief=tk.GROOVE, padx=5, pady=5)
    table.pack(expand=True, fill='both')
    for row in range(rows):
        table.grid_rowconfigure(row, weight=1)
    for col in range(cols):
        table.grid_columnconfigure(col, weight=1)
        cell = tk.Frame(table, bg=gridColor)
        cell.grid(row=0, column=col, sticky='nsew')

    addEntryWidget = tk.Entry(text="Add Layer")
    addEntryWidget.pack(side="left", anchor="w", padx=10, pady=5)
    addColumnButton = tk.Button(
        window, text="Add Layer", command=lambda: addNewColumn(table, addEntryWidget))
    addColumnButton.pack(side="left", anchor="w", padx=10, pady=5)
    return table


def addNewColumn(table, addEntryWidget):
    if len(colTitles) < 7:
        newColTitle = addEntryWidget.get()
        if newColTitle is not None:
            newColIndex = colTitles.index("Uniqueness Score")
            colTitles.insert(newColIndex, newColTitle)
            for row in range(21):
                writeCell(table, row, newColIndex, "-",
                        'white', "gray", ('Arial', 12))
            for col in range(newColIndex, len(colTitles)):
                writeCell(
                    table, 0, col, colTitles[col], 'white', "gray", ('Arial', 14, 'bold'))


def genDropdown(table, row, col, options, bgColor, fgColor, font):
    var = tk.StringVar(value="-")
    dropdown = tk.OptionMenu(table, var, *options)
    dropdown.configure(bg=bgColor, fg=fgColor, font=font)
    dropdown.grid(row=row, column=col, sticky='nsew')


def compSet(optionMenu, list, posa, posb):
    list[posa][posb] = optionMenu.get()


def writeCell(table, row, col, content, bgColor, fgColor, font):
    label = tk.Label(
        table, text=content, bg=bgColor, fg=fgColor, font=font, bd=1, relief=tk.RAISED, highlightbackground="white")
    label.grid(row=row, column=col, sticky='nsew')


def update(window):
    window.mainloop()


