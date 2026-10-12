# AGRICONNECT — User + Marketplace + Crop Advisory Modules

## How to run this locally in VS Code
1. Open this folder in VS Code
2. Terminal > New Terminal
3. pip install -r requirements.txt
4. python app.py
5. Open http://127.0.0.1:5000 in your browser

The database (instance/agriconnect.db) is created and seeded automatically on first run.
Delete that file any time to reset all data and re-seed the advisory rules fresh.

## What's implemented so far

### User Module
Signup/Login with role selection, phone validation, secure passwords, show/hide password,
remember me, login attempt limiting, Dashboard, Edit Profile, Change Password.

### Marketplace Module
Farmers list/edit/mark-sold/delete produce. Buyers browse, search (by crop/location),
view details, and send a direct interest/contact request to the farmer. Role-based
access control and ownership checks throughout.

### Crop Advisory Module
Farmer selects Crop + Soil Condition + Symptom from dropdowns. A rule-based engine
(96 seeded rules across 8 crops x 8 symptoms, with soil-specific overrides for
Yellow Leaves and Wilting) returns a likely issue and a recommendation, plus a
disclaimer to consult a local agriculture officer.

The decision logic lives in one isolated function, get_advisory() in app.py,
so it can be swapped for a trained ML classifier later without changing the
route, form, or database structure around it (see advisory_data.py for the
raw rule dataset, which can double as a training dataset for that upgrade).

## Coming next
- Subsidy Eligibility Module
