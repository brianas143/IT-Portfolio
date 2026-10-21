"""Safe IT automation exercises using the Python standard library."""
import argparse
import csv
from collections import Counter
from pathlib import Path
import shutil

def organize(folder: Path, dry_run: bool = True) -> list[str]:
    if not folder.is_dir():
        raise ValueError(f"Not a directory: {folder}")
    changes = []
    for source in sorted(folder.iterdir()):
        if not source.is_file():
            continue
        category = source.suffix.lower().lstrip('.') or 'no_extension'
        target = folder / category / source.name
        if target.exists():
            changes.append(f"SKIP existing: {target}")
            continue
        changes.append(f"{'WOULD MOVE' if dry_run else 'MOVE'}: {source.name} -> {category}/")
        if not dry_run:
            target.parent.mkdir(exist_ok=True)
            shutil.move(str(source), str(target))
    return changes

def summarize_users(csv_path: Path) -> dict:
    with csv_path.open(newline='', encoding='utf-8-sig') as handle:
        reader = csv.DictReader(handle)
        required = {'name', 'department', 'status'}
        if not required.issubset(set(reader.fieldnames or [])):
            raise ValueError('CSV must contain name,department,status columns')
        rows = list(reader)
    return {'total': len(rows),
            'departments': dict(Counter(r['department'].strip() for r in rows)),
            'statuses': dict(Counter(r['status'].strip().lower() for r in rows))}

def main() -> None:
    parser = argparse.ArgumentParser(description='IT automation exercises')
    sub = parser.add_subparsers(dest='command', required=True)
    org = sub.add_parser('organize')
    org.add_argument('folder', type=Path)
    org.add_argument('--dry-run', action='store_true')
    users = sub.add_parser('users')
    users.add_argument('csv', type=Path)
    args = parser.parse_args()
    if args.command == 'organize':
        print('\n'.join(organize(args.folder, dry_run=args.dry_run)))
    else:
        print(summarize_users(args.csv))

if __name__ == '__main__':
    main()
