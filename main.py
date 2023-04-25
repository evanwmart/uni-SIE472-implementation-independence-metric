import guiFunctions as gf
import backendApis as be

colTitles = ['Categories', 'Components', 'Perception Layer', 'Transport Layer',
             'Processing Layer', 'Application Layer', 'Uniqueness Score']
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
    for col in range(7):
        gf.writeCell(
            table, 0, col, colTitles[col], 'white', "gray", ('Arial', 14, 'bold'))

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

        for c in range(2, 6):
            gf.genDropdown(table, r, c, be.AllOptions[r-1],
                           bgcolor, "black", ('Arial', 12))

    gf.update(window)

    print("Main has concluded.")
