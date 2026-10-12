"""
AGRICONNECT - Crop Advisory rule dataset.

This file defines the raw knowledge used to seed the AdvisoryRule table.
Keeping it separate from app.py means the advisory "knowledge base" can be
edited, extended, or reviewed on its own, without touching routing logic.

Design note (kept in the report too): recommendations are deliberately
general, non-branded, and phrased as guidance rather than instructions,
with an explicit disclaimer shown to the farmer to consult a local
agriculture officer for confirmation before acting.
"""

CROPS = ['Rice', 'Wheat', 'Tomato', 'Cotton', 'Maize', 'Chilli', 'Sugarcane', 'Groundnut']

SOILS = ['Normal', 'Waterlogged', 'Dry']   # shown to the farmer in the dropdown

SYMPTOMS = [
    'Yellow leaves',
    'Brown spots on leaves',
    'Wilting',
    'Stunted growth',
    'Holes in leaves',
    'White powdery coating on leaves',
    'Curling leaves',
    'Blackened or rotting roots',
]

# Base rules: apply regardless of soil condition (soil = 'Any' in the database).
# Format: symptom -> (issue, recommendation_template)
# "{crop}" in the recommendation is filled in per crop when the table is seeded.
BASE_RULES = {
    'Yellow leaves': (
        "Nitrogen deficiency",
        "Apply a nitrogen-rich fertilizer such as urea, split across 2-3 doses during the "
        "growing season. Ensure {crop} receives consistent, balanced watering."
    ),
    'Brown spots on leaves': (
        "Fungal leaf spot disease",
        "Apply a copper-based fungicide and remove affected leaves to prevent spread. Avoid "
        "overhead watering on {crop} to reduce leaf wetness, which encourages fungal growth."
    ),
    'Wilting': (
        "Root rot or vascular wilt disease",
        "Inspect roots for rot or discoloration. Apply a recommended fungicide drench for "
        "{crop} and avoid overwatering until the plant recovers."
    ),
    'Stunted growth': (
        "Nutrient deficiency (Phosphorus/Potassium)",
        "Apply a balanced NPK fertilizer with adequate phosphorus and potassium. A soil test "
        "for {crop} fields is recommended to confirm the exact deficiency before treatment."
    ),
    'Holes in leaves': (
        "Insect or pest infestation (leaf-eating caterpillars or beetles)",
        "Apply a neem-based pesticide and monitor {crop} plants weekly for pest activity. "
        "Remove and dispose of severely damaged leaves."
    ),
    'White powdery coating on leaves': (
        "Powdery mildew (fungal infection)",
        "Apply a sulfur-based or systemic fungicide. Improve air circulation between {crop} "
        "plants through proper spacing to reduce humidity around leaves."
    ),
    'Curling leaves': (
        "Sap-sucking pest damage (aphids/whiteflies) or viral infection",
        "Check the underside of leaves for aphids or whiteflies and apply an appropriate "
        "insecticide if found. If no pests are visible, consult a local agriculture officer "
        "regarding possible viral infection in {crop}."
    ),
    'Blackened or rotting roots': (
        "Root rot due to fungal infection or waterlogging",
        "Improve field drainage and apply a fungicidal soil drench. Avoid replanting {crop} "
        "in the same spot next season without treating the soil first."
    ),
}

# Soil-specific overrides: used when the symptom's underlying cause changes
# meaningfully with soil condition. Format: (symptom, soil) -> (issue, recommendation_template)
SOIL_OVERRIDES = {
    ('Yellow leaves', 'Waterlogged'): (
        "Root suffocation and nitrogen leaching due to waterlogging",
        "Improve field drainage immediately — standing water is likely washing away nitrogen "
        "and suffocating {crop} roots. Hold off on additional fertilizer until water recedes."
    ),
    ('Yellow leaves', 'Dry'): (
        "Drought stress preventing nutrient uptake",
        "Increase irrigation frequency — dry soil is preventing {crop} roots from absorbing "
        "available nutrients, even if fertilizer has already been applied."
    ),
    ('Wilting', 'Waterlogged'): (
        "Root rot caused by waterlogging",
        "Improve drainage urgently — waterlogged soil is starving {crop} roots of oxygen, "
        "which causes wilting despite there being plenty of water present."
    ),
    ('Wilting', 'Dry'): (
        "Water-stress wilting",
        "Increase irrigation immediately — {crop} is most likely wilting from insufficient "
        "soil moisture rather than disease."
    ),
}
