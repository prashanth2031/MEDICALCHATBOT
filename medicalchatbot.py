import random

# Medical knowledge base
medical_db = {
    "headache": {
        "description": "A headache is pain in the head or face.",
        "causes": ["Stress", "Tension", "Migraine", "Dehydration", "Eye strain"],
        "remedies": ["Rest in a quiet room", "Apply cold compress", "Take OTC pain relievers", "Stay hydrated"]
    },
"sunburn": {

"description": "Sunburn is skin damage caused by excessive UV exposure.",

},
"scabies": {

"description": "Scabies is a skin infestation by mites causing itching.",

"causes": ["Mite infestation", "Close contact"],

"remedies": ["Medicated lotions", "Wash clothes in

hot water"]},

"causes": ["Prolonged sun exposure"],

"remedies": ["Aloe vera", "Cool bath", "Hydration"]},
hypothermia": {

"description": "Hypothermia occurs when body temperature drops dangerously low.",

"causes": ["Cold exposure", "Wet clothing"],

"remedies": ["Warm blankets", "Warm drinks", "Medical
help"]},
"heatstroke": {

"description": "Heatstroke is a severe heat-related illness with very high body temperature.",
"causes": ["Prolonged heat exposure", "Dehydration"],

"remedies": ["Cool the body", "Fluids", "Emergency medical care"]
    "motion_sickness": {
         "description": "Motion sickness is nausea and dizziness triggered by movement during travel.",
   "causes": ["Travel by car/boat/air", "Inner ear sensitivity"],
    "remedies": ["Look at horizon", "Ginger", "Motion sickness tablets"]},
    "vitiligo": {
        "description": "Vitiligo causes loss of skin pigmentation.",
        "causes": ["Autoimmune condition"],
        "remedies": ["Skin therapy", "Medical treatment"]
    },
    "psoriasis": {
        "description": "Psoriasis is a chronic skin disease causing red patches.",
        "causes": ["Immune disorder", "Genetics"],
        "remedies": ["Topical creams", "Medication"]
    },
    "epilepsy": {
        "description": "Epilepsy is a neurological disorder causing seizures.",
        "causes": ["Brain injury", "Genetics"],
        "remedies": ["Antiepileptic drugs", "Medical care"]
    },
    "sleep_apnea": {
        "description": "Sleep apnea causes breathing interruptions during sleep.",
        "causes": ["Obesity", "Airway blockage"],
        "remedies": ["CPAP therapy", "Weight loss"]
    },
    "allergic_rhinitis": {
        "description": "Allergic rhinitis causes sneezing and nasal congestion.",
        "causes": ["Dust", "Pollen"],
        "remedies": ["Antihistamines", "Avoid allergens"]
    },
    "influenza": {
        "description": "Influenza is a viral respiratory illness.",
        "causes": ["Influenza virus"],
        "remedies": ["Antivirals", "Rest", "Fluids"]
    },
    "rubella": {
        "description": "Rubella is a viral infection with rash and fever.",