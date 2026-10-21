import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from toolkit import organize, summarize_users

class ToolkitTests(unittest.TestCase):
    def test_dry_run_does_not_move(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'report.txt').write_text('hello')
            self.assertIn('WOULD MOVE', organize(root)[0])
            self.assertTrue((root / 'report.txt').exists())

    def test_organize_moves(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'report.txt').write_text('hello')
            organize(root, dry_run=False)
            self.assertTrue((root / 'txt' / 'report.txt').exists())

    def test_users_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            csv_file = Path(tmp) / 'users.csv'
            csv_file.write_text('name,department,status\nAlex,IT,active\nSam,IT,inactive\n')
            self.assertEqual(summarize_users(csv_file)['departments']['IT'], 2)

if __name__ == '__main__':
    unittest.main()
