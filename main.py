import guiFunctions as gf

colTitles = ['Categories', 'Components', 'Perception Layer', 'Transport Layer',
             'Processing Layer', 'Application Layer', 'Uniqueness Score']
components = ['CPU Architecture', 'Wireless Comms', 'Wired Comms', 'CPU Type', 'Firewall', 'Firmware', 'OS', 'Firewall', 'Libraries & Frameworks',
              'Compiler', 'Languages', 'Cryptoography', 'Auth. Methods', 'Communication', 'Transmission', 'VPN', 'Cloud Service', 'Database', 'DBMS', 'App. Protocol']


if __name__ == "__main__":
    print("Starting main ...")

    window = gf.genWindow("black")
    table = gf.genTable(window, 21, 7, "white", "black")
    for col in range(7):
        gf.writeCell(
            table, 0, col, colTitles[col], "white", "black", ('Arial', 14, 'bold'))
    for row in range(20):
        gf.writeCell(table, row+1, 1,
                     components[row], "white", "black", ('Arial', 14, 'bold'))

    gf.update(window)

    print("Main has concluded.")
