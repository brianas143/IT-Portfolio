import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from system_report import build_report

class SystemReportTests(unittest.TestCase):
    def test_report_fields(self):
        report = build_report()
        self.assertIn("operating_system", report)
        self.assertGreater(report["disk_total_gb"], 0)
        self.assertGreaterEqual(report["disk_free_gb"], 0)
