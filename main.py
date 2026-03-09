import argparse

from sniffer.packet_sniffer import list_interfaces, save_pcap, start_sniffing
from utils.console import banner, error, info, success
from utils.reporter import save_csv_report, save_json_report
from utils.validator import validate_packet_count, validate_protocol


def main():
    parser = argparse.ArgumentParser(description="Python Packet Sniffer")

    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=10,
        help="Number of packets to capture",
    )

    parser.add_argument(
        "-i",
        "--interface",
        default=None,
        help="Network interface to sniff on",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="reports/capture_report.json",
        help="Path to JSON report output file",
    )

    parser.add_argument(
        "--csv",
        default=None,
        help="Optional CSV export path",
    )

    parser.add_argument(
        "--pcap",
        default=None,
        help="Optional PCAP export path",
    )

    parser.add_argument(
        "--protocol",
        default="all",
        help="Protocol filter: all, tcp, udp, icmp",
    )

    parser.add_argument(
        "--list-interfaces",
        action="store_true",
        help="List available network interfaces and exit",
    )

    args = parser.parse_args()

    banner()

    try:
        if args.list_interfaces:
            interfaces = list_interfaces()
            info("Available interfaces:")
            for interface in interfaces:
                print(f" - {interface}")
            return

        validate_packet_count(args.count)
        validate_protocol(args.protocol)

        info(f"Packet count : {args.count}")
        info(f"Interface    : {args.interface if args.interface else 'default'}")
        info(f"Protocol     : {args.protocol}")

        packets, summary = start_sniffing(
            packet_count=args.count,
            interface=args.interface,
            protocol_filter=args.protocol,
        )

        json_report_path = save_json_report(packets, args.output, summary)
        success(f"JSON report saved to: {json_report_path}")

        if args.csv:
            csv_report_path = save_csv_report(packets, args.csv)
            success(f"CSV report saved to: {csv_report_path}")

        if args.pcap:
            pcap_path = save_pcap(args.pcap)
            if pcap_path:
                success(f"PCAP saved to: {pcap_path}")

        info("Capture Summary")
        info(f"Total packets           : {summary['total_packets']}")
        info(f"TCP packets             : {summary['tcp_packets']}")
        info(f"UDP packets             : {summary['udp_packets']}")
        info(f"ICMP packets            : {summary['icmp_packets']}")
        info(f"Other packets           : {summary['other_packets']}")
        info(f"Unique source IPs       : {summary['unique_source_ips']}")
        info(f"Unique destination IPs  : {summary['unique_destination_ips']}")

    except Exception as exc:
        error(str(exc))


if __name__ == "__main__":
    main()