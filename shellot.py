#!/usr/bin/env python3
"""
shellot.sh - A macOS environment backup manager
Main entry point for the application
"""

import argparse
from pathlib import Path
from settings_manager import SettingsManager

def main():
    parser = argparse.ArgumentParser(
        description='shellot.sh - macOS Environment Backup Manager',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Export settings:
    shellot.sh export
  Import settings:
    shellot.sh import
  Use custom backup path:
    shellot.sh export --backup-path ~/my_backups
        """
    )
    parser.add_argument('action', choices=['export', 'import'],
                       help='Action to perform (export or import settings)')
    parser.add_argument('--backup-path', 
                       default=str(Path.home() / 'shellot_backup'),
                       help='Backup directory path')
    
    args = parser.parse_args()
    
    manager = SettingsManager(backup_path=Path(args.backup_path))
    
    if args.action == 'export':
        manager.export_settings()
    else:
        manager.import_settings()

if __name__ == '__main__':
    main()