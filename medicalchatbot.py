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
"superior_canal_dehiscence": {
  "description": "SCDS is a medical condition of the inner ear that leads to various balance and auditory symptoms, most notably the ability to hear internal bodily sounds with abnormal clarity.",
  "symptoms": [
    "Autophony (hearing your own voice, breathing, or heartbeat loudly)",
    "Hearing your eyes move (a 'scratching' or 'swishing' sound)",
    "Tullio phenomenon (vertigo triggered by loud noises)",
    "Hennebert sign (vertigo triggered by pressure changes in the ear)",
    "Hearing your own footsteps 'thumping' in your head",
    "Pulsatile tinnitus (rhythmic whistling or booming synchronous with the pulse)"
  ],
  "causes": [
    "A hole or thinning in the temporal bone (superior semicircular canal)",
    "Congenital developmental abnormality (failure of the bone to thicken)",
    "Head trauma causing a pre-existing thin bone to break",
    "Chronic pressure from the brain against the skull base"
  ],
  "risk_factors": [
    "Genetic predisposition to thin cranial bones",
    "History of head injury",
    "Increased intracranial pressure"
  ],
  "diagnosis": [
    "High-resolution CT scan of the temporal bone",
    "Vestibular Evoked Myogenic Potentials (VEMP) testing",
    "Audiometry (showing a 'gap' between air and bone conduction)",
    "Clinical 'Eye Movement' test (observing nystagmus triggered by sound)"
  ],
  "remedies": [
    "Surgical 'plugging' or resurfacing of the dehiscence",
    "Avoidance of triggers (loud noises, pressure changes)",
    "Pressure equalization (PE) tubes in the eardrum",
    "Vestibular rehabilitation therapy"
  ],
  "prevention": [
    "N/A (largely structural/congenital)",
    "Protecting the head from trauma if bone thinning is known"
  ]
}
"cotards_delusion": {
  "description": "A rare neuropsychiatric syndrome in which a person holds the delusional belief that they are dead, non-existent, or putrefying.",
  "symptoms": [
    "Nihilistic delusions (belief that the world or self does not exist)",
    "Insensitivity to pain (since a 'corpse' cannot feel pain)",
    "Refusal to eat or drink (logic: 'Dead people don't need fuel')",
    "Walking 'corpse' behavior (social withdrawal and stagnation)",
    "Severe depression and anxiety regarding their 'state of decay'",
    "Belief in immortality (logic: 'I cannot die if I am already dead')"
  ],
  "causes": [
    "Severe disconnection between the Fusiform Face Area and the Amygdala",
    "Damage to the Right Temporoparietal Junction (rTPJ)",
    "Atrophy in the Insular Cortex (the 'Interoception' hub)",
    "Adverse reaction to Acyclovir (in patients with renal failure)",
    "Severe clinical depression or schizophrenia"
  ],
  "risk_factors": [
    "Advanced age and neurodegenerative conditions",
    "Bipolar disorder or severe clinical depression",
    "Post-traumatic brain injury affecting the right hemisphere"
  ],
  "diagnosis": [
    "Clinical psychiatric interview and history",
    "MRI to identify atrophy in the frontoparietal and insular regions",
    "Metabolic screening (checking for Acyclovir toxicity or kidney issues)",
    "The 'Nihilistic Belief' assessment scale"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT) — often the 'Hard Reset' that works",
    "Antipsychotic and antidepressant medication",
    "Intravenous fluids and nutrition (to override the 'Dead' logic)",
    "Cognitive Behavioral Therapy (CBT) for delusional restructuring"
  ],
  "prevention": [
    "Early intervention for severe depressive episodes",
    "Careful monitoring of antiviral dosages in kidney patients"
  ]
}

"prosopometamorphopsia": {
  "description": "A visual perception disorder where facial features appear distorted in shape, size, location, or color. It is a highly specific failure of the face-processing circuitry.",
  "symptoms": [
    "Drooping, stretching, or 'melting' of facial features",
    "Hemi-PMO (distortions appearing on only one side of the face)",
    "Features appearing 'too small' (micro-prosopia) or 'too large' (macro-prosopia)",
    "Perceiving faces as 'demonic' or animal-like (pithecoid)",
    "Intact recognition (the patient knows who the person is, despite the distortion)"
  ],
  "causes": [
    "Lesions in the Splenium of the Corpus Callosum",
    "Damage to the Fusiform Face Area (FFA) or Occipital Face Area (OFA)",
    "Temporal lobe seizures",
    "Migraine auras affecting the visual processing pathway",
    "Post-stroke ischemia in the posterior cerebral artery"
  ],
  "risk_factors": [
    "Traumatic brain injury (TBI) to the back of the head",
    "Chronic migraines with complex auras",
    "Vascular disease affecting the occipital lobe"
  ],
  "diagnosis": [
    "The 'Face-Sketch' test (the patient draws what they see)",
    "fMRI to identify specific 'leaky' nodes in the face-processing network",
    "Neurological screening to rule out psychiatric psychosis",
    "Visual field perimetry"
  ],
  "remedies": [
    "Treating the underlying cause (e.g., anti-seizure or migraine meds)",
    "Prism lenses to shift the visual field in Hemi-PMO cases",
    "Desensitization therapy",
    "Wait-and-see (some post-stroke cases resolve as the brain 're-patches' the circuit)"
  ],
  "prevention": [
    "Standard stroke and TBI prevention protocols"
  ]
}
"aiws_temporal_variant": {
  "description": "A neurological condition where the perception of time is distorted, causing external events to appear significantly faster (Tachysensia) or slower than they actually are.",
  "symptoms": [
    "Tachysensia: Everything feels 'sped up' (people talking fast, movements jerky)",
    "Protracted Duration: Time feels 'stretched' (seconds feel like minutes)",
    "Accompanying sense of urgency or 'rushing' in the mind",
    "Distorted perception of sound (voices sounding high-pitched or frantic)",
    "Transience: Episodes typically last 5 to 20 minutes"
  ],
  "causes": [
    "Abnormal electrical activity in the Parietal-Temporal-Occipital (PTO) junction",
    "Migraine auras (the most common 'software trigger')",
    "Temporal Lobe Epilepsy (localized 'clock' seizures)",
    "Infection with the Epstein-Barr virus (common in pediatric cases)",
    "Dysregulation of the Suprachiasmatic Nucleus (the hardware master clock)"
  ],
  "risk_factors": [
    "Childhood (often outgrown by adolescence)",
    "Family history of migraines",
    "High fever or viral infections",
    "Acute stress or sensory overload"
  ],
  "diagnosis": [
    "EEG to rule out subclinical seizure activity",
    "MRI to check for lesions in the PTO junction",
    "Migraine diary to track correlations with headache phases",
    "Neuropsychological evaluation of time-estimation abilities"
  ],
  "remedies": [
    "Treating the underlying migraine or infection",
    "Dark, quiet environments to reduce 'input noise'",
    "Grounding techniques (focusing on rhythmic breathing)",
    "Reassurance (the 'Insight' that the clock will reset itself)"
  ],
  "prevention": [
    "Managing migraine triggers (sleep, diet, hydration)",
    "Reducing screen time during 'high-risk' periods"
  ]
}

"palinacousis": {
  "description": "A rare auditory illusion where a sound is heard repeatedly after the original stimulus has ceased. It is a paroxysmal phenomenon of auditory persistence.",
  "symptoms": [
    "Hearing the exact replay of a previous sound (e.g., a conversation heard earlier)",
    "Sounds can be 'stuck' for seconds or recur hours later",
    "Preserved insight (the user knows the sound is a 'replay')",
    "Often localized to one ear (if the lesion is one-sided)",
    "Not to be confused with 'earworms' (which are mental); these sound physically real"
  ],
  "causes": [
    "Lesions in the Superior Temporal Gyrus (the primary audio hub)",
    "Temporal lobe seizures (ictal or post-ictal states)",
    "Neoplasms (tumors) in the non-dominant hemisphere",
    "Side effects of specific medications (e.g., trazodone or nefazodone)",
    "Migraine auras affecting the auditory cortex"
  ],
  "risk_factors": [
    "History of temporal lobe epilepsy",
    "Recent head trauma to the side of the skull",
    "Vascular issues in the posterior cerebral circulation"
  ],
  "diagnosis": [
    "EEG to detect 'spike and wave' patterns in the temporal lobe",
    "MRI to check for structural anomalies in the auditory cortex",
    "Audiometry to rule out peripheral ear issues",
    "Neurological history to distinguish from psychiatric 'voices'"
  ],
  "remedies": [
    "Treating the underlying cause (e.g., anti-epileptic drugs)",
    "Reviewing and adjusting pharmaceutical 'drivers'",
    "Surgical intervention for localized tumors",
    "Cognitive 'masking' (listening to new sounds to clear the buffer)"
  ],
  "prevention": [
    "Managing seizure disorders",
    "Standard neurological safety protocols"
  ]
}

"ganzfeld_effect": {
  "description": "A phenomenon of perception caused by exposure to an unstructured, uniform stimulation field, leading to 'brain-generated' hallucinations and altered states of consciousness.",
  "symptoms": [
    "Seeing vivid colors and complex geometric shapes in a 'blank' field",
    "Auditory hallucinations (voices, music, or environmental sounds)",
    "Distortion of time perception (feeling like hours passed in minutes)",
    "Feeling of 'floating' or loss of body awareness",
    "A sense of 'blanking out' or temporary blindness (the 'Black-Out' glitch)"
  ],
  "causes": [
    "Sensory deprivation or 'un-patterned' stimulation",
    "Increased neural gain in the thalamo-cortical loops",
    "Spontaneous firing of neurons in the visual and auditory cortex",
    "The brain's inherent 'horror vacui' (fear of the void) driving it to create data"
  ],
  "risk_factors": [
    "Prolonged exposure to white-out conditions (e.g., arctic blizzards)",
    "Intentional use of Ganzfeld goggles (halved ping-pong balls)",
    "Deep-sea diving in murky, featureless water"
  ],
  "diagnosis": [
    "Subjective reporting during controlled sensory experiments",
    "EEG showing increased Alpha and Theta wave activity",
    "Monitoring of 'Neural Noise' levels during isolation",
    "Exclusion of pharmacological hallucinations"
  ],
  "remedies": [
    "Introducing structured sensory input (movement, high-contrast light, varied sound)",
    "Physical movement to re-engage the proprioceptive system",
    "Ending the exposure to the uniform field"
  ],
  "prevention": [
    "Visual and auditory 'anchoring' in uniform environments (e.g., wearing colored goggles in snow)"
  ]
}

