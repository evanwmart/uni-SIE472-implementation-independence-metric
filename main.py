import guiFunctions as gf

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

# Hardware
CPUArchitectureOps = ['x86', 'x86_64', 'ARM',
                      'ARM64', 'MIPS', 'SPARC', 'PowerPC', 'Itanium']
wirelessCommsOps = ["Bluetooth", "WiFi", "NFC", "RFID", "GPS",
                    "Zigbee", "Z-wave", "LoRa", "Sigfox", "LTE", "5G", "Satellite"]
wiredCommsOps = ["Ethernet",    "USB",    "Serial cable",    "Parallel cable",    "HDMI",    "DVI",    "VGA",    "DisplayPort",
                 "Thunderbolt",    "FireWire",    "Coaxial cable",    "Optical fiber",    "RJ45 connector",    "RS-232",    "RS-485"]
CPUTypeOps = ['AMD Ryzen 5', 'AMD Ryzen 7', 'AMD Ryzen 9', 'AMD Threadripper', 'Apple A10', 'Apple A11', 'Apple A12', 'Apple A13', 'Apple A14', 'Apple A15', 'Apple M1', 'ARM Cortex-M', 'Atmel AVR', 'Intel i3', 'Intel i5',
              'Intel i7', 'Intel i9', 'Intel Pentium', 'Intel Quark', 'Intel Xeon', 'MediaTek', 'Nordic Semiconductor', 'NVIDIA Tegra X1', 'NXP I.MX', 'Qualcomm Snapdagon', 'Raspberry Pi', 'Samsung Exynos', 'STMicroelectronics', 'TI MSP430']
hFirewallOps = ['Deep Packet Inspection', 'Industrial Control System', 'IDPS Firewall',
                'Next-Generation', 'Proxy', 'Unified Threat Management', 'VPN Firewall']
# Software
firmwareOps = ['Application', 'Bluetooth', 'Bootloader', 'NFC', 'Network protocol', 'Network',
               'Over-the-air (OTA)', 'Peripheral', 'Radio', 'RFID', 'Real-time operating system (RTOS)', 'Security', 'Sensor', 'Thread', 'Zigbee']
OSOps = ['Android', 'Chrome OS', 'Contiki', 'Embedded Linux', 'FreeBSD', 'FreeRTOS', 'iOS',
         'Linux', 'macOS', 'mbed OS', 'RIOT', 'Solaris', 'TinyOS', 'Unix', 'Windows', 'Zephyr']
sFirewallOps = ['Application-level gateway', 'Circuit-level gateway', 'Container', 'Host-based',
                'Hybrid', 'Next-generation', 'Packet filtering', 'Stateful inspection', 'Virtual']
libFrameworksOps = ['.NET Framework', 'ASP.NET', 'Angular', 'Backbone.js', 'Bootstrap', 'Bulma', 'CodeIgniter', 'Django', 'Express', 'Flask', 'Flask RESTful', 'Foundation', 'Hibernate', 'Ionic', 'jQuery', 'jQuery Mobile', 'Knockout.js', 'Kotlin', 'Laravel', 'Materialize', 'NativeScript', 'Node.js',
                    'NumPy', 'OpenCV', 'Pandas', 'PhoneGap/Cordova', 'PostgreSQL', 'PyTorch', 'Rails API', 'React', 'React Native', 'Redis', 'Ruby on Rails', 'RubyGems', 'Scala', 'Semantic UI', 'Sencha Touch', 'Spring', 'SQLite', 'Symfony', 'Tailwind CSS', 'TensorFlow', 'TypeScript', 'UIKit', 'Vue.js', 'Xamarin']
compilerOps = ['Borland C++', 'Clang', 'GCC', 'G++', 'GHC', 'Go Compiler', 'Intel C++ Compiler', 'Java Compiler', 'Kotlin Compiler',
               'LLVM-GCC', 'Pelles C', 'Rust Compiler', 'Swift Compiler', 'TCC', 'Turbo C++', 'TypeScript Compiler', 'Visual C++']
languageOps = ['Ada', 'ActionScript', 'ARM', 'Bash', 'Blockly', 'C', 'C#', 'C++', 'COBOL', 'Dart', 'F#', 'Fortran', 'Go', 'Groovy', 'Haskell', 'HTML/CSS', 'Java', 'JavaScript', 'Julia', 'Kotlin', 'Lisp', 'Lua', 'MATLAB',
               'MIPS', 'Objective-C', 'Pascal', 'Perl', 'PHP', 'Prolog', 'Python', 'R', 'Ruby', 'Rust', 'Scala', 'Scratch', 'Smalltalk', 'Solidity', 'SQL', 'Swift', 'Tcl', 'TypeScript', 'Visual Basic', 'XML/JSON', 'x86', 'Zsh']

