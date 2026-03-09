# Python Packet Sniffer

A simple packet sniffer written in Python using Scapy.

This project demonstrates packet capture, protocol detection, traffic parsing, and JSON reporting for educational and authorized network analysis.

---

## Features

- Live packet capture
- Source and destination IP parsing
- Protocol detection (TCP, UDP, ICMP)
- Packet length display
- JSON report export
- Colored CLI output

---

## Project Structure

```text
packet-sniffer
│
├── sniffer
│   ├── __init__.py
│   └── packet_sniffer.py
│
├── utils
│   ├── __init__.py
│   ├── console.py
│   ├── parser.py
│   ├── reporter.py
│   └── validator.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

![Example Output](assets/example.png)