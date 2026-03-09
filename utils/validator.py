def validate_packet_count(packet_count):
    if packet_count < 1:
        raise ValueError("Packet count must be at least 1")