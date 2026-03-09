from collections import Counter

from scapy.all import sniff, get_if_list, wrpcap
from utils.parser import parse_packet, matches_protocol_filter
from utils.console import info, success


captured_packets = []
raw_packets = []


def list_interfaces():
    return get_if_list()


def build_bpf_filter(protocol_filter):
    if protocol_filter is None or protocol_filter.lower() == "all":
        return None

    protocol_filter = protocol_filter.lower()

    if protocol_filter in {"tcp", "udp", "icmp"}:
        return protocol_filter

    return None


def packet_callback(packet, protocol_filter):
    if not matches_protocol_filter(packet, protocol_filter):
        return

    parsed = parse_packet(packet)

    if parsed is not None:
        captured_packets.append(parsed)
        raw_packets.append(packet)

        success(
            f"{parsed['src_ip']} -> {parsed['dst_ip']} | "
            f"Protocol: {parsed['protocol']} | Length: {parsed['length']}"
        )


def generate_summary(packets):
    protocol_counter = Counter(packet["protocol"] for packet in packets)
    unique_src = len(set(packet["src_ip"] for packet in packets))
    unique_dst = len(set(packet["dst_ip"] for packet in packets))

    return {
        "total_packets": len(packets),
        "tcp_packets": protocol_counter.get("TCP", 0),
        "udp_packets": protocol_counter.get("UDP", 0),
        "icmp_packets": protocol_counter.get("ICMP", 0),
        "other_packets": protocol_counter.get("OTHER", 0),
        "unique_source_ips": unique_src,
        "unique_destination_ips": unique_dst,
    }


def save_pcap(output_path):
    if not raw_packets:
        return None

    wrpcap(output_path, raw_packets)
    return output_path


def start_sniffing(packet_count=10, interface=None, protocol_filter="all"):
    global captured_packets, raw_packets
    captured_packets = []
    raw_packets = []

    info("Starting packet capture...")

    bpf_filter = build_bpf_filter(protocol_filter)

    sniff(
        prn=lambda packet: packet_callback(packet, protocol_filter),
        count=packet_count,
        iface=interface,
        store=False,
        filter=bpf_filter,
    )

    info(f"Capture complete. Packets captured: {len(captured_packets)}")

    summary = generate_summary(captured_packets)

    return captured_packets, summary