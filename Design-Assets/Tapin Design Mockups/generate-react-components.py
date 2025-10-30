"""
Script: generate-react-components.py
Purpose: Generate React component boilerplate files for each major screen in the Tapin design mockups.
Usage: Run this script to scaffold component files in your frontend/src/components directory.
"""

import os

screens = [
    ("home", "HomePage"),
    ("browse", "BrowseListings"),
    ("detail", "OpportunityDetail"),
    ("profile", "UserProfile"),
    ("dashboard", "Dashboard")
]

output_dir = "../../frontend/src/components"
os.makedirs(output_dir, exist_ok=True)

component_template = """import React from 'react';

function {name}() {{
  return (
    <div className='{css_class}'>
      <h2>{title}</h2>
      {/* TODO: Implement {title} UI based on design mockup */}
    </div>
  );
}}

export default {name};
"""

for filename, comp_name in screens:
    css_class = filename + "-screen"
    title = comp_name.replace("Page", " Page").replace("Listings", " Listings").replace("Detail", " Detail").replace("Profile", " Profile")
    with open(os.path.join(output_dir, f"{comp_name}.js"), "w") as f:
        f.write(component_template.format(name=comp_name, css_class=css_class, title=title))

print("React component files generated in frontend/src/components/")