"visual_snow_syndrome": {
  "description": "Visual Snow Syndrome is a chronic neurological disorder characterized by a continuous visual disturbance that occupies the entire visual field, appearing like 'static' or 'snow'.",
  "symptoms": [
    "Continuous, dynamic, tiny dots (static) across the visual field",
    "Palinopsia (trailing afterimages or 'ghosting' of moving objects)",
    "Enhanced entoptic phenomena (seeing floaters, 'blue field' sparks, or pulses with heartbeats)",
    "Photophobia (severe light sensitivity)",
    "Nyctalopia (impaired night vision/static becoming overwhelming in the dark)",
    "Tinnitus (ringing in the ears, often co-occurring)"
  ],
  "causes": [
    "Hyper-metabolism/Hyper-excitability in the Lingual Gyrus",
    "Thalamocortical dysrhythmia (a mismatch in 'clock speed' between brain centers)",
    "Poor 'gating' or filtering of sensory information in the brainstem",
    "Often triggered or exacerbated by migraines or high stress"
  ],
  "risk_factors": [
    "History of migraines (with or without aura)",
    "Anxiety and depression (comorbidities, not causes)",
    "Certain medications (hallucinogen persisting perception disorder or HPPD)",
    "Concussion or mild TBI"
  ],
  "diagnosis": [
    "Clinical diagnosis based on the ICHD-3 criteria",
    "Ophthalmological exam to rule out eye/retinal issues (eyes are usually healthy)",
    "PET scan to observe glucose metabolism in the lingual gyrus",
    "EEG to detect thalamocortical dysrhythmia"
  ],
  "remedies": [
    "Lamotrigine (anti-seizure medication to 'quiet' the visual cortex)",
    "FL-41 tinted lenses (to manage photophobia)",
    "Visual Snow Protocol (VSP) - specialized neuro-optometric rehabilitation",
    "Stress management and mindfulness to reduce 'focus' on the static"
  ],
  "prevention": [
    "Migraine management",
    "Avoiding illicit hallucinogenic substances (to prevent HPPD)",
    "Protecting against head injury"
  ]
}

"exploding_head_syndrome": {
  "description": "A sensory sleep disorder where an individual hears a loud, imagined noise or experiences an explosive feeling in the head when falling asleep or waking up.",
  "symptoms": [
    "Hearing a sudden, deafening noise (explosion, thunder, or shout)",
    "Seeing a flash of light simultaneously with the noise (in 10% of cases)",
    "Intense but brief feeling of fear or panic",
    "No physical pain (despite the 'exploding' sensation)",
    "Elevated heart rate and sweating immediately after the event"
  ],
  "causes": [
    "Delayed 'shut down' of the Reticular Formation in the brainstem",
    "A sudden burst of neural activity in the Auditory Cortex",
    "Stress and high levels of anxiety",
    "Side effects of withdrawing from certain medications (e.g., SSRIs)",
    "Minor temporal lobe seizures (rarely)"
  ],
  "risk_factors": [
    "Sleep deprivation",
    "High stress environments",
    "Female gender (statistically higher reporting)",
    "History of sleep paralysis or other parasomnias"
  ],
  "diagnosis": [
    "Sleep study (Polysomnography) to rule out apnea or seizures",
    "Patient history (reporting the distinct 'auditory bang' signature)",
    "Neurological exam to ensure no underlying vascular issues",
    "Exclusion of external noise sources"
  ],
  "remedies": [
    "Stress management and relaxation techniques",
    "Improving sleep hygiene to prevent system fatigue",
    "Clomipramine or calcium channel blockers in severe cases",
    "Reassurance (knowing it’s a harmless glitch reduces the 'Fear Spike')"
  ],
  "prevention": [
    "Maintaining a consistent sleep schedule",
    "Reducing caffeine intake in the afternoon",
    "Managing daytime anxiety levels"
  ]
}
"sensed_presence_effect": {
  "description": "A phenomenon where an individual in an extreme or isolated environment feels the distinct presence of another person, despite being alone.",
  "symptoms": [
    "Feeling a 'shadowy' presence just outside the field of vision",
    "Hearing internal 'advice' or 'commands' attributed to the presence",
    "Sensations of being watched or followed",
    "Emotional comfort or a sudden 'second wind' triggered by the presence",
    "Physical manifestations (e.g., feeling a hand on the shoulder)"
  ],
  "causes": [
    "Conflict in the Temporoparietal Junction (TPJ) (Self-Location Logic)",
    "Severe oxygen deprivation (Hypoxia) affecting the Parietal Lobe",
    "Monotony and sensory deprivation (the 'Ganzfeld' effect)",
    "Extreme physical exhaustion and cold (hypothermia)",
    "Amygdala-driven 'Survival Projection' (Limbic defense mechanism)"
  ],
  "risk_factors": [
    "Solo exploration in extreme environments (mountaineering, polar treks)",
    "Sleep deprivation over 48+ hours",
    "High-altitude exposure ($>5000\text{m}$)",
    "Bereavement or intense grief"
  ],
  "diagnosis": [
    "Subjective reporting of 'The Third Man' during extreme events",
    "Post-event psychological debriefing",
    "EEG/fMRI (in lab settings using sensory deprivation)",
    "Exclusion of psychiatric disorders like Schizophrenia"
  ],
  "remedies": [
    "Restoring oxygen and glucose levels",
    "Social reintegration (returning to 'Single-Player' status)",
    "Sleep and temperature regulation",
    "Cognitive-behavioral therapy for processing the event"
  ],
  "prevention": [
    "Avoiding solo missions in extreme conditions",
    "Adequate hydration and supplemental oxygen",
    "Regular 'Social Pings' (radio check-ins) to satisfy the social module"
  ]
}


"musical_ear_syndrome": {
  "description": "A condition where individuals with hearing loss experience non-psychiatric musical hallucinations. The brain 'fills in' the silence with complex, repetitive music.",
  "symptoms": [
    "Hearing music that isn't there (often described as 'radio playing in the next room')",
    "Hallucinations are typically repetitive (loops of 15-30 seconds)",
    "Music is often familiar (childhood songs, hymns, or classic pop)",
    "Awareness that the music is 'internal' (preserved insight)",
    "Hallucinations often stop when real external sound is introduced"
  ],
  "causes": [
    "Sensory deprivation (deafferentation) of the auditory cortex",
    "Hypersensitivity of auditory neurons in the temporal lobe",
    "Spontaneous firing of 'memory-linked' audio circuits",
    "Age-related hearing loss or severe tinnitus"
  ],
  "risk_factors": [
    "Living in a very quiet environment",
    "Advanced age with untreated hearing loss",
    "Use of certain ototoxic medications",
    "Social isolation"
  ],
  "diagnosis": [
    "Audiometry to confirm degree of hearing loss",
    "Psychiatric screening to rule out Schizophrenia (which features 'voices' rather than 'music')",
    "MRI/CT to rule out temporal lobe tumors or seizures",
    "The 'Insight Test' (confirming the patient knows the music isn't real)"
  ],
  "remedies": [
    "Hearing aids (the 'Audio Driver Update' to restore external signals)",
    "White noise machines to give the brain 'dummy data' to process",
    "Cognitive-behavioral techniques to 'ignore' the background task",
    "Reviewing and adjusting medications"
  ],
  "prevention": [
    "Early treatment of hearing loss with hearing aids or cochlear implants",
    "Maintaining a rich 'audio environment' (radio, TV, or social interaction)"
  ]
}
"hyperthymesia_hsam": {
  "description": "HSAM is a rare condition where an individual possesses an extraordinary ability to recall specific details of their daily life and past events with near-perfect accuracy from a very young age.",
  "symptoms": [
    "Vivid, detailed recall of almost every day of their life",
    "Ability to link dates with specific days of the week instantly",
    "Obsessive-like retrieval of past memories",
    "Strong emotional 're-living' of past events upon recall",
    "Inability to 'forget' mundane or negative experiences"
  ],
  "causes": [
    "Structural differences in the Temporal Lobe and Caudate Nucleus",
    "Hyper-connectivity between the hippocampus and the prefrontal cortex",
    "Enhanced 'memory consolidation' during sleep",
    "Possible obsessive-compulsive (OCD) spectrum tendencies for mental rehearsal"
  ],
  "risk_factors": [
    "Genetic predisposition (though extremely rare, only ~60 cases documented)",
    "Neurodevelopmental variations in the memory-indexing architecture",
    "Propensity for rumination"
  ],
  "diagnosis": [
    "Public Events Quiz (testing recall of news from specific dates)",
    "Personal Fact Verification (checking diary entries/family records)",
    "MRI to observe enlargement of the parahippocampal gyrus",
    "Neuropsychological testing for 'Superior Memory' markers"
  ],
  "remedies": [
    "N/A (it is a trait, not a disease)",
    "CBT to manage the 'emotional weight' of negative memories",
    "Focusing techniques to 'dampen' the automatic retrieval of the past",
    "Mindfulness to stay present and avoid 'looping' in 1998"
  ],
  "prevention": [
    "N/A"
  ]
}
"phantom_limb_syndrome": {
  "description": "The vivid perception that an amputated or missing limb is still attached to the body and moving appropriately with other body parts.",
  "symptoms": [
    "Sensations of touch, pressure, or temperature in the missing limb",
    "Phantom pain (stabbing, burning, or 'clenched' sensations)",
    "The feeling that the limb is 'telescoping' (getting shorter over time)",
    "Involuntary 'movement' of the ghost limb",
    "Phantogeusia (phantom tastes) or other sensory equivalents in rare cases"
  ],
  "causes": [
    "Maladaptive neuroplasticity in the somatosensory cortex",
    "Cortical Remapping (neighboring brain areas 'taking over' the empty slot)",
    "Persistent signaling from damaged nerve endings (neuromas) at the stump",
    "The 'Body Schema' module in the parietal lobe failing to update"
  ],
  "risk_factors": [
    "Pre-amputation pain in the limb",
    "Traumatic vs. planned amputation",
    "Psychological stress during recovery"
  ],
  "diagnosis": [
    "Clinical history and physical examination",
    "Exclusion of 'Stump Pain' (which is physical, not neurological)",
    "fMRI to observe activity in the 'vacant' cortical mapping area",
    "Patient reporting of the 'position' of the non-existent limb"
  ],
  "remedies": [
    "Mirror Box Therapy (using visual 'spoofing' to trick the brain)",
    "TENS (Transcutaneous Electrical Nerve Stimulation)",
    "Targeted Muscle Reinnervation (TMR) surgery",
    "Graded Motor Imagery and mental visualization",
    "Pharmacological management (e.g., gabapentin for nerve signals)"
  ],
  "prevention": [
    "Aggressive pain management before and during the amputation procedure",
    "Early use of prosthetic 'feedback' devices"
  ]
}
"reduplicative_paramnesia": {
  "description": "A delusional belief that a place or location has been duplicated, exists in two locations simultaneously, or has been relocated.",
  "symptoms": [
    "Insisting a current location is a 'duplicate' of a familiar one",
    "Believing one is in two places at the same time",
    "Confabulating reasons for why a building has 'moved'",
    "Orientation to person and time is often intact, but orientation to place is 'split'",
    "High level of certainty in the delusion, despite geographical evidence"
  ],
  "causes": [
    "Bilateral Frontal Lobe damage (impaired monitoring and integration)",
    "Right Hemisphere lesions (specifically the Parietal/Occipital areas responsible for spatial mapping)",
    "Stroke or Traumatic Brain Injury (TBI)",
    "Disconnection between the 'Spatial Map' and the 'Familiarity' centers"
  ],
  "risk_factors": [
    "Severe right-hemisphere stroke",
    "Advanced neurodegenerative disease",
    "History of complex head trauma"
  ],
  "diagnosis": [
    "Neurological exam focusing on spatial orientation",
    "MRI/CT to identify frontal and right-parietal lesions",
    "Neuropsychological testing for executive function and monitoring",
    "Clock-drawing or map-reconstruction tasks"
  ],
  "remedies": [
    "Treating the underlying brain injury or inflammation",
    "Cognitive rehabilitation to 're-anchor' spatial logic",
    "Environmental cues (GPS, photos, clear signage)",
    "Antipsychotic medication if the delusion causes extreme distress"
  ],
  "prevention": [
    "Vascular health management to prevent strokes",
    "Standard safety protocols to avoid TBI"
  ]
}


