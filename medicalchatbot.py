# importing library
import random

# Medical knowledge base
medical_db = {
    "headache": {
        "description": "A headache is pain in the head or face.",
        "causes": ["Stress", "Tension", "Migraine", "Dehydration", "Eye strain"],
        "remedies": ["Rest in a quiet room", "Apply cold compress", "Take OTC pain relievers", "Stay hydrated"]
    },
"borderline_personality_disorder": {
  "description": "Borderline personality disorder is a mental health condition affecting mood and relationships.",
  "causes": ["Genetic factors", "Childhood trauma"],
  "remedies": ["Psychotherapy", "Medication"]
},
"zoster_sine_herpete": {
  "description": "Zoster sine herpete is a form of shingles where nerve pain occurs without the typical skin rash.",
  "symptoms": [
    "Burning or stabbing nerve pain",
    "Tingling or numbness",
    "Sensitivity to touch",
    "Headache",
    "Fatigue"
  ],
  "causes": [
    "Reactivation of the varicella-zoster virus",
    "Weak immune system",
    "Previous chickenpox infection"
  ],
  "risk_factors": [
    "Older age",
    "Immunocompromised conditions",
    "Stress or illness"
  ],
  "diagnosis": [
    "Clinical evaluation of nerve pain",
    "PCR test for varicella-zoster virus",
    "Blood antibody tests"
  ],
  "remedies": [
    "Antiviral medications",
    "Pain management medications",
    "Rest and supportive care"
  ],
  "prevention": [
    "Shingles vaccination",
    "Maintaining strong immune health",
    "Early treatment of symptoms"
  ]
},

"narcissistic_personality_disorder": {
  "description": "Narcissistic personality disorder involves inflated self-importance.",
  "causes": ["Environmental and genetic factors"],
  "remedies": ["Psychotherapy"]
},

"antisocial_personality_disorder": {
  "description": "Antisocial personality disorder involves disregard for others.",
  "causes": ["Genetic predisposition", "Childhood environment"],
  "remedies": ["Therapy"]
},

"paranoid_personality_disorder": {
  "description": "Paranoid personality disorder causes distrust of others.",
  "causes": ["Genetic and environmental factors"],
  "remedies": ["Psychotherapy"]
},

"schizoid_personality_disorder": {
  "description": "Schizoid personality disorder involves detachment from social relationships.",
  "causes": ["Genetic factors"],
  "remedies": ["Therapy"]
},

"avoidant_personality_disorder": {
  "description": "Avoidant personality disorder involves social inhibition.",
  "causes": ["Low self-esteem", "Genetics"],
  "remedies": ["Cognitive behavioral therapy"]
},

"dependent_personality_disorder": {
  "description": "Dependent personality disorder involves excessive need for care.",
  "causes": ["Childhood experiences"],
  "remedies": ["Psychotherapy"]
},

"histrionic_personality_disorder": {
  "description": "Histrionic personality disorder involves excessive emotionality.",
  "causes": ["Environmental factors"],
  "remedies": ["Therapy"]
},

"dissociative_identity_disorder": {
  "description": "Dissociative identity disorder involves multiple personality states.",
  "causes": ["Severe trauma"],
  "remedies": ["Long-term psychotherapy"]
},

"dissociative_amnesia": {
  "description": "Dissociative amnesia involves memory loss due to stress.",
  "causes": ["Psychological trauma"],
  "remedies": ["Psychotherapy"]
},

"conversion_disorder": {
  "description": "Conversion disorder presents neurological symptoms without medical cause.",
  "causes": ["Psychological stress"],
  "remedies": ["Therapy"]
},

"somatic_symptom_disorder": {
  "description": "Somatic symptom disorder causes excessive focus on physical symptoms.",
  "causes": ["Psychological factors"],
  "remedies": ["Cognitive therapy"]
},

"illness_anxiety_disorder": {
  "description": "Illness anxiety disorder involves fear of serious illness.",
  "causes": ["Anxiety disorders"],
  "remedies": ["Therapy"]
},

"hoarding_disorder": {
  "description": "Hoarding disorder involves difficulty discarding possessions.",
  "causes": ["Anxiety-related factors"],
  "remedies": ["Behavioral therapy"]
},

"trichotillomania": {
  "description": "Trichotillomania involves compulsive hair pulling.",
  "causes": ["Stress", "Genetic predisposition"],
  "remedies": ["Behavior therapy"]
},

"kleptomania": {
  "description": "Kleptomania is impulse control disorder causing stealing.",
  "causes": ["Impulse regulation issues"],
  "remedies": ["Therapy"]
},

"pyromania": {
  "description": "Pyromania involves compulsive fire setting.",
  "causes": ["Impulse control disorder"],
  "remedies": ["Psychotherapy"]
},

"oppositional_defiant_disorder": {
  "description": "ODD involves defiant and hostile behavior in children.",
  "causes": ["Genetic and environmental factors"],
  "remedies": ["Behavior therapy"]
},

"conduct_disorder": {
  "description": "Conduct disorder involves serious behavioral issues in youth.",
  "causes": ["Environmental and genetic factors"],
  "remedies": ["Therapy"]
},

"intermittent_explosive_disorder": {
  "description": "Intermittent explosive disorder causes sudden anger outbursts.",
  "causes": ["Impulse control issues"],
  "remedies": ["Therapy", "Medication"]
},

"delirium": {
  "description": "Delirium is sudden confusion due to illness or medication.",
  "causes": ["Infection", "Drug effects"],
  "remedies": ["Treat underlying cause"]
},

"mild_cognitive_impairment": {
  "description": "Mild cognitive impairment is slight but noticeable decline in cognition.",
  "causes": ["Aging", "Early dementia"],
  "remedies": ["Cognitive exercises"]
},

"frontotemporal_dementia": {
  "description": "Frontotemporal dementia affects personality and behavior.",
  "causes": ["Neurodegeneration"],
  "remedies": ["Supportive care"]
},

"vascular_dementia": {
  "description": "Vascular dementia is cognitive decline from reduced brain blood flow.",
  "causes": ["Stroke", "Vascular disease"],
  "remedies": ["Manage risk factors"]
},

"lewy_body_dementia": {
  "description": "Lewy body dementia involves abnormal brain protein deposits.",
  "causes": ["Neurodegeneration"],
  "remedies": ["Medication"]
},

"heat_exhaustion": {
  "description": "Heat exhaustion is heat-related illness causing weakness.",
  "causes": ["Prolonged heat exposure"],
  "remedies": ["Cooling", "Hydration"]
},

"altitude_pulmonary_edema": {
  "description": "Altitude pulmonary edema causes fluid in lungs at high altitude.",
  "causes": ["High altitude exposure"],
  "remedies": ["Descend altitude", "Oxygen therapy"]
},

"altitude_cerebral_edema": {
  "description": "Altitude cerebral edema causes brain swelling at high altitude.",
  "causes": ["Rapid ascent"],
  "remedies": ["Immediate descent", "Medical care"]
},

"motion_induced_vertigo": {
  "description": "Motion-induced vertigo causes dizziness during movement.",
  "causes": ["Inner ear imbalance"],
  "remedies": ["Medication", "Vestibular therapy"]
},

"benign_paroxysmal_positional_vertigo": {
  "description": "BPPV causes brief episodes of dizziness.",
  "causes": ["Inner ear crystals displacement"],
  "remedies": ["Epley maneuver"]
},

"labral_tear": {
  "description": "Labral tear is injury to shoulder or hip cartilage.",
  "causes": ["Trauma", "Overuse"],
  "remedies": ["Physical therapy", "Surgery"]
},

"shin_splints": {
  "description": "Shin splints cause pain along shin bone.",
  "causes": ["Overuse"],
  "remedies": ["Rest", "Ice"]
},

"stress_fracture": {
  "description": "Stress fracture is small crack in bone from overuse.",
  "causes": ["Repetitive stress"],
  "remedies": ["Rest"]
},

"compartment_syndrome": {
  "description": "Compartment syndrome is increased pressure in muscle compartments.",
  "causes": ["Trauma"],
  "remedies": ["Emergency surgery"]
},

"rhabdomyolysis": {
  "description": "Rhabdomyolysis is muscle breakdown releasing toxins into blood.",
  "causes": ["Severe injury", "Overexertion"],
  "remedies": ["IV fluids"]
},

"anaphylaxis": {
  "description": "Anaphylaxis is severe allergic reaction.",
  "causes": ["Food allergy", "Insect sting"],
  "remedies": ["Epinephrine injection"]
},

"urticaria": {
  "description": "Urticaria is hives causing itchy skin welts.",
  "causes": ["Allergic reaction"],
  "remedies": ["Antihistamines"]
},

"angioedema": {
  "description": "Angioedema is swelling beneath skin surface.",
  "causes": ["Allergic reaction"],
  "remedies": ["Antihistamines", "Epinephrine"]
}
"neurofibromatosis": {
  "description": "Neurofibromatosis is a genetic disorder causing tumors on nerve tissue.",
  "causes": ["Inherited genetic mutation"],
  "remedies": ["Monitoring", "Surgical removal if needed"]
},
"myocardial_infarction": {
  "description": "Myocardial infarction, commonly called a heart attack, occurs when blood flow to the heart is blocked.",
  "causes": ["Coronary artery blockage", "Blood clot"],
  "remedies": ["Emergency medical care", "Medications", "Surgery"]
},

"hypertrophic_cardiomyopathy": {
  "description": "Hypertrophic cardiomyopathy is thickening of the heart muscle.",
  "causes": ["Genetic mutation"],
  "remedies": ["Medications", "Surgical procedures"]
},

"dilated_cardiomyopathy": {
  "description": "Dilated cardiomyopathy causes enlargement of the heart chambers.",
  "causes": ["Genetics", "Alcohol abuse"],
  "remedies": ["Medications", "Heart transplant in severe cases"]
},

"restrictive_cardiomyopathy": {
  "description": "Restrictive cardiomyopathy reduces heart flexibility.",
  "causes": ["Amyloidosis", "Scar tissue"],
  "remedies": ["Medications", "Treat underlying cause"]
},

"thoracic_aneurysm": {
  "description": "Thoracic aneurysm is abnormal bulging in chest aorta.",
  "causes": ["High blood pressure", "Atherosclerosis"],
  "remedies": ["Surgical repair"]
},

"abdominal_aortic_aneurysm": {
  "description": "Abdominal aortic aneurysm is enlargement of lower aorta.",
  "causes": ["Smoking", "High blood pressure"],
  "remedies": ["Surgery"]
},

"mitral_valve_prolapse": {
  "description": "Mitral valve prolapse occurs when valve bulges backward.",
  "causes": ["Connective tissue disorder"],
  "remedies": ["Monitoring", "Surgery if severe"]
},

"aortic_stenosis": {
  "description": "Aortic stenosis is narrowing of aortic valve.",
  "causes": ["Aging", "Congenital defect"],
  "remedies": ["Valve replacement"]
},

"mitral_regurgitation": {
  "description": "Mitral regurgitation is leakage of blood backward in heart.",
  "causes": ["Valve damage"],
  "remedies": ["Surgery"]
},

"rheumatoid_arthritis": {
  "description": "Rheumatoid arthritis is autoimmune joint inflammation.",
  "causes": ["Immune system attack"],
  "remedies": ["Immunosuppressants", "Physical therapy"]
},

"juvenile_arthritis": {
  "description": "Juvenile arthritis affects children’s joints.",
  "causes": ["Autoimmune factors"],
  "remedies": ["Medication", "Therapy"]
},

"ankle_sprain": {
  "description": "Ankle sprain is ligament injury in ankle.",
  "causes": ["Twisting injury"],
  "remedies": ["Rest", "Ice", "Compression"]
},

"patellar_tendinitis": {
  "description": "Patellar tendinitis causes knee pain.",
  "causes": ["Overuse injury"],
  "remedies": ["Rest", "Physiotherapy"]
},

"meniscus_tear": {
  "description": "Meniscus tear is knee cartilage injury.",
  "causes": ["Sudden twisting"],
  "remedies": ["Rest", "Surgery if severe"]
},

"degenerative_disc_disease": {
  "description": "Degenerative disc disease affects spinal discs.",
  "causes": ["Aging"],
  "remedies": ["Physical therapy", "Pain relief"]
},

"herniated_disc": {
  "description": "Herniated disc occurs when spinal disc bulges.",
  "causes": ["Spinal strain"],
  "remedies": ["Physiotherapy", "Surgery if severe"]
},

"spinal_stenosis": {
  "description": "Spinal stenosis is narrowing of spinal canal.",
  "causes": ["Arthritis"],
  "remedies": ["Medication", "Surgery"]
},

"osteogenesis_imperfecta": {
  "description": "Osteogenesis imperfecta causes brittle bones.",
  "causes": ["Genetic mutation"],
  "remedies": ["Supportive care"]
},

"paget_disease_of_bone": {
  "description": "Paget disease disrupts bone remodeling.",
  "causes": ["Genetic factors"],
  "remedies": ["Medication"]
},

"costochondritis": {
  "description": "Costochondritis is inflammation of chest cartilage.",
  "causes": ["Injury", "Infection"],
  "remedies": ["Pain relievers"]
},

"thalassemia_minor": {
  "description": "Thalassemia minor is mild inherited blood disorder.",
  "causes": ["Genetic mutation"],
  "remedies": ["Monitoring"]
},

"iron_deficiency_anemia": {
  "description": "Iron deficiency anemia results from low iron levels.",
  "causes": ["Poor diet", "Blood loss"],
  "remedies": ["Iron supplements"]
},

"pernicious_anemia": {
  "description": "Pernicious anemia is vitamin B12 deficiency anemia.",
  "causes": ["Autoimmune disorder"],
  "remedies": ["Vitamin B12 injections"]
},

"hemolytic_anemia": {
  "description": "Hemolytic anemia is destruction of red blood cells.",
  "causes": ["Autoimmune disease"],
  "remedies": ["Medication"]
},

"thrombocytopenia": {
  "description": "Thrombocytopenia is low platelet count.",
  "causes": ["Bone marrow disorders"],
  "remedies": ["Treat underlying cause"]
},

"hyperparathyroidism": {
  "description": "Hyperparathyroidism causes excess parathyroid hormone.",
  "causes": ["Parathyroid tumor"],
  "remedies": ["Surgery"]
},

"hypoparathyroidism": {
  "description": "Hypoparathyroidism is low parathyroid hormone.",
  "causes": ["Surgical removal"],
  "remedies": ["Calcium supplements"]
},

"diabetic_neuropathy": {
  "description": "Diabetic neuropathy damages nerves due to diabetes.",
  "causes": ["High blood sugar"],
  "remedies": ["Blood sugar control"]
},

"diabetic_retinopathy": {
  "description": "Diabetic retinopathy damages retinal blood vessels.",
  "causes": ["Uncontrolled diabetes"],
  "remedies": ["Laser therapy"]
},

"diabetic_nephropathy": {
  "description": "Diabetic nephropathy damages kidneys.",
  "causes": ["Chronic high blood sugar"],
  "remedies": ["Blood sugar control"]
},

"methemoglobinemia": {
  "description": "Methemoglobinemia reduces oxygen delivery in blood.",
  "causes": ["Genetic defect", "Drug exposure"],
  "remedies": ["Methylene blue treatment"]
},

"gouty_arthritis": {
  "description": "Gouty arthritis causes joint inflammation from uric acid.",
  "causes": ["High uric acid"],
  "remedies": ["Medication", "Diet control"]
},

"complex_regional_pain_syndrome": {
  "description": "CRPS causes chronic pain after injury.",
  "causes": ["Nerve dysfunction"],
  "remedies": ["Physical therapy", "Medication"]
},

"narcolepsy_type_1": {
  "description": "Narcolepsy type 1 includes sudden muscle weakness.",
  "causes": ["Hypocretin deficiency"],
  "remedies": ["Stimulants"]
},
"sleep_paralysis": {
  "description": "Sleep paralysis is temporary inability to move during sleep.",
  "causes": ["Sleep cycle disruption"],
  "remedies": ["Improve sleep hygiene"]
},

"jet_lag": {
  "description": "Jet lag is temporary sleep disturbance from travel.",
  "causes": ["Time zone changes"],
  "remedies": ["Gradual schedule adjustment"]
},

"seasonal_affective_disorder": {
  "description": "SAD is depression related to seasonal changes.",
  "causes": ["Reduced sunlight"],
  "remedies": ["Light therapy"]
},

"claustrophobia": {
  "description": "Claustrophobia is fear of confined spaces.",
  "causes": ["Anxiety disorder"],
  "remedies": ["Therapy"]
},
    },
    "agoraphobia": {
        "description": "Agoraphobia is fear of open or crowded spaces.",
        "causes": ["Anxiety disorder"],
        "remedies": ["Cognitive behavioral therapy"]
    },
    "social_anxiety_disorder": {
        "description": "Social anxiety disorder causes intense fear of social situations.",
        "causes": ["Psychological factors"],
        "remedies": ["Therapy", "Medication"]
    },
    "tuberous_sclerosis": {
        "description": "Tuberous sclerosis is a genetic disorder causing benign tumors in organs.",
        "causes": ["Genetic mutation"],
        "remedies": ["Medication", "Surgery"]
    },
    "fragile_x_syndrome": {
        "description": "Fragile X syndrome is a genetic condition causing intellectual disability.",
        "causes": ["FMR1 gene mutation"],
        "remedies": ["Supportive therapy"]
    },
    "down_syndrome": {
        "description": "Down syndrome is a genetic disorder caused by extra chromosome 21.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Supportive care", "Therapies"]
    },
    "turner_syndrome": {
        "description": "Turner syndrome affects females due to missing X chromosome.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Hormone therapy"]
    },
    "klinefelter_syndrome": {
        "description": "Klinefelter syndrome affects males with extra X chromosome.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Testosterone therapy"]
    },
    "marfan_syndrome": {
        "description": "Marfan syndrome is a connective tissue disorder.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Hormone therapy"]
    },
    "klinefelter_syndrome": {
        "description": "Klinefelter syndrome affects males with extra X chromosome.",
        "causes": ["Chromosomal abnormality"],
        "remedies": ["Testosterone therapy"]
    },
    "marfan_syndrome": {
        "description": "Marfan syndrome is a connective tissue disorder.",
        "causes": ["Genetic mutation"],
        "remedies": ["Monitoring", "Surgery if needed"]
    },
    "ehlers_danlos_syndrome": {
        "description": "Ehlers-Danlos syndrome affects connective tissues causing hypermobility.",
        "causes": ["Genetic mutation"],
        "remedies": ["Physical therapy"]
    },
    "phenylketonuria": {
        "description": "Phenylketonuria is a metabolic disorder affecting amino acid breakdown.",
        "causes": ["Inherited enzyme deficiency"],
        "remedies": ["Special diet"]
    },
    "galactosemia": {
        "description": "Galactosemia is inability to process galactose sugar.",
        "causes": ["Genetic enzyme deficiency"],
        "remedies": ["Avoid dairy products"]
    },
    "tay_sachs_disease": {
        "description": "Tay-Sachs is genetic disorder destroying nerve cells.",
        "causes": ["Inherited mutation"],
        "remedies": ["Supportive care"]
    },
    "gaucher_disease": {
        "description": "Gaucher disease is inherited disorder affecting fat metabolism.",
        "causes": ["Genetic mutation"],
        "remedies": ["Enzyme replacement therapy"]
    },
    "pompe_disease": {
        "description": "Pompe disease is genetic disorder affecting muscle function.",
        "causes": ["Enzyme deficiency"],
        "remedies": ["Enzyme replacement therapy"]
    },
    "cystic_fibrosis": {
        "description": "Cystic fibrosis affects lungs and digestive system.",
        "causes": ["Inherited gene mutation"],
        "remedies": ["Respiratory therapy", "Medication"]
    },
    "primary_ciliary_dyskinesia": {
        "description": "Primary ciliary dyskinesia affects respiratory tract clearance.",
        "causes": ["Genetic mutation"],
        "remedies": ["Airway clearance therapy"]
    },
    "alpha_1_antitrypsin_deficiency": {
        "description": "Genetic disorder affecting lungs and liver.",
        "causes": ["Inherited mutation"],
        "remedies": ["Augmentation therapy"]
    },
    "goodpasture_syndrome": {
        "description": "Autoimmune disorder affecting lungs and kidneys.",
        "causes": ["Immune system attack"],
        "remedies": ["Immunosuppressants"]
    },
    "sjogren_syndrome": {
        "description": "Autoimmune disease causing dry eyes and mouth.",
        "causes": ["Immune dysfunction"],
        "remedies": ["Artificial tears", "Medication"]
    },
    "hashimoto_thyroiditis": {
        "description": "Autoimmune disease causing hypothyroidism.",
        "causes": ["Immune system attack on thyroid"],
        "remedies": ["Thyroid hormone replacement"]
    },
    "graves_disease": {
        "description": "Autoimmune disease causing hyperthyroidism.",
        "causes": ["Immune system stimulation of thyroid"],
        "remedies": ["Medication", "Radioactive iodine"]
    },
    "idiopathic_thrombocytopenic_purpura": {
        "description": "ITP is immune disorder lowering platelet count.",
        "causes": ["Autoimmune destruction of platelets"],
        "remedies": ["Steroids", "Immunotherapy"]
    },
    "aplastic_anemia": {
        "description": "Aplastic anemia is bone marrow failure.",
        "causes": ["Autoimmune factors", "Radiation"],
        "remedies": ["Transfusions", "Bone marrow transplant"]
    },
    "polycythemia_vera": {
        "description": "Polycythemia vera causes excess red blood cell production.",
        "causes": ["Bone marrow disorder"],
        "remedies": ["Phlebotomy", "Medication"]
    },
    "essential_thrombocythemia": {
        "description": "Essential thrombocythemia increases platelet production.",
        "causes": ["Bone marrow mutation"],
        "remedies": ["Medication"]
    },
    "myelofibrosis": {
        "description": "Myelofibrosis is bone marrow scarring disorder.",
        "causes": ["Genetic mutation"],
        "remedies": ["Medication", "Transplant"]
    },
    "amyloidosis": {
        "description": "Amyloidosis is buildup of abnormal protein in organs.",
        "causes": ["Protein misfolding"],
        "remedies": ["Chemotherapy", "Supportive care"]
    },
    "churg_strauss_syndrome": {
        "description": "Autoimmune disorder causing blood vessel inflammation.",
        "causes": ["Immune dysfunction"],
        "remedies": ["Steroids"]
    },
    "wegener_granulomatosis": {
        "description": "Autoimmune vasculitis affecting respiratory tract.",
        "causes": ["Immune system attack"],
        "remedies": ["Immunosuppressants"]
    },
    "takayasu_arteritis": {
        "description": "Inflammation of large arteries.",
        "causes": ["Autoimmune disorder"],
        "remedies": ["Steroids"]
    },
    "bechets_disease": {
        "description": "Behcet disease causes blood vessel inflammation.",
        "causes": ["Immune system dysfunction"],
        "remedies": ["Immunosuppressants"]
    },
