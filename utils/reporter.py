import csv
import json
import os
from datetime import datetime


def save_json_report(packets, output_path, summary):
    directory = os.path.dirname(output_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    report = {
        "timestamp": datetime.now().isoformat(),
        "captured_count": len(packets),
        "summary": summary,
        "packets": packets,
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return output_path


def save_csv_report(packets, output_path):
    directory = os.path.dirname(output_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["src_ip", "dst_ip", "protocol", "length"],
        )
        writer.writeheader()
        writer.writerows(packets)

    return output_path