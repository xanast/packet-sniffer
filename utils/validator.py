VALID_PROTOCOLS = {"all", "tcp", "udp", "icmp"}


def validate_packet_count(packet_count):
    if packet_count < 1:
        raise ValueError("Packet count must be at least 1")


def validate_protocol(protocol):
    if protocol.lower() not in VALID_PROTOCOLS:
        raise ValueError("Protocol must be one of: all, tcp, udp, icmp")