import json
import os
from datetime import datetime


def save_report(packets, output_path):
    directory = os.path.dirname(output_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    report = {
        "timestamp": datetime.now().isoformat(),
        "captured_count": len(packets),
        "packets": packets,
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return output_path