"""
Script: generate-flask-endpoints.py
Purpose: Scaffold Flask endpoint boilerplate for each major feature in the Tapin project.
Usage: Run this script to append endpoint stubs to backend/app.py.
"""

endpoints = [
    ("/register", "POST", "register_user"),
    ("/login", "POST", "login_user"),
    ("/reset-password", "POST", "reset_password"),
    ("/listings", "GET", "get_listings"),
    ("/listings", "POST", "create_listing"),
    ("/listings/<int:id>", "GET", "get_listing_detail"),
    ("/listings/<int:id>", "PUT", "update_listing"),
    ("/listings/<int:id>", "DELETE", "delete_listing"),
]

with open("../../backend/app.py", "a") as f:
    for route, method, func in endpoints:
        f.write(f"\n\n@app.route('{route}', methods=['{method}'])\ndef {func}():\n    # TODO: Implement {func.replace('_', ' ')}\n    return '{{}}'\n")

print("Flask endpoint stubs appended to backend/app.py")
