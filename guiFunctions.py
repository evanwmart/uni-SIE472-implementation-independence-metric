from tkinter import ttk
import tkinter as tk
from tkinter import simpledialog


class Window:
    def __init__(self):
        self.root = tk.Tk()
        # make the window full-screen
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)  # make the window always on top
        self.root.attributes('-alpha', 1.0)  # set the window opacity to 100%
        # quit on Escape key press
        self.root.bind(
            '<Escape>', lambda event: self.toggle_fullscreen(event))

    def toggle_fullscreen(self, event):
        self.root.attributes(
            '-fullscreen', not self.root.attributes('-fullscreen'))


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
    table = tk.Frame(window, bg=bgColor, bd=2, relief=tk.GROOVE)
    table.pack(expand=True, fill='both')
    for row in range(rows):
        table.grid_rowconfigure(row, weight=1)
    for col in range(cols):
        table.grid_columnconfigure(col, weight=1)
        cell = tk.Frame(table, bg=gridColor)
        cell.grid(row=0, column=col, sticky='nsew')
    return table


def genDropdown(table, row, col, options, bgColor, fgColor, font):
    var = tk.StringVar(value="-")
    dropdown = tk.OptionMenu(table, var, *options)
    dropdown.configure(bg=bgColor, fg=fgColor, font=font)
    dropdown.grid(row=row, column=col, sticky='nsew')


def compSet(optionMenu, list, posa, posb):
    list[posa][posb] = optionMenu.get()


def writeCell(table, row, col, content, bgColor, fgColor, font):
    label = tk.Label(
        table, text=content, bg=bgColor, fg=fgColor, font=font, bd=2, relief=tk.SOLID)
    label.grid(row=row, column=col, sticky='nsew')


def update(window):
    window.mainloop()


window = Window()
display = Display(window.root)
window.root.mainloop()
