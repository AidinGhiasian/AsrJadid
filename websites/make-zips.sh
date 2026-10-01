#!/usr/bin/env bash
# ساخت مجدد بسته‌های ZIP دو قالب (بدون هیچ وابستگی بیرونی)
set -e
cd "$(dirname "$0")/_src"
python3 build.py
cd ..
mkdir -p download
rm -f download/*.zip
(cd 1-asrjadid-classic && zip -qr ../download/AsrJadid-theme1-classic.zip .)
(cd 2-asrjadid-modern  && zip -qr ../download/AsrJadid-theme2-modern.zip  .)
echo "✔ بسته‌ها ساخته شدند:"
ls -lh download/*.zip
