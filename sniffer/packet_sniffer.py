from scapy.all import sniff
from utils.parser import parse_packet
from utils.console import info, success


captured_packets = []


def packet_callback(packet):
    parsed = parse_packet(packet)

    if parsed is not None:
        captured_packets.append(parsed)

        success(
            f"{parsed['src_ip']} -> {parsed['dst_ip']} | "
            f"Protocol: {parsed['protocol']} | Length: {parsed['length']}"
        )


def start_sniffing(packet_count=10, interface=None):
    global captured_packets
    captured_packets = []

    info("Starting packet capture...")

    sniff(
        prn=packet_callback,
        count=packet_count,
        iface=interface,
        store=False,
    )

    info(f"Capture complete. Packets captured: {len(captured_packets)}")

    return captured_packets