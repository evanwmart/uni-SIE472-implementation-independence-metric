import tkinter as tk
import tkinter.ttk as ttk
import requests
import json
from datetime import datetime

# Link for API use and documentation (use the '+' next to 'Developers' for info):
# https://nvd.nist.gov/developers

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

cloudServiceOps = ['Alibaba Cloud', 'Amazon Web Services (AWS)', 'ArangoDB Oasis', 'CockroachCloud', 'DigitalOcean', 'FaunaDB Cloud', 'Firebase',
                   'Google Cloud Platform (GCP)', 'IBM Cloud', 'Microsoft Azure', 'MongoDB Atlas', 'Oracle Cloud', 'Rackspace Cloud Databases', 'Redis Labs', 'Yugabyte Cloud']

databaseOps = ['BDBaaS', 'DLaaS', 'DMaaS', 'DWaaS', 'GDBaaS',
               'IMDBaaS', 'NDaaS', 'OODBaaS', 'RDBaaS', 'TSDBaaS']
DBMSOps = ['Active', 'Analytical', 'Client-server', 'Cloud-based', 'Columnar', 'Distributed', 'Document-oriented', 'Federated', 'Graph', 'Hierarchical', 'In-memory', 'Key-value',
           'Knowledge base (or expert system)', 'Mobile', 'Multidimensional', 'Network', 'Object-relational', 'Object-oriented', 'Operational', 'Real-time', 'Relational', 'Replicated', 'Spatial', 'Time-oriented']
appProtocolOps = ['AMQP', 'Bluetooth Low Energy (BLE)', 'CoAP', 'DDS', 'HTTP', 'LoRaWAN',
                  'MQTT', 'NB-IoT', 'OPC UA', 'Sigfox', 'Thread', 'WebSockets', 'XMPP', 'Z-Wave', 'ZigBee']

AllOptions = [CPUArchitectureOps,
              wirelessCommsOps,
              wiredCommsOps,
              CPUTypeOps,
              hFirewallOps,
              firmwareOps,
              OSOps,
              sFirewallOps,
              libFrameworksOps,
              compilerOps,
              languageOps,
              cryptographyOps,
              authMethodOps,
              communicationOps,
              transmissionOps,
              VPNOps,
              cloudServiceOps,
              databaseOps,
              DBMSOps,
              appProtocolOps]


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
