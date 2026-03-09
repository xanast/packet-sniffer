from scapy.all import IP, TCP, UDP, ICMP


def detect_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    if packet.haslayer(UDP):
        return "UDP"
    if packet.haslayer(ICMP):
        return "ICMP"
    return "OTHER"


def parse_packet(packet):
    if not packet.haslayer(IP):
        return None

    ip_layer = packet[IP]
    protocol = detect_protocol(packet)

    return {
        "src_ip": ip_layer.src,
        "dst_ip": ip_layer.dst,
        "protocol": protocol,
        "length": len(packet),
    }


def matches_protocol_filter(packet, protocol_filter):
    if protocol_filter is None or protocol_filter.lower() == "all":
        return True

    protocol_filter = protocol_filter.lower()

    if protocol_filter == "tcp" and packet.haslayer(TCP):
        return True
    if protocol_filter == "udp" and packet.haslayer(UDP):
        return True
    if protocol_filter == "icmp" and packet.haslayer(ICMP):
        return True

    return False