"trigeminal_neuralgia": {
  "description": "Trigeminal neuralgia is a chronic pain condition affecting the trigeminal nerve, which carries sensation from your face to your brain.",
  "symptoms": [
    "Sudden, intense episodes of facial pain",
    "Pain triggered by touch, eating, or speaking",
    "Spontaneous electric shock-like sensations",
    "Pain localized to the jaw, teeth, or cheek",
    "Brief attacks lasting seconds to minutes"
  ],
  "causes": [
    "Nerve compression by a blood vessel",
    "Multiple sclerosis (demyelination)",
    "Tumor pressing on the nerve",
    "Physical trauma or surgical injury"
  ],
  "risk_factors": [
    "Age (more common in people over 50)",
    "Gender (higher prevalence in women)",
    "High blood pressure",
    "Family history of nerve disorders"
  ],
  "diagnosis": [
    "Neurological examination",
    "MRI (specifically MRA or MRTA to see blood vessels)",
    "Clinical history of pain triggers"
  ],
  "remedies": [
    "Anticonvulsant medications (e.g., carbamazepine)",
    "Muscle relaxants",
    "Microvascular decompression (surgery)",
    "Gamma Knife radiosurgery"
  ],
  "prevention": [
    "Managing underlying conditions like MS",
    "Regular monitoring of vascular health",
    "Avoiding known triggers during flare-ups"
  ]
}
"bells_palsy": {
  "description": "Bell's palsy is a sudden, temporary weakness or paralysis of the facial muscles, typically affecting only one side of the face.",
  "symptoms": [
    "Rapid onset of mild weakness to total paralysis",
    "Facial droop and difficulty making expressions",
    "Drooling",
    "Pain around the jaw or behind the ear",
    "Increased sensitivity to sound (hyperacusis)",
    "Loss of taste on the front of the tongue"
  ],
  "causes": [
    "Inflammation of the 7th cranial (facial) nerve",
    "Viral infections (Herpes simplex, Epstein-Barr)",
    "Immune system response"
  ],
  "risk_factors": [
    "Pregnancy (especially third trimester)",
    "Diabetes",
    "Upper respiratory infections (flu/cold)",
    "Family history"
  ],
  "diagnosis": [
    "Physical exam (observing facial movement)",
    "Electromyography (EMG) to test nerve damage",
    "MRI or CT to rule out stroke or tumor"
  ],
  "remedies": [
    "Corticosteroids (to reduce nerve swelling)",
    "Antiviral medications",
    "Physical therapy (facial exercises)",
    "Eye protection (drops/patches if eye won't close)"
  ],
  "prevention": [
    "Early treatment of viral infections",
    "Stress management",
    "General immune health"
  ]
}
"cluster_headache": {
  "description": "Cluster headaches are a series of relatively short but extremely painful headaches that occur in cyclical patterns or 'clusters.'",
  "symptoms": [
    "Excruciating pain centered around one eye or temple",
    "Redness or watering of the eye on the affected side",
    "Drooping eyelid or constricted pupil (Horner's syndrome)",
    "Nasal congestion or runny nose (one side)",
    "Restlessness or inability to lie still during an attack"
  ],
  "causes": [
    "Hypothalamus dysfunction (the body's 'biological clock')",
    "Dilation of the carotid artery/cavernous sinus",
    "Trigeminal nerve activation"
  ],
  "risk_factors": [
    "Gender (more common in men)",
    "Age (typically starts in the 20s or 30
"complex_regional_pain_syndrome": {
  "description": "CRPS is a form of chronic pain that usually affects an arm or a leg, typically developing after an injury, surgery, stroke, or heart attack.",
  "symptoms": [
    "Continuous burning or 'pins and needles' pain",
    "Allodynia (pain from even a light touch or breeze)",
    "Changes in skin temperature, color, or texture",
    "Swelling in the affected limb",
    "Changes in hair and nail growth patterns",
    "Joint stiffness and muscle atrophy"
  ],
  "causes": [
    "Abnormal inflammation or nerve 'glitching' after trauma",
    "Type 1: Occurs after an injury without direct nerve damage",
    "Type 2: Occurs after a distinct, documented nerve injury",
    "Maladaptive neuroplasticity (the brain 'learning' to stay in pain)"
  ],
  "risk_factors": [
    "Female gender (statistically higher prevalence)",
    "Recent limb trauma or surgery",
    "Periods of prolonged immobilization (e.g., in a cast)",
    "Genetic predisposition to inflammatory responses"
  ],
  "diagnosis": [
    "Clinical diagnosis using the 'Budapest Criteria'",
    "Triple-phase bone scan (to see changes in blood flow/bone)",
    "Infrared thermography to map temperature asymmetry",
    "MRI to rule out underlying tissue damage"
  ],
  "remedies": [
    "Physical therapy (specifically Graded Motor Imagery)",
    "Mirror box therapy to 'retrain' the brain",
    "Medications (Bisphosphonates, gabapentin, or ketamine)",
    "Sympathetic nerve blocks",
    "Spinal Cord Stimulation (SCS) or DRG stimulation"
  ],
  "prevention": [
    "Early mobilization after limb surgery or injury",
    "High-dose Vitamin C after certain fractures (e.g., wrist)",
    "Immediate physical therapy for early-stage nerve pain"
  ]
}
"guillain_barre_syndrome": {
  "description": "Guillain-Barré Syndrome (GBS) is a rare autoimmune disorder where the body's immune system attacks part of the peripheral nervous system, specifically the myelin sheath.",
  "symptoms": [
    "Prickling 'pins and needles' sensations in fingers and toes",
    "Ascending weakness (starts in legs and spreads to upper body)",
    "Unsteady walking or inability to climb stairs",
    "Difficulty with facial movements (speaking, chewing, swallowing)",
    "Severe pain that may feel achy or cramp-like",
    "Rapid heart rate and blood pressure fluctuations"
  ],
  "causes": [
    "Molecular mimicry following an infection",
    "Campylobacter jejuni (common food poisoning bacteria)",
    "Viral infections (Flu, Zika, Cytomegalovirus, COVID-19)",
    "Recent surgery or trauma (rarely)"
  ],
  "risk_factors": [
    "Age (more common in older adults, though anyone can get it)",
    "Gender (slightly more common in men)",
    "Recent gastrointestinal or respiratory infection"
  ],
  "diagnosis": [
    "Spinal tap (Lumbar puncture) to look for elevated protein",
    "Electromyography (EMG) to measure nerve activity",
    "Nerve conduction studies (NCS) to check signal speed"
  ],
  "remedies": [
    "Plasmapheresis (Plasma exchange to 'wash' out antibodies)",
    "Intravenous immunoglobulin (IVIG) therapy",
    "Physical and occupational therapy for rehabilitation",
    "Mechanical ventilation (if breathing muscles are affected)"
  ],
  "prevention": [
    "Safe food handling (to prevent Campylobacter)",
    "Prompt medical attention for rapidly spreading weakness",
    "Vaccination (the risk from the flu itself is higher than the vaccine risk)"
  ]
}
"multiple_sclerosis": {
  "description": "Multiple Sclerosis (MS) is a chronic disease where the immune system attacks the protective myelin sheath in the Central Nervous System (CNS), causing communication problems between the brain and the rest of the body.",
  "symptoms": [
    "Optic neuritis (blurred vision or pain in one eye)",
    "Lhermitte’s sign (electric shock sensation when bending the neck)",
    "Numbness or weakness in one or more limbs",
    "Fatigue and dizziness",
    "Slurred speech",
    "Tremors or lack of coordination"
  ],
  "causes": [
    "Autoimmune response targeting the CNS myelin",
    "Genetic predisposition",
    "Environmental triggers (e.g., Low Vitamin D, smoking)",
    "Viral triggers (notably Epstein-Barr virus)"
  ],
  "risk_factors": [
    "Age (most common between 20 and 40)",
    "Gender (2-3 times more common in women)",
    "Climate (more prevalent in temperate/colder regions)",
    "Family history"
  ],
  "diagnosis": [
    "MRI scans (to detect 'plaques' or lesions in the brain/spine)",
    "Lumbar puncture (to check for oligoclonal bands in spinal fluid)",
    "Evoked potential tests (measuring speed of nerve signals)",
    "Blood tests to rule out other conditions"
  ],
  "remedies": [
    "Disease-Modifying Therapies (DMTs) to slow progression",
    "Corticosteroids (for acute relapses)",
    "Physical therapy and muscle relaxants",
    "Plasma exchange (in severe, non-responsive cases)"
  ],
  "prevention": [
    "No known prevention",
    "Early diagnosis and treatment (to prevent permanent disability)",
    "Maintaining adequate Vitamin D levels",
    "Smoking cessation"
  ]
}
"myasthenia_gravis": {
  "description": "Myasthenia gravis is a chronic autoimmune neuromuscular disorder characterized by fluctuating weakness of the voluntary muscle groups.",
  "symptoms": [
    "Ptosis (drooping of one or both eyelids)",
    "Diplopia (blurred or double vision)",
    "Change in facial expression (a 'snarling' smile)",
    "Dysphagia (difficulty swallowing or chewing)",
    "Shortness of breath",
    "Muscle weakness that worsens with activity and improves with rest"
  ],
  "causes": [
    "Antibodies blocking or destroying nicotinic acetylcholine receptors",
    "Thymus gland abnormalities (tumors or hyperplasia)",
    "Genetic factors (rarely)"
  ],
  "risk_factors": [
    "Gender (more common in women under 40 and men over 60)",
    "History of other autoimmune diseases",
    "Thymic tumors"
  ],
  "diagnosis": [
    "Ice pack test (cold improves eyelid drooping)",
    "Edrophonium (Tensilon) test",
    "Blood test for Acetylcholine Receptor (AChR) antibodies",
    "Repetitive nerve stimulation (EMG)"
  ],
  "remedies": [
    "Cholinesterase inhibitors (e.g., pyridostigmine)",
    "Corticosteroids and immunosuppressants",
    "Thymectomy (surgical removal of the thymus gland)",
    "Plasmapheresis or IVIG for 'crises'"
  ],
  "prevention": [
    "Avoiding triggers (stress, extreme heat, certain medications)",
    "Managing respiratory infections promptly",
    "Regular monitoring of thymus health"
  ]
}
"amyotrophic_lateral_sclerosis": {
  "description": "ALS is a progressive neurodegenerative disease that affects nerve cells in the brain and spinal cord, specifically those that control voluntary muscle movement.",
  "symptoms": [
    "Fasciculations (muscle twitching) in the arm, leg, shoulder, or tongue",
    "Muscle cramps and tight/stiff muscles (spasticity)",
    "Muscle weakness affecting an arm, a leg, neck, or diaphragm",
    "Slurred and nasal speech (dysarthria)",
    "Difficulty chewing or swallowing (dysphagia)"
  ],
  "causes": [
    "Degeneration and death of upper and lower motor neurons",
    "Genetic mutations (e.g., SOD1, C9orf72) in 5-10% of cases",
    "Protein mishandling and oxidative stress within nerve cells"
  ],
  "risk_factors": [
    "Age (most common between 40 and 70)",
    "Gender (slightly more common in men)",
    "Genetics (family history)",
    "Environmental factors (e.g., military service is a statistical risk factor)"
  ],
  "diagnosis": [
    "Electromyography (EMG) to detect electrical activity in muscles",
    "Nerve Conduction Study (NCS)",
    "MRI (to rule out spinal cord tumors or herniated disks)",
    "Blood and urine tests to rule out heavy metal poisoning"
  ],
  "remedies": [
    "Riluzole (blocks glutamate to slow progression)",
    "Edaravone (antioxidant to slow decline in daily functioning)",
    "Tofersen (specifically for SOD1 genetic variants)",
    "Noninvasive ventilation (BiPAP) and feeding tubes"
  ],
  "prevention": [
    "No known prevention",
    "Early intervention for respiratory support",
    "Genetic counseling for families with history"
]
}
"parkinsons_disease": {
  "description": "Parkinson's disease is a progressive disorder of the central nervous system that affects movement, often including tremors, caused by the loss of dopamine-producing neurons.",
  "symptoms": [
    "Tremor at rest (often 'pill-rolling' of the hand)",
    "Bradykinesia (extreme slowness of movement)",
    "Muscle rigidity or stiffness",
    "Postural instability (impaired balance and coordination)",
    "Micrographia (handwriting becoming very small)",
    "Masked face (reduced facial expression)"
  ],
  "causes": [
    "Death of neurons in the substantia nigra",
    "Accumulation of Lewy bodies (alpha-synuclein protein clumps)",
    "Genetic mutations (e.g., LRRK2, PINK1)",
    "Environmental triggers (pesticides, heavy metals)"
  ],
  "risk_factors": [
    "Age (typically begins around age 60 or older)",
    "Heredity",
    "Gender (men are more likely to develop it)",
    "Exposure to toxins"
  ],
  "diagnosis": [
    "Clinical neurological exam (assessment of 'TRAP' symptoms)",
    "DaTscan (imaging to visualize dopamine transporters)",
    "Levodopa challenge (seeing if symptoms improve with medication)",
    "MRI (to rule out other brain disorders)"
  ],
  "remedies": [
    "Levodopa/Carbidopa (the 'gold standard' for dopamine replacement)",
    "Dopamine agonists",
    "MAO-B inhibitors",
    "Deep Brain Stimulation (DBS) surgery",
    "Physical and speech therapy"
  ],
  "prevention": [
    "Regular aerobic exercise",
    "Dietary antioxidants",
    "Avoiding known neurotoxins",
    "Caffeine consumption (statistically associated with lower risk)"
  ]
}
"huntingtons_disease": {
  "description": "Huntington's disease is a rare, inherited disease that causes the progressive breakdown (degeneration) of nerve cells in the brain, primarily affecting movement, cognition, and psychiatric health.",
  "symptoms": [
    "Chorea (involuntary, jerky 'dancing' movements)",
    "Dystonia (muscle rigidity or contractures)",
    "Impaired gait, posture, and balance",
    "Difficulty with speech or swallowing",
    "Cognitive decline (difficulty organizing or focusing)",
    "Psychiatric symptoms (depression, irritability, or OCD)"
  ],
  "causes": [
    "Genetic mutation in the HTT gene",
    "Excessive 'CAG' repeats in the DNA sequence",
    "Degeneration of the striatum (part of the basal ganglia)"
  ],
  "risk_factors": [
    "Heredity (Autosomal dominant: 50% chance of passing it to children)",
    "Family history"
  ],
  "diagnosis": [
    "Genetic testing (counting CAG repeats)",
    "MRI or CT (to see shrinkage/atrophy in the brain's striatum)",
    "Neurological and psychiatric evaluations"
  ],
  "remedies": [
    "Tetrabenazine or Deutetrabenazine (to reduce chorea)",
    "Antipsychotic medications",
    "Psychotherapy and speech therapy",
    "Occupational therapy"
  ],
  "prevention": [
    "No biological prevention",
    "Genetic counseling and pre-implantation genetic diagnosis (PGD)",
    "Early lifestyle interventions for cognitive health"
  ]
}
"narcolepsy": {
  "description": "Narcolepsy is a chronic neurological disorder that affects the brain's ability to control sleep-wake cycles, characterized by excessive daytime sleepiness and sudden bouts of sleep.",
  "symptoms": [
    "Excessive Daytime Sleepiness (EDS)",
    "Cataplexy (sudden loss of muscle tone triggered by emotion)",
    "Sleep paralysis (temporary inability to move or speak while falling asleep or waking)",
    "Hypnagogic hallucinations (vivid, often scary dreams while awake)",
    "Fragmented nighttime sleep"
  ],
  "causes": [
    "Loss of orexin (hypocretin)-producing neurons in the hypothalamus",
    "Autoimmune attack on orexin neurons (often triggered by infection)",
    "Genetic predisposition (HLA-DQB1*06:02 gene)"
  ],
  "risk_factors": [
    "Age (typically starts between 10 and 30 years old)",
    "Family history",
    "Recent history of certain infections (e.g., H1N1 flu)"
  ],
  "diagnosis": [
    "Polysomnography (overnight sleep study)",
    "Multiple Sleep Latency Test (MSLT - measuring how fast one falls asleep)",
    "Cerebrospinal fluid analysis (checking for low orexin levels)"
  ],
  "remedies": [
    "Stimulants (e.g., Modafinil)",
    "Sodium Oxybate (to improve nighttime sleep and reduce cataplexy)",
    "Orexin receptor agonists (new for 2026)",
    "Scheduled short naps and strict sleep hygiene"
  ],
  "prevention": [
    "No known prevention",
    "Early detection to prevent accidents (driving, machinery)",
    "Managing triggers for cataplexy (intense emotions)"
  ]
}
"epilepsy": {
  "description": "Epilepsy is a central nervous system (neurological) disorder in which brain activity becomes abnormal, causing seizures or periods of unusual behavior, sensations, and sometimes loss of awareness.",
  "symptoms": [
    "Temporary confusion",
    "A staring spell (absence seizure)",
    "Uncontrollable jerking movements of the arms and legs",
    "Loss of consciousness or awareness",
    "Psychic symptoms such as fear, anxiety, or deja vu (aura)"
  ],
  "causes": [
    "Genetic influence",
    "Head trauma (TBI)",
    "Brain abnormalities (tumors, vascular malformations)",
    "Infectious diseases (meningitis, AIDS, viral encephalitis)",
    "Prenatal injury or developmental disorders"
  ],
  "risk_factors": [
    "Age (most common in children and older adults)",
    "Family history",
    "Stroke and other vascular diseases",
    "Dementia",
    "History of childhood febrile seizures"
  ],
  "diagnosis": [
    "Electroencephalogram (EEG) to record brain wave patterns",
    "High-resolution MRI or CT to look for structural lesions",
    "Functional MRI (fMRI) or PET scans",
    "Neurological exam to test behavior and motor abilities"
  ],
  "remedies": [
    "Anti-epileptic drugs (AEDs)",
    "Vagus Nerve Stimulation (VNS)",
    "Ketogenic diet (primarily for treatment-resistant children)",
    "Responsive Neurostimulation (RNS) or surgery"
  ],
  "prevention": [
    "Preventing head injuries (helmets/seatbelts)",
    "Proper prenatal care to reduce birth-related trauma",
    "Managing high blood pressure and infections",
    "Avoiding seizure triggers like sleep deprivation or alcohol"
  ]
}
"tourette_syndrome": {
  "description": "Tourette Syndrome (TS) is a neurological disorder characterized by repetitive, involuntary movements and vocalizations called tics.",
  "symptoms": [
    "Simple motor tics (eye blinking, facial grimacing, shoulder shrugging)",
    "Complex motor tics (hopping, twisting, or repeating observed movements)",
    "Simple vocal tics (throat clearing, sniffing, grunting)",
    "Complex vocal tics (repeating words/phrases, or coprolalia—rare involuntary swearing)",
    "Premonitory urge (an uncomfortable 'itch' or tension before the tic)"
  ],
  "causes": [
    "Dysfunction in the basal ganglia, frontal lobes, and cortex",
    "Imbalance in neurotransmitters (dopamine and serotonin)",
    "Genetic mutations and inheritance patterns"
  ],
  "risk_factors": [
    "Gender (3-4 times more common in males)",
    "Family history of tics or other neurological disorders",
    "Prenatal or perinatal complications"
  ],
  "diagnosis": [
    "Clinical evaluation (must have both motor and vocal tics for >1 year)",
    "Observation of tic patterns",
    "Ruling out other conditions (e.g., seizures or Huntington’s)"
  ],
  "remedies": [
    "Comprehensive Behavioral Intervention for Tics (CBIT)",
    "Dopamine-blocking medications",
    "Alpha-adrenergic agonists (e.g., guanfacine)",
    "Deep Brain Stimulation (DBS) for severe, refractory cases"
  ],
  "prevention": [
    "No known prevention",
    "Stress management (as stress significantly increases tic frequency)",
    "Early behavioral therapy to manage urges"
  ]
}
"dystonia": {
  "description": "Dystonia is a movement disorder in which your muscles contract involuntarily, causing repetitive or twisting movements or abnormal postures.",
  "symptoms": [
    "Involuntary muscle contractions that cause twisting",
    "A dragging leg or cramping in the foot",
    "Involuntary neck tilting (cervical dystonia)",
    "Uncontrollable blinking (blepharospasm)",
    "Speech difficulties or 'tightness' in the voice"
  ],
  "causes": [
    "Basal ganglia dysfunction (the brain's movement processor)",
    "Genetic mutations (e.g., DYT1 gene)",
    "Secondary to trauma, stroke, or oxygen deprivation",
    "Side effect of certain medications (tardive dystonia)"
  ],
  "risk_factors": [
    "Family history",
    "Repetitive tasks (e.g., 'Musician's Dystonia' or 'Writer's Cramp')",
    "Exposure to neuroleptic/antipsychotic drugs",
    "Wilson's disease (copper buildup)"
  ],
  "diagnosis": [
    "Clinical observation of postures and movements",
    "EMG (to see which muscles are firing together)",
    "Genetic testing",
    "MRI to rule out structural brain damage"
  ],
  "remedies": [
    "Botulinum toxin (Botox) injections to 'silence' specific muscles",
    "Anticholinergic medications",
    "Physical and occupational therapy",
    "Deep Brain Stimulation (DBS)"
  ],
  "prevention": [
    "Early detection of medication side effects",
"Ergonomic adjustments for task-specific triggers",
    "Genetic counseling"
  ]
}
"stiff_person_syndrome": {
  "description": "Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder characterized by persistent muscle stiffness and painful episodes of violent muscle spasms.",
  "symptoms": [
    "Progressive stiffness in the trunk and limbs",
    "Hunched-over or 'board-like' posture",
    "Painful muscle spasms triggered by sudden noise, touch, or emotional stress",
    "Fear of open spaces (due to fear of triggers causing a fall)",
    "Difficulty walking or moving freely"
  ],
  "causes": [
    "Autoimmune attack on the GAD (glutamic acid decarboxylase) enzyme",
    "Severe deficiency of GABA (the brain's primary inhibitory 'calm down' neurotransmitter)",
    "Paraneoplastic syndrome (rarely associated with certain cancers)"
  ],
  "risk_factors": [
    "Gender (more common in women)",
    "Middle age (typically appearing between 30 and 60)",
    "Co-existing autoimmune conditions (Type 1 diabetes, thyroiditis, vitiligo)"
  ],
  "diagnosis": [
    "Blood test for GAD antibodies (present in ~60-80% of cases)",
    "Electromyography (EMG) showing continuous motor unit activity",
    "Lumbar puncture to check for GAD antibodies in spinal fluid"
  ],
  "remedies": [
    "High-dose Benzodiazepines (to boost GABA activity)",
    "IVIG (Intravenous Immunoglobulin) to dampen the immune attack",
    "Muscle relaxants (e.g., Baclofen)",
    "Plasmapheresis (plasma exchange)"
  ],
  "prevention": [
    "No known prevention",
    "Managing autoimmune health",
    "Avoiding known sensory triggers (loud noises or physical startles)"
  ]
}
"small_fiber_neuropathy": {
  "description": "Small fiber neuropathy is a condition where the small, unmyelinated or thinly myelinated nerve fibers are damaged, leading to sensory and autonomic symptoms.",
  "symptoms": [
    "Intense burning or 'searing' pain in the hands and feet",
    "Pins and needles (paresthesia)",
    "Electric shock-like bursts",
    "Autonomic issues (dizziness when standing, abnormal sweating)",
    "Hypersensitivity (allodynia)—even socks or bedsheets can hurt"
  ],
  "causes": [
    "Diabetes or pre-diabetes (the most common cause)",
    "Vitamin B12 deficiency",
    "Autoimmune conditions (e.g., Sjögren’s syndrome, Celiac disease)",
    "Genetic mutations (SCN9A or SCN10A sodium channel genes)"
  ],
  "risk_factors": [
    "Metabolic syndrome",
    "Chronic alcohol consumption",
    "Chemotherapy history",
    "Older age"
  ],
  "diagnosis": [
    "Skin punch biopsy (measuring Intraepidermal Nerve Fiber Density)",
    "QSART (test to measure sweat response)",
    "Skin wrinkling test",
    "Genetic testing for sodium channel mutations"
  ],
  "remedies": [
    "Neuropathic pain meds (Gabapentin, Duloxetine)",
    "Topical treatments (Capsaicin or Lidocaine patches)",
    "Managing the underlying cause (e.g., blood sugar control)",
    "IVIG (if an autoimmune cause is found)"
  ],
  "prevention": [
    "Tight blood sugar management",
    "Maintaining healthy Vitamin B12 and B6 levels",
    "Avoiding neurotoxins like excessive alcohol",
    "Early screening for metabolic disorders"
  ]
}
"essential_tremor": {
  "description": "Essential tremor is a neurological disorder that causes involuntary and rhythmic shaking, primarily affecting the hands during voluntary movement.",
  "symptoms": [
    "Tremor that occurs during action (writing, eating, reaching)",
    "Shaking that worsens with stress, caffeine, or temperature extremes",
    "Nodding or 'shaking' of the head (yes-yes or no-no motion)",
    "Quivering voice",
    "Difficulty with fine motor tasks (threading a needle)"
  ],
  "causes": [
    "Abnormal electrical communication in the cerebello-thalamo-cortical circuit",
    "Genetic mutations (found in roughly 50% of cases)",
    "Degeneration of Purkinje cells in the cerebellum (debated)"
  ],
  "risk_factors": [
    "Age (more common in those over 40)",
    "Genetics (Autosomal dominant inheritance)",
    "Environmental toxins (under investigation)"
  ],
  "diagnosis": [
    "Clinical observation (Action tremor vs. Rest tremor)",
    "Archimedes Spiral test (drawing a spiral to see the tremor pattern)",
    "DaTscan (to rule out Parkinson’s Disease)",
    "Blood tests to rule out thyroid disease or caffeine toxicity"
  ],
  "remedies": [
    "Beta-blockers (e.g., Propranolol)",
    "Anti-seizure medications (e.g., Primidone)",
    "Focused Ultrasound (HIFU) to 'burn' the tiny glitchy area",
    "Deep Brain Stimulation (DBS)",
    "Adaptive tools (weighted utensils)"
  ],
  "prevention": [
    "No known prevention",
    "Limiting caffeine and stimulants",
    "Stress management techniques"
  ]
}