"anton_babinski_syndrome": {
  "description": "A form of anosognosia (lack of insight) where patients who are cortically blind insist that they can see, often providing detailed but false descriptions of their visual environment.",
  "symptoms": [
    "Visual Anosognosia (denial of blindness)",
    "Confabulation (inventing visual details to fill the 'darkness')",
    "Walking into objects while claiming to see them",
    "Extreme defensiveness or logical 'patches' when confronted with evidence of blindness",
    "Complete cortical blindness (loss of light perception)"
  ],
  "causes": [
    "Bilateral damage to the Occipital Lobes (Primary Visual Cortex)",
    "Disconnection between the visual area and the language/logic centers",
    "Stroke involving the posterior cerebral arteries",
    "Traumatic brain injury (TBI) affecting the back of the head"
  ],
  "risk_factors": [
    "Major vascular events (strokes)",
    "Severe hypertensive crisis",
    "Bilateral occipital tumors"
  ],
  "diagnosis": [
    "Visual field testing (patient fails but claims success)",
    "MRI/CT showing bilateral occipital lesions",
    "The 'Finger-Counting' Test (patient guesses numbers with total confidence)",
    "Neurological assessment for Anosognosia"
  ],
  "remedies": [
    "Treating the underlying cause (e.g., managing stroke or pressure)",
    "Neuro-rehabilitation to slowly 'introduce' the reality of blindness",
    "Safety monitoring (since patients believe they can drive or walk unassisted)",
    "Occupational therapy for the blind"
  ],
  "prevention": [
    "Vascular health management",
    "Protective gear to avoid posterior brain trauma"
  ]
}

"riddoch_phenomenon": {
  "description": "A rare type of visual impairment often caused by lesions in the primary visual cortex (V1). The patient is blind to static objects but can perceive objects in motion.",
  "symptoms": [
    "Statosegnosia (inability to see static objects)",
    "Perception of 'flashes' or 'shadows' only when an object moves",
    "Inability to describe the color or shape of the moving object",
    "Navigational ability in crowded areas (as long as people are moving)",
    "The 'Ghosting' effect (seeing a trail but no object)"
  ],
  "causes": [
    "Damage to the Primary Visual Cortex (V1/Brodmann Area 17)",
    "Post-stroke recovery of the V5/MT area (the motion processor)",
    "Traumatic brain injury (TBI) to the occipital lobe",
    "Tumors affecting the early visual pathway"
  ],
  "risk_factors": [
    "Occipital lobe stroke",
    "Surgical complications in the posterior brain",
    "Severe head trauma"
  ],
  "diagnosis": [
    "Static vs. Kinetic Perimetry (mapping what the patient sees while still vs. moving)",
    "fMRI to check for activity in area V5/MT without activity in V1",
    "Neurological testing for 'Blindsight' capabilities",
    "Ophthalmological exams to confirm the eyes are functioning normally"
  ],
  "remedies": [
    "Visual rehabilitation (training the brain to use motion to 'map' surroundings)",
    "Compensatory strategies (manually moving the head to 'activate' the scene)",
    "Occupational therapy for navigating 'static' environments",
    "Prism lenses in some specific stroke recovery cases"
  ],
  "prevention": [
    "Stroke prevention (blood pressure and cholesterol management)",
    "Head protection in high-risk environments"
  ]
}

"aphantasia": {
  "description": "Aphantasia is the inability to voluntarily create mental images in the 'mind's eye.' It is a variation in human experience rather than a disability, affecting the 'internal visualization' module.",
  "symptoms": [
    "Inability to 'see' images when closing the eyes and imagining",
    "Conceptual recall instead of visual recall (knowing a car has 4 wheels without 'seeing' it)",
    "Difficulty with 'visual memory' tasks (e.g., describing a crime suspect's face)",
    "Often accompanied by 'SDAM' (Severely Deficient Autobiographical Memory)",
    "Dreaming can still be visual (showing the 'display' works, but the 'user command' is broken)"
  ],
  "causes": [
    "Hypo-connectivity between the Frontal Cortex and the Visual Cortex",
    "Failure of the 'top-down' feedback loop required for visualization",
    "Structural differences in the Precuneus and Medial Prefrontal Cortex",
    "Can be congenital (from birth) or acquired via brain injury"
  ],
  "risk_factors": [
    "Genetic predisposition (often runs in families)",
    "Often correlates with high performance in STEM or logic-based fields",
    "Potential links to certain neurodivergent traits"
  ],
  "diagnosis": [
    "Vividness of Visual Imagery Questionnaire (VVIQ)",
    "Pupillary Response Test (pupils normally contract when imagining light; in Aphantasiacs, they don't)",
    "fMRI showing lack of activation in the visual cortex during 'imagination' tasks",
    "Binocular Rivalry tests"
  ],
  "remedies": [
    "N/A (not considered a disorder requiring a 'cure')",
    "Utilization of 'Semantic' memory strategies",
    "Using external visual aids (sketches, mood boards, or 3D models)",
    "Focusing on other senses (audio/tactile) for creative work"
  ],
  "prevention": [
    "N/A"
  ]
}
"mirror_speech_synesthesia": {
  "description": "A form of synesthesia where auditory perception of speech sounds triggers involuntary tactile sensations in the listener's own vocal tract or body.",
  "symptoms": [
    "Feeling the 'shape' of words in the mouth while someone else speaks",
    "Physical sensations of vocal cord vibration when hearing deep voices",
    "Involuntary tongue or lip movements mimicking the speaker (sub-vocalization)",
    "Tactile 'weight' or 'texture' associated with specific phonemes (e.g., 'K' feels sharp, 'M' feels soft)",
    "Sensory overload in loud or multi-speaker environments"
  ],
  "causes": [
    "Hyper-connectivity between the Auditory Cortex and the Motor/Somatosensory regions",
    "Over-activation of the Mirror Neuron System (MNS)",
    "Structural 'leakage' between Broca's area (speech production) and the sensory strip",
    "Failure of the 'Self vs. Other' inhibitory signal in the parietal lobe"
  ],
  "risk_factors": [
    "High levels of empathy (correlated with mirror-neuron density)",
    "Presence of other forms of synesthesia (e.g., Grapheme-Color)",
    "Genetic predisposition to neuroplasticity"
  ],
  "diagnosis": [
    "Consistency testing (feeling the same sensation for the same word over time)",
    "fMRI showing co-activation of the motor cortex during passive listening",
    "EMG (Electromyography) of the jaw and tongue muscles during auditory tasks",
    "Subjective reporting of 'tactile speech' since early childhood"
  ],
  "remedies": [
    "N/A (often viewed as a 'Hyper-Empathy' trait)",
    "Selective attention training to decouple the audio-tactile link",
    "Using earplugs or noise-canceling headphones to reduce haptic 'noise'",
    "Mindfulness to manage the 'physicality' of conversation"
  ],
  "prevention": [
    "N/A"
  ]
}

"misophonia": {
  "description": "Misophonia is a condition in which specific sounds, known as 'triggers,' evoke strong negative emotional or physiological responses that most people would find negligible.",
  "symptoms": [
    "Immediate, intense anger, irritation, or disgust toward a sound",
    "Physical fight-or-flight response (sweating, increased heart rate, muscle tension)",
    "Extreme urge to flee the area or stop the sound source",
    "Hyper-focus on the trigger once it starts (the 'Tracking' glitch)",
    "Anticipatory anxiety (worrying about encountering a trigger sound)"
  ],
  "causes": [
    "Hyper-connectivity between the Auditory Cortex and the Anterior Insular Cortex (AIC)",
    "Abnormal 'salience' processing (deciding what is important vs. background noise)",
    "Over-activation of the Limbic System (the emotional CPU)",
    "Conditioned neural pathways from past negative experiences"
  ],
  "risk_factors": [
    "Family history of sound sensitivity",
    "Co-occurrence with OCD or anxiety disorders",
    "Onset typically during late childhood or early adolescence"
  ],
  "diagnosis": [
    "Misophonia Questionnaire (MQ) or Amsterdam Misophonia Scale (A-MISO-S)",
    "fMRI to observe AIC activity during trigger exposure",
    "Audiological testing to rule out Hyperacusis (physical pain from loud sounds)",
    "Psychological screening for comorbid conditions"
  ],
  "remedies": [
    "Sound masking (white noise, brown noise, or pink noise)",
    "Noise-canceling headphones to 'shield' the input",
    "Counter-conditioning (pairing a trigger sound with a pleasant stimulus)",
    "Tinnitus Retraining Therapy (TRT) modified for Misophonia"
  ],
  "prevention": [
    "Early exposure to diverse auditory environments",
    "Stress management and autonomic nervous system regulation"
  ]
}


