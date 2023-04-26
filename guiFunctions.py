import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from datetime import datetime
import backendApis as ba
from tkinter import filedialog
from reportlab.pdfgen import canvas
import shutil
import collections

colTitles = ['Categories', 'Components', 'Uniqueness Score']
diversityScore = 0
dropDownCells = []
richardosDictionary = {
    'CPU Architecture': [],
    'Wireless Communications': [],
    'Wired Communications': [],
    'CPU Type': [],
    'Hardware Firewall': [],
    'Firmware': [],
    'Operating System': [],
    'Software Firewall': [],
    'Libraries & Frameworks': [],
    'Compiler': [],
    'Implementation Language': [],
    'Cryptography': [],
    'Authentication Method': [],
    'Communication': [],
    'Transmission': [],
    'VPN': [],
    'Cloud Service ': [],
    'Database': [],
    'DBMS': [],
    'Application Protocol': []
}


def genWindow(bgColor):
    root = tk.Tk()
    root.geometry("1000x500")
    root.title("IILA Metric")
    root.configure(bg=bgColor)
    root.attributes('-fullscreen', True)  # make the window full-screen
    root.attributes('-topmost', True)  # make the window always on top
    root.attributes('-alpha', 1.0)  # set the window opacity to 100%
    # quit on Escape key press
    root.bind('<Escape>', lambda event: toggle_fullscreen(event, root))

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=0)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

    return root


def toggle_fullscreen(event, root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))


def genTable(window, rows, cols, gridColor, bgColor):
    table = tk.Frame(window, bg=bgColor, bd=2,
                     relief=tk.GROOVE, padx=5, pady=5)
    table.grid(column=0, row=0, columnspan=5, rowspan=20, sticky="wens")
    for row in range(rows):
        table.grid_rowconfigure(row, weight=1)
    for col in range(cols):
        table.grid_columnconfigure(col, weight=1)
        cell = tk.Frame(table, bg=gridColor)
        cell.grid(row=0, column=col, sticky='wens')

    # Add Layer trio
    addLayerLabel = tk.Label(window, text="Enter Layer Name to Add:",
                             background="lightgray", foreground="black", width=20)
    addLayerLabel.grid(column=5, row=0, padx=5, pady=5, sticky="ew")

    addLayerEntry = tk.Entry(window, background="black", foreground="white")
    addLayerEntry.grid(column=5, row=1, padx=5, pady=5, sticky="ew")
    addLayerEntry.focus_set()

    addLayerButton = tk.Button(
        window, text="Add Layer", command=lambda: addNewColumn(window, table, addLayerEntry), highlightbackground="lightgray", fg="navy")
    addLayerButton.grid(column=5, row=2, padx=5, pady=5, sticky="ew")

    # Set starting date duo
    startDateLabel = tk.Label(window, text="CVE Search Start Date (Month/Year):",
                              background="lightgray", foreground="black")
    startDateLabel.grid(column=5, row=3, padx=5, pady=5, sticky="ew")

    year_var = tk.StringVar()
    month_var = tk.StringVar()

    startDateLabel = tk.Label(
        window, background="lightgray", width=20, highlightbackground="lightgray")
    startDateLabel.grid(column=5, row=4, padx=5, pady=5, sticky="ew")
    month_combo = ttk.Combobox(startDateLabel, width=6, textvariable=month_var,
                               values=list(range(1, 13)))
    year_combo = ttk.Combobox(startDateLabel, width=6, textvariable=year_var,
                              values=list(range(2000, datetime.today().year+1)))
    month_combo.pack(fill="x")
    year_combo.pack(fill="x")

    genPDFButton = tk.Button(
        window, text="Generate Report", command=lambda: genPDF(window, genPDFButton), highlightbackground="lightgray", fg="navy")
    genPDFButton.grid(column=5, row=5, padx=5, pady=5, sticky="ew")

    return table


def addNewColumn(window, table, addEntryWidget):
    if len(colTitles) < 7:
        newColTitle = addEntryWidget.get()
        if newColTitle is not None:
            dropDownCells.append(["-"] * 20)
            for k in richardosDictionary:
                richardosDictionary[k].append("-")
            newColIndex = colTitles.index("Uniqueness Score")
            colTitles.insert(newColIndex, newColTitle)
            c = len(colTitles) - 2
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
                genDropdown(window, table, r, c, ba.AllOptions[r-1],
                            bgcolor, "black", ('Arial', 12), )
    for c in range(len(colTitles)):
        writeCell(
            table, 0, c, colTitles[c], 'white', "gray", ('Arial', 14, 'bold'))


