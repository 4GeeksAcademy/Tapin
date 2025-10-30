
# Create simplified updated design system documentation
import csv

# Updated Tapin Design System based on style guide
design_specs = [
    ["Category", "Element", "Value", "Usage"],
    ["Art Direction", "Primary Style", "Energetic Human", "Recommended - approachable, vibrant, people-focused"],
    ["Art Direction", "Alternative", "Calm Civic / Friendly Tech", "Backup options for specific contexts"],
    ["Typography", "Headlines", "Large, bold, rounded sans-serif", "Page titles and major sections"],
    ["Typography", "Subheads", "Medium weight, clear hierarchy", "Section headers and card titles"],
    ["Typography", "Body", "Regular weight, high readability", "Paragraphs and descriptions"],
    ["Typography", "Meta", "Small, subtle", "Labels, timestamps, secondary info"],
    ["Layout", "Grid Approach", "Mobile-first, 4 columns", "Responsive design foundation"],
    ["Layout", "Margins", "Compact to Standard slider", "Adjustable based on content density"],
    ["Layout", "Density", "Bday (balanced)", "Between Resserknads and Cozy"],
    ["Components", "Buttons", "Primary (bright blue), Secondary, Ghost", "Rounded corners, 48px min height"],
    ["Components", "Cards", "White background, subtle shadow, rounded corners", "Container for listings and content"],
    ["Components", "Input Fields", "Rounded borders, clear labels", "Forms and search functionality"],
    ["Components", "Badges/Achievements", "Colorful, icon-based, gamification", "Profile and achievement display"],
    ["Components", "Chat Bubbles", "Rounded, message-style", "Notifications and messaging"],
    ["Components", "Toasts/Notifications", "Slide-in, auto-dismiss", "Feedback and alerts"],
    ["Iconography", "Style", "Outlined, rounded corners", "Consistent with overall design language"],
    ["Iconography", "Set", "Location pin, search, user, briefcase, list, chat", "Core app functionality icons"],
    ["Page Compositions", "Landing", "Hero with search, category cards", "First impression and main entry"],
    ["Page Compositions", "Search/Browse", "Filter chips, listing cards, map toggle", "Discovery and filtering"],
    ["Page Compositions", "Opportunity Detail", "Hero image/map, details grid, CTA button", "Full opportunity information"],
    ["Page Compositions", "Tabs & Pills", "Segmented controls", "Navigation within screens"],
    ["Page Compositions", "Messages", "Chat-style interface", "Communication between users"],
    ["Accessibility", "Contrast thresholds", "WCAG AA minimum (4.5:1 text, 3:1 UI)", "Ensures readability for all users"],
    ["Accessibility", "Focus appearance", "Visible focus indicators", "Keyboard navigation support"],
    ["Accessibility", "Minimum target size", "48x48px touch targets", "Mobile-friendly tap zones"],
    ["Accessibility", "Error state visibility", "Clear visual and text indicators", "Form validation and feedback"],
    ["Accessibility", "Readability", "High contrast, appropriate line spacing", "Comfortable reading experience"],
    ["BMAD Mapping", "Midlae integration", "Design token system", "Consistent design-to-development handoff"]
]

with open('tapin_updated_design_system.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(design_specs)

print("✓ Updated Tapin Design System CSV created")
print(f"\nTotal design specifications: {len(design_specs)-1}")
print("\nKey Updates from Style Guide:")
print("  • Art Direction: Energetic Human (people-focused, vibrant)")
print("  • Primary Color: Bright Blue (matching existing logo)")
print("  • Typography: Rounded sans-serif with clear hierarchy")
print("  • Layout: Mobile-first with flexible density options")
print("  • Components: 8 core UI component types defined")
print("  • Page Compositions: 5 key screen layouts specified")
print("  • Accessibility: Full WCAG AA compliance checklist")
print("  • BMAD Mapping: Midlae design token integration")
