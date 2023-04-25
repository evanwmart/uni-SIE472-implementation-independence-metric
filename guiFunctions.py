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
And here is my main.py: import guiFunctions as gf
import backendApis as be

hardwareCat = ['CPU Architecture', 'Wireless Comms',
               'Wired Comms', 'CPU Type', 'Firewall']
softwareCat = ['Firmware', 'OS', 'Firewall', 'Libraries & Frameworks',
               'Compiler', 'Languages']
secProtocolCat = ['Cryptography', 'Auth. Methods']
networkCat = ['Communication', 'Transmission', 'VPN']
dataManagementCat = ['Cloud Service', 'Database', 'DBMS', 'App. Protocol']

dropdownCells = [['-', '-', '-', '-'] * 20]

if __name__ == "__main__":
    print("Starting main ...")

    window = gf.genWindow("lightgray")
    table = gf.genTable(window, 21, 7, "gray", "lightgray")
    for col in range(len(gf.colTitles)):
        gf.writeCell(
            table, 0, col, gf.colTitles[col], 'white', "gray", ('Arial', 14, 'bold'))

    # Hardware
    hardwareCol = 'darkgray'
    gf.writeCell(table, 1, 0,
                 'Hardware', hardwareCol, "white", ('Arial', 14, 'bold'))
    for row in range(5):
        gf.writeCell(table, row+1, 1,
                     hardwareCat[row], hardwareCol, "white", ('Arial', 14))

    # Software
    softwareCol = 'gray'
    gf.writeCell(table, 6, 0,
                 'Software', softwareCol, "white", ('Arial', 14, 'bold'))
    for row in range(6):
        gf.writeCell(table, row+6, 1,
                     softwareCat[row], softwareCol, "white", ('Arial', 14))

    # Security Protocol
    secProtocolCol = 'darkgray'
    gf.writeCell(table, 12, 0,
                 'Security Protocol', secProtocolCol, "white", ('Arial', 14, 'bold'))
    for row in range(2):
        gf.writeCell(table, row+12, 1,
                     secProtocolCat[row], secProtocolCol, "white", ('Arial', 14))

    # Network
    networkCol = 'gray'
    gf.writeCell(table, 14, 0,
                 'Network', networkCol, "white", ('Arial', 14, 'bold'))
    for row in range(3):
        gf.writeCell(table, row+14, 1,
                     networkCat[row], networkCol, "white", ('Arial', 14))

    # Data Management
    dataManagementCol = 'darkgray'
    gf.writeCell(table, 17, 0,
                 'Data Management', dataManagementCol, "white", ('Arial', 14, 'bold'))
    for row in range(4):
        gf.writeCell(table, row+17, 1,
                     dataManagementCat[row], dataManagementCol, "white", ('Arial', 14))

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

        for c in range(2, len(gf.colTitles)):
            titleCell = table.grid_slaves(row=0, column=c)[0]

            if titleCell.cget("text") != "Uniqueness Score":
                gf.genDropdown(table, r, c, be.AllOptions[r-1],
                               bgcolor, "black", ('Arial', 12))

    gf.update(window)

    print("Main has concluded.")
