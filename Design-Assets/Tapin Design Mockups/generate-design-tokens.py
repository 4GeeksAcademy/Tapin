"""
Script: generate-design-tokens.py
Purpose: Generate a design-tokens.js file for use in the React frontend, based on the Tapin design system.
Usage: Run this script to create/update frontend/src/design-tokens.js.
"""

design_tokens = {
    "primaryColor": "#FFBCE",
    "secondaryColor": "#58824",
    "accentColor": "#58747",
    "backgroundColor": "#6471",
    "fontFamily": "'Rounded Sans', Arial, sans-serif",
    "borderRadius": "16px",
    "buttonHeight": "48px",
    "cardShadow": "0 2px 8px rgba(0,0,0,0.08)",
    "focusOutline": "2px solid #FFBCE"
}

with open("../../frontend/src/design-tokens.js", "w") as f:
    f.write("// Auto-generated design tokens for Tapin\n")
    f.write("export const designTokens = ")
    f.write(str(design_tokens))
    f.write(";\n")

print("Design tokens written to frontend/src/design-tokens.js")
