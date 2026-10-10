#!/usr/bin/env bash
# ساخت بسته‌های ZIP تحویلی عصرجدید — بدون هیچ وابستگی بیرونی
#   1) Asr-Jadid-template.zip  → قالب «مدرن شهری» به‌صورت HTML مستقل
#   2) Asr-Jadid-1.0.0.zip     → پروژهٔ کامل ASP.NET Core با فرانت‌اند (قالب چسبیده به پروژه)
#                              + نسخهٔ مستقل HTML قالب داخل پوشهٔ websites
# سورس قالب ۱ در websites/_src موجود است؛ در صورت نیاز به بازگردانی،
# یک خط مشابه برای 1-asrjadid-classic اضافه کنید.
set -e
cd "$(dirname "$0")"

# ---------- ۱) بازسازی قالب ۲ از سورس ----------
(cd _src && python3 - <<'PY'
import build
build.build_theme(2)
PY
)

mkdir -p download

# ---------- ۲) بستهٔ قالب مستقل ----------
rm -f download/Asr-Jadid-template.zip
(cd 2-asrjadid-modern && zip -qr ../download/Asr-Jadid-template.zip .)

# ---------- ۳) بستهٔ پروژهٔ کامل (فرانت‌اند چسبیده به پروژه) ----------
rm -f download/Asr-Jadid-1.0.0.zip
ROOT="$(cd .. && pwd)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
DEST="$STAGE/Asr-Jadid-1.0.0"
mkdir -p "$DEST"

# همهٔ پروژه به‌جز پوشه‌های گذرا و بسته‌های ZIP
python3 - "$ROOT" "$DEST" <<'PY'
import os, shutil, sys
root, dest = sys.argv[1], sys.argv[2]
skip_dirs = {'.git', 'bin', 'obj', '.vs', 'node_modules'}
for cur, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    rel = os.path.relpath(cur, root)
    out = os.path.join(dest, rel) if rel != '.' else dest
    os.makedirs(out, exist_ok=True)
    for f in files:
        if f.endswith('.user') or f.endswith('.zip'):
            continue
        shutil.copy2(os.path.join(cur, f), os.path.join(out, f))
PY

# نسخهٔ مستقل HTML قالب هم داخل بسته می‌آید تا «فرانت‌اند» هم به‌صورت
# صفحات Razor (AsrJadid/Pages + wwwroot) و هم به‌صورت HTML قابل مشاهده باشد.

(cd "$STAGE" && zip -qr Asr-Jadid-1.0.0.zip Asr-Jadid-1.0.0)
mv "$STAGE/Asr-Jadid-1.0.0.zip" download/

echo "✔ بسته‌ها ساخته شدند:"
ls -lh download/Asr-Jadid-template.zip download/Asr-Jadid-1.0.0.zip
