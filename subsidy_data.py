"""
AGRICONNECT - Subsidy Eligibility rule dataset.

Kept separate from app.py for the same reason as advisory_data.py: the
knowledge base (which schemes exist, and their eligibility criteria) can be
reviewed, sourced, and extended independently of routing logic.

Eligibility here is intentionally simplified for a student-project scope —
'Any' means a field does not restrict eligibility for that scheme. Real
scheme rules are considerably more detailed (income limits, documentation,
etc.); production use would require verifying current official criteria.
"""

from advisory_data import CROPS   # reuse the same crop list across modules

REGIONS = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Punjab', 'Uttar Pradesh']

LAND_CATEGORIES = ['Less than 1 acre', '1-2 acres', '2-5 acres', 'More than 5 acres']

# Each row: (scheme_name, region, crop, land_category, benefit, how_to_apply)
# region/crop/land_category = 'Any' means that field does not restrict this scheme.
SCHEME_RULES = [
    (
        "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "Any", "Any", "Any",
        "₹6,000 per year paid directly to the farmer's bank account, in three instalments.",
        "Register at pmkisan.gov.in or through your local Common Service Centre (CSC)."
    ),
    (
        "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
        "Any", "Any", "Any",
        "Low-premium crop insurance covering yield loss from natural calamities, pests, or disease.",
        "Apply through your bank at the time of taking a crop loan, or online at pmfby.gov.in."
    ),
    (
        "Soil Health Card Scheme",
        "Any", "Any", "Any",
        "Free soil testing and a personalised fertilizer/nutrient recommendation, once every 2 years.",
        "Contact your local Krishi Vigyan Kendra (KVK) or Agriculture Department office."
    ),
    (
        "Kisan Credit Card (KCC)",
        "Any", "Any", "Any",
        "Short-term credit at subsidised interest rates for crop cultivation and related expenses.",
        "Apply at any nationalised or cooperative bank branch with land ownership documents."
    ),
    (
        "National Food Security Mission (NFSM)",
        "Any", "Rice", "Any",
        "Subsidised seeds and farm equipment support to improve rice yield and reduce input cost.",
        "Apply through your District Agriculture Officer."
    ),
    (
        "National Food Security Mission (NFSM)",
        "Any", "Wheat", "Any",
        "Subsidised seeds and farm equipment support to improve wheat yield and reduce input cost.",
        "Apply through your District Agriculture Officer."
    ),
    (
        "National Food Security Mission (NFSM)",
        "Any", "Maize", "Any",
        "Subsidised seeds and farm equipment support to improve maize yield and reduce input cost.",
        "Apply through your District Agriculture Officer."
    ),
    (
        "Per Drop More Crop — Micro Irrigation Subsidy (PMKSY)",
        "Any", "Any", "1-2 acres",
        "Up to 55% subsidy on drip/sprinkler irrigation equipment installation.",
        "Apply through your state Horticulture or Agriculture Department portal."
    ),
    (
        "Per Drop More Crop — Micro Irrigation Subsidy (PMKSY)",
        "Any", "Any", "2-5 acres",
        "Up to 55% subsidy on drip/sprinkler irrigation equipment installation.",
        "Apply through your state Horticulture or Agriculture Department portal."
    ),
    (
        "Per Drop More Crop — Micro Irrigation Subsidy (PMKSY)",
        "Any", "Any", "More than 5 acres",
        "Up to 45% subsidy on drip/sprinkler irrigation equipment installation for larger holdings.",
        "Apply through your state Horticulture or Agriculture Department portal."
    ),
    (
        "Rythu Bandhu",
        "Telangana", "Any", "Any",
        "₹10,000 per acre per year in direct investment support for seeds, fertilizers, and pesticides.",
        "Contact your local Agriculture Extension Officer in Telangana with land records."
    ),
    (
        "Rythu Bharosa (YSR Rythu Bharosa)",
        "Andhra Pradesh", "Any", "Any",
        "₹13,500 per year in direct investment support per eligible farmer family.",
        "Register through the AP Agriculture Department's village-level portal."
    ),
    (
        "Paramparagat Krishi Vikas Yojana (PKVY)",
        "Any", "Any", "Any",
        "Financial assistance of ₹50,000 per hectare over 3 years for farmer clusters adopting organic farming.",
        "Apply through your local Agriculture Department cluster coordinator."
    ),
    (
        "Agriculture Infrastructure Fund (AIF)",
        "Any", "Any", "More than 5 acres",
        "Subsidised-interest loans for building on-farm storage, cold storage, or processing infrastructure.",
        "Apply through a participating bank under the AIF portal (agriinfra.dac.gov.in)."
    ),
]
