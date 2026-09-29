#!/usr/bin/env bash
# build-edition.sh <full|free> — Build one edition
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
EDITION="${1:?Usage: build-edition.sh <full|free>}"

cd "$ROOT"

[ "$EDITION" = "full" ] || [ "$EDITION" = "free" ] || { echo "Bad edition"; exit 1; }
[ -f "MANIFEST-${EDITION}.yaml" ] || { echo "Missing MANIFEST-${EDITION}.yaml"; exit 1; }

mkdir -p "out/${EDITION}/epub" "out/${EDITION}/pdf" "out/${EDITION}/html"

echo "[1/3] Building EPUB3..."
python3 build/build-epub.py "$EDITION"

echo "[2/3] Building PDF..."
python3 build/build-pdf.py "$EDITION"

echo "[3/3] Building HTML..."
python3 build/build-html.py "$EDITION"

# Optional: MOBI via Calibre's ebook-convert
if command -v ebook-convert >/dev/null 2>&1; then
  echo "[bonus] Building MOBI..."
  mkdir -p "out/${EDITION}/mobi"
  ebook-convert \
      "out/${EDITION}/epub/mullvad-vpn-ebook.epub" \
      "out/${EDITION}/mobi/mullvad-vpn-ebook.mobi" \
      --language en \
      --authors "S. Langley" \
      --title "Mullvad VPN — A Practical Guide"
fi

echo ""
echo "=== ${EDITION} edition build complete ==="
find "out/${EDITION}" -type f -exec ls -lh {} \;