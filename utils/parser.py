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

    return {
        "src_ip": ip_layer.src,
        "dst_ip": ip_layer.dst,
        "protocol": detect_protocol(packet),
        "length": len(packet),
    }