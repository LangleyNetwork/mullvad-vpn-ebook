#!/usr/bin/env bash
# build-all.sh — Build both editions of the Mullvad VPN ebook
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"

cd "$ROOT"

echo "=== Preflight ==="
[ -d "MANUSCRIPT" ]            || { echo "ERROR: MANUSCRIPT/ missing"; exit 1; }
[ -f "MANIFEST-full.yaml" ]    || { echo "ERROR: MANIFEST-full.yaml missing"; exit 1; }
[ -f "MANIFEST-free.yaml" ]    || { echo "ERROR: MANIFEST-free.yaml missing"; exit 1; }
[ -f "assets/qr-codes/urls.json" ] || { echo "ERROR: assets/qr-codes/urls.json missing"; exit 1; }
command -v python3 >/dev/null  || { echo "ERROR: python3 not in PATH"; exit 1; }
[ -x /usr/sbin/google-chrome ] || { echo "WARN: Chrome not at /usr/sbin/google-chrome; PDF may fail"; }

echo ""
echo "=== [A] Building per-edition QR manifests + codes ==="
python3 build/generate-qr-manifests.py
python3 build/generate-qr.py assets/qr-codes/manifest-full.json assets/qr-codes
python3 build/generate-qr.py assets/qr-codes/manifest-free.json assets/qr-codes

echo ""
echo "=== [B] Building Free Limited Edition ==="
bash build/build-edition.sh free

echo ""
echo "=== [C] Building Paid Full Edition ==="
bash build/build-edition.sh full

echo ""
echo "=== Build Summary ==="
for ED in free full; do
  echo ""
  echo "${ED^^}:"
  find "out/${ED}" -type f -exec ls -lh {} \; 2>/dev/null | awk '{print "  " $5 "\t" $9}'
done
echo ""
echo "=== All builds successful ==="