"foreign_accent_syndrome": {
  "description": "FAS is a rare speech disorder that causes a person to speak their native language with an accent that sounds 'foreign' to listeners, resulting from damage to the speech-production centers of the brain.",
  "symptoms": [
    "Altered vowel duration (lengthening or shortening sounds)",
    "Changes in pitch and intonation (melody of speech)",
    "Errors in 'voicing' (e.g., saying 'p' instead of 'b')",
    "Insertion of extra vowels between consonants",
    "Preserved vocabulary and grammar (it is not a loss of language knowledge)"
  ],
  "causes": [
    "Stroke (most common, usually in the left hemisphere)",
    "Traumatic Brain Injury (TBI)",
    "Brain tumors or MS lesions in the motor cortex",
    "Psychogenic factors (rare cases triggered by severe trauma)"
  ],
  "risk_factors": [
    "High blood pressure or cardiovascular issues (stroke risk)",
    "High-impact sports or occupations (TBI risk)",
    "History of neurological conditions"
  ],
  "diagnosis": [
    "Speech-language pathology assessment",
    "MRI/CT to locate lesions in the pre-central gyrus or Broca's area",
    "Spectrographic analysis of speech patterns",
    "Psychiatric screening to rule out functional disorders"
  ],
  "remedies": [
    "Speech therapy to 're-tune' the prosody engine",
    "Counseling to deal with the 'Identity Crisis' of sounding like a stranger",
    "Techniques to mimic the original native accent through repetitive drills",
    "Targeted neuro-rehabilitation"
  ],
  "prevention": [
    "Standard stroke prevention protocols",
    "Helmet use and head protection",
    "Management of chronic neurological health"
  ]
}

"alice_in_wonderland_syndrome": {
  "description": "AIWS (Todd’s Syndrome) is a disorienting neuropsychological condition that affects perception, causing objects and body parts to appear larger (macropsia), smaller (micropsia), or distorted in shape.",
  "symptoms": [
    "Micropsia (objects appearing smaller than they are)",
    "Macropsia (objects appearing much larger than they are)",
    "Pelopsia (objects appearing closer than they are)",
    "Teleopsia (objects appearing further away than they are)",
    "Distorted body image (feeling like your hand is 10 feet long)",
    "Time distortion (time moving in slow motion or 'fast-forward')"
  ],
  "causes": [
    "Migraines (the most common trigger in adults)",
    "Epstein-Barr Virus (EBV) or other viral infections (common in children)",
    "Temporal lobe epilepsy",
    "Lesions in the posterior parietal cortex (spatial mapping hub)",
    "Psychoactive substance use"
  ],
  "risk_factors": [
    "Childhood (symptoms often disappear after puberty)",
    "History of complex migraines",
    "Family history of AIWS or epilepsy"
  ],
  "diagnosis": [
    "MRI to rule out structural brain abnormalities",
    "EEG to detect seizure activity during an episode",
    "Blood tests to check for viral infections like EBV",
    "Visual and perceptual testing batteries"
  ],
  "remedies": [
    "Managing the underlying trigger (e.g., migraine medication)",
    "Rest and sensory deprivation during an episode",
    "Reassurance (especially for children who find the distortions terrifying)",
    "Wait-and-see approach (as many cases are self-limiting)"
  ],
  "prevention": [
    "Avoiding migraine triggers (stress, diet, sleep loss)",
    "Effective treatment of childhood viral infections"
  ]
}

"prosopometamorphopsia": {
  "description": "A rare visual perception disorder where faces appear distorted. Unlike Prosopagnosia, the patient can often still identify the person, but the 'rendering' of their features is grotesque.",
  "symptoms": [
    "Hemi-prosopometamorphopsia (distortion on only one side of a face)",
    "Features appearing to 'melt,' 'stretch,' or 'vibrate'",
    "Eyes or mouths appearing vastly oversized or out of place",
    "Faces taking on animalistic or 'demon-like' qualities",
    "Preserved recognition (knowing it's your spouse, even if they look like a monster)"
  ],
  "causes": [
    "Lesions or strokes in the Splenium of the Corpus Callosum",
    "Dysfunction in the right Fusiform Face Area (FFA)",
    "Migraine auras affecting the visual processing pathway",
    "Epilepsy or localized brain tumors",
    "Post-traumatic brain injury (TBI)"
  ],
  "risk_factors": [
    "Vascular disease affecting the posterior brain",
    "Chronic migraines",
    "History of seizures",
    "Toxicity from certain substances or medications"
  ],
  "diagnosis": [
    "The 'Face-Distortion Task' (drawing what they see)",
    "fMRI to identify hyper-activity or lesions in the occipito-temporal cortex",
    "Ophthalmological exams (to confirm the eyes are fine; it's a 'processor' issue)",
    "Neurological mapping of the 'Face Processing Network'"
  ],
  "remedies": [
    "Treating the underlying cause (e.g., anti-seizure meds or migraine preventatives)",
    "Prism glasses to shift the visual field (for hemi-distortions)",
    "Reassurance and education to manage the fear of 'losing one's mind'",
    "Digital 'Face-Correction' filters in AR (experimental)"
  ],
  "prevention": [
    "Blood pressure management to prevent occipital stroke",
    "Prompt medical attention for sudden visual changes"
  ]
}

"alien_hand_syndrome": {
  "description": "Alien Hand Syndrome is a rare neurological disorder in which one hand functions involuntarily, with the victim feeling as though it is operated by an external force.",
  "symptoms": [
    "Involuntary but purposeful movement (e.g., reaching for an object, buttoning/unbuttoning clothes)",
    "Intermanual conflict (one hand undoing what the other is doing)",
    "Feeling of 'estrangement' from the limb (it doesn't feel like it belongs to the person)",
    "The hand may 'clasp' or 'grasp' objects and refuse to let go"
  ],
  "causes": [
    "Damage to the corpus callosum (the bridge between brain hemispheres)",
    "Stroke affecting the medial frontal lobe or parietal lobe",
    "Neurodegenerative diseases (e.g., Corticobasal Degeneration)",
    "Post-surgical complications (following a commissurotomy)"
  ],
  "risk_factors": [
    "History of stroke or cerebrovascular disease",
    "Aneurysm or brain tumor",
    "Surgery involving the brain's midline",
    "Advanced neurodegenerative conditions"
  ],
  "diagnosis": [
    "Neurological observation of 'purposeful' involuntary movements",
    "MRI to identify lesions in the corpus callosum or frontal lobes",
    "Rule-out of movement disorders like Chorea or Dystonia",
    "Functional connectivity studies"
  ],
  "remedies": [
    "Bilateral task training (giving the 'alien' hand something to hold)",
    "Sensory muffling (wearing an oven mitt to reduce the hand's input)",
    "Cognitive behavioral strategies to 'distract' the rogue circuit",
    "Botox or Clonazepam (to reduce muscle spasms)"
  ],
  "prevention": [
    "Vascular health management to prevent stroke",
    "Minimally invasive neurosurgical techniques",
    "Early detection of neurodegenerative symptoms"
  ]
}
"fregoli_delusion": {
  "description": "Fregoli Delusion is a rare neuropsychiatric disorder in which a person holds a delusional belief that different people are in fact a single person who changes appearance or is in disguise.",
  "symptoms": [
    "Hyper-familiarity with strangers (believing a stranger is a known person)",
    "Delusional belief in disguises or shapeshifting",
    "Paranoia or feeling of being 'stalked' by a single entity",
    "Inability to distinguish unique identities despite distinct physical features",
    "Associated deficits in executive function and memory"
  ],
  "causes": [
    "Over-activation of the nodes linking faces to memories",
    "Bilateral damage or dysfunction in the right hemisphere (frontal/temporal)",
    "Dopaminergic system hyperactivity",
    "Neurodegenerative diseases (e.g., Lewy Body Dementia)",
    "Complication of Schizophrenia or Bipolar disorder"
  ],
  "risk_factors": [
    "History of traumatic brain injury (TBI)",
    "Treatment with Levodopa (dopamine agonists)",
    "Existing psychotic or affective disorders",
    "Seizure disorders in the temporal lobe"
  ],
  "diagnosis": [
    "Neuropsychological evaluation for 'associative' face processing",
    "MRI to check for right-hemisphere lesions",
    "Psychiatric assessment for delusional consistency",
    "Observation of 'identification' errors in controlled tests"
  ],
  "remedies": [
    "Antipsychotic medications (to reduce dopaminergic firing)",
    "Anticonvulsants if seizure-related",
    "Cognitive Behavioral Therapy (CBT) to challenge the 'disguise' logic",
    "Treating the underlying neurodegenerative cause"
  ],
  "prevention": [
    "Early intervention in psychotic episodes",
    "Monitoring dopamine levels in Parkinson's treatment",
    "Protecting against right-hemisphere brain trauma"
  ]
}
"hyperthymesia_hsam": {
  "description": "HSAM is a rare condition where an individual possesses an extraordinary ability to recall specific details of their daily life and past events with near-perfect accuracy from a very young age.",
  "symptoms": [
    "Vivid, detailed recall of almost every day of their life",
    "Ability to link dates with specific days of the week instantly",
    "Obsessive-like retrieval of past memories",
    "Strong emotional 're-living' of past events upon recall",
    "Inability to 'forget' mundane or negative experiences"
  ],
  "causes": [
    "Structural differences in the Temporal Lobe and Caudate Nucleus",
    "Hyper-connectivity between the hippocampus and the prefrontal cortex",
    "Enhanced 'memory consolidation' during sleep",
    "Possible obsessive-compulsive (OCD) spectrum tendencies for mental rehearsal"
  ],
  "risk_factors": [
    "Genetic predisposition (though extremely rare, only ~60 cases documented)",
    "Neurodevelopmental variations in the memory-indexing architecture",
    "Propensity for rumination"
  ],
  "diagnosis": [
    "Public Events Quiz (testing recall of news from specific dates)",
    "Personal Fact Verification (checking diary entries/family records)",
    "MRI to observe enlargement of the parahippocampal gyrus",
    "Neuropsychological testing for 'Superior Memory' markers"
  ],
  "remedies": [
    "N/A (it is a trait, not a disease)",
    "CBT to manage the 'emotional weight' of negative memories",
    "Focusing techniques to 'dampen' the automatic retrieval of the past",
    "Mindfulness to stay present and avoid 'looping' in 1998"
  ],
  "prevention": [
    "N/A"
  ]
}