# Security Protocol
cryptographyOps = ['AES', 'Blowfish', 'DES', 'Diffie-Hellman key exchange', 'Digital Signatures', 'ECC', 'HMAC', 'IPsec',
                   'Kerberos', 'MD5', 'OpenSSH', 'PBKDF2', 'PGP', 'RC4', 'RSA', 'SHA', 'TLS/SSL', 'Triple DES', 'Twofish', 'WPA2']
authMethodOps = ['Biometric', 'Certificate-based', 'Email-based', 'Federated identity', 'Kerberos', 'Knowledge-based', 'Multi-factor',
                 'OAuth', 'OpenID Connect', 'Passwordless', 'Risk-based', 'Single sign-on (SSO)', 'SMS-based', 'Smart card', 'SSH key', 'Time-based one-time password (TOTP)', 'Token-based', 'Two-factor (2FA)']

# Network
communicationOps = ['Bluetooth', 'CAN bus', 'Cellular/mobile', 'DNS', 'Distributed systems and messaging protocols', 'Ethernet', 'FTP', 'HTTP', 'Instant messaging and chat protocols',
                    'NFC', 'RFID', 'SONET', 'SMTP', 'Satellite', 'VPN (Virtual Private Network)', 'Video conferencing and collaboration tools', 'Wi-Fi', 'Zigbee']
transmissionOps = ['Broadband over Power Lines (BPL)', 'Bluetooth', 'Coaxial', 'Deep Space Network (DSN)', 'Ethernet', 'Infrared', 'Li-Fi', 'Microwave', 'Optical', 'Power line',
                   'Radio', 'Satellite', 'Terrestrial Microwave', 'IoT Transmission', 'Ultra-wideband (UWB)', 'Wifi']
VPNOps = ['BGP', 'DMVPN', 'GETVPN', 'GRE', 'IPsec', 'IKEv2', 'L2TP/IPSec', 'MPLS',
          'Mobile', 'Open', 'PPTP', 'Remote Access', 'SSL/TLS', 'SSTP', 'Site-to-Site']

# Data Management
# cloudServiceOps =
# databaseOps =
# DBMSOps =
# appProtocolOps =


if __name__ == "__main__":
    print("Starting main ...")

    window = gf.genWindow("black")
    table = gf.genTable(window, 21, 7, "white", "black")
    for col in range(7):
        gf.writeCell(
            table, 0, col, colTitles[col], 'cyan', "black", ('Arial', 14, 'bold'))

    # Hardware
    hardwareCol = 'Slategray1'
    gf.writeCell(table, 1, 0,
                 'Hardware', hardwareCol, "black", ('Arial', 14, 'bold'))
    for row in range(5):
        gf.writeCell(table, row+1, 1,
                     hardwareCat[row], hardwareCol, "black", ('Arial', 14))

    # Software
    softwareCol = 'Slategray3'
    gf.writeCell(table, 6, 0,
                 'Software', softwareCol, "black", ('Arial', 14, 'bold'))
    for row in range(6):
        gf.writeCell(table, row+6, 1,
                     softwareCat[row], softwareCol, "black", ('Arial', 14))

    # Security Protocol
    secProtocolCol = 'Slategray1'
    gf.writeCell(table, 12, 0,
                 'Security Protocol', secProtocolCol, "black", ('Arial', 14, 'bold'))
    for row in range(2):
        gf.writeCell(table, row+12, 1,
                     secProtocolCat[row], secProtocolCol, "black", ('Arial', 14))

    # Network
    networkCol = 'Slategray3'
    gf.writeCell(table, 14, 0,
                 'Network', networkCol, "black", ('Arial', 14, 'bold'))
    for row in range(3):
        gf.writeCell(table, row+14, 1,
                     networkCat[row], networkCol, "black", ('Arial', 14))

    # Data Management
    dataManagementCol = 'Slategray1'
    gf.writeCell(table, 17, 0,
                 'Software', dataManagementCol, "black", ('Arial', 14, 'bold'))
    for row in range(4):
        gf.writeCell(table, row+17, 1,
                     dataManagementCat[row], dataManagementCol, "black", ('Arial', 14))

    # for row in range()
    # gf.genDropdown(table, 1, 2, CPUArchitectureOps,
    #                "black", "lightcyan", ('Arial', 12, 'bold'), command=lambda selectedOption: gf.compSet(optionMenu, lst, 0, 1))

    gf.update(window)

    print("Main has concluded.")
