#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys
import pymysql

#MySql設定
pymysql.install_as_MySQLdb()

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "djangobook.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
