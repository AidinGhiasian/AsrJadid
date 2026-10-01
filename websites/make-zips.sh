#!/usr/bin/env bash
# ساخت مجدد بسته ZIP قالب ۲ (مدرن شهری) — بدون هیچ وابستگی بیرونی
# سورس قالب ۱ در websites/_src موجود است؛ در صورت نیاز به بازگردانی،
# یک خط مشابه برای 1-asrjadid-classic اضافه کنید.
set -e
cd "$(dirname "$0")/_src"
python3 - <<'PY'
import build
build.build_theme(2)
PY
cd ..
mkdir -p download
rm -f download/theme2-modern.zip
(cd 2-asrjadid-modern && zip -qr ../download/theme2-modern.zip .)
echo "✔ بسته ساخته شد:"
ls -lh download/theme2-modern.zip
