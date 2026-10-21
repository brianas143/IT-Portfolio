"""Report local system basics using the Python standard library."""
import json
import platform
import shutil
from datetime import datetime, timezone
from pathlib import Path

def build_report(path: Path = Path.home()) -> dict:
    disk = shutil.disk_usage(path)
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "python_version": platform.python_version(),
        "disk_total_gb": round(disk.total / 1e9, 2),
        "disk_free_gb": round(disk.free / 1e9, 2),
    }

if __name__ == "__main__":
    print(json.dumps(build_report(), indent=2))
