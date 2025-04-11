This directory contains the core components of the web application: route handling, user interface templates, and static files.

main.py
Purpose: Entry point of the Flask web app.

Functionality:

Initializes the Flask app.

Registers routes from routes.py.

Configures any global settings.

routes.py
Purpose: Manages URL endpoints and user interactions.

Functionality:

Defines routes like /, /upload, /analyze.

Handles file uploads, processing calls, and template rendering.

Bridges frontend and backend logic.

/static/
Purpose: Stores all static assets.

Contents:

CSS files for styling the UI.

JavaScript files (if applicable).

Images, icons, etc.

/templates/
Purpose: Contains HTML templates for rendering views.

Contents:

index.html – Upload form and dashboard layout.

result.html – Displays extracted bottle features.

Shared layout files (base.html) for consistency.