def genDropdown(window, table, row, col, options, bgColor, fgColor, font):
    var = tk.StringVar(value="-")
    dropdown = tk.OptionMenu(table, var, *options,
                             command=lambda selection: dropSelection(window, table, row, col, var))
    dropdown.configure(bg=bgColor, fg=fgColor, font=font)
    dropdown.grid(row=row, column=col, sticky='nsew')


def dropSelection(window, table, row, col, var):
    dropDownCells[col-2][row-1] = var.get()
    uScores = calcUniqueness()
    for i, s in enumerate(uScores):
        bgcolor = "#{:02X}{:02X}{:02X}".format(
            int(255 * (1-s)), 0, int(255 * s))
        writeCell(table, i+1, len(colTitles) - 1, str(s),
                  bgcolor, "white", ('Arial', 14, 'bold'))
    dScore = calcMetric(uScores)
    circleMet(window, dScore)


def calcUniqueness():
    scores = []
    for i in range(0, len(dropDownCells[0])):
        key = list(richardosDictionary.keys())[i]
        for j in range(0, len(dropDownCells)):
            richardosDictionary[key][j] = dropDownCells[j][i]

    for k in richardosDictionary:
        countDict = collections.Counter(richardosDictionary[k])
        numUniqueTypes = len(countDict)
        mostLayers = max(countDict.values())

        if numUniqueTypes == 4 and mostLayers == 1:
            scores.append(1.0)
        elif numUniqueTypes == 3 and mostLayers == 2:
            scores.append(0.75)
        elif numUniqueTypes == 2 and mostLayers == 2:
            scores.append(0.50)
        elif numUniqueTypes == 2 and mostLayers == 3:
            scores.append(0.25)
        else:
            scores.append(0.0)

    return scores


def calcMetric(uScores):
    dScore = 0
    for i in uScores:
        dScore += i
    return dScore / len(uScores)


def compSet(optionMenu, list, posa, posb):
    list[posa][posb] = optionMenu.get()


def writeCell(table, row, col, content, bgColor, fgColor, font):
    label = tk.Label(
        table, text=content, bg=bgColor, fg=fgColor, font=font, bd=1, relief=tk.RAISED, highlightbackground="white")
    label.grid(row=row, column=col, sticky='nsew')


def genPDF(window, genPDFButton):
    # Disable the button to prevent multiple PDF generation
    genPDFButton.config(state="disabled")

    # Generate the PDF file
    c = canvas.Canvas("example.pdf")
    c.drawString(100, 750, "Hello World")
    c.save()

    window.overrideredirect(True)
    window.after_idle(window.attributes, '-topmost', False)

    #

    # Prompt the user for a file save location
    filepath = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")])

    # If the user selected a file, move the generated PDF to that location
    if filepath:
        import shutil
        shutil.move("example.pdf", filepath)

    window.overrideredirect(False)
    window.attributes('-topmost', True)

    # Re-enable the button once the PDF generation is complete
    genPDFButton.config(state="normal")


def circleMet(window, score):

    canvas = tk.Canvas(window, width=26, height=26,
                       bg="lightgray", highlightthickness=0)
    canvas.grid(row=6, column=5, rowspan=4, sticky="nsew")

    bgcolor = "#{:02X}{:02X}{:02X}".format(
        int(255 * (1-score)), 0, int(255 * score))

    # draw the first circle (larger)
    canvas.create_oval(10, 10, 230, 230, fill=bgcolor, outline="white")

    canvas.create_arc(10, 10, 230, 230, start=90, extent=int(score*360),
                      fill="green", outline="white", style=tk.PIESLICE)

    # draw the second circle (smaller)
    canvas.create_oval(40, 40, 200, 200, fill="lightgray", outline="white")

    # write the numeric value in the center of the top circle
    canvas.create_text(120, 120, text=str(score), font=(
        "Arial", 40, "bold"), fill="black")

    return canvas


def update(window):
    window.mainloop()
