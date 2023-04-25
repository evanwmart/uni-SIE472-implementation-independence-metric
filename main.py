import guiFunctions as gf
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

    gf.update(window)

    print("Main has concluded.")