"charles_bonnet_syndrome": {
  "description": "CBS is a condition where people with significant vision loss experience vivid, complex visual hallucinations, despite having no psychiatric illness.",
  "symptoms": [
    "Vivid hallucinations (e.g., people, animals, landscapes, or patterns)",
    "Lilliputian hallucinations (seeing people or objects as much smaller than life)",
    "Hallucinations that appear suddenly and last for minutes to hours",
    "Full awareness that the images aren't real (insight is preserved)",
    "Absence of other sensory hallucinations (no voices, just images)"
  ],
  "causes": [
    "Deafferentation (loss of sensory input) to the visual cortex",
    "Hyper-excitability of visual neurons in the absence of external signals",
    "Spontaneous firing of 'cached' visual patterns in the ventral stream",
    "Severe vision loss (macular degeneration, glaucoma, or cataracts)"
  ],
  "risk_factors": [
    "Advanced age (correlated with vision loss)",
    "Social isolation (decreased overall sensory input)",
    "Sudden drop in visual acuity"
  ],
  "diagnosis": [
    "Ophthalmological exam to confirm vision loss",
    "Psychiatric evaluation to rule out schizophrenia or dementia",
    "MRI to rule out tumors or strokes in the visual pathway",
    "Clinical interview confirming the patient has 'insight' into the hallucinations"
  ],
  "remedies": [
    "Improving vision where possible (e.g., cataract surgery)",
    "Blinking or moving the eyes to 'reset' the visual buffer",
    "Increasing ambient lighting to stimulate surviving neurons",
    "Reassurance (the 'Fear-Reduction' patch: knowing you aren't 'going crazy')"
  ],
  "prevention": [
    "Regular eye checkups to slow the progression of vision loss",
    "Early treatment of retinal diseases"
  ]
}

"exploding_head_syndrome": {
  "description": "EHS is a type of sensory parasomnia in which a person hears a loud, imaginary noise or experiences an explosive feeling in their head while falling asleep or waking up.",
  "symptoms": [
    "Hearing a sudden 'explosion,' 'gunshot,' or 'thunderclap' inside the head",
    "Painless but terrifying auditory hallucination",
    "Occasional flash of light (photopsia) accompanying the noise",
    "Sudden muscle twitch (myoclonic jerk) or surge of adrenaline",
    "Intense tachycardia (racing heart) upon waking"
  ],
  "causes": [
    "Delayed 'shut-down' of the Reticular Formation in the brainstem",
    "Temporary surge of activity in the auditory neurons as the brain enters sleep",
    "Minor seizures in the temporal lobe",
    "Ear structure malfunctions (e.g., sudden movement of parts of the middle ear)"
  ],
  "risk_factors": [
    "High levels of stress and anxiety",
    "Sleep deprivation (insomnia or irregular schedules)",
    "History of sleep paralysis",
    "Common in women over 50, though it can affect any age/gender"
  ],
  "diagnosis": [
    "Clinical history (usually sufficient for diagnosis)",
    "Polysomnogram (sleep study) to rule out apnea or seizures",
    "Neurological exam to ensure no structural brain damage",
    "Evaluating stress levels and sleep hygiene"
  ],
  "remedies": [
    "Stress management and relaxation techniques",
    "Improving sleep hygiene (consistent wake/sleep times)",
    "Tricyclic antidepressants (e.g., Clomipramine) in severe cases",
    "Reassurance (knowing it's not a stroke or tumor reduces the fear-loop)"
  ],
  "prevention": [
    "Regular sleep patterns",
    "Reducing caffeine intake before bed",
    "Managing underlying anxiety disorders"
  ]
}

"visual_snow_syndrome": {
  "description": "Visual Snow Syndrome is a chronic neurological disorder characterized by a continuous visual disturbance that occupies the entire visual field, appearing like 'static' or 'snow'.",
  "symptoms": [
    "Continuous, dynamic, tiny dots (static) across the visual field",
    "Palinopsia (trailing afterimages or 'ghosting' of moving objects)",
    "Enhanced entoptic phenomena (seeing floaters, 'blue field' sparks, or pulses with heartbeats)",
    "Photophobia (severe light sensitivity)",
    "Nyctalopia (impaired night vision/static becoming overwhelming in the dark)",
    "Tinnitus (ringing in the ears, often co-occurring)"
  ],
  "causes": [
    "Hyper-metabolism/Hyper-excitability in the Lingual Gyrus",
    "Thalamocortical dysrhythmia (a mismatch in 'clock speed' between brain centers)",
    "Poor 'gating' or filtering of sensory information in the brainstem",
    "Often triggered or exacerbated by migraines or high stress"
  ],
  "risk_factors": [
    "History of migraines (with or without aura)",
    "Anxiety and depression (comorbidities, not causes)",
    "Certain medications (hallucinogen persisting perception disorder or HPPD)",
    "Concussion or mild TBI"
  ],
  "diagnosis": [
    "Clinical diagnosis based on the ICHD-3 criteria",
    "Ophthalmological exam to rule out eye/retinal issues (eyes are usually healthy)",
    "PET scan to observe glucose metabolism in the lingual gyrus",
    "EEG to detect thalamocortical dysrhythmia"
  ],
  "remedies": [
    "Lamotrigine (anti-seizure medication to 'quiet' the visual cortex)",
    "FL-41 tinted lenses (to manage photophobia)",
    "Visual Snow Protocol (VSP) - specialized neuro-optometric rehabilitation",
    "Stress management and mindfulness to reduce 'focus' on the static"
  ],
  "prevention": [
    "Migraine management",
    "Avoiding illicit hallucinogenic substances (to prevent HPPD)",
    "Protecting against head injury"
  ]
}
"cotards_delusion": {
  "description": "A rare neuropsychiatric condition where a person holds the delusional belief that they are dead, dying, putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Absolute negation of existence ('I don't exist')",
    "Belief that one is a walking corpse or a ghost",
    "Insensitivity to pain (analgesia)",
    "Severe depression and social withdrawal",
    "Refusal to eat (because 'dead people don't need food')",
    "Delusions of immortality (ironically, because you can't 'die' if you're already dead)"
  ],
  "causes": [
    "Disconnected circuitry between the fusiform face area and the amygdala",
    "Atrophy or dysfunction in the Insular Cortex (the 'interoception' hub)",
    "Severe depression or psychotic disorders",
    "Complication of neurological injuries (stroke, tumor, or TBI)",
    "Adverse reaction to certain medications (e.g., Acyclovir in renal failure)"
  ],
  "risk_factors": [
    "Advanced age with underlying brain atrophy",
    "Severe mood disorders (Major Depressive Disorder with psychosis)",
    "Schizophrenia",
    "Right-hemisphere lesions"
  ],
  "diagnosis": [
    "Psychiatric evaluation based on the 'Walking Corpse' criteria",
    "MRI to check for lesions in the frontoparietal or insular regions",
    "Metabolic screening to rule out drug-induced psychosis",
    "Insight assessment (patients typically have zero insight into the delusion)"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT) - remarkably effective for 'rebooting' the system",
    "Antipsychotic and antidepressant combinations",
    "Treating the underlying neurological injury",
    "Psychotherapy (once the acute 'dead' phase is managed)"
  ],
  "prevention": [
    "Early intervention in severe depression",
    "Monitoring renal function during antiviral treatments",
    "Managing vascular health to prevent right-hemisphere strokes"
  ]
}


"transient_global_amnesia": {
  "description": "TGA is a sudden, temporary episode of memory loss that can't be attributed to a common neurological condition, such as epilepsy or stroke.",
  "symptoms": [
    "Sudden onset of anterograde amnesia (inability to form new memories)",
    "Repetitive questioning (e.g., asking 'How did we get here?' every 2 minutes)",
    "Preserved self-identity (you know exactly who you are and recognize family)",
    "Lack of other neurological deficits (no paralysis, no slurred speech)",
    "Retrograde amnesia for the hours or days immediately preceding the event"
  ],
  "causes": [
    "Temporary dysfunction of the CA1 neurons in the hippocampus",
    "Triggers: Physical exertion, extreme emotional stress, cold water immersion",
    "The Valsalva maneuver (straining, which may cause venous congestion)",
    "Migraine-related vascular changes"
  ],
  "risk_factors": [
    "Age (most common in people over 50)",
    "History of migraines",
    "Psychological stressors",
    "Strenuous physical activity"
  ],
  "diagnosis": [
    "Clinical diagnosis based on the 'Hodge and Warlow' criteria",
    "DWI MRI (often shows a 'punctate' lesion in the hippocampus 24-48 hours later)",
    "EEG to rule out 'Transient Epileptic Amnesia'",
    "Blood tests to rule out metabolic or toxic causes"
  ],
  "remedies": [
    "No specific treatment required (resolves spontaneously within 24 hours)",
    "Observation to ensure it is not a TIA (Transient Ischemic Attack)",
    "Patient and family reassurance (the 'looping' behavior is terrifying to watch)",
    "Rest and hydration"
  ],
  "prevention": [
    "Avoiding known triggers if the condition is recurrent (though recurrence is rare)",
    "Managing vascular health"
  ]
}


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
"kluver_bucy_syndrome": {
  "description": "Klüver-Bucy is a rare behavioral impairment characterized by inappropriate sexual behaviors, an urge to put objects in the mouth, and a complete loss of fear and anger response.",
  "symptoms": [
    "Placidity (complete loss of fear/anger, even toward predators or fire)",
    "Hyper-orality (compulsion to examine everything with the mouth)",
    "Hyper-metamorphosis (irresistible impulse to touch/notice every object)",
    "Hyper-sexuality (inappropriate or indiscriminate sexual advances)",
    "Visual Agnosia (difficulty recognizing objects, though sight is fine)",
    "Altered dietary habits (eating non-food items)"
  ],
  "causes": [
    "Bilateral damage to the anterior temporal lobes/Amygdala",
    "Herpes Simplex Encephalitis (the most common medical cause)",
    "Pick's Disease (Frontotemporal Dementia)",
    "Severe Traumatic Brain Injury (TBI)",
    "Post-surgical complications from temporal lobectomy"
  ],
  "risk_factors": [
    "Infections of the central nervous system",
    "Advanced neurodegenerative diseases",
    "Stroke affecting the temporal region"
  ],
  "diagnosis": [
    "Observation of the 'triad' (hyper-orality, hyper-sexuality, placidity)",
    "MRI/CT showing bilateral temporal lobe lesions",
    "Cerebrospinal fluid (CSF) analysis for viral infections",
    "Neuropsychological behavioral mapping"
  ],
  "remedies": [
    "Antiviral medication (if caused by encephalitis)",
    "Mood stabilizers (e.g., Carbamazepine) to manage behavior",
    "SSRIs to reduce hyper-sexual impulses",
    "Structured, high-supervision environments for safety"
  ],
  "prevention": [
    "Prompt treatment of viral fevers and neurological symptoms",
    "Protective gear for head injury prevention",
    "Early screening for cognitive/behavioral shifts in the elderly"
  ]
}

