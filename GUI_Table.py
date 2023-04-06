import tkinter as tk
from tkinter import ttk


class Table:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.header_names = ['Components', 'Perception', 'Transport', 'Processing', 'Application', 'Uniqueness Score']
        self.create_table()

    def create_table(self):
        # Create table frame
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(side='left', padx=10, pady=10)

        # Create table headers
        self.header_labels = []
        for col in range(self.columns):
            header_label = ttk.Label(self.table_frame, text=self.header_names[col])
            header_label.grid(row=0, column=col, padx=5, pady=5)
            self.header_labels.append(header_label)

        # Create table rows and cells
        self.cells = {}
        row_names = ['CPU Architecture', 'Wireless Comms', 'Wired Comms', 'CPU Type', 'Firewall',
                     'Firmware', 'OS', 'Firewall', 'Lib & Framework', 'Compiler', 'Languages',
                     'Cryptography', 'Auth. Methods', 'Communication', 'Transmission', 'VPN',
                     'Cloud Service', 'Database', 'DBMS', 'App. Protocol']
        for row in range(20):
            # Create row label
            row_label = ttk.Label(self.table_frame, text=row_names[row])
            row_label.grid(row=row+1, column=0, padx=5, pady=5)

            for col in range(1, self.columns): # start from 1 to skip the first column
                # Create dropdown menu
                values = []
                if row == 0 and col == 1: # CPU Architecture row
                    values = ['Select','x86', 'x86_64', 'ARM', 'ARM64', 'MIPS', 'SPARC', 'PowerPC', 'Itanium']
                elif row == 1 and col == 1: # Wireless Comms row
                    values = ['Select',"Bluetooth", "WiFi", "NFC", "RFID", "GPS", "Zigbee", "Z-wave", "LoRa", "Sigfox", "LTE", "5G", "Satellite"]
                else:
                    values = ['Select','Option 1', 'Option 2', 'Option 3']
                var = tk.StringVar()
                var.set(values[0])
                dropdown = ttk.OptionMenu(self.table_frame, var, *values)
                dropdown.grid(row=row+1, column=col, padx=5, pady=5)

                # Add cell to dictionary
                self.cells[(row, col)] = var


    def get_values(self):
        # Print values of all cells
        row_names = ['CPU Architecture', 'Wireless Comms', 'Wired Comms', 'CPU Type', 'Firewall',
                     'Firmware', 'OS', 'Firewall', 'Lib & Framework', 'Compiler', 'Languages',
                     'Cryptography', 'Auth. Methods', 'Communication', 'Transmission', 'VPN',
                     'Cloud Service', 'Database', 'DBMS', 'App. Protocol']
        header_names = ['Components', 'Perception', 'Transport', 'Processing', 'Application', 'Uniqueness Score']
        for row in range(self.rows):
            component = row_names[row]
            for col in range(1, self.columns): # start from 1 to skip the first column
                value = self.cells[(row, col)].get()
                if col <= 5: # normal columns
                    header_name = header_names[col - 1] # subtract 1 to account for skipping first column
                    print(f'{component}, {header_name}: {value}')
                else: # score column
                    score = 0
                    if value == 'Option 1':
                        score = 1
                    elif value == 'Option 2':
                        score = 2
                    elif value == 'Option 3':
                        score = 3
                    print(f'{component}, {header_names[-1]}: {score}')



# Create tkinter window
root = tk.Tk()
root.title('Table Test')

# Create table with 21 rows and 6 columns
table = Table(root, rows=20, columns=6)

# Add a button to print cell values
button = tk.Button(root, text='Print Cell Values', command=table.get_values)
button.pack()

# Run tkinter window
root.mainloop()
