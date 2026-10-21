# Python IT Automation Toolkit

Standard-library Python 3.10+ CLI. Safely organize files by extension and summarize sample CSV user records.

```bash
python toolkit.py organize ./sample_files --dry-run
python toolkit.py organize ./sample_files
python toolkit.py users ./users.csv
python -m unittest discover -s tests -v
```

`--dry-run` previews file moves. Existing target files are never overwritten. The CSV command only reads example records; it does not create or modify real user accounts.

**Status:** Python implementation and tests included. Run locally and record results.