"schizoid_personality_disorder": {
  "description": "Schizoid personality disorder involves detachment from social relationships.",
  "causes": ["Genetic factors"],
  "remedies": ["Therapy"]
},
"savant_syndrome": {
  "description": "Savant syndrome is a condition where persons with significant mental disabilities, including autistic disorder, have a 'prodigious island of genius' that stands in marked contrast to their overall disability.",
  "symptoms": [
    "Hyper-calculia (lightning-fast mental math)",
    "Hyperthymesia or photographic memory",
    "Instant musical virtuosity (playing a complex piece after one hearing)",
    "Exceptional artistic ability without formal training",
    "Absolute pitch or perfect calendar counting"
  ],
  "causes": [
    "Compensatory right-brain growth due to left-brain injury or dysfunction",
    "Hyper-systemizing (extreme attention to detail and patterns)",
    "Acquired Savantism (emerging after a traumatic brain injury or stroke)",
    "Genetic factors linked to neurodevelopmental conditions"
  ],
  "risk_factors": [
    "Autism Spectrum Disorder (approx. 10% of autistic people exhibit savant skills)",
    "History of early childhood left-hemisphere injury",
    "Gender (statistically more common in males)"
  ],
  "diagnosis": [
    "Standardized IQ and cognitive testing",
    "Specialized talent assessments",
    "fMRI to observe 'over-activation' in specific lobes (e.g., parietal or occipital)",
    "MRI to check for left-hemisphere anomalies"
  ],
  "remedies": [
    "None (the skills are usually nurtured and preserved)",
    "Therapy to improve general life skills and social communication",
    "Educational programs tailored to the specific talent"
  ],
  "prevention": [
    "N/A (it is a structural/developmental trait)"
  ]
}
"hemispatial_neglect": {
  "description": "A neuropsychological condition where, after damage to one hemisphere of the brain is sustained, a deficit in attention to and awareness of one side of the field of vision is observed.",
  "symptoms": [
    "Ignoring food on the left side of a plate",
    "Shaving or applying makeup to only one side of the face",
    "Reading only the right-hand side of a page",
    "Walking into obstacles on the left side",
    "Anosognosia (unawareness that a deficit even exists)"
  ],
  "causes": [
    "Stroke (most commonly in the right posterior parietal cortex)",
    "Traumatic Brain Injury (TBI)",
    "Brain tumors",
    "Neurodegenerative diseases (e.g., Posterior Cortical Atrophy)"
  ],
  "risk_factors": [
    "Hypertension and cardiovascular disease (stroke risk)",
    "Age (higher risk of stroke/degeneration)",
    "Severe head trauma"
  ],
  "diagnosis": [
    "Clock Drawing Test (patient crowds all numbers onto the right side)",
    "Line Bisection Test (patient marks the 'middle' far to the right)",
    "Cancellation tasks (crossing out all targets on a sheet of paper)",
    "MRI/CT to identify the parietal lesion"
  ],
  "remedies": [
    "Prism Adaptation Therapy (using glasses to shift the visual field)",
    "Visual Scanning Training (consciously forcing the 'pointer' to the left)",
    "Limb Activation Therapy (moving the neglected limb to trigger the brain)",
    "Virtual Reality (VR) rehabilitation"
  ],
  "prevention": [
    "Vascular health management (BP, cholesterol)",
    "Safety gear to prevent TBI",
    "Early neurological assessment after any stroke-like symptoms"
  ]
}
"mirror_touch_synesthesia": {
  "description": "MTS is a rare neurological condition where individuals experience a physical sensation of touch on their own body when they see another person being touched.",
  "symptoms": [
    "Feeling a touch on the same or opposite side of your body as the person seen being touched",
    "Experiencing physical 'echoes' of others' pain (synesthetic pain)",
    "Feeling the 'pressure' of textures or movements seen on screen or in person",
    "Extreme emotional exhaustion (emotional contagion)",
    "Inability to watch 'slapstick' comedy or horror due to physical discomfort"
  ],
  "causes": [
    "Hyper-excitability of the mirror neuron system",
    "Structural differences in the somatosensory cortex (V1/V2)",
    "Lack of 'self-other' distinction in the temporoparietal junction (TPJ)",
    "Potential developmental variations in neural pruning"
  ],
  "risk_factors": [
    "Presence of other forms of synesthesia (e.g., color-grapheme)",
    "High scores on standardized empathy scales",
    "Left-handedness (statistically higher correlation)"
  ],
  "diagnosis": [
    "Synesthetic Masking Task (testing if real touch and 'seen' touch interfere)",
    "fMRI to observe activation in the somatosensory cortex while watching videos of touch",
    "Self-reported consistency over time",
    "The Interpersonal Reactivity Index (IRI)"
  ],
  "remedies": [
    "Sensory shielding (avoiding crowded places or intense media)",
    "Cognitive-behavioral techniques to strengthen the 'self-other' boundary",
    "Focusing on one's own physical sensations to 'ground' the system",
    "Mindfulness-based stress reduction (MBSR)"
  ],
  "prevention": [
    "N/A (it is a structural trait)"
  ]
}


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
"color_agnosia": {
  "description": "Color agnosia is a rare neurological disorder where a person can perceive colors but cannot recognize or name them, nor can they associate colors with specific objects (e.g., knowing that a 'banana' is 'yellow').",
  "symptoms": [
    "Ability to pass a color blindness test (Ishihara plates) perfectly",
    "Inability to name a color when shown a sample",
    "Difficulty grouping objects by color",
    "Loss of 'color knowledge' (e.g., not knowing that grass is green)",
    "Correct perception of 'shade' and 'brightness' without the 'identity' of the hue"
  ],
  "causes": [
    "Lesions in the left occipito-temporal region (specifically the lingual and fusiform gyri)",
    "Stroke affecting the posterior cerebral artery",
    "Carbon monoxide poisoning",
    "Neurodegenerative diseases like Alzheimer's"
  ],
  "risk_factors": [
    "Vascular disease (stroke risk)",
    "Exposure to neurotoxins",
    "Advanced age-related cognitive decline"
  ],
  "diagnosis": [
    "Ishihara Color Test (to rule out retinal color blindness)",
    "Color-Object Association tests (e.g., 'What color is a fire truck?')",
    "fMRI to observe activity in Area V4",
    "Color sorting and matching tasks"
  ],
  "remedies": [
    "Compensatory labeling (using text tags on clothing)",
    "Using digital color-identifiers",
    "Rehabilitation focused on associative memory",
    "Treating the underlying vascular or toxic cause"
  ],
  "prevention": [
    "Standard stroke prevention (BP and cholesterol management)",
    "Safety protocols for carbon monoxide (detectors)",
    "Maintaining cardiovascular health"
  ]
}

"akinetopsia": {
  "description": "Akinetopsia is a rare neuropsychological disorder in which a patient cannot perceive motion in their visual field, despite being able to see stationary objects clearly.",
  "symptoms": [
    "Seeing moving objects as a series of 'frozen' snapshots",
    "Difficulty pouring liquids (the liquid appears frozen, then suddenly overflows)",
    "Difficulty following conversations (facial expressions and mouth movements 'jump' from one state to another)",
    "Feeling overwhelmed in busy environments (cars or people 'teleport' from place to place)",
    "Inability to track the trajectory of a moving ball or vehicle"
  ],
  "causes": [
    "Lesions or damage to the V5/MT area of the visual cortex",
    "Traumatic brain injury (TBI)",
    "Stroke (specifically in the posterior visual pathways)",
    "Side effects of certain medications (e.g., high doses of nefazodone)",
    "Severe Alzheimer's disease"
  ],
  "risk_factors": [
    "Bilateral damage to the temporo-parietal-occipital junction",
    "History of posterior cortical atrophy",
    "Exposure to specific neurotoxins"
  ],
  "diagnosis": [
    "Computerized motion perception tests",
    "fMRI to check for lack of activation in Area V5 during motion stimuli",
    "Goldmann perimetry to rule out general field loss",
    "Neurological mapping of the 'Dorsal Stream'"
  ],
  "remedies": [
    "Compensatory strategies (relying on sound to judge speed)",
    "Developing 'static' cues (judging distance by how large an object appears)",
    "Adjusting medication (if drug-induced)",
    "Tinted glasses (to reduce visual noise in some cases)"
  ],
  "prevention": [
    "Vascular health to prevent stroke",
    "Protective headgear",
    "Careful monitoring of neuro-active prescriptions"
  ]
}
"anton_babinski_syndrome": {
  "description": "Anton-Babinski Syndrome is a rare symptom of brain damage in the occipital lobe where patients who are cortically blind affirm, despite clear evidence, that they can see.",
  "symptoms": [
    "Visual anosognosia (complete denial of blindness)",
    "Confabulation (inventing visual details of the environment)",
    "Walking into objects/walls while claiming to see them",
    "Inappropriate affect (acting unconcerned about their frequent collisions)",
    "Providing excuses for 'missed' visual cues (e.g., 'The light is just too dim')"
  ],
  "causes": [
    "Bilateral damage to the primary visual cortex (V1)",
    "Ischemic stroke in the Posterior Cerebral Artery (PCA) territory",
    "Traumatic brain injury (TBI) to the back of the head",
    "Rare cases of hypertensive encephalopathy or leukoencephalopathy"
  ],
  "risk_factors": [
    "Hypertension (leading to bilateral PCA strokes)",
    "Cardiac arrhythmias (embolic risk)",
    "Vascular dementia",
    "Advanced age with cardiovascular complications"
  ],
  "diagnosis": [
    "Neurological testing of the 'menace reflex' (no blink when threatened)",
    "MRI/CT showing bilateral occipital lobe infarcts",
    "Preserved pupillary light reflexes (the eyes work, but the brain doesn't)",
    "Observation of blatant denial during visual field testing"
  ],
  "remedies": [
    "Treatment of the underlying stroke or injury",
    "Safety interventions (preventing falls/collisions)",
    "Gentle reality orientation (though often resisted)",
    "Rehabilitation to improve awareness of the deficit"
  ],
  "prevention": [
    "Aggressive management of blood pressure",
    "Stroke prevention protocols",
    "Prompt treatment of TBI"
  ]
}

