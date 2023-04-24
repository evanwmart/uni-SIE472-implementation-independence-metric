from tkinter import simpledialog
import tkinter as tk
import tkinter.ttk as ttk
import requests
import json
from datetime import datetime

# Link for API use and documentation (use the '+' next to 'Developers' for info):
# https://nvd.nist.gov/developers


def dateFormatter(m, d, y):
    if (m == -1):
        now = datetime.now()
        return datetime(now.year, now.month, now.day).strftime("%Y-%m-%dT%H:%M:%S.") + "000"
    else:
        return datetime(y, m, d).strftime("%Y-%m-%dT%H:%M:%S.") + "000"


def getCVEs(keyword, start_date=dateFormatter(1, 1, 2023), end_date=dateFormatter(-1, 0, 0), max_results=10):
    # url = f'https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate={}&pubEndDate={}'
    print(type(start_date))
    print(end_date)
    url = f'https://services.nvd.nist.gov/rest/json/cves/2.0/?keywordSearch={keyword}&pubStartDate={start_date}&pubEndDate={end_date}&resultsPerPage={str(max_results)}'
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        return_list = []
        data = json.loads(response.content)

        for item in data['vulnerabilities']:
            ID = item['cve']['id']
            pDate = item['cve']['published']
            description = item['cve']['descriptions'][0]['value']
            lmDate = item['cve']['lastModified']
            return_list.append([ID, pDate, description, lmDate])

        return return_list

    else:
        return ([["ERROR: ", str(response.status_code)]])


def CVEdictToList(CVE_list):
    print(CVE_list[0])
    print("\t", CVE_list[1])
    print("\t", CVE_list[2])
    print("\t", CVE_list[3])
    print("\n")


# mylist = getCVEs("Microsoft", dateFormatter(8, 4, 2021),
#                  dateFormatter(10, 21, 2021), 2)
# for i in mylist:
#     CVEdictToList(i)


class Table:
    def __init__(self, master):
        self.master = master
        self.cols = ["Name", "Age", "City"]
        self.table_frame = tk.Frame(self.master)
        self.table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create first treeview widget
        self.tree1 = ttk.Treeview(self.table_frame, columns=self.cols, show="headings")
        self.tree1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add table headers to first treeview
        for col in self.cols:
            self.tree1.heading(col, text=col, anchor=tk.CENTER)
            self.tree1.column(col, width=100, anchor=tk.CENTER)

        # Create second frame for second table
        self.table_frame2 = tk.Frame(self.table_frame)
        self.table_frame2.pack(side=tk.LEFT, padx=10)

        # Create second treeview widget
        self.tree2_cols = ["Country", "Language", "Population"]
        self.tree2 = ttk.Treeview(self.table_frame2, columns=self.tree2_cols, show="headings")
        self.tree2.pack(fill=tk.BOTH, expand=True)

        # Add table headers to second treeview
        for col in self.tree2_cols:
            self.tree2.heading(col, text=col, anchor=tk.CENTER)
            self.tree2.column(col, width=100, anchor=tk.CENTER)

        # Add "+" button to add new columns to first table
        add_col_button = tk.Button(self.master, text="Add Layer", command=self.add_column)
        add_col_button.pack(pady=10)

    def add_column(self):
        # Prompt user to enter the name/title of the next column
        title = tk.simpledialog.askstring(
            "Add column", "Enter the name/title of the next column:"
        )

        if title:
            # Add new column to first table
            self.cols.append(title)

            # Clear old table
            self.tree1.delete(*self.tree1.get_children())

            # Add updated table headers to first table
            for col in self.cols:
                self.tree1.heading(col, text=col, anchor=tk.CENTER)
                self.tree1.column(col, width=100, anchor=tk.CENTER)



root = tk.Tk()
table = Table(root)
root.mainloop()
