from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import backendApis as ba

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


class Display:
    def __init__(self, window):
        self.window = window
        self.cols = ["Categories", "Components"]
        self.rows = 21  # set the number of rows

        self.table_frame = tk.Frame(self.window)
        self.table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a new frame for the entry widget
        self.entry_frame = tk.Frame(self.window)
        self.entry_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

        # Add a label and an entry widget to the entry frame
        self.label = tk.Label(
            self.entry_frame, text="Add layer:")
        self.label.pack(side=tk.LEFT)
        self.entry = tk.Entry(self.entry_frame)
        self.entry.pack(side=tk.LEFT)

        # Add "+" button to add new columns
        add_col_button = tk.Button(
            self.entry_frame, text=" + ", command=self.add_column)
        add_col_button.pack(side=tk.LEFT, padx=5)

        # Create the treeview widget
        self.treeview = ttk.Treeview(
            self.table_frame, columns=self.cols, show="headings")
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add table headers
        for col in self.cols:
            self.treeview.heading(col, text=col)

        # Add table rows
        for i in range(self.rows):
            self.treeview.insert("", tk.END, values=["" for col in self.cols])

    def add_column(self):
        num_cols = len(self.treeview['columns'])
        col_index = '#{}'.format(num_cols)
        self.treeview['columns'] += (col_index,)
        content = self.entry.get()
        self.treeview.heading(col_index, text=content)
        for child in self.treeview.get_children():
            values = self.treeview.item(child)['values']
            values += ('',)
            self.treeview.item(child, values=values)


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
            print(colTitles)

    for r in range(1, 21):
        if r > 16:
            bgcolor = "lightgray"
        elif r > 13:
            bgcolor = "darkgray"
        elif r > 11:
            bgcolor = "lightgray"
        elif r > 5:
            bgcolor = "darkgray"
        elif r > 0:
            bgcolor = "lightgray"

        for c in range(2, len(colTitles)):
            writeCell(
                table, 0, c, colTitles[c], 'white', "gray", ('Arial', 14, 'bold'))
            genDropdown(
                table, r, c, ba.AllOptions[r-1], bgcolor, "black", ('Arial', 12))


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


window = Window()
display = Display(window.root)
window.root.mainloop()