"alice_in_wonderland_syndrome": {
  "description": "AIWS is a rare neurological condition characterized by distorted sensory perception, particularly regarding the size and distance of objects or one's own body parts.",
  "symptoms": [
    "Micropsia (objects appearing smaller than they are)",
    "Macropsia (objects appearing larger than they are)",
    "Teleopsia (objects appearing further away than they are)",
    "Pelopsia (objects appearing closer than they are)",
    "Time distortion (time moving too fast or too slow)",
    "Zoopsia (hallucinations of swarming animals)",
    "Altered sense of touch or sound (sounds feeling 'loud' or 'staccato')"
  ],
  "causes": [
    "Migraines (the most common cause in adults)",
    "Epstein-Barr Virus / Mononucleosis (common cause in children)",
    "Epilepsy (specifically temporal lobe seizures)",
    "Brain tumors or lesions in the parietal lobe",
    "Psychoactive drug use"
  ],
  "risk_factors": [
    "Childhood (most cases resolve by adulthood)",
    "History of migraine with aura",
    "Infectious diseases in the family",
    "Underlying seizure disorders"
  ],
  "diagnosis": [
    "Detailed clinical history and symptom mapping",
    "MRI or CT to rule out structural brain damage",
    "EEG to check for seizure activity",
    "Blood tests to screen for Epstein-Barr Virus (EBV)"
  ],
  "remedies": [
    "Treating the underlying cause (e.g., migraine prophylaxis)",
    "Rest and sensory deprivation during an episode",
    "Reassurance (as the symptoms can be terrifying but are usually benign)",
    "Anti-epileptic drugs (if seizure-related)"
  ],
  "prevention": [
    "Avoiding migraine triggers (stress, diet, sleep loss)",
    "Proper management of viral infections",
    "Routine neurological follow-ups for seizure patients"
  ]
}
"foreign_accent_syndrome": {
  "description": "FAS is a rare speech disorder that causes a person to speak their native language with an accent that sounds 'foreign' to listeners, despite the person having never lived in that region.",
  "symptoms": [
    "Changes in vowel length and pitch",
    "Errors in syllable stress (stressing the wrong part of a word)",
    "Inserting 'uh' or extra vowels between consonants",
    "Voicing errors (e.g., saying 'p' as 'b')",
    "Slowed, rhythmic speech patterns"
  ],
  "causes": [
    "Stroke (usually in the dominant hemisphere's speech centers)",
    "Traumatic Brain Injury (TBI)",
    "Brain tumors or lesions",
    "Severe psychological distress (Functional FAS)",
    "Multiple Sclerosis (MS) flare-ups"
  ],
  "risk_factors": [
    "Vascular health issues (stroke risk)",
    "Head trauma history",
    "Underlying neurological conditions in the motor cortex",
    "Certain psychiatric conditions"
  ],
  "diagnosis": [
    "MRI or CT to locate brain damage in Broca's area or the cerebellum",
    "Detailed speech and language assessment by a SLP",
    "Psychiatric evaluation to rule out functional causes",
    "Acoustic analysis of speech patterns"
  ],
  "remedies": [
    "Speech-Language Pathology (SLP) to retrain vocal muscle control",
    "Counseling to deal with the social impact/identity crisis",
    "Targeting the underlying cause (e.g., stroke rehabilitation)",
    "Techniques to mimic the original accent's rhythm"
  ],
  "prevention": [
    "Standard stroke prevention (BP management)",
    "Head protection in high-risk activities",
    "Early neurological intervention following head injuries"
  ]
}

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
"capgras_delusion": {
  "description": "Capgras Delusion is a psychiatric and neurological disorder in which a person holds a delusion that a friend, spouse, parent, or other close family member (or even a pet) has been replaced by an identical-looking impostor.",
  "symptoms": [
    "Firm belief that a loved one is a 'double' or impostor",
    "Preserved ability to recognize faces (no face blindness)",
    "Emotional disconnection during visual contact",
    "Occasional 'logical' explanations for the replacement (e.g., 'The government did it')",
    "Symptoms may resolve when the person is heard (voice) but not seen"
  ],
  "causes": [
    "Disconnection between the Fusiform Face Area and the Amygdala (the emotional center)",
    "Right hemisphere brain damage (specifically the temporal or frontal lobes)",
    "Neurodegenerative diseases (e.g., Lewy Body Dementia, Alzheimer's)",
    "Schizophrenia or severe brain injury"
  ],
  "risk_factors": [
    "Traumatic brain injury (TBI)",
    "History of psychotic disorders",
    "Advanced age with neurodegeneration",
    "Right-sided cerebral lesions"
  ],
  "diagnosis": [
    "Neuropsychological testing",
    "MRI to check for lesions in the right hemisphere",
    "EEG to rule out seizure-related confusion",
    "Skin Conductance Response (SCR) tests (checking for emotional arousal to faces)"
  ],
  "remedies": [
    "Treating the underlying condition (e.g., dementia or psychosis meds)",
    "Cognitive Behavioral Therapy (CBT) to challenge the delusion",
    "Validation therapy (reducing conflict with the patient)",
    "Using auditory-only communication (phone calls often bypass the glitch)"
  ],
  "prevention": [
    "Managing vascular health to prevent stroke",
    "Prompt treatment of psychiatric symptoms",
    "Early screening for cognitive decline"
  ]
}
"cotard_delusion": {
  "description": "Cotard's Delusion is a rare neuropsychiatric condition in which the affected person holds the delusional belief that they are dead, do not exist, or have lost their blood or internal organs.",
  "symptoms": [
    "Nihilistic delusions (belief that nothing exists, including themselves)",
    "Belief that they are decaying or smell of death",
    "Self-starvation (because 'dead people don't need to eat')",
    "Insensitivity to pain",
    "Severe depression and withdrawal",
    "Belief in immortality (paradoxically, because they 'already died')"
  ],
  "causes": [
    "Severe disconnection between the sensory processing areas and the emotional amygdala",
    "Atrophy or lesions in the right parietal lobe",
    "Severe depression or psychotic disorders",
    "Adverse reactions to certain medications (e.g., Acyclovir in patients with renal failure)"
  ],
  "risk_factors": [
    "History of severe clinical depression",
    "Bipolar disorder or schizophrenia",
    "Brain injury or tumor in the right hemisphere",
    "Elderly age (though it can occur in young people)"
  ],
  "diagnosis": [
    "Clinical psychiatric interview",
    "Neurological imaging (MRI/PET) to look for frontal-parietal atrophy",
    "Blood tests to check for metabolic causes (kidney function)",
    "Rule-out of general delirium"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT) - often the most effective treatment",
    "Antidepressants and antipsychotics",
    "Psychotherapy (once the patient is stabilized)",
    "Hydration and nutritional support (feeding tubes if necessary)"
  ],
  "prevention": [
    "Early intervention for severe depression",
    "Careful monitoring of antiviral medication doses",
    "Comprehensive care for traumatic brain injury recovery"
  ]
}
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
"prosopagnosia": {
  "description": "Prosopagnosia is a neurological disorder characterized by the inability to recognize faces, despite intact vision and intellectual functioning.",
  "symptoms": [
    "Inability to recognize familiar people (even family or oneself in a mirror)",
    "Reliance on non-facial cues (hair, gait, voice, or clothing) to identify others",
    "Difficulty following movie plots with many characters",
    "Social anxiety due to the fear of not acknowledging acquaintances"
  ],
  "causes": [
    "Damage to the fusiform gyrus (specifically the Fusiform Face Area)",
    "Congenital/Developmental (present from birth without brain injury)",
    "Acquired through stroke, traumatic brain injury, or neurodegeneration"
  ],
  "risk_factors": [
    "Genetics (in developmental cases)",
    "History of stroke in the right temporal lobe",
    "Certain neurodevelopmental conditions (e.g., Autism spectrum)"
  ],
  "diagnosis": [
    "Benton Facial Recognition Test (BFRT)",
    "Cambridge Face Memory Test (CFMT)",
    "fMRI to observe activity in the Fusiform Face Area (FFA)",
    "Neurological exams to rule out general vision loss"
  ],
  "remedies": [
    "Compensatory strategy training (focusing on voice/clothing)",
    "Contextual association (remembering people by where they usually are)",
    "Social skill training to manage 'blind' interactions",
    "No current 'cure' for developmental cases"
  ],
  "prevention": [
    "Stroke prevention (vascular health)",
    "Protective headgear to avoid TBI",
    "Early intervention in children to develop coping mechanisms"
  ]
}
"synesthesia": {
  "description": "Synesthesia is a neurological trait where the stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway.",
  "symptoms": [
    "Involuntary 'blended' sensations (e.g., seeing blue when hearing a C-sharp)",
    "Consistent associations (the letter 'A' is always red, forever)",
    "Spatial sequences (seeing months or numbers arranged in physical space)",
    "Lexical-gustatory sensations (certain words trigger specific tastes)",
    "Enhanced memory for associated items (using color to remember names)"
  ],
  "causes": [
    "Increased cross-talk between neighboring brain regions (e.g., V4 for color and the grapheme area)",
    "Failure of 'neural pruning' during early development",
    "Genetic predisposition (often runs in families)",
    "Temporary induction via certain psychoactive substances"
  ],
  "risk_factors": [
    "Genetics (highly heritable)",
    "Left-handedness (statistically higher correlation)",
    "Creative professions (more common in artists, musicians, and writers)"
  ],
  "diagnosis": [
    "Consistency testing (testing associations months apart)",
    "fMRI showing multi-modal activation (e.g., visual cortex lighting up for sounds)",
    "The Synesthesia Battery (standardized online testing)"
  ],
  "remedies": [
    "No 'cure' needed (it is usually considered a neutral or positive trait)",
    "Coping strategies if certain associations are overwhelming (e.g., loud 'yellow' noises)",
    "Mindfulness to manage sensory overload"
  ],
  "prevention": [
    "None (it is a structural/developmental trait)"
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
"functional_neurological_disorder": {
  "description": "FND is a condition where patients experience neurological symptoms such as limb weakness, tremors, or seizures, despite having no structural or organic damage to the nervous system.",
  "symptoms": [
    "Functional weakness or paralysis (often fluctuating)",
    "Non-epileptic seizures (dissociative seizures)",
    "Functional tremors or gait (walking) abnormalities",
    "Chronic pain or sensory changes",
    "Speech difficulties (whispering or stuttering)"
  ],
  "causes": [
    "Maladaptive brain connectivity",
    "Psychological or physical stressors (as a trigger)",
    "History of previous neurological conditions",
    "Functional 'miswiring' of the motor and sensory cortex"
  ],
  "risk_factors": [
    "Gender (more common in women)",
    "History of childhood trauma or intense stress",
    "Presence of other neurological diseases (e.g., Epilepsy or MS)",
    "Anxiety or depressive disorders"
  ],
  "diagnosis": [
    "Clinical exam identifying 'Positive Signs' (e.g., Hoover's sign)",
    "Video-EEG (to distinguish from epilepsy)",
    "Physical therapy assessment of movement patterns",
    "MRI/CT (specifically to rule out structural damage)"
  ],
  "remedies": [
    "Specialized physical and occupational therapy",
    "Cognitive Behavioral Therapy (CBT)",
    "Education about the diagnosis (vital for recovery)",
    "Transcranial Magnetic Stimulation (TMS)"
  ],
  "prevention": [
    "Early stress intervention",
    "Prompt physical therapy after a trigger event",
    "Education to prevent symptom 'internalization'"
  ]
}
"fatal_familial_insomnia": {
  "description": "FFI is an extremely rare and fatal genetic degenerative brain disorder characterized by an inability to sleep that progressively worsens.",
  "symptoms": [
    "Progressive, worsening insomnia",
    "Panic attacks and paranoia",
    "Phobias and hallucinations",
    "Significant weight loss",
    "Dementia and loss of motor control (ataxia)",
    "Complete inability to sleep"
  ],
  "causes": [
    "Mutation in the PRNP gene (Prion protein)",
    "Misfolding of proteins into prions that accumulate in the thalamus",
    "Physical atrophy (shrinking) of the thalamus"
  ],
  "risk_factors": [
    "Genetics (Autosomal dominant inheritance)",
    "Extremely rare sporadic cases (sFFI)"
  ],
  "diagnosis": [
    "Genetic testing for the PRNP mutation",
    "Polysomnography (sleep study showing zero REM/Slow-wave sleep)",
    "PET scan showing reduced metabolism in the thalamus",
    "Cerebrospinal fluid analysis (checking for 14-3-3 proteins)"
  ],
  "remedies": [
    "No known cure (currently 100% fatal)",
    "Symptom management (sedatives usually fail)",
    "Palliative care",
    "Experimental gene-silencing therapies (Antisense Oligonucleotides)"
  ],
  "prevention": [
    "Genetic counseling for affected families",
    "In-vitro fertilization with genetic screening (PGD)"
  ]
}
"tardive_dyskinesia": {
  "description": "Tardive dyskinesia is a movement disorder characterized by involuntary, repetitive body movements, typically caused by long-term use of dopamine-antagonist medications.",
  "symptoms": [
    "Grimacing or puckering of the lips",
    "Repeated tongue protrusion (the 'fly-catcher' tongue)",
    "Rapid, involuntary eye blinking",
    "Smacking of the lips or puffing of the cheeks",
    "Finger-tapping or 'piano-playing' movements with the hands",
    "Jerking movements of the torso or hips"
  ],
  "causes": [
    "Upregulation of D2 dopamine receptors in the basal ganglia",
    "Long-term use of antipsychotics or certain GI medications (e.g., metoclopramide)",
    "Oxidative stress causing neuron damage"
  ],
  "risk_factors": [
    "Duration of medication use (years vs. months)",
    "Age (older adults are at higher risk)",
    "Gender (statistically slightly more common in women)",
    "Pre-existing mood disorders"
  ],
  "diagnosis": [
    "AIMS (Abnormal Involuntary Movement Scale) exam",
    "Observation of the 'piano-playing' hands or lip smacking",
    "Ruling out Huntington's or Parkinson's through imaging"
  ],
  "remedies": [
    "VMAT2 inhibitors (Valbenazine or Deutetrabenazine)",
    "Adjusting or tapering the triggering medication",
    "Vitamin E (as an antioxidant support)",
    "Botox (for specific focal movements)"
  ],
  "prevention": [
    "Using the lowest effective dose of dopamine-blocking meds",
    "Regular AIMS screenings (every 6 months)",
    "Switching to 'atypical' medications with lower TD risk"
  ]
}
"brown_sequard_syndrome": {
  "description": "Brown-Séquard Syndrome is a rare neurological condition caused by a lesion or hemisection (half-cut) of the spinal cord, resulting in asymmetrical sensory and motor loss.",
  "symptoms": [
    "Ipsilateral (same side) paralysis or weakness",
    "Ipsilateral loss of vibration and 'position sense' (proprioception)",
    "Contralateral (opposite side) loss of pain and temperature sensation",
    "Hyperesthesia (extreme sensitivity) just above the level of the injury"
  ],
  "causes": [
    "Traumatic injury (e.g., puncture wound or spinal fracture)",
    "Spinal cord tumors",
    "Ischemia (loss of blood flow to the spine)",
    "Infectious or inflammatory diseases (e.g., Tuberculosis or MS)"
  ],
  "risk_factors": [
    "High-impact trauma history",
    "Spinal disc herniation",
    "Cervical spondylosis (wear and tear of spinal discs)"
  ],
  "diagnosis": [
    "Neurological sensory mapping (pin-prick vs. vibration tests)",
    "MRI or CT Myelography to locate the spinal lesion",
    "Somatosensory Evoked Potentials (SSEP)"
  ],
  "remedies": [
    "High-dose corticosteroids (to reduce acute swelling)",
    "Surgery (to remove tumors or stabilize fractures)",
    "Intensive physical and occupational therapy",
    "Management of secondary issues like bladder/bowel dysfunction"
  ],
  "prevention": [
    "Safety equipment in high-risk environments",
    "Early treatment of spinal infections",
    "Proper management of severe disc herniations"
  ]
}
"locked_in_syndrome": {
  "description": "Locked-In Syndrome is a rare neurological disorder characterized by complete paralysis of voluntary muscles in all parts of the body except for those that control eye movement.",
  "symptoms": [
    "Inability to move limbs, trunk, or face",
    "Loss of speech (aphonia)",
    "Preserved consciousness and cognitive function",
    "Preserved hearing and vision",
    "Vertical eye movement and blinking (the only remaining motor control)"
  ],
  "causes": [
    "Brainstem stroke (specifically the ventral pons)",
    "Traumatic brain injury",
    "Demyelinating diseases (e.g., severe GBS or MS)",
    "Medication overdose or poisoning (rare)"
  ],
  "risk_factors": [
    "High blood pressure or cardiovascular disease (stroke risk)",
    "Clotting disorders",
    "Severe head or neck trauma"
  ],
  "diagnosis": [
    "MRI or CT to identify the brainstem lesion",
    "EEG to confirm preserved brain activity (consciousness)",
    "Evoked potential tests",
    "Clinical assessment of eye-movement responses"
  ],
  "remedies": [
    "Brain-Computer Interfaces (BCI) for communication",
    "Eye-tracking assistive technology",
    "Physical therapy (to prevent muscle contractures)",
    "Supportive care (respiratory and nutritional support)"
  ],
  "prevention": [
    "Stroke prevention (blood pressure and cholesterol control)",
    "Prompt treatment of basilar artery thrombosis",
    "Safety measures to prevent traumatic brain injury"
  ]
}
# Common greetings and responses
greetings = ["hello", "hi", "hey", "greetings"]
farewells = ["bye", "goodbye", "see you", "exit"]
thanks = ["thanks", "thank you", "appreciate it"]


def get_response(user_input):
    user_input = user_input.lower().strip()

    # Check for greetings
    if any(word in user_input for word in greetings):
        return random.choice([
            "Hello! I'm MediBot. How can I help you today?",
            "Hi there! What health concerns do you have?",
            "Greetings! I'm here to provide general health information."
        ])

    # Check for farewells
    if any(word in user_input for word in farewells):
        return random.choice([
            "Take care and stay healthy!",
            "Goodbye! Remember to consult a doctor for serious symptoms.",
            "See you later! Wishing you good health."
        ])

    # Check for thanks
    if any(word in user_input for word in thanks):
        return random.choice([
            "You're welcome!",
            "Happy to help!",
            "No problem! Stay healthy."
        ])

    # Check for conditions in the database
    for condition, info in medical_db.items():
        # Match both underscore and spaced versions
        if condition in user_input or condition.replace("_", " ") in user_input:
            response = f"About {condition.replace('_', ' ').title()}:\n"
            response += f"Description: {info['description']}\n"
            response += f"Possible causes: {', '.join(info['causes'])}\n"
            response += f"Suggested remedies: {', '.join(info['remedies'])}\n"
            response += "Note: If symptoms persist or worsen, please consult a doctor."
            return response

    # Default response if no matches found
    return ("I'm sorry, I couldn't find information on that condition. "
            "Please try a specific condition name such as 'headache', 'diabetes', or 'fever'. "
            "For medical concerns, please consult a healthcare professional.")


def main():
    print("MediBot: Hello! I'm a simple medical chatbot providing general health information.")
    print("Type 'bye' to exit at any time.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in farewells:
            print("MediBot:", get_response(user_input))
            break
        response = get_response(user_input)
        print("MediBot:", response)
        print()


if __name__ == "__main__":
    main()

