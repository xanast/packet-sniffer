import argparse

from sniffer.packet_sniffer import start_sniffing
from utils.console import banner, error, info, success
from utils.reporter import save_report
from utils.validator import validate_packet_count


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

    args = parser.parse_args()

    banner()

    try:
        validate_packet_count(args.count)

        info(f"Packet count : {args.count}")
        info(f"Interface    : {args.interface if args.interface else 'default'}")

        packets = start_sniffing(
            packet_count=args.count,
            interface=args.interface,
        )

        report_path = save_report(packets, args.output)
        success(f"Report saved to: {report_path}")

    except Exception as exc:
        error(str(exc))


if __name__ == "__main__":
    main()