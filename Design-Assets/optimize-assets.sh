#!/bin/bash
# Design-Assets Optimization Script
# Minifies SVG, optimizes PNG/JPG, and reports size savings
# Usage: ./optimize-assets.sh

set -euo pipefail

ASSETS_DIR="Design-Assets"
echo "🎨 Tapin Design Assets — Optimization Script"
echo "=============================================="
echo ""

# Check dependencies
command -v svgo >/dev/null 2>&1 || { echo "⚠️  svgo not found. Install: npm install -g svgo"; exit 1; }
command -v pngquant >/dev/null 2>&1 || { echo "⚠️  pngquant not found. Install: brew install pngquant"; exit 1; }
command -v jpegoptim >/dev/null 2>&1 || { echo "⚠️  jpegoptim not found. Install: brew install jpegoptim"; exit 1; }

echo "✓ Dependencies found."
echo ""

# Helper: get file size (portable)
filesize() {
  if stat --version >/dev/null 2>&1; then
    stat -c%s "$1" 2>/dev/null || stat -f%z "$1" 2>/dev/null
  else
    stat -f%z "$1" 2>/dev/null || stat -c%s "$1" 2>/dev/null
  fi
}

# SVG Optimization
echo "📦 Optimizing SVG files..."
find "$ASSETS_DIR" -type f -name "*.svg" | while IFS= read -r file; do
  original_size=$(filesize "$file")
  svgo "$file" --multipass >/dev/null 2>&1 || true
  optimized_size=$(filesize "$file")
  saved=$(( original_size - optimized_size ))
  percent=0
  if [ "$original_size" -gt 0 ]; then
    percent=$(( (saved * 100) / original_size ))
  fi
  echo "  ✓ $file (-${percent}% | -${saved} bytes)"
done

echo ""
echo "📦 Optimizing PNG files..."
find "$ASSETS_DIR" -type f -name "*.png" | while IFS= read -r file; do
  original_size=$(filesize "$file")
  # pngquant writes a new file; use --force --ext .png to overwrite
  pngquant --force --ext .png --quality=80-95 "$file" >/dev/null 2>&1 || true
  optimized_size=$(filesize "$file")
  saved=$(( original_size - optimized_size ))
  if [ "$saved" -gt 0 ]; then
    percent=$(( (saved * 100) / original_size ))
    echo "  ✓ $file (-${percent}% | -${saved} bytes)"
  else
    echo "  ✓ $file (already optimized)"
  fi
done

echo ""
echo "📦 Optimizing JPG files..."
find "$ASSETS_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" \) | while IFS= read -r file; do
  original_size=$(filesize "$file")
  jpegoptim --max=85 --progressive --strip-all "$file" >/dev/null 2>&1 || true
  optimized_size=$(filesize "$file")
  saved=$(( original_size - optimized_size ))
  if [ "$saved" -gt 0 ]; then
    percent=$(( (saved * 100) / original_size ))
    echo "  ✓ $file (-${percent}% | -${saved} bytes)"
  else
    echo "  ✓ $file (already optimized)"
  fi
done

echo ""
echo "✅ Optimization complete!"
echo ""
echo "📊 Total asset sizes:"
du -sh "$ASSETS_DIR"
