#!/bin/bash
# Design-Assets Optimization Script
# Minifies SVG, optimizes PNG/JPG, and reports size savings
# Usage: ./optimize-assets.sh

set -e

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

# SVG Optimization
echo "📦 Optimizing SVG files..."
find "$ASSETS_DIR" -type f -name "*.svg" | while read file; do
  original_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
  svgo "$file" --multipass
  optimized_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
  saved=$(( original_size - optimized_size ))
  percent=$(( (saved * 100) / original_size ))
  echo "  ✓ $file (-${percent}% | -${saved} bytes)"
done

echo ""
echo "📦 Optimizing PNG files..."
find "$ASSETS_DIR" -type f -name "*.png" | while read file; do
  original_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
  pngquant --force --ext .png --quality=80-95 "$file"
  optimized_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
  saved=$(( original_size - optimized_size ))
  if [ $saved -gt 0 ]; then
    percent=$(( (saved * 100) / original_size ))
    echo "  ✓ $file (-${percent}% | -${saved} bytes)"
  else
    echo "  ✓ $file (already optimized)"
  fi
done

echo ""
echo "📦 Optimizing JPG files..."
find "$ASSETS_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" \) | while read file; do
  original_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
  jpegoptim --max=85 --progressive --strip-all "$file"
  optimized_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
  saved=$(( original_size - optimized_size ))
  if [ $saved -gt 0 ]; then
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
