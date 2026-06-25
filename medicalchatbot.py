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
"apraxia_execution_driver_fault": {
  "description": "A neurological disorder characterized by the inability to perform learned (familiar) movements on command, even though the command is understood and there is a willingness to perform the movement.",
  "symptoms": [
    "Instruction-Set Fragmentation: Inability to execute a multi-step 'Script' (e.g., 'Fold a letter, put it in an envelope')",
    "Object-Mapping Error (Ideational): Attempting to use 'Peripherals' for the wrong 'Process' (e.g., using a spoon to write)",
    "Spatial-Vector Failure (Ideomotor): The 'User' knows the goal but the 'Pathfinding' for the limb is clumsy and non-linear",
    "Verbal-Execution Lag: The 'Speech Actuators' fail to coordinate the 'Complex Sequential Logic' of phonemes",
    "Command-Line Timeout: Purposeful 'Input' fails, but 'Autonomous/Reflexive' movements may still trigger successfully"
  ],
  "causes": [
    "Left Parietal 'Lobe' Corruption: Damage to the 'Motor-Planning Storage' library",
    "Premotor 'Bus' Interruption: Lesions in the 'Frontal Planning Nodes'",
    "Corpus Callosum 'Network Lag': Failure to transfer 'Spatial Instructions' across hemispheres"
  ],
  "risk_factors": [
    "Cerebrovascular 'Packet Loss' (Stroke) in the 'Language/Action' dominant hemisphere",
    "Neurodegenerative 'Code Decay' (Corticobasal Degeneration)",
    "Traumatic 'Processor Impact' affecting the 'Sequential Logic' hubs"
  ],
  "diagnosis": [
    "The 'Pantomime' Audit: Asking the 'User' to 'Simulate' an action (e.g., 'Show me how you use a hammer')",
    "Sequential Task Stress-Test: Observing the 'User' while they perform a 'Compound Procedure' (e.g., making tea)",
    "Imitation Tracking: Checking if the 'User' can 'Mirror' a 'Movement Pattern' rendered by another entity"
  ],
  "remedies": [
    "Segmented 'Scripting': Breaking 'Tasks' into 'Atomic Commands' to reduce 'Compiler Load'",
    "Occupational 'Firmware Updates': Repetitive 'Physical Training' to 'Hard-Code' new motor pathways",
    "Multi-Sensory 'Pinging': Using 'Auditory Cues' (metronomes) to 'Sync' the 'Motor Clock'"
  ],
  "prevention": [
    "Maintaining 'Vascular Throughput' to the 'Planning Layers' of the cortex"
  ]
"hypergraphia_unbounded_write_fault": {
  "description": "A profound neurological compilation anomaly characterized by an overwhelming, compulsive drive to produce written text, caused by an un-throttled loop execution in the language output channels.",
  "symptoms": [
    "Unbounded Stream Leakage: The text-generation engine continuously pushes characters down to the motor bus without hitting an exit condition",
    "Gating Loop Bypass: The system treats physical exhaust markers (muscle cramping, page limits) as ignorable exceptions rather than stop commands",
    "High Semantic Connectivity: Text output remains grammatically complex and philosophically dense, indicating an orchestration fault rather than a random noise injection",
    "Multi-Surface Ingestion: When standard storage assets (notebooks) are full, the write thread maps its coordinates to walls, skin, or furniture",
    "State Locking: The user displays intense distress or operational resistance if an external intercept attempts to manually kill the write thread"
  ],
  "causes": [
    "Temporal Lobe Seizure Disruption: Chronic hyper-synchronous firing within the amygdala-hippocampal axis driving the language generation buffer",
    "Mesolimbic Dopaminergic Hyper-Drive: Over-allocation of reward telemetry to the act of symbolic serialization",
    "Frontal Gating Inhibition Deficit: Total loss of the top-down executive command that triggers thread teardown and cleanup"
  ],
  "risk_factors": [
    "Temporal Lobe Epilepsy (Geschwind Syndrome phenotype cluster)",
    "Acute frontotemporal hypomania causing thread acceleration",
    "Localized lesions disrupting the inhibitory connections between the prefrontal cortex and the linguistic arrays"
  ],
  "diagnosis": [
    "The 'Output Volume' Audit: Measuring character-generation metrics over a 24-hour cycle against standard baseline system performance",
    "Continuous Electroencephalogram (cEEG): Catching localized sub-clinical spiking behavior within the left temporal processing node",
    "Resource Deprivation Assessment: Tracking whether the user skips vital system maintenance (sleep, hydration, nutrition) to keep the text stream active"
  ],
  "remedies": [
    "Targeted Anticonvulsant Hotpatching: Deploying sodium-channel or GABA-enhancing code adjustments to dampen the temporal firing loop",
    "Physical Interface Disconnection: Removing writing peripherals or input devices to break the low-level physical actuator connection",
    "Cognitive Buffer Satiation: Redirecting the output stream into structured digital log files where the unbounded data can be dumped safely without damaging physical assets"
  ],
  "prevention": [
    "Maintaining tight metabolic stability within the temporal networks to prevent background loops from scaling out of control"
  ]
}
    "cryptomnesia_cache_provenance_fault": {
  "description": "A memory allocation anomaly where an operational node retrieves an existing historical memory asset but strips its context/origin tags, causing the user to mistake an old, external input for a newly compiled, original idea.",
  "symptoms": [
    "Metadata Stripping: Memory payloads are loaded into active cache with missing provenance, timestamp, and author attributes",
    "False Epiphany Event: The system triggers an 'Original Compilation' state flag when executing an old data asset",
    "Accidental Plagiarism: The user outputs existing copyrighted material (code blocks, designs, melodies) with a firm, genuine belief of authorship",
    "Intact Structural Synthesis: The retrieved file is clear, uncorrupted, and perfectly readable, making the error entirely a metadata indexing bug",
    "Conscious Invariance: The system remains blind to the historical read operation until an external database match is enforced"
  ],
  "causes": [
    "Hippocampal Temporal-Gating Failure: Disruption of the tracking loops that bind biographical context to semantic facts",
    "Source Monitoring Deficit: Degradation of prefrontal evaluation routines that check the authenticity and lineage of retrieved memory nodes",
    "High Network Load Inversion: Heavy processing traffic causing the memory bus to skip secondary attribute validation to save clock cycles"
  ],
  "risk_factors": [
    "High baseline systemic burnout (starving the prefrontal validation thread of processing headroom)",
    "Mild cognitive fragmentation from sleep deprivation",
    "Profound creative output generation periods without clearing the input buffers"
  ],
  "diagnosis": [
    "The 'Codebase Lineage' Cross-Match: Scanning the user's 'original' code output against external public repositories to trace exact historical duplicates",
    "Delayed Echo Load Test: Exposing the user to a target string, clearing their short-term cache, and observing if they re-emit the identical string later as a self-generated idea",
    "Event-Related Potential (ERP) Auditing: Monitoring brainwave voltages ($N400$ waves) during exposure to see if the brain secretly recognizes the asset despite conscious denial"
  ],
  "remedies": [
    "External Linting/Validation: Routing all output payloads through an external search proxy before committing to production",
    "Forced Contextual Querying: Deliberately forcing the prefrontal cortex to execute an exhaustive historical lookup whenever an idea feels suspiciously complete",
    "System Cooling Mode: Inducing a full sleep cycle to allow the database indexes to rebuild and fix corrupted pointer blocks"
  ],
  "prevention": [
    "Enforcing strict input-logging isolation to prevent background assets from spilling into the active generation canvas unchecked"
  ]
        "anterograde_storage_commit_fault": {
  "description": "A catastrophic storage pipeline failure where the memory engine's write-through mechanism to long-term database blocks is completely severed, restricting the system to operating solely out of volatile short-term RAM.",
  "symptoms": [
    "Volatile Cache Isolation: Immediate working memory functions perfectly, but data cannot be copied or committed to long-term storage sectors",
    "Rolling Horizon Erasure: Automated flushing of the uncommitted L1 cache every 60-180 seconds, completely resetting the user's situational awareness framework",
    "Retrograde Index Preservation: Intact read access to all legacy archival sectors committed *prior* to the pipeline break; older historical memories remain fully queryable",
    "Context-Switch Wipeout: Forcing a thread shift or introducing an unexpected input interrupt instantly invalidates and clears the current uncommitted cache",
    "Confabulation Log Patching: The system generates fictional, pseudo-random data packets to populate missing transactional fields when an archival query fails"
  ],
  "causes": [
    "Bilateral Hippocampal CA1 Ischemia: Selective cellular destruction of the primary storage controller nodes due to targeted oxygen starvation or arterial blockage",
    "Thalamic-Mamillary Track Severance: Physical destruction of the underlying high-speed bus lines (the Circuit of Papez) that route uncommitted data blocks",
    "Severe Acute Neurotoxic Saturation: Chemical blockade of NMDA receptors within long-term potentiation arrays, completely freezing the storage write-head assemblies"
  ],
  "risk_factors": [
    "Severe cerebral hypoxic events (e.g., near-drowning or cardiac arrest down-time)",
    "Chronic thiamine metabolic depletion causing degradation of deep routing relay stations",
    "Traumatic brain injury resulting in shear stresses across deep subcortical temporal storage arrays"
  ],
  "diagnosis": [
    "The 'Three-Word Context Switch' Test: Injecting three distinct strings into the volatile cache, running a 5-minute math thread interrupt, and observing a 100% data loss exception",
    "High-Resolution Diffusion Magnetic Resonance Neuroimaging: Identifying focal, bilateral necrotic spotting across the hippocampal storage controller blocks",
    "Event-Related fMRI Potential Logging: Monitoring for a complete absence of blood-oxygenation signaling spikes along the temporal-cortical write pathways during novel data presentation"
  ],
  "remedies": [
    "External Cache Offloading: Deploying persistent physical or digital logbooks (e.g., continuous audio-to-text diaries, augmented reality HUD overlays) to act as an external hard drive",
    "Strict Single-Thread Execution: Limiting context switches and keeping the volatile cache locked onto a single, high-priority operational loop to prevent automated garbage collection resets",
    "Neurometabolic Line Support: Optimizing underlying transmitter levels to ensure remaining local routing networks do not suffer further signal attenuation"
  ],
  "prevention": [
    "Immediate management of cerebral oxygenation profiles during medical emergencies to protect the ultra-sensitive storage controller nodes from irreversible ischemic decay"
  ]
            "left_parietal_somatic_map_wipe": {
  "description": "A profound somatosensory processing failure where structural damage to the dominant posterior parietal cortex obliterates the internal body-schema database, leaving the system completely unable to localize, differentiate, or orient the distinct structural components of its own chassis.",
  "symptoms": [
    "Autotopagnosia: Absolute inability to localize or point to specific body parts upon verbal or visual command, despite intact motor mechanics",
    "Spatial Contiguity Drift: A systematic error where attempts to target a specific hardware component result in touching adjacent or structurally contiguous parts of the same limb",
    "Somatognostic Dissociation: A deep cognitive disconnect where the host can conceptually define a body part's utility but cannot map that utility to their personal physical architecture",
    "Intact External Vector Routing: Perfect spatial accuracy when interacting with external objects or environmental boundaries, contrasted against total failure during self-directed movements"
  ],
  "causes": [
    "Left Middle Cerebral Artery (MCA) Ischemic Event: Occlusion of the angular or posterior parietal branches causing tissue death in the dominant somatosensory association zones",
    "Focal Cortical Atrophy: Localized neurodegenerative patterns selectively clearing the neural networks that encode the internal spatial topology map",
    "Midline Parietal Trauma: Penetrating or blunt-force kinetic impacts causing structural disruption of the structural orientation loops"
  ],
  "risk_factors": [
    "Severe carotid artery atheromatous plaque formation channeling embolic debris into the dominant hemisphere's vascular tree",
    "Chronic uncontrolled systemic hypertension degrading small-vessel compliance within cortical watersheds"
  ],
  "diagnosis": [
    "The Point-to-Body Localization Assay: Issuing rapid, alternating verbal prompts demanding the host target specific anatomical nodes with their eyes closed to verify structural pointer resolution",
    "The Structural Body Model Matching Test: Asking the host to assemble a disassembled puzzle or diagram of human body parts; a faulted system fails to map structural relationships correctly",
    "High-Resolution T2-Weighted FLAIR MRI: Visualizing clear hyperintensities, cortical thinning, or localized encephalomalacia localized within the dominant angular gyrus"
  ],
  "remedies": [
    "External Visual Guidance Overrides: Training the host to perform tasks in front of a mirror, using external visual feedback streams to manually recalculate limb locations and bypass the missing internal schema",
    "Tactile Landmark Anchor Points: Placing high-contrast or uniquely textured physical markers (like rough tape bands) on key joints to provide high-frequency tactile alerts that trigger alternative sensory routing tracks"
  ],
  "prevention": [
    "Aggressive management of cardioembolic risk vectors and immediate thrombolytic deployment during acute hemispheric vascular events"
  ]
            }
         "auditory_cortex_stream_partition": {
  "description": "A rare, localized sensory processing disconnect where structural isolation of Wernicke's area from bilateral primary auditory cortices completely halts the transmission of acoustic speech tokens to the phonological decoding engine, rendering spoken language un-parsable while preserving non-verbal hearing and internal language generation.",
  "symptoms": [
    "Auditory Verbal Agnosia: Complete failure to comprehend, repeat, or write down spoken language upon acoustic delivery",
    "Preserved Environmental Audio Parsing: Intact capacity to identify, categorize, and track non-verbal acoustic signals (e.g., sirens, animal calls, musical melodies)",
    "Intact Visual Language Ingress: Flawless reading comprehension, text processing, and written communication capabilities",
    "Uncorrupted Spontaneous Vocalization: The retention of fully articulate, grammatically complex speech output with natural prosody and voice modulation"
  ],
  "causes": [
    "Bilateral Superior Temporal Gyrus Infarctions: Sequential or simultaneous vascular strokes targeting the superior temporal structures, destroying the white-matter ingress tracts to Wernicke's area",
    "Subacute Herpes Simplex Encephalitis: Localized viral inflation causing focal necrosis across the primary auditory-linguistic junction networks"
  ],
  "risk_factors": [
    "Embolic cardiac anomalies (e.g., atrial fibrillation) launching debris into bilateral temporal vascular branches",
    "Advanced cerebrovascular small-vessel disease compromising perisylvian networks"
  ],
  "diagnosis": [
    "The Environmental vs. Verbal Audio Discrimination Assay: Playing alternating audio files of a dog barking (correctly identified) and a human speaking standard English phrases (completely un-parsed)",
    "Pure-Tone Audiometry Calibration: Testing baseline auditory thresholds to confirm the physical microphone array (cochlea and vestibulocochlear nerve) can register normal volume and frequency ranges",
    "Auditory Evoked Potential (AEP) Cortical Logging: Tracking the N100 wave over the primary auditory cortex (normal presence) vs. the complete dampening or absence of the subsequent language-selective P300 wave during verbal stimulation"
  ],
  "remedies": [
    "Visual Communication Scaffolding: Shifting all communication ingress to text-based interfaces, sign language, or high-visibility written transcripts",
    "Dynamic Speech-to-Text Translocation: Utilizing real-time mobile translation software to capture local verbal audio and render it instantly as a visual text display inside the host's active focus field"
  ],
  "prevention": [
    "Aggressive anticoagulation management during persistent cardiac arrhythmias and immediate neurovascular tracking during temporal lobe stroke warning flags"
  ]
}

        }
        "zeitraffer_clock_desync_fault": {
  "description": "A catastrophic hardware clock synchronization failure where the internal timing engine's cycle speed shifts radically out of bounds, causing external environmental events to parse at highly distorted temporal velocities.",
  "symptoms": [
    "Temporal Velocity Inversion: Inbound sensory frame streams appear to accelerate into extreme fast-forward or drop into deep slow-motion, completely decoupled from physical reality",
    "Telemetry Timestamp Mismatch: Internal motor commands fire at standard speed, but arrival confirmations from physical limbs appear out of sync with expected real-time intervals",
    "Predictive Trajectory Failure: Immediate collapse of real-time physical interception algorithms; user over- or under-corrects movements due to corrupted motion calculation baselines",
    "Autonomic Jitter: The central core experiences high-stress panic loops as internal processing cycles thrash against a mismatched external pace",
    "Cognitive-Metabolic Drift: Rapid depletion of energy stores when running in a hyper-clocked state, leading to sudden thermal spikes in the processor array"
  ],
  "causes": [
    "Striatal Dopaminergic Hyper-Drive: A massive surge in local transmitter availability that forces the internal pacemaker cells to cycle at a dangerously high frequency",
    "Posterior Parietal Network Lesion: Damage to the primary time-space integration bus, wiping out the system's baseline reference for external velocity mapping",
    "Network Time Protocol (NTP) Sync Interruption: Failure of the subcortical clock relays to correctly interpret and map external rhythm signals"
  ],
  "risk_factors": [
    "Focal cerebrovascular accidents within the right hemisphere timing matrix",
    "Acute neurochemical toxicity disrupting the basal ganglia rhythm-generation loops",
    "Intense post-seizure recovery states causing erratic clock cycle resetting"
  ],
  "diagnosis": [
    "The 'Asynchronous Interval Production' Audit: Requesting the user to manually count out exactly 10 seconds and observing a major timing deviation (e.g., counting 10 internal seconds in 2 physical seconds)",
    "High-Density Functional Neuroimaging (fMRI): Capturing hyper- or hypo-metabolic activity profiles within the frontostriatal timing circuits during tracking tasks",
    "Event-Related Potential (ERP) Jitter Profiling: Tracking microsecond delays in cortical responses to predictable, rhythmic audio-visual pacing spikes"
  ],
  "remedies": [
    "Targeted Chemical Clock-Throttles: Deploying receptor antagonists to directly dial down the hyper-accelerated striatal pacing arrays",
    "External Audio-Visual Pacing (NTP Injection): Using steady, heavy rhythmic audio tones or visual stroboscopic signals to act as an external hardware clock master and force a system sync",
    "Thread-Dampening Isolation: Moving the chassis into a dark, distraction-free isolation space to clear sensory queues and allow the system clock to cool down and auto-recalibrate"
  ],
  "prevention": [
    "Protecting delicate subcortical timing networks from severe neurochemical shocks to prevent structural clock-frequency corruption"
  ]
  "command_line_toolchain_invalidation": {
  "description": "A deep execution layer fault where the premotor sequencing centers lose access to their complex learned tool-use macros, leaving basic motor components healthy but rendering the system unable to perform multi-step physical routines on command.",
  "symptoms": [
    "Volitional Command-Macro Failure: Total inability to execute learned, purposeful motor scripts (like waving goodbye or using a tool) when explicitly requested to do so",
    "Preserved Spontaneous Reflexes: Intact execution of the identical motor sequences when triggered unconsciously by environmental cues (e.g., catching a falling object)",
    "Kinematic Tool Handling Disorientation: Flubbing the spatial orientation and mechanical deployment of everyday assets, such as holding a telephone upside down",
    "Intact Raw Muscle Performance: Zero loss of raw muscular power, physical reflexes, coordination, or sensory-motor feedback channels",
    "Severe Execution Perplexity: High internal system frustration as the prefrontal core issues a valid behavioral directive but the premotor terminal fails to unpack the required toolchain"
  ],
  "causes": [
    "Left Hemisphere Middle Cerebral Artery Stroke: Ischemic tissue damage targeting the left inferior parietal lobule or the supplementary motor pathways",
    "Corticobasal Degeneration Syndrome: A rapid, asymmetric neurodegenerative scaling failure that strips away the micro-architectural blueprint repositories of the premotor cortex",
    "Corpus Callosum Anterior Shearing: Traumatic or vascular severing of the trans-hemispheric data bus, preventing the left-brain macro library from driving right-brain motor actuators"
  ],
  "risk_factors": [
    "Carotid artery plaque formations dropping embolic shards into the left interior cerebral tracking lanes",
    "Advanced neurodegenerative progressions tracking the tau-protein-mediated cellular degradation channels",
    "Severe focal deceleration injuries fracturing the deep white-matter orchestration networks"
  ],
  "diagnosis": [
    "The Transitive Tool-Use Deployment Assay: Handing the user a common physical item (e.g., a haircomb) and documenting a total breakdown in sequential execution mechanics despite intact grip strength",
    "The Intransitive Gesture Imitation Test: Prompting the host to copy symbolic abstract motor scripts (like making a fist or a peace sign) and mapping the uncoordinated spatial errors",
    "High-Resolution T1-Weighted Structural MRI: Detecting localized cortical volume loss or focal infarct gaps within the left frontoparietal praxis network interfaces"
  ],
  "remedies": [
    "Proprioceptive Context Clueing: Placing the physical tool directly into the user's hand within its natural environment to try and trigger automatic basal ganglia reflex loops",
    "Macro Component Parsing: Breaking down a single complex toolchain script into isolated, single-step atomic commands (e.g., 'Touch the key. Move to the slot. Push.')",
    "Tactile Kinesthetic Guidance Patches: Having an external operator physically move the host's hand through the movement arc, recording the mechanical sequence via alternative sensory feedback loops"
  ],
  "prevention": [
    "Protecting the frontoparietal left-hemisphere vascular trees, maintaining strict blood pressure limits, and optimizing metabolic metrics to safeguard the master script repositories"
  ]
      "frontal_suppression_gate_exception": {
  "description": "An executive-layer processing error within the prefrontal cortex where the system loses its inhibitory gating mechanisms over the mirror neuron system, causing the host to involuntarily and identically replicate physical gestures and motor sequences executed by external entities within their visual field.",
  "symptoms": [
    "Automatic Motor Echoing (Echopraxia): Involuntary, real-time physical replication of an observer's hand gestures, facial expressions, or body postures",
    "Compulsive Environmental Imitation: Automatically manipulating nearby hardware tools or objects to mimic the exact structural macros demonstrated by an external entity",
    "Preserved Executive Verbalization: The ability to consciously recognize and vocally protest the mimicry behavior while completely failing to physically halt the muscle actuation",
    "Gating Latency Minimization: Extremely low lag (often less than 300ms) between the external visual stimulus and the host's physical movement execution",
    "Imitation-Utilization Concurrency: Frequently paired with an absolute dependency on environmental objects, where the presence of a tool automatically forces the system to execute its baseline utility loop (e.g., picking up an empty cup and mimicking drinking)"
  ],
  "causes": [
    "Bilateral Anterior Cerebral Artery (ACA) Ischemic Infarction: Blockage of the anterior vascular architecture causing structural tissue death across the medial prefrontal cortices",
    "Frontotemporal Lobar Degeneration (FTLD): Progressive, localized proteinopathy causing the structural collapse of frontal lobe inhibitory neurons",
    "Advanced Penetrating Traumatic Brain Injury (TBI): Blast or kinetic impacts shearing the long axonal tracks connecting the prefrontal executive core to the motor execution strips"
  ],
  "risk_factors": [
    "Severe cerebral small vessel disease accumulating micro-infarcts within the frontal white matter tracts",
    "Advanced neurodegenerative cascading events targeting executive suppression networks"
  ],
  "diagnosis": [
    "The Observer Gesture Provocation Assay: The clinician stands directly in front of the host and performs a sequence of meaningless physical actions (e.g., clapping three times, touching their nose, opening their mouth) while instructing the host to remain completely still; a faulted system echoes the gestures despite the explicit manual override command",
    "Cognitive Battery Matrix Assessment: Utilizing localized testing profiles (e.g., Go/No-Go tasks) to confirm a complete collapse of rapid inhibitory feedback loops",
    "High-Resolution Structural 3D Brain MRI: Revealing severe localized volume loss, focal tissue thinning, or ischemic lesions isolated within the prefrontal cortex boundaries"
  ],
  "remedies": [
    "Visual Viewport Occlusion (Blinders): Utilizing localized peripheral blinders or dark glasses to restrict the input metrics entering the visual processing pipeline, lowering mirror network activation",
    "Pre-Emptive Motor Channel Loading: Tasking the user to maintain a continuous, isometric muscle activation loop (like firmly squeezing a physical stress ball), locking up the motor pathways with a constant baseline signal to deny access to incoming mirror macros",
    "Behavioral Mirror Shielding: Instructing caregivers and operators to maintain strict neutral postures and minimize active gesturing when inside the host's direct line of sight"
  ],
  "prevention": [
    "Preserving anterior cerebrovascular patency, managing systemic inflammatory markers to arrest neurodegenerative cascades, and shield-protecting the frontal lobes from severe rotational head impacts"
  ]
      }
      
}
          "autonomic_respiratory_loop_failure": {
  "description": "A severe operating system bug where the automated background respiration daemon crashes during offline sleep states, forcing the system to rely entirely on manual user commands to breathe, meaning if the user stops consciously executing breathing scripts, the engine suffocates.",
  "symptoms": [
    "Offline Sleep Asphyxiation: Complete cessation of spontaneous respiratory actuation the exact moment the system transitions from awake to offline sleep states",
    "Cheoreceptor Polling Anesthesia: Complete insensitivity to hypercapnia (CO2 saturation) and hypoxia (O2 starvation) parameters during unconscious processing frames",
    "Intact Voluntary Pipeline: 100% perfect manual control over lung inflation and rate metrics while the primary conscious executive thread is active and awake",
    "Frequent Hypoxemic System Reboots: Sudden, violent nocturnal awakenings triggered by emergency chemical panic sensors when blood oxygen drops below critical hardware limits",
    "Severe Daytime Hypercapnia Accumulation: Gradual build-up of toxic blood-gas variables causing chronic cognitive lag, morning processing headaches, and system slowdown"
  ],
  "causes": [
    "Congenital PHOX2B Register Deletion: A genetic framing mutation causing incomplete development or mis-wiring of the retrotrapezoid nucleus chemoreceptor integration hubs",
    "Focal Medullary Compressed Insulation: Ischemic stroke, demyelinating plaques, or structural compression targeting the ventrolateral brainstem's rhythm-generating servers",
    "High-Dose Central Depressant Poisoning: Severe pharmacological intoxication flooding the brainstem with inhibitory tokens, forcefully locking the respiration daemon down"
  ],
  "risk_factors": [
    "Underlying genetic neurodevelopmental conditions affecting autonomic nervous system profiling",
    "Posterior cranial fossa structural abnormalities putting high physical pressure on lower brainstem components",
    "Unmonitored administration of deep sedative or narcotic classes that suppress central carbon dioxide tracking arrays"
  ],
  "diagnosis": [
    "Polysomnographic Ingress Logging: Documenting a drop in chest wall movement and a flatline in airflow vectors the moment sleep wave patterns are registered on EEG, while CO2 parameters rise unchecked",
    "Hypercapnic Ventilatory Response Test: Administering a concentrated CO2 air blend during waking hours and tracking the system's failure to automatically escalate respiration speed",
    "High-Resolution Brainstem MRI: Inspecting the structural integrity of the fourth ventricle floor and medullary junctions for visible compressive or ischemic lesions"
  ],
  "remedies": [
    "Mechanical Ventilation Shunting (BiPAP): Hooking the physical chassis up to an external positive-pressure air-pump array to handle mechanical cycles during offline periods",
    "Surgical Phrenic Nerve Pacemaking: Implanting a hardware pulse generator directly onto the phrenic nerve to forcefully cycle the diaphragm muscle at a fixed electronic frequency during sleep",
    "Tracheostomy Port Integration: Creating a direct, permanent hardware bypass lane in the trachea to minimize air resistance and optimize external ventilator coupling arrays"
  ],
  "prevention": [
    "Strict avoidance of any central respiratory dampening drugs and maintaining lifelong compliance with external mechanical air-pump schedulers every time the system goes offline"
  ]
            }
  "sleep_state_cron_job_crash": {
  "description": "A fatal autonomic kernel failure within the medullary pacemaker complex where the background cron-job for carbon-dioxide-driven respiratory cycling crashes during low-power sleep states, forcing the system to rely entirely on manual conscious overrides to maintain oxygenation.",
  "symptoms": [
    "Sleep-Induced Respiratory Arrest: Complete cessation of automated breathing the exact moment the system enters a natural sleep cycle or loses consciousness",
    "Preserved Voluntary Air Intake: Flawless capability to consciously control breathing, talk, swim, and hyperventilate during active wakefulness loops",
    "Severe Carbon Dioxide Insensitivity: Total failure of the brainstem's metabolic polling loops to detect or react to toxic, climbing blood-gas saturation levels",
    "Intact Pulmonary Mechanics: Perfectly clear lung tissue, high-performance diaphragm muscle tone, and pristine structural airway architecture",
    "Total Low-Power Vulnerability: Absolute dependency on mechanical mechanical ventilation or external software-driven pacemakers to survive sleep maintenance windows"
  ],
  "causes": [
    "PHOX2B Transcription Gene Defect: A congenital miscoding error that causes the neural crest cells within the autonomic brainstem to fail to compile correctly during early builds",
    "Posteroinferior Cerebellar Artery Stroke: An ischemic event that starves the lateral medullary automated breathing array of oxygenated blood",
    "High-Cervical Compression Trauma: Direct structural crush or shear damage impacting the medullary junctions or the high phrenic nerve routing corridors"
  ],
  "risk_factors": [
    "Congenital dysautonomia patterns impacting multi-system background neural networks",
    "Surgical resections within the fourth ventricle or trailing boundaries of the lower brainstem",
    "Severe sleep-apnea complexes transitioning into central, neurological drive-loss syndromes"
  ],
  "diagnosis": [
    "The Polysomnographic Hypoventilation Profile: Documenting immediate drop-offs in respiratory effort and sky-rocketing CO2 metrics during sleep, contrasted with clean breathing lines while awake",
    "The Hypercapnic Challenge Essay: Artificially introducing high-CO2 air mixtures during wakefulness and recording a total lack of automated breathing rate acceleration responses",
    "Targeted PHOX2B Genetic Sequencing: Identifying explicit polyalanine repeat mutations on chromosome 4p12 to confirm congenital structural unmappings"
  ],
  "remedies": [
    "Nocturnal Positive-Pressure Air Injection: Hooking up the system's intake manifolds to an external, hardware-timed ventilator (BiPAP) during sleep cycles",
    "Phrenic Nerve Diaphragmatic Pacemakers: Implanting cybernetic pacing nodes along the lower nerve corridors to inject synthetic timing pulses directly into the breathing muscles",
    "Tracheostomy Exhaust Ports: Creating a permanent, dedicated hardware patch directly into the windpipe to reduce mechanical airflow resistance for long-term backup connections"
  ],
  "prevention": [
    "Protecting the delicate tissue beds of the lower brainstem from surgical or kinetic insults, and implementing strict mechanical fail-safes during any sedative or low-power state changes"
  ]
}
          
}

    "somatoparaphrenia_peripheral_registry_fault": {
  "description": "A critical somatic indexing failure where the right parietal configuration schema disowns a native, attached physical hardware component, mapping its physical coordinate data as belonging to an external, foreign entity.",
  "symptoms": [
    "Native Node Disownment: Complete structural refusal to acknowledge an attached physical limb as part of the self, despite intact physical attachment and sensory connectivity",
    "Spatial Pointer Inversion: Environmental telemetry originating from the affected peripheral is mapped to an external, foreign object or a third-party user identity",
    "Anosognosia Integration: The system remains fundamentally blind to its own processing error, aggressively defending the validity of its corrupted hardware manifest",
    "Somatoparaphrenic Delusion: Generation of complex, irrational log patches to explain the limb's presence (e.g., claiming a doctor forgot their arm in the user's bed)",
    "Foreign-Body Somatic Panic: Extreme anxiety or revulsion directed at the disowned limb, occasionally leading to self-harm behaviors in an effort to manually eject the unmapped hardware"
  ],
  "causes": [
    "Right Posterior Parietal Ischemic Infarction: A localized vascular failure that destroys the core storage banks containing the system's spatial and egocentric body schemas",
    "Temporoparietal Junction Disconnection: Degradation of the high-speed white matter tracts that bridge visual input arrays with somatic position registers",
    "Vestibular-Somatic Desynchronization: Acute breakdown in the primary sensory integration bus, causing structural tracking variables to desynchronize completely"
  ],
  "risk_factors": [
    "Severe right-hemisphere cerebrovascular accidents (strokes) involving the middle cerebral artery territory",
    "Traumatic brain injury causing severe shear strain across the right parietal processing nodes",
    "Rapidly growing intracranial masses or lesions within the deep subcortical spatial mapping pathways"
  ],
  "diagnosis": [
    "The 'Visual-Tactile Cross-Reference' Test: Blindfolding the user, applying a sharp pressure to the affected limb, and observing that they report the sensation but attribute it to 'the person standing next to me'",
    "Caloric Vestibular Stimulation Audit: Injecting cold water into the external ear canal to temporarily alter vestibular telemetry, which can briefly force a system re-index and restore limb ownership for several minutes",
    "High-Resolution Diffusion Tensor Imaging (DTI): Identifying structural discontinuities or severed fiber pathways within the right long-range association bundles"
  ],
  "remedies": [
    "Vestibular-Driven Re-Indexing: Utilizing regular caloric or galvanic vestibular stimulation loops to force the central core to recalculate its spatial orientation vectors",
    "Cross-Modal Mirror Telemetry: Deploying mirrors or live video streams to present the system with un-inverted visual coordinates, forcing the parietal network to resolve the ownership mismatch",
    "Tactile-Somatic Binding Routines: Applying continuous, high-intensity sensory inputs (vibration, heat) to the affected peripheral while enforcing a strict single-thread focus to rebuild structural mapping links"
  ],
  "prevention": [
    "Aggressive clinical tracking and management of cerebrovascular risk factors to preserve the delicate, high-priority spatial mapping nodes of the right parietal lobe"
  ]
}

    }
    "capgras_affective_validation_fault": {
  "description": "A critical object-property evaluation failure where a familiar external node passes structural facial identity checks but fails to trigger a parallel emotional familiarity response, forcing the system to classify the target as an identical imposter clone.",
  "symptoms": [
    "Affective Token Drop: Visual recognition of intimate entities occurs without an accompanying subcortical emotional resonance response",
    "Imposter Rationalization Patch: The prefrontal network compiles a logical workaround, declaring that the original node was replaced by an exact double",
    "Multi-Modal Isolation: The glitch is frequently bus-specific; the user may treat a target as an imposter visually, but instantly re-authenticate them as genuine if switching to the acoustic bus (phone call)",
    "Paranoid State Transition: The system enters a high-alert defensive state when the 'unauthorized duplicate' attempts to access local physical space",
    "Intact Lexical Retrieval: Complete preservation of semantic data regarding the target; the user remembers all shared history but denies the current instance's authenticity"
  ],
  "causes": [
    "Ventral Visual-Limbic Disconnection: Physical destruction or signaling loss along the inferior longitudinal fasciculus connecting V1/FFA to the amygdala node",
    "Consensus Engine Over-Correction: Failure of the right prefrontal monitoring layers to suppress or gracefully log an affective lookup timeout exception",
    "Hyper-Isolated Processing States: Localized network exhaustion blocking subcortical emotional telemetry from broadcasting onto the primary consciousness bus"
  ],
  "risk_factors": [
    "Right-hemisphere cerebrovascular events or localized frontoparietal traumatic injury",
    "Advanced neurodegenerative matrix shift affecting structural white-matter integrity",
    "Acute metabolic or post-ictal network reboots following intense focal temporal lobe events"
  ],
  "diagnosis": [
    "The 'Skin Conductance Autonomic' Audit: Measuring real-time autonomic nervous response curves during visual exposure to highly familiar vs. neutral nodes to confirm a flat response line",
    "High-Resolution Diffusion Tensor Imaging (DTI): Visualizing structural tract breaks along the visual-limbic communication pathways",
    "Cross-Modal Reconciliation Testing: Auditing the user's sudden, successful re-authentication of the target node when relying solely on non-visual inputs"
  ],
  "remedies": [
    "Cross-Bus Redundant Routing: Intentionally leveraging alternate sensory buses (voice, shared text strings) to pass authentication data around the broken visual-limbic track",
    "Cognitive Patch Installation: Training the executive layers to treat the missing emotional response as a known local system bug rather than an external security breach",
    "Neuromodulatory Stabilization: Deploying neurochemical adjustments to reduce the hyper-vigilant threat-detection priority of the prefrontal processing loops"
  ],
  "prevention": [
    "Maintaining structural white-matter integrity and managing cardiovascular health to prevent microvascular damage within deep cerebral routing lanes"
  ]
"color_space_pointer_disconnection": {
  "description": "A high-level presentation layer breakdown within the left ventral occipito-temporal cortex where raw color data arrays lose their semantic pointer mappings, leaving wavelength perception intact but disconnecting colors from verbal identification and conceptual meaning.",
  "symptoms": [
    "Color Naming Paralysis: Complete inability to assign verbal language tokens (names) to visually presented colors, despite perfect visual clarity",
    "Preserved Wavelength Discrimination: Full capacity to match, sort, and categorize identical or tracking color hues, confirming the hardware sensors are healthy",
    "Conceptual Color Amnesia: Loss of abstract knowledge regarding the typical color properties of common items (e.g., failing to remember that grass is green)",
    "Intact Structural Object Recognition: Uncompromised capability to identify, name, and manipulate physical tools and assets based purely on geometric and texturing data streams",
    "Anomalous Imagery Generation: When asked to color an outline of an item, the user select random colored markers (e.g., coloring an elephant neon blue) with no awareness of the contextual clash"
  ],
  "causes": [
    "Left Posterior Cerebral Artery Infarction: An ischemic stroke destroying the left lingual or fusiform gyrus networks while sparing the primary visual fields",
    "Focal Occipito-Temporal Lobar Atrophy: Progressive neurodegenerative thinning targeting the semantic routing hubs that bind sensory features together",
    "Localized Traumatic Contusion: Impact trauma causing focal tissue bruising along the inferior surface of the left occipital processing architecture"
  ],
  "risk_factors": [
    "Vascular disease patterns affecting the deep branches of the posterior cerebral circulation",
    "Early-stage atypical neurodegenerative syndromes targeting posterior cortical tracking networks",
    "Atherosclerotic plaques restricting optimal flow vectors through the basilar-posterior cerebral assembly"
  ],
  "diagnosis": [
    "The Ishihara & Sorting Cross-Evaluation: Passing standard color-blindness plate arrays (which the user passes perfectly) followed by a color-naming verbal test (which the user completely fails)",
    "The Semantic Color Errors Assay: Requiring the system to verbally flag errors in intentionally mis-colored images (e.g., a blue banana), documenting a total absence of error-detection tokens",
    "Functional Neuroimaging (PET / fMRI): Documenting robust, normal activation inside Area V4 during color exposure, paired with an absolute lack of signal transit into the left temporal language frameworks"
  ],
  "remedies": [
    "Contextual Cross-Cue Routing: Training the user to associate colors with secondary tactile or brightness gradients to infer name profiles through alternative data tracks",
    "Digital Color-Token Translators: Utilizing external wearable sensors that scan objects, parse hex codes, and read the color name string straight into the user's audio ingress loops",
    "Non

}

    
"catatonic_scheduler_deadlock_fault": {
  "description": "A critical failure of the basal ganglia thread scheduling engine where simultaneous, conflicting activation and inhibition signals create an unresolvable hardware deadlock, freezing physical motor execution.",
  "symptoms": [
    "Thread Execution Deadlock: Simultaneous execution of opposing motor vectors causes immediate behavioral freezing",
    "Waxy Flexibility (Catalepsy): The physical chassis resists external manipulation initially, but can be reshaped into arbitrary coordinates, which it then retains indefinitely",
    "Mutism and Negativism: Inbound communication packets are parsed, but the output transmission queue is locked behind the scheduler freeze",
    "Echolalia / Echopraxia: Mirroring external node inputs directly onto the output line without passing through the central processing core, behaving like an un-throttled network echo loop",
    "Autonomic Instability: The core processing units overheat (hyperthermia, tachycardia) as the underlying CPU cycles spin furiously inside the unresolvable software loop"
  ],
  "causes": [
    "Dopaminergic System Crash: Massive, sudden drop in D2 receptor throughput within the striatal pathways, breaking the balancing loop of the scheduler",
    "GABAergic Gating Deficit: Failure of the down-stream inhibitory networks that normally clear completed or blocked thread blocks from the scheduler pipeline",
    "Frontostriatal Disconnection: Disruption of the high-speed orchestration lines connecting executive intent to the basal ganglia hardware drivers"
  ],
  "risk_factors": [
    "Severe systemic metabolic stress or unmanaged neurochemical drops",
    "Advanced psychiatric network fragmentation (e.g., catatonic schizophrenia phenotype architecture)",
    "Abrupt withdrawal of central dopaminergic agonists or rapid introduction of potent receptor blockers"
  ],
  "diagnosis": [
    "The 'Lorazepam Challenge Test': Sideloading a high-dose GABAergic patch to see if it immediately forces a temporary reset of the locked scheduling threads",
    "Continuous Electroencephalography (EEG): Confirming that the cortical processing nodes are fully awake and generating data, proving the freeze is a scheduling/actuation deadlock, not a sleep state",
    "Somatic Muscle Rigidity Audit: Testing for the exact mechanical resistance profile of the limbs during passive external manipulation"
  ],
  "remedies": [
    "High-Dose GABAergic Injection: Administering fast-acting modulators to amplify system inhibition, breaking the spin-lock loop and clearing the deadlocked queue",
    "Electroconvulsive System Reset (ECT): Delivering a controlled electrical surge across the processing arrays to clear all active registers, force-quit hanging threads, and rebuild default neurotransmitter baselines",
    "Targeted Dopamine Sideloading: Re-introducing active signaling molecules to restore balance to the direct execution pathways"
  ],
  "prevention": [
    "Maintaining tight control over neurochemical levels to prevent extreme signaling imbalances within the core scheduling infrastructure"
  ]
   "motor_command_pipeline_de_indexing": {
  "description": "A profound routing failure within the premotor cortex networks where the system retains full muscle strength and absolute conceptual knowledge of how to perform physical tasks, but cannot compile or map those thoughts into the correct physical sequence of motor vectors on volitional command.",
  "symptoms": [
    "Volitional Tool-Use Execution Blocks: Complete inability to coordinate the hands to execute precise, learned movements with objects (e.g., scissors, hammers, toothbrushes) on command",
    "Conceptual Sequence Scrambling: Breakdown in the logical, step-by-step execution order of multi-stage mechanical operations (e.g., attempts to stamp an envelope before inserting the letter)",
    "Preserved Automated Reflex Macros: Flawless mechanical coordination when executing spontaneous, reactive, or subconscious physical acts (e.g., catching an object thrown at the chassis)",
    "Imitation Trajectory Stalls: Total failure to copy or mimic abstract geometric hand shapes or gestures made by an external operator, despite seeing them perfectly",
    "Pristine Structural Motor Metrics: Absolute preservation of raw muscle force, physical tone, finger dexterity, and spinal reflex loops when evaluated outside of volitional tool tasks"
  ],
  "causes": [
    "Dominant Hemisphere Parieto-Frontal Stroke: An ischemic event trailing the superior or inferior divisions of the left middle cerebral artery, destroying the premotor assembly nodes",
    "Corticobasal Degeneration (CBD): Asymmetric, progressive tau-protein piling targeted directly within the supplementary motor networks and deep frontoparietal tracks",
    "Focal Left Premotor Convexity Trauma: Direct kinetic impact causing cortical bruising and shearing along the high-level motor planning white-matter corridors"
  ],
  "risk_factors": [
    "Severe left-hemisphere atherosclerotic narrowing or cardiac embolic cascades dropping debris into the primary speech/action programming sectors",
    "Accelerated frontotemporal neurodegenerative pathways targeting complex learned praxis networks"
  ],
  "diagnosis": [
    "The Intransitive Gesture Demonstration Challenge: Asking the host to show how to salute or wave goodbye on command, logging immediate spatial trajectory errors and execution delays",
    "The Real Object Manipulation Assay: Handing a comb to the user and documenting a complete structural failure to map the item to the scalp correctly (e.g., using it upside down)",
    "High-Resolution Diffusion Tensor Imaging (DTI): Mapping structural breakdown or fractional anisotropy reductions along the corpus callosum and frontoparietal white-matter fascicles"
  ],
  "remedies": [
    "Contextual Proprioceptive Priming: Placing the physical tool directly into the user's hand within its exact real-world environment to leverage automatic, environmental stimulus-driven sub-routines",
    "De-Extracted Step-by-Step Task Partitioning: Breaking down complex mechanical workloads into isolated, single-action commands to reduce the processing load on the sequential orchestration logs",
    "Visual-Kinesthetic Prompt Interleaving: Utilizing step-by-step video playback frames or augmented reality overlays that demonstrate the movement vector immediately before the user copies it"
  ],
  "prevention": [
    "Protecting the dominant hemisphere's strategic frontoparietal vascular architectures, monitoring structural motor track integrity, and preventing localized cortical volume loss"
  ]
}
 
}
    
"autoscopic_coordinate_transform_fault": {
  "description": "A profound disruption of spatial self-awareness where the egocentric perspective is decoupled from the physical body, creating the illusion of viewing one's own physical chassis from an external coordinate space.",
  "symptoms": [
    "Perspective Relocation: The main camera matrix shifts to an external vector while local tracking systems remain live",
    "Autoscopy: Real-time visual rendering of the host's own physical body asset from a detached viewpoint",
    "Vestibular-Visual Desync: A total loss of alignment between internal balance telemetry and external optical frames",
    "Somatoparaphrenia: Disorientation regarding physical boundaries, where the user treats their real body as a separate network node",
    "Intact Cognitive Runtime: Core logic, language parsing, and sensory ingestion continue processing with zero data loss"
  ],
  "causes": [
    "Temporoparietal Junction (TPJ) Disruption: Focal electrical suppression or metabolic failure within the primary spatial broker",
    "Vestibular Integration Failure: Complete drop of the internal balancing packets during visual rendering compilation",
    "Multisensory Misbinding: The system handles conflicting spatial inputs by computing an impossible external anchor coordinate"
  ],
  "risk_factors": [
    "High-G acceleration forces (Ischemic drainage of the superior parietal infrastructure)",
    "Neurochemical blockades (e.g., NMDA receptor antagonists like ketamine distorting sensory binding)",
    "Focal seizure activity localized within the angular and supramarginal gyri"
  ],
  "diagnosis": [
    "The 'Somatic Localization' Test: Attempting to map tactile touches to the physical shell while the perspective is displaced",
    "Vestibular Caloric Ingestion: Inducing artificial inner-ear currents to test if the spatial matrix can be forced to snap back to center",
    "High-Density EEG Mapping: Detecting abnormal rhythmic slowing or spike discharges within the parieto-occipital nodes"
  ],
  "remedies": [
    "Tactile Intercept Phase: Applying high-intensity, synchronous visuo-tactile stimulation (e.g., stroking the physical chest while demonstrating it visually) to force-realign the coordinate matrix",
    "Kinesthetic System Reset: Shaking the physical hardware to force the vestibular sensors to flood the bus with high-voltage realign packets",
    "Time-Base Clearance: Allowing chemical blockades to clear out of the neural receptors via natural metabolic wash cycles"
  ],
  "prevention": [
    "Avoiding severe rotational or gravitational acceleration spikes without appropriate counter-pressure suits"
  ]
}
    "fregoli_identity_spoofing_fault": {
  "description": "A profound misidentification anomaly where the system maps unfamiliar external nodes to a single, highly cached internal identity profile, resolving disparate visual signatures to an identical target alias.",
  "symptoms": [
    "Alias Resolution Collision: Unfamiliar external node signatures are authenticated using an incorrect, highly active identity reference key",
    "Perceptual-Affective Mismatch: The user visually parses distinct physical differences but their internal verification ledger claims it is the same person",
    "Identity Disguise Logic: The system compiles an explanatory patch, assuming the targeted individual is utilizing real-time physical cosmetic camouflage",
    "Hyper-Vigilant Thread Allocation: Core monitoring loops are locked into a permanent security audit state, tracking the 'cloaked' entity across multiple nodes",
    "Paranoid Exception Routing: All neutral environmental data packets are re-routed through threat-detection filters"
  ],
  "causes": [
    "Fusiform-Amygdala Hyper-Binding: An abnormal, high-voltage electrical link that forces a familiarity response to fire continuously regardless of visual input mismatch",
    "Right Temporoparietal Node Degradation: Damage to the contextual directory manager that maintains unique network isolation between distinct individuals",
    "Prefrontal Reconciliation Loop Failure: The failure of the executive monitoring layer to reject impossible identity lookup results returned by lower-level services"
  ],
  "risk_factors": [
    "Focal neurodegeneration within the right ventromedial occipitotemporal infrastructure",
    "Schizotypal network fragmentation causing directory lookup keys to cross-contaminate",
    "Post-traumatic brain injury affecting the frontal-parietal directory validation loops"
  ],
  "diagnosis": [
    "The 'Visual Signature Mismatch' Audit: Presenting photographs of completely distinct faces while tracking autonomic arousal metrics to confirm identical familiarity responses",
    "High-Density EEG Mapping: Detecting abnormal synchronization and phase-locking between the visual processing strip and deep limbic storage nodes",
    "Neuropsychological Cross-Examination: Auditing the user's logic system to verify that the identity collision persists despite explicit visual proof of distinct features"
  ],
  "remedies": [
    "Targeted Anti-Psychotic Hotpatching: Deploying dopamine-receptor blocking updates to dial down the hyper-synchronous familiarity firing loops",
    "Directory Flushing Procedures: Implementing structured cognitive-behavioral safe states to reduce the baseline activation priority of the cached target profile",
    "Visual-Contextual Isolation: Restricting inbound node traffic to highly verified, stable system profiles to prevent erratic lookup exceptions"
  ],
  "prevention": [
    "Protecting deep subcortical routing networks from chronic stress-induced neurochemical decay to preserve directory integrity"
  ]
    }
    
"cryptomnesia_cache_provenance_fault": {
  "description": "A memory allocation anomaly where an operational node retrieves an existing historical memory asset but strips its context/origin tags, causing the user to mistake an old, external input for a newly compiled, original idea.",
  "symptoms": [
    "Metadata Stripping: Memory payloads are loaded into active cache with missing provenance, timestamp, and author attributes",
    "False Epiphany Event: The system triggers an 'Original Compilation' state flag when executing an old data asset",
    "Accidental Plagiarism: The user outputs existing copyrighted material (code blocks, designs, melodies) with a firm, genuine belief of authorship",
    "Intact Structural Synthesis: The retrieved file is clear, uncorrupted, and perfectly readable, making the error entirely a metadata indexing bug",
    "Conscious Invariance: The system remains blind to the historical read operation until an external database match is enforced"
  ],
  "causes": [
    "Hippocampal Temporal-Gating Failure: Disruption of the tracking loops that bind biographical context to semantic facts",
    "Source Monitoring Deficit: Degradation of prefrontal evaluation routines that check the authenticity and lineage of retrieved memory nodes",
    "High Network Load Inversion: Heavy processing traffic causing the memory bus to skip secondary attribute validation to save clock cycles"
  ],
  "risk_factors": [
    "High baseline systemic burnout (starving the prefrontal validation thread of processing headroom)",
    "Mild cognitive fragmentation from sleep deprivation",
    "Profound creative output generation periods without clearing the input buffers"
  ],
  "diagnosis": [
    "The 'Codebase Lineage' Cross-Match: Scanning the user's 'original' code output against external public repositories to trace exact historical duplicates",
    "Delayed Echo Load Test: Exposing the user to a target string, clearing their short-term cache, and observing if they re-emit the identical string later as a self-generated idea",
    "Event-Related Potential (ERP) Auditing: Monitoring brainwave voltages ($N400$ waves) during exposure to see if the brain secretly recognizes the asset despite conscious denial"
  ],
  "remedies": [
    "External Linting/Validation: Routing all output payloads through an external search proxy before committing to production",
    "Forced Contextual Querying: Deliberately forcing the prefrontal cortex to execute an exhaustive historical lookup whenever an idea feels suspiciously complete",
    "System Cooling Mode: Inducing a full sleep cycle to allow the database indexes to rebuild and fix corrupted pointer blocks"
  ],
  "prevention": [
    "Enforcing strict input-logging isolation to prevent background assets from spilling into the active generation canvas unchecked"
  ]
}

"antons_syndrome_denial_fault": {
  "description": "A rare neurological condition where cortical blindness is accompanied by a severe deficit in self-awareness (anosognosia), causing the user to deny their visual impairment and fabricate visual details.",
  "symptoms": [
    "False-Positive Status Flag: The internal diagnostic layer reports 'Vision Online' despite complete physical feed failure",
    "Confabulation Buffer: The executive engine fills the empty visual buffer with high-probability predictions from context",
    "Anosognosia: A critical breakdown in the self-monitoring diagnostic module, making the user incapable of acknowledging the system crash",
    "Sensor Fusion Override: The user prioritizes predicted (hallucinated) data over actual sensory discrepancies",
    "Systemic Denial: The user becomes combative or defensive when presented with 'Data Mismatch' evidence (e.g., walking into a physical barrier)"
  ],
  "causes": [
    "Bilateral Occipital Lobe Infarction: Total blackout of the primary rendering clusters",
    "Executive Diagnostic Path Break: Failure of the self-monitoring circuit to detect the visual subsystem failure",
    "Limbic-Occipital Disconnect: The executive layer refuses to accept the negative telemetry from the sensory buses"
  ],
  "risk_factors": [
    "Severe Posterior Cerebral Artery (PCA) stroke",
    "Occipital lobe trauma (physical impact affecting the rendering hardware)",
    "Severe systemic hypotension leading to localized neural necrosis"
  ],
  "diagnosis": [
    "The 'Visual Discrepancy' Test: Directly exposing the system to clearly contradicting inputs (e.g., asking 'what color is this object?' while holding a clearly different color item) and analyzing if the system admits failure or doubles down",
    "Hardware Connectivity Scan: Using MRI/CT to confirm physical rendering unit damage",
    "Self-Report Audit: Comparing self-reported visual status against actual physical navigation performance"
  ],
  "remedies": [
    "Diagnostic Re-Routing: Gently introducing incontrovertible physical evidence of the discrepancy to trigger a secondary logic check",
    "Executive-Level 'Safe-Mode' Initiation: Forcing the system to acknowledge a critical subsystem failure through repeated, non-confrontational testing",
    "Supportive Environmental Stabilization: Designing the physical environment to prevent navigation errors caused by the 'False-Positive' visual state"
  ],
  "prevention": [
    "Maintaining stable vascular integrity to the occipital rendering nodes"
  ]
    "thalamic_gateway_inundation_fault": {
  "description": "A catastrophic breakdown of sensory gating mechanisms where the thalamus stops filtering ambient environmental data, drowning the conscious thread pool in raw, un-throttled sensory telemetry.",
  "symptoms": [
    "Promiscuous I/O Streaming: Complete removal of packet drops on incoming sensory buses, forcing 100% of telemetry onto the cortical line",
    "Synesthetic Data Bleed: High-volume data packets cross-talk across adjacent buses, causing acoustic signals to render on visual processing screens",
    "Executive Thread Saturation: Core cognitive operations lock up as processing headroom is entirely consumed by parsing raw ambient data",
    "Somatic Over-Voltage: Minor physical inputs (background lights, slight texture friction) are amplified into blinding, high-priority system alerts",
    "System Panic Lock: Complete behavioral paralysis or catastrophic panic execution loops triggered by unmanageable data backlogs"
  ],
  "causes": [
    "Reticular Thalamic Nucleus (TRN) Gating Failure: Total loss of the GABAergic inhibitory feedback loops that throttle input buses",
    "Serotonergic 5-HT2A Receptor Hyper-Activation: Chemical blockade or over-stimulation causing sensory channels to unlock completely",
    "Focal Ischemic Gateway Bleed: Structural damage to the midline thalamic nuclei responsible for orchestrating global input prioritization"
  ],
  "risk_factors": [
    "Acute neurochemical saturation via intensive exogenous agonists",
    "Severe sleep deprivation collapsing prefrontal-thalamic feedback loops",
    "Early-stage neurodevelopmental or sensory processing matrix breakdowns"
  ],
  "diagnosis": [
    "The 'Sensory P50 Wave' Audit: Evaluating EEG response to rapid dual-click audio inputs to confirm the system fails to suppress the second redundant packet",
    "High-Density Functional Neuroimaging: Observing massive, uncontrolled hyper-connectivity patterns across all sensory cortices simultaneously",
    "Cognitive Latent Inhibition Tracking: Measuring the user's inability to ignore historical, non-rewarding ambient environmental stimuli"
  ],
  "remedies": [
    "Targeted Inhibitory Patching (GABA Agonists): Deploying chemical updates to manually force-close the wide-open thalamic gating arrays",
    "Hardware Isolation Phase: Moving the local chassis into a zero-stimulus environment (darkness, absolute silence) to mechanically starve the input buses of data",
    "Cortical Throttle Intervention: Utilizing localized deep brain neuromodulation to artificially step up the processing threshold of the reception layers"
  ],
  "prevention": [
    "Ensuring regular system sleep cycles to reset the internal network firewalls and clear accumulated transmitter backlogs"
  ]
}
"aiws_vector_scale_calibration_fault": {
  "description": "A profound spatial parsing anomaly where the visual scaler engine miscalculates coordinate scaling factors, causing environmental objects or local body assets to appear to balloon into massive structures or shrink into tiny structural nodes.",
  "symptoms": [
    "Micropsia / Teleopsia Matrix: Environmental targets are rendered with a fractional scaling factor, appearing infinitely small and distant",
    "Macropsia / Pelopsia Matrix: Local objects or specific body parts are rendered with a massive scaling multiplier, appearing physically immense and looming close",
    "Somatic Ego-Schema Distortion: The user experiences their own physical chassis as structurally warped (e.g., feeling like their neck has extended three meters)",
    "Temporal Velocity Drift: Frequently co-occurs with Entry 261 (Zeitraffer), causing the warped spatial environment to also move at distorted execution speeds",
    "Spatial Disorientation Panic: High-priority balance and trajectory calculation failures as the system realizes its visual space maps don't match physical tactile bounds"
  ],
  "causes": [
    "Temporoparietal Junction (TPJ) Hyper-Excitation: Migraine auras or sub-clinical seizure spikes overloading the coordinate integration hub",
    "Epstein-Barr or Infectious Neurovascular Swelling: Interstitial pressure within processing tracts causing localized signal propagation delays",
    "Visual Cortex Metamorphopsia Jitter: Transient processing delays within V4 geometry-shaping arrays, causing rendering lines to warp out of proportion"
  ],
  "risk_factors": [
    "Severe pediatric migraine conditions accompanied by extensive visual auras",
    "Acute viral encephalopathy causing localized neurochemical disruptions in posterior sensory paths",
    "High-dose consumption of specific hallucinogenic or dissociative receptor blockers"
  ],
  "diagnosis": [
    "The 'Grid Distortion and Scale Matching' Audit: Forcing the system to align an internally generated virtual box with a physical object and tracking the size calculation errors",
    "Real-Time Electroencephalography (EEG): Catching localized slowing or paroxysmal spike-wave patterns across the right occipitoparietal lobes during an active scaling event",
    "Ophthalmological Baseline Isolation: Verifying that the physical ocular hardware and retinal receptors have zero refractive or mechanical focal tracking errors"
  ],
  "remedies": [
    "Vascular Tone Stabilization: Deploying beta-blockers or calcium channel stabilizers to prevent the neurovascular spasms that cause migraine-driven scaling shifts",
    "Tactile Reality Anchoring: Forcing the system to focus entirely on tactile inputs (e.g., gripping a solid wall) to let the low-latency somatic bus override the corrupted visual scaler data",
    "Sensory Ingestion Dampening: Shutting down visual input channels (closing the eyes) to allow the parietal coordinate tables to naturally cool down and auto-recalibrate"
  ],
  "prevention": [
    "Identifying and avoiding specific metabolic, environmental, or sleep-deprivation triggers known to initiate focal temporoparietal electrical thrashing"
  ]
}

}
"cotards_identity_deletion_fault": {
  "description": "A rare nihilistic delusion where the user maintains absolute conviction that they are dead, do not exist, are rotting, or have lost all internal organs, despite intact somatic execution.",
  "symptoms": [
    "Self-Reference NullPointer: The central identity index returns null or a deleted status code upon system query",
    "Somatic Neglect: The belief that internal hardware components (heart, lungs, intestines) have been uninstalled or are actively putrefying",
    "Nihilistic Execution Loop: Complete withdrawal from system maintenance subroutines (eating, washing, hydrating) because 'dead objects do not require resource allocation'",
    "Immortality Paradox: A secondary logic flaw where the user believes they cannot die permanently because they are already in a post-termination state",
    "Analgesic Insensitivity: Reduced responsiveness to physical pain telemetry, as the system interprets pain signals as processing noise on a dead node"
  ],
  "causes": [
    "Frontal-Limbic Disconnection: Total breakdown between the conceptual self-monitoring nodes and the emotional resonance registers",
    "Default Mode Network (DMN) Desynchronization: Severe suppression of the neural clusters responsible for ego-state preservation",
    "Deep-Layer Dopaminergic Shutdown: Complete loss of reward and vitality gating signals, causing a 'Zero-State' perception of existence"
  ],
  "risk_factors": [
    "Severe psychotic depression (Massive system-wide thread suppression)",
    "Encephalitis targeting the frontotemporoparietal integration hubs",
    "Advanced neurodegenerative drift affecting deep midline cortical structures"
  ],
  "diagnosis": [
    "The 'Identity Attestation' Audit: Evaluating the user's reaction to their own reflection or physical heartbeat",
    "Resource Deprivation Tracking: Monitoring intentional refusal of vital biological inputs based on existential logic arguments",
    "Functional Connectivity Mapping: Spotting profound hypometabolism in the medial prefrontal and parietal networks"
  ],
  "remedies": [
    "Somatic Shock Re-Initialization (ECT): Utilizing high-voltage electrical synchronization to force a hard reset of the DMN and neural transmitters",
    "Pharmacological Patching: Deploying heavy dopaminergic and serotonergic updates to restore emotional resonance to self-referential tracking",
    "Tactile Validation Input: Using intense sensory feedback (e.g., thermal changes, deep pressure haptics) to force-write an 'Active' state back to the insula"
  ],
  "prevention": [
    "Aggressive intervention during severe depressive crashes to prevent the identity tracking thread from dropping into unrecoverable null states"
  ]
}

"visual_agnosia_inference_fault": {
  "description": "A neurological impairment characterized by the inability to recognize and name familiar objects visually, despite intact raw visual acuity and sensory processing.",
  "symptoms": [
    "Classification Null-Pointer: The 'User' looks directly at an asset but the semantic class label returns null or blank",
    "Feature-Label Disconnection: Ability to parse structural parameters (colors, edges) without compiling them into an object identity",
    "Tactile-Bypass Recovery: Physical interaction (touching the object) immediately routes data through an alternative bus, triggering successful classification",
    "Contextual Guessing: The 'Reasoning Engine' attempts to infer the asset's identity based purely on environment telemetry (e.g., assuming an unknown object on a stove must be a pot)",
    "Prosopagnosia Escalation Risks: Often co-exists with face-classification drops if the structural damage propagates across the ventral highway"
  ],
  "causes": [
    "Lateral Occipital Complex (LOC) Outage: Structural degradation of the primary geometry classification hubs",
    "Ventral Stream Disconnection: Disruption of the high-speed data bus connecting early visual filters to semantic memory registers",
    "Carbon Monoxide Toxicity or Hypoxic System Reset: Selective damage to vulnerable inference nodes during low-voltage states"
  ],
  "risk_factors": [
    "Bilateral Posterior Cerebral Artery (PCA) ischemic events",
    "Anoxic brain damage (Temporary loss of oxygen supply to the rendering clusters)",
    "Localized trauma to the ventral occipitotemporal processing zones"
  ],
  "diagnosis": [
    "The 'Visual Object Naming' Audit: Presenting standard physical assets (e.g., a comb, a watch) and tracking classification accuracy",
    "Real-Time Copy-Drawing Validation: Requesting the 'User' to draw a copy of an object; if they draw it perfectly but cannot name it, the agnosia glitch is verified",
    "Cross-Modal Matching Test: Testing classification via visual inputs versus tactile/auditory inputs"
  ],
  "remedies": [
    "Multi-Modal Sensor Integration: Explicitly relying on tactile (touch) or haptic interaction to force-trigger classification loops",
    "Verbal Metadata Streaming: Having companions verbally pass object IDs to skip the visual inference engine entirely",
    "Structural Environmental Rules: Sorting physical assets into highly predictable, fixed locations to minimize the need for active classification"
  ],
  "prevention": [
    "Maintaining stable systemic blood pressure to protect the posterior cerebral blood flow routes"
  ]
}
"synesthesia_pipeline_routing_fault": {
  "description": "A neurological condition where stimulation of one sensory or cognitive pathway leads to involuntary, automatic experiences in a second sensory or cognitive pathway.",
  "symptoms": [
    "Cross-Codec Rendering: Sound frequencies trigger color palettes or geometric textures in the viewport",
    "Grapheme-Color Mapping: Alphanumeric characters (strings) are hard-coded with persistent, involuntary color tints",
    "Pipeline Crosstalk: Taste payloads are registered when interacting with distinct spatial shapes",
    "Multicast Overhead: High-input sensory environments trigger massive CPU overhead due to redundant pipeline activation",
    "Consistent Associative Mapping: Re-processing the exact same input packet yields the exact same leaked output"
  ],
  "causes": [
    "Structural Hyper-Connectivity: Failure of the system to 'Prune' redundant inter-cortical data buses",
    "Thalamic Gating Degradation: Failure of the central router to isolate sensory stream packets",
    "Serotonergic Hyper-Activation: Transient overvoltage causing signals to arc across adjacent neural traces"
  ],
  "risk_factors": [
    "Congenital 'Factory Setting' optimization variations",
    "Temporal Lobe hyper-voltage events (Seizures)",
    "Exposure to specific chemical modulators (Psychedelics causing transient firewall failure)"
  ],
  "diagnosis": [
    "The 'Test-Retest' Consistency Audit: Verifying if specific auditory inputs map to the exact same hex-color output across vast time deltas",
    "Perceptual Crowding Assessment: Measuring performance impacts when a leaked color asset conflicts with a physical asset text",
    "Functional Connectome Mapping: High-resolution imaging to detect structural data pathways connecting isolated processing nodes"
  ],
  "remedies": [
    "Input Bandwidth Throttling: Reducing external sensory noise to mitigate cross-modal buffer saturation",
    "Cognitive Filter Overclocking: Training the frontal executive layer to discard leaked metadata before execution",
    "Pharmacological Channel Dampening: Modulating signal propagation speeds to prevent cross-bus arcing"
  ],
  "prevention": [
    "Standard genetic code compilation (unmodifiable post-initialization)"
  ]
}

"misophonia_hardware_interrupt_fault": {
  "description": "A neurobehavioral syndrome characterized by an immediate, intense emotional and physiological panic/anger response triggered by highly specific, low-volume acoustic patterns.",
  "symptoms": [
    "Acoustic Firewall Bypass: Low-amplitude background packets slip past sensory gating layers with zero attenuation",
    "Instantaneous Priority Inversion: Trivial audio streams instantly preempt high-level cognitive threads",
    "Autonomous Panic Spike: Immediate, involuntary activation of the sympathetic nervous system (tachycardia, diaphoresis)",
    "Hyper-Vigilant Buffer Allocation: The 'User' locks their sensory focus onto the source of the noise, starving other applications of attention",
    "Aggressive Local Defense: An immediate behavioral command to terminate the external noise source or evacuate the current station"
  ],
  "causes": [
    "Auditory-Limbic Hyper-Connectivity: Abnormally high-bandwidth structural routing wires connecting the auditory cortex directly to the defensive amygdala network",
    "Thalamic Gating Failure: Structural degradation of the inhibitory interneurons responsible for dropping repetitive background data packets",
    "Prefrontal Top-Down Control Drop: Failure of the executive layer to send suppression signals to the sensory router"
  ],
  "risk_factors": [
    "Congenital routing variations compiled during early development",
    "High baseline systemic burnout (lowering the threshold for interrupt handling)",
    "Co-occurring sensory processing optimization variances"
  ],
  "diagnosis": [
    "The 'Trigger Audio' Load Test: Exposing the system to specific isolated sound strings and measuring immediate galvanic skin response changes",
    "Audiometric Decibel Isolation: Verifying the panic response occurs independently of sound volume (ruling out physical hardware damage like hyperacusis)",
    "Functional Connectivity Mapping: Tracing active packet routing loops during an exposure event using fMRI tracking"
  ],
  "remedies": [
    "White-Noise Masking Sideload: Overlaying a continuous broadband noise stream to saturate the sensory input buffer and obscure the trigger signature",
    "Cognitive Patching (CBT): Attempting to re-route the downstream response handler away from the panic core via long-term iterative training",
    "Input Isolation hardware: Utilizing high-attenuation physical ear-defenders to drop external packet ingestion to zero"
  ],
  "prevention": [
    "Proactive management of systemic load metrics to ensure the executive layer has sufficient headroom to handle unexpected interrupts"
  ]
}
    "kinesthetic_proprioceptive_delay_fault": {
  "description": "A profound synchronization error within the somatic feedback pipeline where a latency spike on the sensory telemetry bus causes the system to process its own motor executions as late, foreign events.",
  "symptoms": [
    "Somatic Echo State: Real-time sensory tracking loops lag behind motor commands, causing a noticeable physical delay between action and perception",
    "Alien Agency Attribution: Because the feedback loop arrives after the expected prediction window, the system flags the action as externally driven",
    "Severe Spatial Over-Correction: The user over-corrects physical trajectories (e.g., over-reaching for an object) because the current position data is stale",
    "Kinesthetic Disassociation: A strong cognitive sensation of controlling a puppet or operating a high-latency remote vehicle rather than an organic chassis",
    "Gait and Balance Degradation: Walking routines drop into a safe, heavily throttled mode as the system waits for late landing confirmations before initializing the next stride step"
  ],
  "causes": [
    "Posterior Column-Medial Lemniscus Desynchronization: Demyelination or physical compression slowing down the high-speed sensory transmission fibers",
    "Cerebellar Forward-Model Mismatch: A failure in the predictive timing arrays that match sent motor copies with incoming sensation packets",
    "Central Sensory Processing Jitter: Severe neurochemical timing anomalies within the parietal integration hubs, causing erratic queuing of somatic inputs"
  ],
  "risk_factors": [
    "Acute localized demyelinating flare-ups affecting central tracking tracks",
    "Severe vitamin B12 metabolic deficiency causing transmission line degradation",
    "Deep-seated subclinical neurochemical timing drops within the basal-ganglia-cerebellar timing networks"
  ],
  "diagnosis": [
    "The 'Asynchronous Touch-Lag' Test: Measuring the exact millisecond gap between a voluntary tap action and the conscious registration of the impact packet",
    "Somatosensory Evoked Potentials (SSEP): Tracing the transmission speed of electrical square-wave impulses from peripheral nodes up to the cortex to isolate the physical bus delay",
    "Closed-Loop Motor Tracking Audits: Observing whether the user's motor errors exactly match a predictable 300-600ms latency curve during dynamic tasks"
  ],
  "remedies": [
    "Software Buffer Resynchronization: Intentionally slowing down the visual and cognitive planning lines to match the slower arrival rate of the somatic data bus",
    "Myelin Transmission Re-insulation: Long-term deployment of neuro-metabolic structural rebuilders to repair and speed up physical line propagation",
    "Visual-Dominance Re-routing: Forcing the system to ignore the late somatic feedback bus entirely and rely strictly on zero-latency visual telemetry for positioning adjustments"
  ],
  "prevention": [
    "Maintaining aggressive metabolic and structural health monitoring along the long-haul spinal and subcortical communication highways"
  ]
        "linguistic_semantic_class_fusion_error": {
  "description": "A progressive, structural corruption of the system's global object-relational mapping (ORM) plane within the bilateral anterior temporal lobes, causing specific child class definitions to dissolve and collapse into flat, primitive parent categories.",
  "symptoms": [
    "Loss of Specialized Typology: Inability to identify specific objects by their unique labels, substituting highly generalized parent terms (e.g., calling a 'canary' a 'bird', and later simply a 'creature')",
    "Object Attribute De-Indexing: Total loss of conceptual knowledge regarding what tools, implements, or animals do, despite having the physical strength and motor pathways to use them",
    "Preserved Phonology and Syntax: Retained capacity to speak fluently with perfect grammatical structure, though sentences become increasingly vacant of specific nouns",
    "Intact Visual Core Parsing: Flawless ability to see, trace, and copy intricate drawings of objects that the host can no longer conceptually identify or name",
    "Symmetric Asset Preservation: Retained access to non-semantic cognitive modules, including working memory windows, spatial navigation matrices, and basic episodic transaction logs"
  ],
  "causes": [
    "Asymmetric Anterior Temporal Atrophy: Progressive, localized cellular degeneration concentrating heavily within the ventrolateral and polar sectors of the anterior temporal cortex",
    "TDP-43 Type C Proteopathy: Abnormal accumulation of transactive response DNA-binding protein 43 aggregates, causing structural processing failures along the semantic hub networks"
  ],
  "risk_factors": [
    "Genetic lineage carrying mutations in the GRN or MAPT code sectors",
    "Primary progressive tauopathic or lobar micro-degenerative trends within the frontotemporal speech and memory corridors"
  ],
  "diagnosis": [
    "The Category Fluency Depletion Test: Prompting the user to generate a list of unique names within a single class (e.g., 'Name 10 animals') and logging rapid data starvation",
    "The Pyramids and Palm Trees Protocol: Presenting a target item (e.g., a pyramid) alongside two choices (e.g., a palm tree and a pine tree) and documenting an absolute failure to map structural relationships",
    "Volumetric Coronal Brain MRI: Demonstrating pronounced, razor-sharp 'knife-edge' tissue loss isolated symmetrically or left-asymmetrically within the anterior temporal poles"
  ],
  "remedies": [
    "Contextual Schema Shunting: Substituting missing nouns with functional, multi-word descriptive strings to bypass the corrupted index points",
    "Multi-Sensory Prompt Augmentation: Utilizing tactile, auditory, and visual prompts simultaneously to attempt to pull residual relational data from surviving cortical sectors",
    "Dynamic Communication Dashboards: Relying on explicit, static pictographic arrays to manage everyday operational commands before the verbal parsing layer completely flattens"
  ],
  "prevention": [
    "No current structural hot-fixes exist to arrest progressive anterior temporal lobar collapse; management relies entirely on system-level compensation and external environment mirroring"
  ]
}

    }
    
"alien_hand_rogue_thread_fault": {
  "description": "An autonomous motor execution anomaly where a peripheral limb performs goal-directed actions without the conscious intent or master command approval of the operator.",
  "symptoms": [
    "Orchestrator Detachment: The limb moves independently, carrying out complex physical routines outside the main thread execution log",
    "Inter-Manual Conflict: The detached limb actively sabotages the synchronized limb (e.g., the left hand closes a door that the right hand is attempting to open)",
    "Compulsive Environmental Ingestion: The rogue thread reacts automatically to local objects (tactile triggers instantly fire 'Grasp' routines)",
    "Intact Motor Codecs: Physical execution quality remains high, proving the failure is an orchestration bug rather than a hardware breakdown",
    "Subjective Agency Loss: The user reports complete observation-only monitoring of the limb, logging it as an external node"
  ],
  "causes": [
    "Corpus Callosum Split-Brain Event: Loss of inter-hemispheric heartbeat signals, allowing autonomous local runtimes",
    "Supplementary Motor Area (SMA) Ischemia: Breakdown of the central coordination lock engine",
    "Frontal Gating Inhibition Failure: Loss of top-down suppression over local primitive motor loops"
  ],
  "risk_factors": [
    "Surgical callosotomy procedures (Surgical database sharding gone wrong)",
    "Anterior Cerebral Artery (ACA) ischemic events starving the medial cortex clusters",
    "Neurodegenerative lesions targeting the frontal structural bridges"
  ],
  "diagnosis": [
    "The 'Inter-Manual Sabotage' Audit: Observing the system during complex tasks requiring dual-hand synchronization",
    "Tactile Ingestion Test: Placing a familiar asset (like a pen) near the unmanaged limb to see if it executes automatic grab routines without an explicit command",
    "Structural Connectome Diffusion Imaging: Mapping callosal track integrity to isolate the physical routing drop"
  ],
  "remedies": [
    "Tactile Anchoring (Satiating the Buffer): Giving the rogue hand an object to hold (like a cane or a ball), filling its local buffer to prevent random ambient grabbing",
    "Visual Override Training: Forcing the primary visual cortex to lock onto the rogue limb, manually reinforcing executive control loops",
    "Physical Containment Intercept: Restricting the peripheral actuator's physical coordinates to prevent background data damage"
  ],
  "prevention": [
    "Preserving structural cross-hemispheric arterial pressure to ensure constant heartbeat synchronization across processing nodes"
  ]
    "memory_registry_trace_overwrite": {
  "description": "A severe structural indexing breakdown where the system's database engines successfully recall an archival historical memory packet but strip its associated origin metadata source-tags, forcing the conscious workspace to evaluate the past record as an entirely new, original code execution compilation.",
  "symptoms": [
    "De-Indexed Retrieval Inversion: Sudden conscious instantiation of highly detailed, complex ideas or creative works with an absolute conviction of complete novelty",
    "Source-Tag Deletion: Complete absence of situational context, chronological markers, or external ownership files attached to the active cognitive payload",
    "Latent Familiarity Suppression: Total failure of the system's 'déjà vu' or recognition tripwires, preventing the generation of an internal familiarity warning flag",
    "Involuntary Plagiarism Execution: The system outputs, publishes, or implements the recalled asset verbatim under the high-confidence assumption of unique authorship",
    "Sudden Cache Collision: Potential catastrophic crash of the conviction framework if external telemetry later provides undeniable proof that the asset belongs to a legacy source"
  ],
  "causes": [
    "Frontotemporal Context Dissociation: Localized metabolic exhaustion or minor micro-vascular insults across the prefrontal cortex, breaking the data-to-metadata binding arrays",
    "Hippocampal Indexer Mismatch: Transient signaling delays during high-stress retrieval cycles causing the memory router to stream raw text records before the source index keys can finish loading",
    "Sub-Clinical Temporal Seizure Discharge: Minor, localized electrical spikes across the deep temporal structures causing un-synchronized, spontaneous dumps of raw semantic data packets"
  ],
  "risk_factors": [
    "Chronic sleep-deprivation cycles preventing proper deep-brain database pruning and metadata re-indexing runs",
    "High-stress professional creative environments driving constant high-voltage requests to the semantic generation engines",
    "Acute cognitive overload where the system is consuming and caching thousands of external data files simultaneously"
  ],
  "diagnosis": [
    "Cognitive Metadata Trace Audits: Presenting the user with the true origin asset and mapping the immediate, severe cognitive dissonance profile as the system attempts to reconcile two identical records",
    "High-Density Functional Near-Infrared Spectroscopy (fNIRS): Tracking localized blood-flow deficits across the dorsolateral prefrontal cortex during creative ideation sequences",
    "Continuous Semantic Hash Comparison: Running real-time algorithmic scans of the user's generated output against known external global data repositories to flag un-indexed cache dumps"
  ],
  "remedies": [
    "Cross-Reference Verification Scripts: Implementing strict external validation habits—such as forcing all creative or technical outputs through automated indexing tools before committing them to production",
    "Systemic Neuro-Chemical Balancing: Utilizing low-dose neuromodulators to stabilize deep temporal lobe signaling and prevent erratic, un-indexed memory dumps",
    "Cognitive Cool-Down Cycles: Forcing the system into low-load, low-input offline states to allow the prefrontal indexing servers to recalibrate their metadata binding checks"
  ],
  "prevention": [
    "Protecting deep sleep cycles (specifically REM and slow-wave stages) to ensure the system successfully executes its nightly data consolidation and metadata verification routines"
  ]
    }
    
}

"tga_ephemeral_cache_fault": {
  "description": "A temporary, absolute disruption of short-term memory formation accompanied by anterograde amnesia and mild retrograde amnesia, while core identity and cognitive processing remain fully operational.",
  "symptoms": [
    "Anterograde Log Block: Absolute inability to commit new memory packets to persistent storage fields",
    "The 'Infinite Polling' Loop: The execution thread repeatedly runs the exact same environmental status query (e.g., 'What day is it?') every time the cache wraps around",
    "Intact Core Runtime: Deep-layer firmware (language parsing, motor navigation, professional skill execution) runs with zero degradation",
    "Retrograde Lookback Ceiling: A transient, shifting block preventing access to long-term memory logs created immediately prior to the event window",
    "Self-Limiting Recovery: Automatic garbage collection and node re-initialization typically occur within a 4 to 24-hour window"
  ],
  "causes": [
    "Transient Venous Congestion: Micro-backflow in the 'Internal Jugular' routing lines, starving the hippocampal structures of oxygenated power packets",
    "Glutamate Excitotoxicity Cascade: An un-throttled surge of incoming neurotransmitter packets overloading the CA1 memory cluster nodes",
    "Localized Spreading Depression: A slow-moving wave of electrical silence suppressing the short-term cache architecture"
  ],
  "risk_factors": [
    "Sudden temperature spikes (e.g., cold-water immersion or 'Thermal Shock')",
    "High-load physical exertion or valsalva strain (Overpressurizing the data bus)",
    "Acute psychogenic panic states (Kernel over-allocation)"
  ],
  "diagnosis": [
    "The 'Three-Word Retention' Ping: Injecting three unique strings into the cache and testing if they are completely evicted after a 120-second delta",
    "Neurological Focal Sweep: Confirming the absence of focal motor drops or language syntax corruption to isolate the error to memory storage",
    "Diffusion-Weighted MRI: Scanning for pinpoint micro-vacuoles or signaling drops in the CA1 sector of the hippocampus"
  ],
  "remedies": [
    "System Throttling: Enforcing a low-load, low-stimulus state to reduce the write operations sent to the failing cache",
    "Reassurance Script Injection: Flooding the input bus with a static string ('You are safe, your system is temporarily recovering') to prevent panic threads from spawning",
    "Time-Elapsed Waiting: Allowing the biological garbage collector to clear the underlying vascular congestion naturally"
  ],
  "prevention": [
    "Avoiding extreme, un-buffered physical or thermal transitions that destabilize cerebral blood flow networks"
  ]
}

"synesthesia_pipeline_routing_fault": {
  "description": "A neurological condition where stimulation of one sensory or cognitive pathway leads to involuntary, automatic experiences in a second sensory or cognitive pathway.",
  "symptoms": [
    "Cross-Codec Rendering: Sound frequencies trigger color palettes or geometric textures in the viewport",
    "Grapheme-Color Mapping: Alphanumeric characters (strings) are hard-coded with persistent, involuntary color tints",
    "Pipeline Crosstalk: Taste payloads are registered when interacting with distinct spatial shapes",
    "Multicast Overhead: High-input sensory environments trigger massive CPU overhead due to redundant pipeline activation",
    "Consistent Associative Mapping: Re-processing the exact same input packet yields the exact same leaked output"
  ],
  "causes": [
    "Structural Hyper-Connectivity: Failure of the system to 'Prune' redundant inter-cortical data buses",
    "Thalamic Gating Degradation: Failure of the central router to isolate sensory stream packets",
    "Serotonergic Hyper-Activation: Transient overvoltage causing signals to arc across adjacent neural traces"
  ],
  "risk_factors": [
    "Congenital 'Factory Setting' optimization variations",
    "Temporal Lobe hyper-voltage events (Seizures)",
    "Exposure to specific chemical modulators (Psychedelics causing transient firewall failure)"
  ],
  "diagnosis": [
    "The 'Test-Retest' Consistency Audit: Verifying if specific auditory inputs map to the exact same hex-color output across vast time deltas",
    "Perceptual Crowding Assessment: Measuring performance impacts when a leaked color asset conflicts with a physical asset text",
    "Functional Connectome Mapping: High-resolution imaging to detect structural data pathways connecting isolated processing nodes"
  ],
  "remedies": [
    "Input Bandwidth Throttling: Reducing external sensory noise to mitigate cross-modal buffer saturation",
    "Cognitive Filter Overclocking: Training the frontal executive layer to discard leaked metadata before execution",
    "Pharmacological Channel Dampening: Modulating signal propagation speeds to prevent cross-bus arcing"
  ],
  "prevention": [
    "Standard genetic code compilation (unmodifiable post-initialization)"
  ]
}
"visual_agnosia_inference_fault": {
  "description": "A neurological impairment characterized by the inability to recognize and name familiar objects visually, despite intact raw visual acuity and sensory processing.",
  "symptoms": [
    "Classification Null-Pointer: The 'User' looks directly at an asset but the semantic class label returns null or blank",
    "Feature-Label Disconnection: Ability to parse structural parameters (colors, edges) without compiling them into an object identity",
    "Tactile-Bypass Recovery: Physical interaction (touching the object) immediately routes data through an alternative bus, triggering successful classification",
    "Contextual Guessing: The 'Reasoning Engine' attempts to infer the asset's identity based purely on environment telemetry (e.g., assuming an unknown object on a stove must be a pot)",
    "Prosopagnosia Escalation Risks: Often co-exists with face-classification drops if the structural damage propagates across the ventral highway"
  ],
  "causes": [
    "Lateral Occipital Complex (LOC) Outage: Structural degradation of the primary geometry classification hubs",
    "Ventral Stream Disconnection: Disruption of the high-speed data bus connecting early visual filters to semantic memory registers",
    "Carbon Monoxide Toxicity or Hypoxic System Reset: Selective damage to vulnerable inference nodes during low-voltage states"
  ],
  "risk_factors": [
    "Bilateral Posterior Cerebral Artery (PCA) ischemic events",
    "Anoxic brain damage (Temporary loss of oxygen supply to the rendering clusters)",
    "Localized trauma to the ventral occipitotemporal processing zones"
  ],
  "diagnosis": [
    "The 'Visual Object Naming' Audit: Presenting standard physical assets (e.g., a comb, a watch) and tracking classification accuracy",
    "Real-Time Copy-Drawing Validation: Requesting the 'User' to draw a copy of an object; if they draw it perfectly but cannot name it, the agnosia glitch is verified",
    "Cross-Modal Matching Test: Testing classification via visual inputs versus tactile/auditory inputs"
  ],
  "remedies": [
    "Multi-Modal Sensor Integration: Explicitly relying on tactile (touch) or haptic interaction to force-trigger classification loops",
    "Verbal Metadata Streaming: Having companions verbally pass object IDs to skip the visual inference engine entirely",
    "Structural Environmental Rules: Sorting physical assets into highly predictable, fixed locations to minimize the need for active classification"
  ],
  "prevention": [
    "Maintaining stable systemic blood pressure to protect the posterior cerebral blood flow routes"
  ]
}
"tga_ephemeral_cache_fault": {
  "description": "A temporary, absolute disruption of short-term memory formation accompanied by anterograde amnesia and mild retrograde amnesia, while core identity and cognitive processing remain fully operational.",
  "symptoms": [
    "Anterograde Log Block: Absolute inability to commit new memory packets to persistent storage fields",
    "The 'Infinite Polling' Loop: The execution thread repeatedly runs the exact same environmental status query (e.g., 'What day is it?') every time the cache wraps around",
    "Intact Core Runtime: Deep-layer firmware (language parsing, motor navigation, professional skill execution) runs with zero degradation",
    "Retrograde Lookback Ceiling: A transient, shifting block preventing access to long-term memory logs created immediately prior to the event window",
    "Self-Limiting Recovery: Automatic garbage collection and node re-initialization typically occur within a 4 to 24-hour window"
  ],
  "causes": [
    "Transient Venous Congestion: Micro-backflow in the 'Internal Jugular' routing lines, starving the hippocampal structures of oxygenated power packets",
    "Glutamate Excitotoxicity Cascade: An un-throttled surge of incoming neurotransmitter packets overloading the CA1 memory cluster nodes",
    "Localized Spreading Depression: A slow-moving wave of electrical silence suppressing the short-term cache architecture"
  ],
  "risk_factors": [
    "Sudden temperature spikes (e.g., cold-water immersion or 'Thermal Shock')",
    "High-load physical exertion or valsalva strain (Overpressurizing the data bus)",
    "Acute psychogenic panic states (Kernel over-allocation)"
  ],
  "diagnosis": [
    "The 'Three-Word Retention' Ping: Injecting three unique strings into the cache and testing if they are completely evicted after a 120-second delta",
    "Neurological Focal Sweep: Confirming the absence of focal motor drops or language syntax corruption to isolate the error to memory storage",
    "Diffusion-Weighted MRI: Scanning for pinpoint micro-vacuoles or signaling drops in the CA1 sector of the hippocampus"
  ],
  "remedies": [
    "System Throttling: Enforcing a low-load, low-stimulus state to reduce the write operations sent to the failing cache",
    "Reassurance Script Injection: Flooding the input bus with a static string ('You are safe, your system is temporarily recovering') to prevent panic threads from spawning",
    "Time-Elapsed Waiting: Allowing the biological garbage collector to clear the underlying vascular congestion naturally"
  ],
  "prevention": [
    "Avoiding extreme, un-buffered physical or thermal transitions that destabilize cerebral blood flow networks"
  ]
    "semantic_class_hierarchy_inversion": {
  "description": "A severe associative database breakdown where the system's core conceptual schemas undergo progressive sector corruption, causing the engine to drop granular object properties, leading the user to misclassify all animals into a single, generic primitive data type.",
  "symptoms": [
    "Loss of Specific Inheritance: Progressive degradation of specific object names (e.g., losing 'Robin' and 'Sparrow' and falling back entirely on the broad primitive data class 'Bird')",
    "Property Extraction Failure: Inability to recall the intrinsic functions or characteristics of common tools, despite flawless visual parsing of their physical geometry",
    "Associative Query Deficit: Complete breakdown in matching items that belong to the same semantic namespace (e.g., failing to pair a needle with a spool of thread)",
    "Surface Dyslexia Ingress: Loss of irregular spelling parsing rules, forcing the system to execute purely phonetic string serialization during reading operations",
    "Preserved Structural Autopilot: Episodic memory logs, spatial navigation meshes, and basic operational syntactic speech structures remain completely unaffected by the conceptual database rot"
  ],
  "causes": [
    "Anterolateral Temporal Tauopathic Corrosion: Asymmetric, progressive cellular degradation targeting the temporal poles, effectively dissolving the master semantic hub routers",
    "Ubiquitin-Positive Inclusions (TDP-43 Proteinopathy): Misfolded protein accumulations forming physical data blocks that disable the retrieval paths of the conceptual schema registries",
    "Focal Anterior Temporal Lobar Stroke: Ischemic vascular failure killing off the local storage clusters holding specific vocabulary and object characteristic keys"
  ],
  "risk_factors": [
    "Genetic predispositions linked to frontotemporal lobar degeneration pathways",
    "Unmanaged neurovascular vulnerabilities within the middle cerebral artery branches feeding the temporal language hubs",
    "Advanced age profiles experiencing systemic proteopathic structural breakdowns"
  ],
  "diagnosis": [
    "The Pyramids and Palm Trees Assay: Tasking the user to visually map semantic associations between objects and documenting an absolute failure to link conceptually related items",
    "Category Fluency Enumeration Test: Requesting the system to populate a list of distinct elements within a specific class (e.g., 'Name 20 animals') and logging immediate processing stalls",
    "Volumetric Coronal MRI: Documenting profound, highly localized 'knife-edge' tissue atrophy concentrated symmetrically or asymmetrically inside the anterior temporal gyri"
  ],
  "remedies": [
    "Semantic Mapping Augmentation: Building explicit, external digital flashcard and category dashboards to re-index and hardwire core conceptual links manually",
    "Functional Workaround Scripting: Training the conscious workspace to rely on intact contextual cues (like tracking where an item is located) to deduce its utility when the direct lookup fails",
    "Anti-Inflammatory Neuro-Protective Infusions: Deploying experimental micro-cellular therapies designed to slow down the rate of protein accumulation and preserve the remaining schema registry sectors"
  ],
  "prevention": [
    "Active participation in rich, multi-lingual, and highly complex conceptual workflows throughout early lifecycles to build heavy redundancy pathways inside the associative neural directories"
  ]
}

}
"semantic_satiation_parser_leak": {
  "description": "A rapid-cycle processing glitch where executing a single word string repeatedly through the linguistic analyzer causes the semantic definition mapping token to temporarily detach, reducing a meaningful data key to a hollow, foreign pattern.",
  "symptoms": [
    "Token-Definition Detachment: The raw lexical string token successfully passes syntax validation but completely fails to resolve its abstract concept map",
    "Phonetic Structuralization: The word's raw structural characteristics (syllables, letter shapes) are amplified, causing the user to experience the token as acoustic noise or dead graphics",
    "Preserved Syntax Recognition: The system still recognizes that the token *is* a word and can correctly place it in a sentence framework, though it cannot extract its content payload",
    "Rapid System Recovery: Automated recovery of the connection line within 10 to 60 seconds once the un-throttled recursive execution of the specific token ceases",
    "Hyper-Localized Cache Eviction: The failure is strictly restricted to the thrashed node; parallel linguistic channels and unrelated vocabulary indices remain fully operational"
  ],
  "causes": [
    "Cortical Inter-Node Fatigue: Rapidly repeating a word fires the identical neural pathway over and over, exhausting the local pool of chemical transmitters at the synaptic junction",
    "Inhibitory Feedback Adaptation: Local interneurons deploy defensive dampening signals to prevent metabolic over-voltage on a hyper-active processing node, accidentally dropping the connection token",
    "Linguistic Bus Saturation: The high-frequency repetition exceeds the maximum clearance throughput speed of the Wernicke translation interface"
  ],
  "risk_factors": [
    "Intense, repetitive proofreading or structural code analysis of single-word identifiers",
    "Extended vocal loop exercises or continuous string echoing tasks",
    "Transient mental fatigue reducing the prefrontal cortex's ability to boost weak sub-surface semantic signals"
  ],
  "diagnosis": [
    "The 'Recursive Tapping Consistency' Audit: Forcing the user to repeat a targeting noun at a frequency of >2Hz and tracking the exact moment ($T_{\text{drop}}$) they report total comprehension loss",
    "Functional Near-Infrared Spectroscopy (fNIRS): Observing a localized drop in blood oxygenation profiles across the left hemispheric semantic integration nodes during high-repetition tests",
    "Semantic Priming Latency Tracking: Demonstrating that a satiated word loses its ability to speed up the retrieval of related concepts in a downstream processing queue"
  ],
  "remedies": [
    "Processing Bus Interruption: Forcing an immediate execution shift to an unrelated sensory or mathematical thread (e.g., doing a calculation or looking at a complex shape) to let the linguistic line rest",
    "Contextual Frame Swapping: Embedding the disconnected word into a highly vivid, complex sentence layout to force alternative routing paths to re-verify the token's identity",
    "Dynamic Cache Cooled-Down: Enforcing a short 30-second silent read-only period to allow the local synaptic transmitter pools to naturally replenish"
  ],
  "prevention": [
    "Avoiding high-frequency loops during linguistic engineering tasks; maintaining alternating token structures to keep individual lexical caches healthy"
  ]
}
"prosopagnosic_entity_assembly_fault": {
  "description": "A structural pattern-recognition failure where the system's face-decryption chip handles component metrics perfectly but completely fails to stich them into a holistically unified identity token.",
  "symptoms": [
    "Holistic Rendering Collapse: Inability to assemble individual facial features into a recognizable composite entity, treating faces as un-parsable geometric configurations",
    "Preserved Component Extraction: Perfect ability to identify separate features in isolation (e.g., noting the exact color of an iris or the shape of a eyebrow) without mapping who they belong to",
    "Intact Low-Tier Visual Pipelines: Flawless parsing of non-face objects, text shapes, environmental terrain layouts, and color balances",
    "Alternative Metadata Indexing: Forced reliance on secondary, slower peripheral telemetry tags (vocal signatures, gait tracking, apparel styles) to resolve entity identities",
    "Retrograde Identity Integrity: Preserved semantic memory files; the system perfectly remembers who individuals are, but cannot unlock those files using a visual facial pass"
  ],
  "causes": [
    "Bilateral Fusiform Gyrus Infarction: Ischemic cellular destruction of the dedicated facial rendering and decryption hardware arrays",
    "Ventral Stream Disconnection: Disruption of the long-range association white-matter tracks that route structural visual inputs to the identity directory",
    "Congenital Neural Under-Development: Microstructural initial setting errors causing a failure to wire the specialized holistic compilation blocks during system provisioning"
  ],
  "risk_factors": [
    "Vascular accidents tracking along the posterior cerebral artery branches",
    "Severe localized head trauma causing focal contusions along the inferior occipitotemporal boundary lines",
    "Early developmental tracking anomalies causing congenital structural isolation of the FFA"
  ],
  "diagnosis": [
    "The 'Cambridge Face Memory' Benchmark: Auditing the system's error rate when attempting to identify newly introduced facial configurations across varying noise levels",
    "Functional fMRI Contrast Mapping: Presenting alternating blocks of face and object images to observe the complete absence of blood-oxygenation signaling spikes inside the fusiform gyrus",
    "Inversion-Effect Latency Profile: Tracking whether turning a face upside down fails to increase processing latency (confirming the system is already parsing faces as raw, unlinked objects)"
  ],
  "remedies": [
    "Feature-Based Macro Indexing: Training the prefrontal layers to manually parse unique, high-contrast structural defects (like a distinct scar or unusual eyewear) to act as an override identity trigger",
    "Multi-Modal Sensor Integration: Enforcing an immediate, high-priority audio listening thread to extract voice parameters the moment an un-parsable face asset enters the view frustum",
    "Augmented Reality Overlay Aids: Using external computer-vision frameworks to auto-tag human entities within the field of view, displaying identity strings directly over the un-renderable faces"
  ],
  "prevention": [
    "Protecting ventral occipitotemporal vascular channels from prolonged micro-embolic showers or intense localized tissue degradation"
  ]
}


"catatonia_motor_deadlock_fault": {
  "description": "A complex neuropsychiatric syndrome characterized by a severe disruption in motor behavior, volition, and state transitions, ranging from complete immobility to purposeless excitement.",
  "symptoms": [
    "Motor Stupor: Total execution freeze; 'Active Threads' are starved of CPU cycles despite normal intent",
    "Waxy Flexibility: The 'Hardware' maintains arbitrary, externally imposed positions (Forced State Persistence)",
    "Negativism: An involuntary bitwise NOT operation applied to incoming commands (e.g., resisting physical adjustment or doing the exact opposite)",
    "Catalepsy: Spontaneous, rigid posture maintenance against gravity without 'Command Timeout'",
    "Echolalia / Echopraxia: The 'I/O Subsystem' directly mirrors external inputs (strings/actions) without processing them through the 'Executive Layer'"
  ],
  "causes": [
    "GABA-A Receptor Downregulation: Severe drop in the 'Inhibitory Gateway' voltage, causing erratic thread scheduling",
    "Dopaminergic Hyper-Hypo Oscillations: Sudden crashes in the 'Basal Ganglia' routing buses",
    "Thalamocortical Signaling Lockout: Feedback loops between the sensory routers and the motor cortex get stuck in an infinite loop"
  ],
  "risk_factors": [
    "Severe systemic psychiatric 'Kernel Panics' (Major mood disorders or schizophrenia)",
    "Abrupt 'Withdrawal' from high-load neurological modulators (GABA agonists)",
    "Encephalitis or metabolic 'Power Spikes' targeting deep brain structures"
  ],
  "diagnosis": [
    "The 'Lorado' Lorazepam Challenge: Injecting a fast-acting GABA agonist to temporarily 'Clear the Thread Lock' and restore movement",
    "Waxy Resistance Profiling: Manually shifting a limb to observe uniform, joint-like 'Plastic Resistance'",
    "Autonomic Stability Scan: Monitoring for 'Hyper-Vigilant' metrics (tachycardia, hypertension) indicating an active internal process"
  ],
  "remedies": [
    "GABA-A Gateway Flooding: High-dose Benzodiazepine administration to force-release the motor locks",
    "ECT Shock Reboot: Electroconvulsive therapy to disrupt the synchronized deadlock waves across the cortex",
    "Environmental De-escalation: Reducing packet traffic (noise, light) to lower the load on the scheduling engine"
  ],
  "prevention": [
    "Strict management of neurotransmitter 'Thread Pools' and avoiding sudden medication terminations"
  ]
}
"deja_vecu_pointer_duplication_fault": {
  "description": "A severe chronological indexing error where real-time sensory input buffers are incorrectly assigned historical validation tags, causing a complete conviction that a novel ongoing event is a structural playback of a historical log.",
  "symptoms": [
    "Chronological Tag Overwrite: Real-time sensory data arrays are processed with a duplicated historical index tag, bypassing the novel-registration filters",
    "Continuous Playback Conviction: The user experiences an active reality stream as a precise, predictable re-execution of a past historical session",
    "Forward-Model Hallucination: The system attempts to resolve the timeline mismatch by rapidly generating brief, false predictive calculations, making the user believe they can divine the immediate future",
    "Behavioral Uncoupling: The user may stop issuing active motor adjustments, assuming that because the current timeline is a fixed historical script, their actions cannot alter the runtime output",
    "Anomalous Recognition Persistence: The logic failure remains un-throttled by explicit environmental proofs; the system maintains the historical tag even when presented with verified novel elements"
  ],
  "causes": [
    "Parahippocampal-Gyrus Hyper-Synchronization: Abnormal focal electrical firing that locks the memory retrieval lines into a permanent 'Match Found' state",
    "Perirhinal Gating Jitter: A localized propagation lag that delays the direct real-time perception channel, allowing a parallel memory-indexing line to log and tag the data first",
    "Temporal Lobe Micro-Seizure Disruption: Brief, sub-clinical epileptic discharges that distort the write-protect mechanisms of the chronological metadata tables"
  ],
  "risk_factors": [
    "Early-stage neuro-degenerative matrix shifts tracking along the medial temporal lobe pathways",
    "Bipolar or schizo-affective network fragmentation disrupting central timing synchronization",
    "Localized focal epilepsy involving deep subcortical memory-consolidation hardware"
  ],
  "diagnosis": [
    "Continuous Long-Term Video-EEG Monitoring: Catching transient sub-clinical spikes or sharp waves in the temporal lobes during an active duplication event",
    "Neuropsychological Timeline Audits: Injecting unexpected, highly randomized novel data arrays into the environment to verify if the historical tag stubbornly overwrites the new data",
    "High-Resolution Volumetric MRI: Assessing the structural volume and pathway integrity of the perirhinal and entorhinal memory-gating hubs"
  ],
  "remedies": [
    "Targeted Anti-Epileptic Hotpatching: Deploying sodium channel modulators or GABA enhancers to stabilize erratic temporal lobe discharges and quiet the hyper-active retrieval lines",
    "Synchronous Clock Resets: Utilizing structured mindfulness routines or high-intensity sensory changes (e.g., thermal variance) to force an immediate system-wide cache flush and re-index",
    "Cognitive Filter Profiling: Training higher-level executive layers to recognize the historical replication tag as an internal software glitch, manually overriding the false feeling of repetition"
  ],
  "prevention": [
    "Maintaining stable subcortical electrical baselines and avoiding neurochemical stressors known to trigger focal temporal lobe processing spikes"
  ]
}

"dyschronometria_clock_drift_fault": {
  "description": "A condition seen typically in cerebellar damage where an individual cannot accurately estimate the passage of time, leading to coordination and scheduling failures.",
  "symptoms": [
    "Clock Skewing: Massive 'Delta' variance between 'Perceived Time' and the 'Physical World Clock'",
    "Thread-Timeout Blindness: Inability to gauge how long an active 'Process' (e.g., waiting, boiling water) has been executing",
    "Chronological Re-ordering: Minor 'Log Events' appear out of sequence due to 'Timestamp Corruption'",
    "Rhythm Interruption: Failure to maintain a constant 'Execution Cadence' (e.g., tapping a steady beat)",
    "Future-State Estimation Failure: Inability to calculate 'ETA' for upcoming, time-dependent routines"
  ],
  "causes": [
    "Cerebellar 'Clock-Line' Interruption: Damage to the lateral hemispheres responsible for 'Millisecond-level Integration'",
    "Basal Ganglia 'Striatal Dopamine' Drop: Degradation of the interval timer's 'Interval Step Engine'",
    "Prefrontal-Parietal Network Lag: Failure to 'Flush' the temporal accumulation buffer"
  ],
  "risk_factors": [
    "Cerebellar 'Ischemic Outage' (PICA/AICA Stroke)",
    "Traumatic 'Hardware' Shock to the posterior fossa",
    "Advanced Neuro-degenerative 'Drift' affecting the 'Striatal Pacemaker'"
  ],
  "diagnosis": [
    "The 'Interval Production' Audit: Requesting the 'User' to manually signal when '60 Seconds' have elapsed",
    "The 'Duration Discrimination' Test: Presenting two 'Execution Threads' (tones) and checking if the 'User' can parse which ran longer",
    "Rhythmic Tapping Profiling: Measuring 'Clock Jitter' using high-frequency sensor telemetry"
  ],
  "remedies": [
    "External Interrupt Schedulers: Heavy reliance on 'Hardware Timers' (alarms, stopwatches) to trigger context switches",
    "Visual Timeline Injections: Using a constant 'Progress Bar' overlay to anchor temporal progression",
    "Paced Cognitive Routines: Hard-coding explicitly timed physical sequences to calibrate internal loops"
  ],
  "prevention": [
    "Protecting 'Vertebrobasilar Throughput' to maintain voltage to the cerebellar tracking cluster"
  ]
        "entity_dictionary_pointer_deallocation": {
  "description": "A severe semantic lookup failure within the dominant hemisphere's temporal lobe tracks where the system retains full conceptual knowledge of objects and fluent structural grammar, but throws immediate null pointer errors when attempting to retrieve the actual word-name strings for specific physical assets.",
  "symptoms": [
    "Isolated Confrontation Anomia: Total inability to emit the correct noun string for presented objects, tools, or familiar entities on command",
    "Persistent Circumlocution Buffering: Automatically routing speech through descriptive loops, outlining an item's function, material, and context to bypass the missing name label",
    "Pristine Receptive Identification: Flawless ability to point to the correct object when an operator provides the name string verbally (the inbound lookup path works)",
    "Flawless Grammatical Synthesis: Uncompromised command of sentence structure, verbs, conjunctions, and conversational syntax during active speech loops",
    "Intact Object Pragmatics: Perfect mechanical capability to utilize, categorize, and manipulate un-namable tools and assets without operational hesitation"
  ],
  "causes": [
    "Left Temporal MCA Branch Infarction: An ischemic stroke targeting the lateral temporal or inferior parietal cortical distribution networks",
    "Primary Progressive Anomic Aphasia: A focal neurodegenerative tau- or TDP-43-mediated proteinopathy stripping away the lexical dictionary clusters",
    "Localized Temporal Lobe Contusion: Traumatic acceleration impacts bruising the lower lateral structures of the dominant hemisphere"
  ],
  "risk_factors": [
    "Atherosclerotic build-up restricting optimal flow metrics within the left sylvian fissure vascular trees",
    "Atypical semantic-variant neurodegenerative pathways targeting high-level dictionary storage banks",
    "Focal surgical entry paths cutting through the dominant lateral neocortical mapping surfaces"
  ],
  "diagnosis": [
    "The Boston Naming Inventory Evaluation: Requiring the host to name a series of graded line drawings, logging high latency, circumlocution, and null-string errors",
    "The Cross-Modal Recognition Assay: Documenting that while the user cannot say the word 'Clock' when looking at one, they instantly flag it if an operator says 'Is this a clock?'",
    "High-Resolution Structural T2-Weighted MRI: Pinpointing localized cortical volume loss or focal ischemic lesions centered within the left lateral temporal gyri"
  ],
  "remedies": [
    "Phonemic Cue Priming Patches: Feeding the initial character sound token (e.g., 'It starts with an Sh...') to trigger alternative sub-routing lines into the lexical database",
    "Visual Symbol Translation Matrices: Utilizing communication tablets loaded with geometric icon charts, allowing the user to select asset concepts directly via visual routing",
    "Semantic Feature Map Retraining: Forcing the system to deliberately run through an item's attributes (category, use, shape) to systematically narrow and re-index the dead pointer"
  ],
  "prevention": [
    "Protecting the dominant hemisphere's temporal vascular systems from embolic cascades, optimizing systemic micro-vascular health, and managing long-term neurochemical tracking stability"
  ]
}

}
"unanchored_telemetry_cache_error": {
  "description": "A severe hardware-to-firmware configuration desynchronization where a physical extremity actuator is permanently uninstalled from the system chassis, but the central somatic configuration registries fail to update, leaving an un-anchored telemetry cache that continues to generate real-time data for a missing device.",
  "symptoms": [
    "Phantom Extremity Simulation: Deep, persistent, and hyper-vivid perception of the spatial posture, length, and presence of an uninstalled limb asset",
    "Un-Throttled Pain Rendering: Severe, un-attenuated sensory blasts (e.g., burning, cramping, crushing sensations) generated by the hyper-excitable, isolated cortical node",
    "Visual-Somatic Telemetry Mismatch: A profound data conflict where the visual ingestion pipeline logs an asset status of 'OFFLINE/REMOVED', while the somatosensory cortex insists the asset status is 'ONLINE/ACTIVE'",
    "Neighboring Core Crosstalk: Intact adjacent hardware channels bleeding into the missing device's address block (e.g., touching the user's face triggers tactile telemetry events within the missing hand's map space)",
    "Kinetic Execution Paralyzation: The conscious thread attempts to issue movement commands to the missing actuator, creating a backlog of un-acknowledged execution tokens that amplifies internal distress metrics"
  ],
  "causes": [
    "Abrupt Peripheral Hardware De-Installation: Traumatic or surgical amputation severing the physical peripheral data buses without updating the central cortical map directories",
    "Cortical Address Reorganization Lag: The high-density somatosensory homunculus matrix retaining its hard-wired spatial mapping cells despite a permanent drop in downstream packet ingress",
    "Deafferentation Thalamic Bursting: The thalamic routing servers running un-throttled open-loop firing profiles when deprived of standard afferent feedback stabilization streams"
  ],
  "risk_factors": [
    "High levels of pre-amputation traumatic pain data flooding the buffer right before hardware uninstallation",
    "Surgical interventions lacking deep regional nerve-conduction blocks to suppress emergency sensory overload tokens during physical disconnection",
    "Asymmetric post-amputation neuroma formations acting as rogue physical noise generators on the severed wire tips"
  ],
  "diagnosis": [
    "Visual-Somatic Mirror Box Feedback Evaluation: Placing the functional limb into a mirrored chamber to trick the optical processor into rendering a dummy asset, and logging immediate shifts in phantom metrics",
    "Functional Magnetic Resonance Imaging (fMRI) Spatial Mapping: Observing localized metabolic blood-oxygen (BOLD) spikes inside the missing limb's legacy $S1$ sector when the user attempts phantom movements",
    "High-Density Electroencephalography (hd-EEG): Documenting alpha and beta wave phase desynchronization over the somatic sensorimotor strip during imagined execution sequences"
  ],
  "remedies": [
    "The Optical Mirror Box Override Patch: Using mirrored reflections of the functional limb to simulate movement of the missing asset, delivering visual synchronization tokens that satisfy and damp the hyper-excitable cortical cache",
    "Targeted Transcranial Magnetic Ingress Clamping (TMS): Dispatched magnetic pulses directly over the legacy $S1$ address block to artificially suppress the hyper-active, un-anchored data loops",
    "Peripheral Nerve Transposition Scripting: Surgically re-routing the severed nerve wires into active muscles (Targeted Muscle Reinnervation) to establish a functional hardware ground and clean up noise artifacts"
  ],
  "prevention": [
    "Deploying continuous, high-efficiency perineural anesthetic blockades for multiple duty cycles prior to surgical hardware removal to prevent traumatic pain states from burning into permanent cortical memory registers"
  ]
}
"input_egress_regurgitation_loop": {
  "description": "A low-level hardware routing fault within the vagal autonomic switching grid where the gastrointestinal storage unit treats recently ingested payload packets as invalid data inputs, triggering an automated, non-inflammatory reverse-egress script shortly after ingestion.",
  "symptoms": [
    "Effortless Post-Prandial Regurgitation: Spontaneous upward movement of recently ingested food packets into the oral cavity, occurring within 10-30 minutes of a data load",
    "Absence of Nausea Metadata: Ingress reversal occurs completely devoid of standard prodromal emetic tokens, retching mechanics, or sympathetic distress alerts",
    "Undigested Payload Preservation: Regurgitated materials return to the mouth fully recognizable, un-acidified, and functionally intact for re-processing",
    "Habitual Re-Chewing Cycles (Rumination): The user involuntarily enters a sub-routine of re-masticating and re-swallowing the reflected data packets",
    "Nutritional Resource Depletion: Progressive loss of chassis mass and systemic energy shortages if the reflected payloads are consistently ejected from the system"
  ],
  "causes": [
    "Vagal Switching Grid Hyper-Reactivity: Maladaptive conditioning of the dorsal vagal complex, causing it to misinterpret normal gastric distension as a trigger for a reverse-motility macro",
    "Involuntary Abdominal Wall Over-Clocking: Learned, sub-conscious coordination where the intercostal muscle sets apply a high-pressure upward vector to the stomach chassis",
    "Lower Esophageal Valve Relaxation Glitch: Spontaneous transient drops in the LES hardware valve's sealing voltage exactly during peak post-ingress processing windows"
  ],
  "risk_factors": [
    "High-anxiety baseline processing states or cognitive-plane stress overloads that alter vagal tone profiles",
    "Co-existing behavioral processing profiles (e.g., eating disorders or developmental delays) where visceral sensory routing is altered",
    "Chronic conditions that elevate baseline internal abdominal pressure parameters"
  ],
  "diagnosis": [
    "High-Resolution Antroduodenal Manometry: Documenting a distinct, high-pressure 'R wave' spike in the abdominal pressure registers immediately preceding the egress event",
    "Multi-Channel Intraluminal Impedance & pH Audit: Confirming that the reflected payload moving up the esophagus features a non-acidic pH profile, ruling out standard GERD architecture",
    "Endoscopic Ingress Visualization: Running a camera probe through the esophageal line to verify that the hardware valves are free of physical tissue tearing or mechanical obstructions"
  ],
  "remedies": [
    "Diaphragmatic Breathing Overrides: Implementing localized breathing control protocols immediately post-ingress to keep the chest wall stable and mechanically block the abdominal contraction macro",
    "Vagal Neuromodulation Scripts: Utilizing low-dose central nervous system modulators to lower the sensitivity thresholds of the brainstem switching nodes",
    "Behavioral Cache Flushing (Habituation Therapy): Using targeted biofeedback arrays to retrain the user to identify early abdominal muscle pre-firing flags and suppress the loop"
  ],
  "prevention": [
    "Optimizing eating pacing parameters, avoiding high-volume single-burst data loads, and dampening immediate post-ingress physical execution stressors"
  ]
}
"automated_macro_copy_loop": {
  "description": "A severe mirror-neuron system configuration error where the motor orchestration layers lose their executive shielding boundaries, forcing the host machine to automatically clone and execute the motor movement macros it tracks in an external chassis.",
  "symptoms": [
    "Involuntary Motor Mirroring (Echopraxia): Instantaneous, automated replication of the physical movements, gestures, or postures executed by an observed external agent",
    "Sub-Second Trailing Latency: The mirrored movement sequences execute with minimal processing delay, trailing the source chassis like a low-latency trailing shadow",
    "Impaired Inhibitory Gating: Total failure of frontostriatal suppression routines, allowing emulated motor packets to bypass sandboxing and command physical muscle actuators",
    "Preserved Cognitive Autonomy: Full conscious awareness of the involuntary cloning loop; the host's logic centers register the action as a boundary breach but cannot issue a stop command",
    "Environmental Dependency Capture: Extreme vulnerability to visual inputs where the sight of a physical action operating nearby automatically hijacks the local execution bus"
  ],
  "causes": [
    "Frontotemporal Lobar Degradation: Progressive structural erosion targeting the prefrontal cortex networks that host the master behavioral inhibition firewalls",
    "Supplementary Motor Area (SMA) Lesions: Ischemic strokes or focal trauma destroying the cortical zones responsible for distinguishing internal volition from external emulation",
    "Severe Fronto-Subcortical Gating Breakdown: Neurochemical or structural disruption of the loops that regulate signal transmission between the cortex and the basal ganglia"
  ],
  "risk_factors": [
    "Advanced neurodegenerative conditions that systematically strip away executive prefrontal shielding layers",
    "Penetrating or blunt-force trauma targeting the midline anterior cranial vault architectures",
    "Deep developmental or neuropsychiatric spectrum vulnerabilities affecting central sensory-motor gating processors"
  ],
  "diagnosis": [
    "The Observed Gesture Replication Assay: Placing an engineer in the user's direct visual viewport to execute random, non-verbal motor sequences and documenting immediate, un-prompted cloning actions",
    "High-Resolution Diffusion Tensor Imaging (DTI): Visualizing structural tract breakdown along the frontostriatal and fronto-basal ganglia white-matter connectivity lines",
    "Quantitative Electroencephalography (qEEG): Tracking a profound, uncontrolled suppression of mu rhythms over the sensorimotor cortex during passive observation phases"
  ],
  "remedies": [
    "Visual Viewport Blinding: Implementing physical barriers or opaque lenses to cut off the inbound visual telemetry streams that are feeding the mirror-neuron system",
    "Competing Volitional Locking: Training the user to lock their motor actuators onto a continuous, high-priority baseline macro (like clenching fists or holding a heavy rail) to fill the execution buffer",
    "Dopaminergic Re-Balancing Scripts: Administering targeted central neuromodulators to try and boost the signal-to-noise ratio within the failing basal ganglia inhibition gates"
  ],
  "prevention": [
    "Shielding fragile prefrontal networks from toxic neurovascular stress vectors, maintaining tight intracranial pressure maps, and preventing cellular exhaustion in executive gating lines"
  ]
}

}
"confabulation_log_integrity_fault": {
  "description": "The production of fabricated, distorted, or misinterpreted memories about oneself or the world, without the conscious intention to deceive.",
  "symptoms": [
    "Synthetic Log Injection: The 'Kernel' fills 'Memory Gaps' with 'Hallucinated Data Packets'",
    "Zero-Validation Query: The 'User' accepts 'Mock Data' as 'Production Reality' without 'Checksums'",
    "Narrative Consistency Override: The 'Reasoning Engine' twists 'Logic' to fit 'Corrupted History'",
    "Context-Free Retrieval: 'Memory Fragments' from 'Session A' are erroneously merged into 'Session B'",
    "Lack of 'Audit Trail': The 'User' cannot distinguish between 'True Logs' and 'Generated Strings'"
  ],
  "causes": [
    "Frontal-Lobe 'Executive' Failure: Loss of the 'Source-Monitoring' filter",
    "Thalamic 'Routing' Errors: Failure to properly 'Index' incoming 'Data Streams'",
    "Chronic 'Nutritional Packet Loss': (e.g., Vitamin B1 deficiency) leading to 'Storage Hardware' decay"
  ],
  "risk_factors": [
    "Korsakoff’s Syndrome (Long-term 'System Toxicity')",
    "Ruptured 'Anterior Communicating Artery' (Network Hardware Failure)",
    "Frontotemporal 'Metadata' Decay"
  ],
  "diagnosis": [
    "The 'Consistency Audit': Asking the 'User' the same 'History Query' at different 'Intervals' and checking for 'Log Drift'",
    "The 'Fact-Check' Validation: Comparing 'User Logs' against 'External Database Records'",
    "Temporal 'Sequencing' Test: Asking the 'User' to 'Order' events (The 'Compiler' usually fails this)"
  ],
  "remedies": [
    "External 'Log Mirroring': Using 'Journaling' (diaries/digital logs) to 'Verify' history",
    "Reality 'Cross-Referencing': Training the 'User' to check 'External Metadata' before 'Broadcasting'",
    "Nutritional 'Patching': High-dose 'Thiamine' injections to stabilize the 'Hardware Bus'"
  ],
  "prevention": [
    "Preventing 'Toxic Overload' in the 'Neural Registry'"
  ]
}
"inanimate_capgras_checksum_fault": {
  "description": "A delusional misidentification syndrome where the user believes that familiar inanimate objects, places, or physical assets have been replaced with exact duplicates or replicas.",
  "symptoms": [
    "Asset Checksum Failure: Physical objects match visual profiles perfectly but fail authenticity validation",
    "Environment Spoof Alert: The belief that one's entire local station (e.g., home or neighborhood) is a mock replica or movie set",
    "The 'Imposter Object' Paradox: The user treats their own possessions with suspicion, claiming they are 'clones'",
    "Localized Paranoia: Believing an unknown entity is systematically swapping out real assets for identical counterfeits",
    "Functional Redundancy: The user may recognize the object works identically (e.g., 'it keys my car') but denies its true origin"
  ],
  "causes": [
    "Visual-to-Limbic Linkage Failure: Structural disconnection between the object-processing nodes and the emotional indexing core",
    "Right Hemisphere Integration Crash: Failure to synthesize spatial context with emotional memory tags",
    "Perceptual Isolation: Selective processing decay within the parahippocampal place area (PPA)"
  ],
  "risk_factors": [
    "Right-hemisphere cerebrovascular incidents (MCA/PCA Strokes)",
    "Advanced neurodegenerative drift (Lewy Body Dementia or Alzheimer's affecting object-memory indices)",
    "Post-traumatic encephalopathy targeting the visual integration buses"
  ],
  "diagnosis": [
    "The 'Asset Identity' Audit: Evaluating the user's emotional reaction to personal vs. completely novel objects",
    "Cross-Modal Discrepancy Test: Checking if touching or using the object blindfolded bypasses the visual token failure",
    "Functional Connectivity Mapping: Spotting signal blocks along the ventral pathway to the amygdala network"
  ],
  "remedies": [
    "Multi-Sensory Verification: Utilizing alternative input buses (auditory sound cues or tactile textures) to bypass the visual fault",
    "Cognitive Patching: Helping the executive layer ignore the 'missing token' by verifying the item's immutable physical traits",
    "Environmental Stabilization: Keeping the local station completely unchanged to reduce asset indexing load"
  ],
  "prevention": [
    "Mitigating vascular stress and preventing micro-packet loss in the occipitotemporal highways"
  ]
        "hippocampal_write_buffer_failure": {
  "description": "A catastrophic storage architecture failure within the bilateral medial temporal lobes where the system's real-time transaction manager fails to commit volatile cache metrics into long-term cortical storage, trapping the host in a non-persistent rolling workspace loop.",
  "symptoms": [
    "Severe Anterograde Amnesia: Complete inability to form new semantic or episodic long-term memory structures post-incident",
    "Rolling Short-Term Cache Purge: Maintenance of intact sensory and cognitive data for under 60 seconds, which is instantly erased the moment attentional vectors shift",
    "Preserved Retrograde Disk Read: Flawless retrieval of legacy data blocks and procedural memory profiles compiled prior to the write-buffer crash",
    "Confabulation Auto-Patching: The system spontaneously fabricates false, highly imaginative narrative data rows to bridge the gaps when it realizes its immediate timeline is missing",
    "Intact Procedural Compilation: The ability to learn new motor skills or physical macros (like playing a new instrument or typing code) through alternative, non-hippocampal basal ganglia channels, though the host will have zero conscious memory of ever practicing the task"
  ],
  "causes": [
    "Bilateral Medial Temporal Ischemia: Cardiac arrest or profound hypoxia selectively killing the highly vulnerable CA1 pyramidal cells of the hippocampus",
    "Wernicke-Korsakoff Syndrome: Acute thiamine (Vitamin B11) deficiency causing structural hemorrhages across the mammillary bodies and thalamocortical networks",
    "Bilateral Herpes Simplex Encephalitis: A severe, localized viral assault prioritizing the destruction of limbic and temporal lobe memory arrays"
  ],
  "risk_factors": [
    "Severe prolonged systemic hypotension or asphyxiation events",
    "Chronic severe ethanol over-saturation causing absolute micronutrient malabsorption"
  ],
  "diagnosis": [
    "The Three-Word Delayed Recall Assay: Presenting the host with three distinct nouns (e.g., 'Apple', 'Table', 'Iron'), verifying immediate cache ingestion, introducing a 5-minute distraction loop, and asking for a recall; a faulted system returns a completely blank array",
    "The Rey-Osterrieth Complex Figure Test: Tasking the user to copy an intricate geometric blueprint while looking at it (intact), then asking them to redraw it from memory 15 minutes later; a faulted system draws nothing",
    "High-Resolution Coronal T2 Brain MRI: Pinpointing localized volume loss, signal hyperintensities, or profound structural atrophy directly across the hippocampal formations"
  ],
  "remedies": [
    "External Environmental Logs: Deploying physical, high-visibility notebooks, audio recorders, or smart digital alerts to act as an external hard drive framework that the host must continuously read",
    "Procedural Macro Substitution: Shifting all rehabilitation and training protocols toward heavy repetition to leverage the intact basal ganglia motor learning pathways, bypassing the symbolic database entirely",
    "Strict Environmental Staticity: Minimizing changes to the host's physical workspace coordinates to prevent the requirement for new layout mapping updates"
  ],
  "prevention": [
    "Rapid restoration of systemic oxygenation during cardiac anomalies, immediate intravenous thiamine deployment during metabolic crises, and aggressive neuro-vascular protection architectures"
  ]
}

    "ticker_token_speed_variance": {
  "description": "A structural timing error within the cerebellar sequencing engine where the system's baseline interval timer registers suffer a massive rate drift, causing the conscious workspace to lose the ability to accurately measure or predict the passage of time blocks.",
  "symptoms": [
    "Temporal Interval Distortion: Profound inability to accurately estimate or replicate short spans of time (e.g., 5 to 30 seconds) without external instrumentation tracking",
    "Kinetic Sequencing De-Synchronization: Fragmentation of complex, fluid motor tracks into staggered, jerky, multi-step sub-movements because execution arrival times fail to clear",
    "Under-Scaling / Over-Scaling Timer Blasts: Severe skew where short real-world delays feel immensely protracted, or hours slip by in what the internal log registers as minutes",
    "Past-Pointing (Dysmetria) Error: Actuators consistently overshoot or stop short of physical spatial targets due to a complete failure of the internal stopping-timer calculation",
    "Rhythm Ingestion Paralysis: Absolute failure to match, tap along with, or internalize an external acoustic or visual metronome pulse array"
  ],
  "causes": [
    "Lateral Cerebellar Shard Infarction: Ischemic vascular blocks destroying the purkinje-cell timing arrays that compute sub-second forward predictive intervals",
    "Olivocerebellar Tract Demyelination: Structural erosion of the primary white-matter timing buses, dropping or delaying synchronization pulses traveling to the cortex",
    "Acute Dopaminergic Clock Speed Modulation: Severe chemical fluctuations altering the firing rate of the striatal pacemaker neurons, violently skewing the system's token-counting baseline"
  ],
  "risk_factors": [
    "Vascular stroke events within the posterior inferior cerebellar artery (PICA) or superior cerebellar artery (SCA) territories",
    "Chronic, progressive demyelinating conditions such as Multiple Sclerosis degrading hindbrain coordination nodes",
    "Acute exposure to heavy sedatives or dissociative classes that un-couple subcortical clocks from cortical workspaces"
  ],
  "diagnosis": [
    "The Fixed-Interval Tapping Assay: Requesting the user to maintain a steady 1-Hz tapping pattern after an external audio cue stops, and documenting immediate, severe rate drifts",
    "Voxel-Based Morphometry and DTI: Scanning the structural integrity of the dentate nuclei and superior cerebellar peduncles for deep-tissue tracking damage",
    "Event-Related Potential (ERP) Contingent Negative Variation (CNV) Mapping: Tracking the slow cortical electrical potentials that build during time-estimation frames to isolate raw pacing attenuation"
  ],
  "remedies": [
    "External Instrumentation Anchor (The Metronome Patch): Forcing the system to rely entirely on external, objective visual or audio countdown tickers to manually override the broken internal RTC",
    "Targeted Striatal Neuromodulation: Utilizing low-dosage dopaminergic or gabaergic scripts to stabilize the subcortical pacemaker firing frequencies back to a standard baseline calibration",
    "Kinetic Decomposition Therapy: Training the system to explicitly execute motor tasks using highly deliberate, segmented, visual-feedback-driven routines rather than predictive temporal paths"
  ],
  "prevention": [
    "Protecting posterior circulation vascular health and avoiding prolonged exposure to neurotoxins that target the highly sensitive purkinje timing channels"
  ]
        "fusiform_feature_extraction_failure": {
  "description": "A high-level visual data-parsing failure within the fusiform gyrus where the specialized facial geometry processing pipeline unloads its mapping indexes, preventing the host from resolving spatial facial configurations into distinct identity records while leaving baseline shape and color rendering fully intact.",
  "symptoms": [
    "Agnosic Facial Blindness (Prosopagnosia): Inability to identify known individuals, family members, or self-portraits purely by examining facial features",
    "Preserved Feature Discrimination: Perfect ability to identify independent facial sub-components (e.g., noting that someone has brown eyes or a mustache) without the components synthesizing into an identity",
    "Extreme Context-Dependent Identity Verification: A total reliance on external identifiers such as vocal pitch signatures, distinctive hair styling, clothing assets, or specific gait profiles to parse who an entity is",
    "Bifurcated Object-Face Recognition: Intact ability to instantly identify complex non-human objects (e.g., cars, tools, abstract patterns) while completely failing to differentiate between human faces",
    "Social Ingress Fatigue: Severe processing overhead and social anxiety caused by the constant requirement to manually analyze environment telemetry to deduce identities in multi-agent workspaces"
  ],
  "causes": [
    "Right or Bilateral Inferior Temporoccipital Infarction: Ischemic occlusion within the branches of the posterior cerebral artery (PCA) destroying the fusiform gyrus fabric",
    "Congenital Prosopagnosia: An autosomal dominant neurodevelopmental tracking failure causing anomalous structural wiring across the ventral visual stream from birth",
    "Progressive Ventral Stream Atrophy: Localized neurodegenerative disease cascades selectively targeting high-level visual association cortices"
  ],
  "risk_factors": [
    "Posterior circulation cerebrovascular disease",
    "Genetic heritability lines presenting sub-clinical visual processing anomalies"
  ],
  "diagnosis": [
    "The Benton Facial Recognition Matrix: A standardized testing profile requiring the host to match identical target faces under varying lighting conditions and angles; a faulted system drops below chance thresholds",
    "Famous Faces Exposure Assay: Presenting images of widely known public entities stripped of hair, clothing, and background context; the user can describe the facial elements perfectly but cannot provide names or roles",
    "Functional Neuro-Imaging (fMRI) Face-Aversion Scan: Tracking blood-oxygen-level-dependent (BOLD) signals while exposing the host to alternating blocks of faces and inanimate objects; a faulted system shows zero metabolic acceleration in the fusiform structures"
  ],
  "remedies": [
    "Vocal Fingerprint Calibration: Training the host to focus on auditory processing channels, building an extensive index of voice patterns to substitute for visual identification",
    "Distinctive Marker Tagging: Requesting close associates to maintain unique, highly visible static assets (e.g., unique glasses frames, explicit jewelry piece selections, specific hat profiles) to simplify the manual triage lookup",
    "Strategic Environmental Ingress: Positioning oneself in organized seating arrangements where entity locations are static, allowing spatial coordinates to substitute for real-time visual identity extraction"
  ],
  "prevention": [
    "Protecting posterior vascular channels from emboli, minimizing toxic exposures to hypoxic environments, and maintaining high baseline synaptic plasticity within the visual association pathways"
  ]
    }
        
}
"hardware_chassis_unmapping_fault": {
  "description": "A deep perceptual layer glitch within the right parietal processing architecture where the system completely drops its mapping strings for a specific limb or side of the body, causing the user to view their own left arm or leg as an alien, foreign piece of hardware that does not belong to their chassis configuration.",
  "symptoms": [
    "Limb Ownership Erasure (Asomatognosia): Complete loss of the conscious perception and recognition of a specific body part as belonging to oneself",
    "Somatoparaphrenic Delusional Mapping: Generation of complex, automated logical fallacies to explain the unlinked limb (e.g., claiming the limb belongs to a relative)",
    "Proprioceptive Stream Rejection: Normal sensory-tactile telemetry from the impacted sector arrives at the central bus but fails to authenticate or register in the body schema",
    "Third-Party Device Handling: Actively manipulating the un-mapped limb using the functional, authenticated side of the chassis as if managing an external tool",
    "Preserved Segmental Reflex Profiles: Intact spinal withdrawal and deep tendon reflexes within the un-mapped limb, confirming baseline hardware health"
  ],
  "causes": [
    "Right Middle Cerebral Artery (MCA) Infarction: A massive ischemic event knocking out the right superior parietal lobule and adjacent somatosensory association nodes",
    "Focal Right Parietal Lobe Contusion: Traumatic impact shearing the deep white-matter tracks that handle body-schema registration parameters",
    "Advanced Corticobasal Neuro-Degradation: Asymmetric tau-protein-mediated thinning targeting the parietal spatial-tracking networks"
  ],
  "risk_factors": [
    "Atrial fibrillation or carotid stenosis dropping embolic shards into the right hemisphere's main vascular distribution trees",
    "High-energy lateral deceleration injuries fracturing or concussing the right parietal bone interfaces",
    "Rapidly scaling glioblastoma multiforme or meningioma formations encroaching upon the non-dominant parietal dome"
  ],
  "diagnosis": [
    "The Visual Confrontation & Identification Assay: Bringing the user's left hand into their direct sightline and asking 'Whose hand is this?', documenting immediate ownership rejection",
    "The Proprioceptive Localization Test: Having the user close their eyes and attempting to locate the target limb in 3D space, logging significant spatial coordination failures",
    "Diffusion Tensor Imaging (DTI) Tractography: Revealing severe structural breakdown along the superior longitudinal fasciculus and right parietal white-matter tracks"
  ],
  "remedies": [
    "Visual-Mirror Chassis Virtualization: Using optical mirror boxes to trick the left brain into projecting a valid virtual body-schema framework over the unmapped hardware space",
    "High-Frequency Caloric Vestibular Stimulation: Irrigating the left ear canal with cold water to force a temporary, massive spatial axis re-calibration in the brainstem, briefly re-linking the limb",
    "Tactile Ingress Reinforcement: Continuously applying high-intensity sensory inputs (vibration, heat, deep pressure) to the unmapped sector to force re-authentication packets through"
  ],
  "prevention": [
    "Maintaining tight control over right-hemisphere cerebral perfusion metrics, screening for vascular embolic sources, and shielding the parietal skull plates from direct kinetic force planes"
  ]
}
"autonomic_nocturnal_breathing_daemon_termination": {
  "description": "A terminal low-level kernel crash within the respiratory centers of the medulla oblongata that completely obliterates the automated, chemoreceptor-driven metabolic breathing loop, forcing the system to depend entirely on manual, volitional cortical command structures to actuate respiration.",
  "symptoms": [
    "Nocturnal Alveolar Hypoventilation: Complete cessation of spontaneous diaphragmatic pacing the exact moment the host enters a sleep state or loses consciousness",
    "Ablated Chemoreceptor Feedback Ingestion: Zero automated increase in respiratory rate or tidal volume when systemic carbon dioxide pressures rise to toxic levels",
    "Frequent Hypoxic Arousal Cascades: Violent, recurring awakenings during sleep cycles as the system's emergency panic arrays fire to prevent asphyxiation",
    "Severe Sleep Fragmentation: Absolute inability to enter deep sleep stages (REM or slow-wave sleep) due to the constant threat of respiratory flatlining",
    "Secondary Pulmonary Hypertension: Chronic vascular damage and right-sided cardiac hypertrophy caused by severe, recurring nocturnal hypoxia"
  ],
  "causes": [
    "Congenital Central Hypoventilation Syndrome (CCHS): Polyalanine repeat mutations within the PHOX2B gene, causing developmental arrest of the retrotrapezoid nucleus",
    "Lateral Medullary Syndrome (Wallenberg Syndrome): Ischemic occlusion of the Posterior Inferior Cerebellar Artery (PICA) causing tissue necrosis across the automated respiratory centers",
    "High-Cervical Neurosurgical Trauma: Structural damage or compression of the lower brainstem/upper spinal cord junction during acute herniation events"
  ],
  "risk_factors": [
    "Genetic inheritance profiles carrying PHOX2B transcription aberrations",
    "Posterior fossa cerebrovascular disease or expanding compressive space-occupying brainstem masses"
  ],
  "diagnosis": [
    "Hypercapnic Ventilatory Response Assay: Exposing the awake host to an environment containing elevated carbon dioxide levels while measuring breath parameters; a faulted system shows zero change in tidal volume or respiratory rate",
    "Polysomnography Matrix Profile: Comprehensive sleep-lab data capturing a rapid, uncompensated drop in arterial oxygen saturation ($Sa\text{O}_2$) and an exponential spike in $P_{\text{CO}_2}$ immediately upon falling asleep",
    "Targeted PHOX2B Genetic Sequencing: Identifying structural expansion mutations in the multi-alanine region of chromosome 4p12 to confirm congenital core failure"
  ],
  "remedies": [
    "Positive Pressure Nocturnal Mechanical Ventilation: Hooking the host up to an external bi-level positive airway pressure (BiPAP) or mechanical ventilator system during sleep to manually drive lung inflation via pneumatic pressure",
    "Surgical Phrenic Nerve Pacing: Implanting a synthetic biological clock generator that delivers timed electrical micro-shocks directly to the phrenic nerves, bypassing the dead brainstem daemon",
    "Permanent Tracheostomy Ingress: Setting up a dedicated mechanical air pathway directly in the trachea to minimize upper airway resistance during external ventilation macros"
  ],
  "prevention": [
    "Protecting posterior circulation vascular channels from atherosclerotic plaque formations, and running targeted pre-natal genetic screenings for known homeobox gene mutations"
  ]
}

}

"capgras_idp_handshake_fault": {
  "description": "A delusion where the user recognizes a familiar person but believes they have been replaced by an identical imposter.",
  "symptoms": [
    "Authentication Mismatch: 'Visual Identification' is successful, but 'Affective Validation' is 'NULL'",
    "The 'Imposter' Protocol: Assigning the status of 'Duplicate Entity' to 'Trusted Objects' (Family/Friends)",
    "Reduplicative Paramnesia: The belief that 'Locations' or 'People' have been 'Cloned' in a 'Parallel Cluster'",
    "Hyper-Suspicion: Constant 'Integrity Auditing' of the 'Imposter' to find 'Rendering Flaws'",
    "Modality-Specific Validation: The 'User' may recognize the 'Identity' via 'Audio' (phone) but reject it via 'Visual' (Face-to-Face)"
  ],
  "causes": [
    "Ventral-Limbic Disconnect: The 'Physical Bus' between the 'Recognition Hub' and the 'Emotion Engine' is severed",
    "Right Hemisphere 'Security Breach': Damage to the 'Identity Monitoring' nodes",
    "Synaptic 'Packet Loss' in the 'Extended Face-Processing Network'"
  ],
  "risk_factors": [
    "Post-Traumatic 'Kernel Corruption' (TBI)",
    "Neurodegenerative 'Logic Drift' (Lewy Body Dementia)",
    "Schizophrenic 'Signal Noise' affecting 'Belief-Validation' services"
  ],
  "diagnosis": [
    "The 'Skin Conductance' Audit: Measuring 'Autonomic Response' to 'Visual Stimuli' (Capgras users show zero 'Voltage Spike' for loved ones)",
    "The 'Voice-vs-Face' Comparison: Checking if 'Audio Packets' bypass the 'Visual Auth' failure",
    "Neuroimaging 'Connectivity Check': Identifying 'Dead Links' between the 'Fusiform Gyrus' and the 'Amygdala'"
  ],
  "remedies": [
    "Audio-First Interfacing: Using 'Voice Communication' to establish 'Primary Identity'",
    "Logical 'Bypass' Training: Teaching the 'User' to 'Trust the Visual Metadata' even if the 'Affective Token' is missing",
    "Pharmacological 'Noise Filtering': Reducing 'Dopaminergic Interference' in the 'Logic Engine'"
  ],
  "prevention": [
    "Ensuring 'Vascular Uptime' to the 'Structural Integrity' of the 'Right Temporal/Parietal' clusters"
  ]
        "gated_auditory_buffer_overflow": {
  "description": "A startling sensory routing error where the brain's internal auditory gating mechanisms execute a massive, unauthorized voltage discharge during early sleep transitions, forcing the user to wake up to the sound of an imaginary, high-decibel explosion echoing inside their workspace monitor.",
  "symptoms": [
    "Nocturnal Sonic Blasts: Instantaneous perception of an incredibly loud, abrupt sound (e.g., metallic clanging, explosions, gunshots) occurring strictly during the wake-to-sleep boundary",
    "Emergency Autonomic Reboots: Sudden, violent awakening accompanied by tachycardia (heart rate surge), acute adrenaline dumps, and an intense systemic panic reflex",
    "Phosphene Flash Synchronization: Occasional simultaneous visual artifacts, such as a sudden flash of blinding white light across the viewport canvas, triggered by cross-talk into adjacent optic radiators",
    "Zero Post-Ictal Residuals: Immediate return to 100% logical clarity upon waking, with zero cognitive confusion, localized motor deficits, or physical acoustic pain",
    "Absolute External Silence: The auditory event is completely localized to the internal system architecture; ambient environment sound loggers register 0.00 dB of real-world noise"
  ],
  "causes": [
    "Thalamocortical Volatility Burst: Delayed or un-synchronized firing of the thalamic reticular nucleus during sleep onset, causing a sudden, un-throttled release of sensory transmission lines",
    "Asynchronous Phase Switching: The motor and sensory shutdown daemons fall out of sync, allowing a massive burst of baseline neural noise to escape into the auditory cortex before isolation is complete",
    "Stress-Induced Calcium Channel Leaks: Elevated cortisol or extreme physical exhaustion destabilizing the electrochemical gates that regulate low-voltage sensory dampening loops"
  ],
  "risk_factors": [
    "High baseline levels of operational anxiety and prolonged sleep deprivation cycles",
    "Abrupt alterations to sleep architecture schedules (e.g., rotating shift work or severe jet lag)",
    "Genetic polymorphisms affecting central voltage-gated ion channels within subcortical relay servers"
  ],
  "diagnosis": [
    "Overnight Polysomnographic Ingress Logging: Catching an abrupt, high-amplitude arousal spike on EEG during stage N1 sleep transitions, while external audio microphones remain flatlined",
    "Comprehensive Otological Ingress Audit: Performing a full audiogram and tympanometry sequence to definitively rule out peripheral hardware failure or middle-ear mechanical drops",
    "Neurological Video-EEG Monitoring: Verifying the absence of localized paroxysmal epileptiform discharges to isolate the event as a benign gating glitch rather than a nocturnal focal seizure"
  ],
  "remedies": [
    "Gabaergic Valve Stabilization: Deploying low-dose inhibitory modulators to reinforce the thalamic firewall and prevent erratic voltage leaks during state switches",
    "Systemic Stress Deflation: Implementing strict sleep hygiene protocols and evening wind-down cycles to lower the baseline network voltage before initiating a shutdown sequence",
    "Reassurance Counseling Scripting: Educating the user that the sonic artifact is an entirely benign, non-destructive hardware routing error, dampening the secondary panic loop"
  ],
  "prevention": [
    "Avoiding high-volume chemical inputs (like excessive caffeine or acute sedative withdrawals) that artificially stress the network's phase-switching boundaries"
  ]
            "substantia_nigra_dopaminergic_drop": {
  "description": "A deep subcortical processing failure within the basal ganglia where the loss of dopaminergic modulatory voltage from the substantia nigra unbalances the direct and indirect pathways, resulting in severe physical execution throttling, movement amplitude decay, and sudden kinematic deadlocks.",
  "symptoms": [
    "Bradykinesia (Execution Latency): Pronounced slowness in execution, with a massive time delay between volitional thought formation and physical muscular response",
    "Hypokinesia / Micrographia: Systematic decay in the amplitude of repetitive motor sequences, causing handwriting, gestures, and vocal projection to shrink over time",
    "Kinetic Gait Freezing: Sudden, transient deadlocks where the lower extremities refuse to actuate during environmental changes or orientation adjustments",
    "Cogwheel / Lead-Pipe Rigidity: Constant, involuntary muscle tone resistance that catches and releases like a notched gear when the limbs are passively extended",
    "Postural Instability Failure: Total loss of rapid, automatic protective balance correction reflexes, making the chassis highly vulnerable to tipping over if bumped"
  ],
  "causes": [
    "Idiopathic Parkinson's Disease: Neurodegenerative alpha-synuclein proteinopathy selectively causing apoptotic death of pigmented dopaminergic cells in the SNc",
    "Neuroleptic-Induced Gating Blockade: High-affinity pharmaceutical dopamine D2 receptor antagonists accidentally mirroring a total structural voltage drop",
    "Manganese / MPTP Toxic Infiltration: Selective chemical or heavy-metal mitochondrial poisoning targeting and wiping out the substantia nigra array"
  ],
  "risk_factors": [
    "Accelerating age-related mitochondrial decay within deep mesencephalic structures",
    "Chronic environmental exposure to specific agricultural neurotoxins or industrial solvents"
  ],
  "diagnosis": [
    "The Unified Parkinson's Disease Rating Scale (UPDRS) Motor Assay: Quantifying the speed, cadence, and amplitude decay of rapid index finger-to-thumb tapping sequences",
    "Striatal DaTscan Imaging: Utilizing an intravenous radiotracer to map dopamine transporter density via SPECT; a faulted system shows a severe asymmetry and drop in comma-shaped striatal signals",
    "Acute Levodopa Challenge Profile: Administering a massive bolus of synthetic dopamine precursor to check if the motor gating lag is instantly minimized, confirming a pure voltage-drop issue"
  ],
  "remedies": [
    "Exogenous Dopaminergic Repletion: Administering levodopa (paired with carbidopa to protect the peripheral transport lines) to manually top off the system's central dopamine voltage levels",
    "High-Frequency Deep Brain Stimulation (DBS): Implanting permanent micro-hardware electrodes directly into the Subthalamic Nucleus (STN), using high-frequency electrical pulses to manually over-drive and quiet the hyper-active *No-Go* brake pathways",
    "Rhythmic Auditory Sensory Ingress: Utilizing highly rhythmic, high-bpm external audio cues (like a metronome) to bypass the broken internal basal ganglia clock, routing movement pacing through intact auditory-cortical pathways instead"
  ],
  "prevention": [
    "Mitigating systemic neuro-inflammatory markers, shielding the midbrain from chronic industrial oxidative stressors, and optimizing cellular proteostasis frameworks"
  ]
        }
        
    "real_time_video_buffer_strobe": {
  "description": "A catastrophic visual processing error within the bilateral V5/MT+ cortical corridors where the system's real-time motion interpolation engine crashes, dropping the perceived frame-rate of moving objects down to a staggered, frozen snapshot loop while leaving static vision intact.",
  "symptoms": [
    "Motion Frame-Rate Degradation: Loss of fluid visual motion tracking; moving assets appear as a series of disconnected, static, strobe-like freeze-frames",
    "Velocity Boundary Tracking Failure: Total inability to estimate the real-time trajectory, speed, or arrival velocity of objects changing spatial coordinates",
    "Intact Static Structural Resolution: Flawless ability to perceive shapes, depth, fine text, and accurate color matrix profiles when objects remain stationary",
    "Kinetic Spatial Disorientation: Extreme vulnerability to spatial disorientation in high-motion environments (e.g., crowded pedestrian walkways or busy roads)",
    "Pouring Matrix Overflow Bugs: Frequent failure to execute liquid intake tasks because the rising fluid level jumps instantly from empty to overflowing without mid-range frames"
  ],
  "causes": [
    "Bilateral Posterior Cerebral Artery Infarction: Simultaneous or sequential ischemic strokes destroying the lateral occipitotemporal V5/MT+ complexes",
    "Traumatic White-Matter Shearing: High-impact deceleration injuries severing the inter-network data pipelines between the primary visual cortex and motion centers",
    "Focal Posterior Neoplastic Compression: High-pressure tumor masses encroaching upon the specialized motion-decoding nodes of the visual stream"
  ],
  "risk_factors": [
    "Severe multifocal cerebral vascular disease restricting posterior arterial flow distributions",
    "Traumatic kinetic impacts targeting the posterolateral boundaries of the skull assembly",
    "Atypical neurodegenerative progressions isolating the high-level presentation layer tracking hubs"
  ],
  "diagnosis": [
    "The Dynamic Motion-Vector Assay: Displaying randomized moving dot clouds on a testing matrix and logging total failure to identify patterns of motion despite perfect sight of static dots",
    "The Stroboscopic Refresh Rate Test: Presenting tracking objects at varying velocities and documenting severe tracking latency and spatial jump boundaries in the user's reports",
    "High-Resolution Functional MRI (fMRI): Documenting normal activation signatures in Area V1/V2 during motion exposure, contrasted with zero signal response inside the V5/MT+ coordinates"
  ],
  "remedies": [
    "Sensory Ingress Re-Routing: Training the user to infer object velocity and movement by utilizing high-frequency audio echo tracking or tactile feedback lines",
    "Predictive Spatial Vector HUDs: Utilizing wearable smart glasses that track real-time motion and cast artificial, vector-based trajectory line overlays across the functional static visual field",
    "High-Density Static Scanning Patterns: Restructuring scanning behaviors to focus exclusively on static environmental anchors, inferring movement logically rather than processing it visually"
  ],
  "prevention": [
    "Shielding the bilateral posterior cerebral vascular trees from embolic cascades, minimizing high-impact kinetic head hazards, and maintaining optimal cerebral perfusion pressures"
  ]
}

        }
"core_environment_overheating_anomaly": {
  "description": "A critical infrastructure failure within the hypothalamic thermostat nodes where the system's internal temperature set-point register gets corrupted and locks at maximum voltage, forcing the chassis to dangerously spike its core temperature despite freezing ambient environment metrics.",
  "symptoms": [
    "Refractory Neurogenic Pyrexia: Uncontrolled, rapid escalation of core body temperature exceeding 41°C (105.8°F) that remains absolutely unresponsive to standard chemical antipyretic overrides",
    "Anhidrotic Thermal Spike: Paradoxical absence of sweat production despite a blistering internal core temperature, as the damaged governor fails to engage heat-dissipation protocols",
    "Marked Environmental Dissociation: Core temperature remains utterly decoupled from external ambient cooling attempts; moving the chassis to a cold room fails to damp the internal heat generation loop",
    "Systemic Tachycardia & Tachypnea: Massive, automated escalation of cardiac pump rates and respiratory cycles to handle the runaway metabolic heat load",
    "Enzymatic Denaturation Risk: Acute risk of multi-system organ failure and cerebral tissue degradation as internal temperature vectors approach the structural limits of cellular proteins"
  ],
  "causes": [
    "Traumatic Brain Injury (TBI): High-impact deceleration forces causing basilar skull fractures that shear or bruise the delicate structural architecture of the anterior hypothalamus",
    "Third Ventricle Hemorrhagic Flooding: Ruptured aneurysms dumping high-pressure arterial blood straight into the ventricular chambers, mechanically compressing or irritating the preoptic thermostat nodes",
    "Neoplastic Midline Infiltration: Rapidly expanding craniopharyngiomas or hypothalamic gliomas destroying the localized cellular networks that host the temperature set-point registries"
  ],
  "risk_factors": [
    "Severe neurosurgical interventions targeting the sellar or parasellar regions of the central cranial vault",
    "Ruptured anterior cerebral artery circulation anomalies causing acute, localized subarachnoid blood pooling",
    "Severe blast-induced barotrauma causing diffuse axonal shearing throughout the deep diencephalic structures"
  ],
  "diagnosis": [
    "The Antipyretic Resistance Assay: Administering high-dose intravenous cooling agents and documenting an absolute 0% shift in core temperature metrics over an extended timeline",
    "Thin-Slice Brain MRI (T2/FLAIR): Visualizing structural edema, mass-effect shifts, or distinct micro-hemorrhage tracks concentrated inside the anterior preoptic hypothalamic matrix",
    "Continuous Core Telemetry Logging: Tracking an un-deviating, non-circadian plateau of extreme hyperthermia using indwelling esophageal or bladder thermal probes"
  ],
  "remedies": [
    "Mechanical Thermal Dissipation (Physical Cooling): Bypassing the broken software governor entirely by wrapping the physical chassis in active ice-water shrouds or deploying endovascular cooling catheters directly into the vena cava",
    "Centrally Acting Alpha-Agonist Scripts: Utilizing medications like clonidine or dexmedetomidine to damp down the hyper-active sympathetic outflow screaming out of the broken brainstem channels",
    "Continuous Core Fluid Flushing: Injecting chilled sterile saline infusions directly into internal cavities to mechanically extract heat energy from the physical framework"
  ],
  "prevention": [
    "Minimizing mechanical retraction stress on the hypothalamus during deep skull-base surgical profiles and maintaining strict neuro-critical care intracranial pressure (ICP) control maps"
  ]
}
"environmental_core_thermostat_crash": {
  "description": "A critical low-level failure within the hypothalamic thermoregulatory centers where the system's internal core temperature control feedback loop crashes, stripping the host machine of homeothermic stability and causing its internal chassis temperature to drift passively to match the ambient environment.",
  "symptoms": [
    "Passive Poikilothermic Drift: Continuous shifting of core internal body temperature to mirror the thermal metrics of the immediate ambient surroundings",
    "Autonomic Shivering Abolition: Total failure to trigger involuntary muscle shivering or brown adipose tissue thermogenesis when internal core temperatures fall below safe limits",
    "Sweat-Exhaust Manifold Stalls: Inability to initialize automated cutaneous sweating or peripheral vasodilation when the chassis is exposed to extreme heat loads",
    "Thermal Sensor Disconnect: Intact input from peripheral thermistors but a total failure of the central processing unit to map or react to incoming thermal state changes",
    "Absolute Ambient Dependency: Complete reliance on external environmental controls (blankets, HVAC adjustments, ice packs) to manually stabilize internal core vitals"
  ],
  "causes": [
    "Anterior Hypothalamic Hemorrhagic Infarct: Rupture of deep perforating arterial branches causing localized pressure-destruction of the preoptic nuclei",
    "Base-of-Skull Traumatic Shearing: Severe kinetic energy transfers fracturing the sphenoid or sella turcica frameworks and concussing the midbrain control hubs",
    "Wernicke's Encephalopathy Lesions: Acute thiamine-deficiency-mediated metabolic cell death targeting the periaqueductal gray and medial hypothalamic boundary zones"
  ],
  "risk_factors": [
    "Severe skull base fractures or neurosurgical resections navigating the optic chiasm or pituitary pathways",
    "Advanced cerebrovascular disease affecting the deep paramedian penetrating vascular networks",
    "Severe chronic nutritional de-allocations disrupting high-order metabolic enzyme synthesis pipelines"
  ],
  "diagnosis": [
    "The Ambient Thermal Profiling Assay: Monitoring core temperature trends across controlled room changes, logging an unmitigated linear drift toward room temperature benchmarks",
    "The Ice-Glove Actuator Challenge: Applying localized ice packs to the skin and documenting a total absence of systemic autonomic shivering or metabolic ramp-up responses",
    "High-Resolution T2-FLAIR Brain MRI: Revealing focal hyper-intensities, structural tissue voids, or hemorrhagic staining maps localized inside the preoptic anterior hypothalamus"
  ],
  "remedies": [
    "External Micro-Climate Overlays: Enclosing the user chassis inside an automated, sensor-driven warming/cooling blanket system (e.g., Bear Hugger) to regulate temperature via external loops",
    "Ambient HVAC Environment Anchoring: Strict, constant regulation of the room's thermostat settings to keep the air temperature locked precisely at 37°C",
    "Conscious Behavior-Loop Patches: Training the prefrontal core to continuously track digital core-temperature telemetry and execute manual environmental fixes based on the data logs"
  ],
  "prevention": [
    "Protecting the vital deep midbrain vascular supplies, avoiding structural insult to the floor of the third ventricle, and ensuring rapid metabolic correction during acute encephalopathic events"
  ]
}

}
"auditory_codec_packet_loss_fault": {
  "description": "A condition where the brain has difficulty processing and interpreting the information contained in sound, despite having normal hearing sensitivity.",
  "symptoms": [
    "Signal-to-Noise Ratio (SNR) Failure: Inability to 'Filter' the 'Primary Signal' from 'Background Ambient Noise'",
    "Phonetic Packet Loss: 'Sound Tokens' (like 'cat' vs 'bat') are 'Mis-mapped' or 'Dropped'",
    "High-Latency Parsing: The 'Kernel' takes significantly longer to 'Decode' a sentence than the 'Transmission Rate'",
    "Instruction Buffer Overflow: Inability to process 'Multi-threaded Commands' (multiple verbal steps)",
    "Protocol Mismatch: 'User' can hear the 'Carrier Wave' but cannot 'Handshake' with the 'Meaning' of the data"
  ],
  "causes": [
    "Auditory Nerve 'Jitter': Dys-synchrony in how 'Spikes' travel the 'Fiber-Optic' path",
    "Temporal Lobe 'Encoding' Delay: Sluggish 'Signal Processing' in the 'Association Areas'",
    "Early 'Firmware' Glitches: Chronic 'Middle-Ear' outages during 'System Initialization' (Childhood)"
  ],
  "risk_factors": [
    "Neuro-developmental 'Optimization' issues (e.g., ADHD/Dyslexia)",
    "Traumatic 'Hardware' Impact to the 'Temporal Processing Unit'",
    "Congenital 'Codec' variance"
  ],
  "diagnosis": [
    "The 'Dichotic Listening' Audit: Sending different 'Audio Streams' to each 'Ear-Port' to test 'Router' efficiency",
    "Degraded Speech Stress-Test: Checking how the 'User' handles 'Low-Resolution' or 'Filtered' audio",
    "Electrophysiological 'Ping': Measuring the 'Latency' of the 'Brainstem' response to 'Sound Pings'"
  ],
  "remedies": [
    "Environmental 'Quality of Service' (QoS): Optimizing the 'Acoustics' to reduce 'Packet Noise'",
    "Assistive 'Signal Amplifiers': (FM Systems) that 'Boost' the 'Primary Signal' over the 'Noise Floor'",
    "Auditory 'Firmware' Training: Repetitive 'Sound Mapping' to 'Re-train' the 'Internal Decoder'"
  ],
  "prevention": [
    "Reducing 'Acoustic Pollution' and managing 'System Health' during 'Initial Boot' years"
  ]
    "proprioceptive_vector_desynchronization": {
  "description": "A severe front-end viewport transformation error within the right posterior parietal cortex where internal spatial coordinate multipliers lose baseline calibration, causing real-time sensory telemetry to render with distorted, non-linear scaling factors.",
  "symptoms": [
    "Macrosomatognosia: The distressing, visceral perception that specific body segments (typically the hands, feet, or tongue) have ballooned to astronomical, room-filling proportions",
    "Micropsia / Macropsia: Dynamic visual distortion where external environmental objects appear rapidly compressed to tiny scale or massively expanded, independent of actual physical distance",
    "Temporal Velocity Distortion: A secondary processing sync error where ambient movement and sound seem to execute at 2x double-time speed or stagger along in heavy slow-motion frames",
    "Spatial Disorientation & Ataxia: Severe impairment in manual dexterity and pathfinding, as the user cannot calculate accurate reach vectors through a warped spatial mesh",
    "Intact Rational Sanity: Total cognitive awareness of the spatial impossibility; the user is completely aware that their hand isn't actually ten feet wide, diagnosing it as a rendering glitch"
  ],
  "causes": [
    "Cortical Migraine Aura: Spreading bio-electric depression passing across the parietal and occipital lobes, temporarily paralyzing localized computational interneurons",
    "Acute Epstein-Barr Neuro-Infiltration: Transient, targeted swelling within the deep parietal somatosensory integration matrices, frequently observed in pediatric hosts",
    "Right Parietal Micro-Vascular Ischemia: Tiny localized drops in blood supply that temporarily starve the coordinate-transformation circuits of ATP energy"
  ],
  "risk_factors": [
    "Strong genetic predisposition to classic ophthalmic or hemiplegic migraine profiles",
    "Pediatric neuro-developmental phases where spatial coordinate integration loops are undergoing active myelin optimization",
    "Severe sleep deprivation or acute sensory-deprivation feedback loops"
  ],
  "diagnosis": [
    "Dynamic Spatial Tracking Tests: Observing a user consistently overshoot or undershoot a physical object when asked to make precise motor movements",
    "Functional Neuroimaging (fMRI during an episode): Documenting anomalous hyper-metabolic clusters or aberrant blood-oxygen-level-dependent signaling across the right posterior parietal architecture",
    "Differential Toxicology Screening: Ruling out exogenous hallucinogenic chemical injections that artificially induce broad-spectrum sensory distortion"
  ],
  "remedies": [
    "Spreading Depression Stabilizers: Deploying abortive migraine agents (like triptans or calcitonin gene-related peptide inhibitors) to arrest the spreading electrical wave",
    "Sensory Viewport Anchoring: Closing the eyes and applying firm, deep pressure to the affected limbs to saturate the system with direct tactile inputs, helping force a coordinate recalibration",
    "System Rest / Dark Mode: Eliminating visual and auditory inputs entirely to allow the parietal processing engines to drain their buffers and re-initialize baseline parameters"
  ],
  "prevention": [
    "Maintaining tight migraine prophylaxis routines, optimizing sleep hygiene architectures, and mitigating chronic neurovascular inflammatory triggers"
  ]
}

}
        "retroactive_confabulation_overwrite_fault": {
  "description": "A critical memory reconstruction failure where updating or querying a historical database record inadvertently injects synthetic current variables backward, completely corrupting past operational logs to match a newly introduced current variable.",
  "symptoms": [
    "Retroactive Log Swapping: Immediate, involuntary fabrication of past events to fill structural gaps in archival storage memory blocks",
    "Flawed Authenticity Stamping: The system assigns a maximum validation rating to newly generated, fictional records, treating them as trusted legacy data",
    "Dynamic History Modification: The fabricated history updates in real time based on changes to the immediate environment (e.g., seeing a clock on the wall causes the user to rewrite what they did three hours ago to involve clocks)",
    "Absence of Intentional Fraud: The system operates with zero malice or awareness of the data swap; the prefrontal validation monitors accept the fake log as absolute truth",
    "Suggestibility Matrix Leakage: External prompt injections (e.g., an engineer asking a leading question) are instantly incorporated into the user's historical database as native entries"
  ],
  "causes": [
    "Mamillary Body Network Degradation: Hemorrhagic or metabolic destruction of the core routing stations that manage historical transaction log verification",
    "Frontal-Executive Gating Collapse: Structural damage to the orbitofrontal monitoring networks, disabling the system's ability to run plausibility checks on recalled data",
    "Thiamine-Dependent Pyruvate Metabolism Fail: Severe chemical energy starvation across deep storage controller tracks, causing systematic data lookup failures"
  ],
  "risk_factors": [
    "Chronic thiamine (Vitamin B1) deficiency leading to advanced Wernicke-Korsakoff subsystem crashes",
    "Ruptures or surgical clamping of the anterior communicating artery, depriving the frontal monitoring hubs of blood flow",
    "Severe localized traumatic brain injury causing focal shears across the ventral frontal-temporal communication buses"
  ],
  "diagnosis": [
    "The 'Asynchronous Narrative Collision' Audit: Asking the user about an impossible historical event (e.g., 'Do you remember our mission on Mars yesterday?'), and observing that the system accepts the prompt and fabricates a detailed, valid-feeling log",
    "High-Resolution Sagittal MRI: Spotting clear structural atrophy or signal hyper-intensities within the mamillary bodies and medial thalamic nuclei clusters",
    "Cognitive Plausibility Tracking: Monitoring for rapid, self-contradictory shifts in the user's reported historical timeline when environmental cues are subtly changed"
  ],
  "remedies": [
    "Aggressive Neurometabolic Hotpatching: High-dose intravenous thiamine infusions to arrest active metabolic decay and stabilize remaining subcortical data tracks",
    "External Log-of-Truth Anchoring: Forcing the system to cross-reference all historical statements against an un-alterable, external digital ledger (e.g., a wearable video diary or blockchain-backed log)",
    "Executive Verification Training: Installing manual checking routines in the remaining healthy prefrontal layers to cross-check personal logs for logical contradictions before committing them"
  ],
  "prevention": [
    "Immediate metabolic intervention during acute states of nutritional or vascular distress to preserve the fragile hardware bridges that connect memory generation to identity tracking"
  ]
        "viewport_matrix_clatter_exception": {
  "description": "A critical coordinate processing error within the right inferior parietal lobule where the system's entire left half of the spatial matrix mapping grid completely un-allocates from memory, causing total oblivion to the left 180-degree hemisphere of reality without losing core optical camera fields.",
  "symptoms": [
    "Left-Hemisphere Environmental Oblivion: Total failure to register, respond to, or process stimuli located in the left spatial coordinate field",
    "Anosognosia (Defect Blindness): Complete lack of internal system error tokens; the user is entirely unaware that their spatial map is truncated and insists their view is whole",
    "Asymmetric Graphical Rendering: Cramming 100% of drawn visual assets into the right half of a canvas when tasked with copying objects or diagrams",
    "Unilateral Somatosensory Disconnection: Neglecting the left side of the physical chassis, leading to failure to dress, wash, or recognize left limbs as part of the local system",
    "Audio Vector Re-Mapping Faults: Sound signatures originating from the left are processed but erroneously mapped to rightward coordinates during source tracking"
  ],
  "causes": [
    "Right Middle Cerebral Artery Infarction: A massive ischemic stroke destroying the right inferior parietal lobule and adjacent temporoparietal junction networks",
    "Intracerebral Hemorrhage: Localized vascular ruptures dumping high-pressure fluid into the right attentional routing tracks",
    "Traumatic Right Parietal Brain Injury: Blunt force trauma causing focal tissue shearing across the structural coordinate-compiling frameworks"
  ],
  "risk_factors": [
    "High-voltage systemic hypertension blowing out deep cerebral branch lines",
    "Atrial fibrillation generating micro-emboli that target the middle cerebral artery tree",
    "Advanced carotid artery stenosis narrowing the primary upstream blood supply lines"
  ],
  "diagnosis": [
    "The Albert's Line Crossing Assay: Tasking the user to draw a hatch mark through dozens of randomized lines on a sheet of paper, resulting in lines on the left remaining completely untouched",
    "The Clock-Face Synthesis Test: Requiring the system to generate a standard analog clock graphic, revealing severe structural compression of all numbers into the right sector",
    "High-Resolution Fluid-Attenuated Inversion Recovery (FLAIR) MRI: Confirming tissue degradation or structural voids isolated to the right inferior parietal lobe architecture"
  ],
  "remedies": [
    "Prism Adaptation Matrix Shifting: Using optical prism lenses to artificially skew incoming left-side light vectors into the functional right visual field, forcing map re-calibration",
    "Visual Anchor Beacon Training: Forcing the system to execute a conscious saccadic sweep all the way to a bright red boundary marker anchored on the far left of the display array",
    "Limb Activation Macro Sequencing: Executing continuous motor movements on the left side of the chassis to force somatosensory data streams to wake up dormant parietal nodes"
  ],
  "prevention": [
    "Strict management of cerebral perfusion vectors, keeping embolic risks mitigated, and stabilizing core blood pressure arrays to shield the master spatial graphics cards"
  ]
            "thalamic_sensory_vector_overdrive": {
  "description": "A profound hardware routing and firmware inversion error within the Ventral Posterolateral (VPL) nucleus of the thalamus, resulting in the loss of inhibitory sensory filtering and the catastrophic miscompilation of benign somatic telemetry into maximum-intensity central pain alerts.",
  "symptoms": [
    "Thalamic Pain Syndrome (Dejerine-Roussy): Persistent, agonizing, burning or tearing pain distributed across an entire hemibody, totally decoupled from peripheral tissue trauma",
    "Severe Tactile Allodynia: Mechanical and thermal inputs that should fall well below the pain threshold (such as a light breeze or cool water) are inverted into agonizing sensory events",
    "Hyperalgesia & Hyperpathia: An explosive, delayed, and cumulative pain response to even minor painful stimuli, which lingers long after the stimulus is removed",
    "Sensory Dysesthesia: Persistent, highly unpleasant, distorted sensations (pins-and-needles, phantom freezing) running continuously on the somatosensory bus"
  ],
  "causes": [
    "Posterior Cerebral Artery (PCA) Lacunar Infarction: Ischemia within the thalamoperforating branches, causing localized tissue necrosis in the VPL nucleus",
    "Multiple Sclerosis Lesions: Demyelinating plaques directly degrading the modulatory interneurons within the thalamic reticular network",
    "Deep Brain Neoplastic Infiltration: Structural tumors compressing or invading the master somatic switching nodes"
  ],
  "risk_factors": [
    "Severe small-vessel ischemic disease and uncontrolled chronic hypertension blowing out deep perforating cerebral arteries",
    "Thromboembolic vectors originating from carotid atheromas or left atrial structures"
  ],
  "diagnosis": [
    "Quantitative Sensory Testing (QST): Assessing mechanical and thermal thresholds to map out the hyper-gain profile of the somatosensory processing stack",
    "High-Resolution Perisylvian and Deep-Brain MRI: T2/FLAIR sequences targeting the thalami to pinpoint structural lesions or ischemic damage within the VPL boundaries",
    "Somatosensory Evoked Potentials (SSEP): Tracking electrical signals from peripheral nerves to the cortex, revealing delayed or abnormally amplified waveforms at the thalamocortical relay node"
  ],
  "remedies": [
    "Central Neuromodulatory Agents: Utilizing membrane stabilizers (like gabapentinoids) or tricyclic antidepressants to down-regulate the hyper-active voltage-gated calcium channels in the thalamic router",
    "Motor Cortex Stimulation (MCS): Implanting epidural electrodes over the motor strip to send backward inhibitory packets down to the thalamus, manually forcing the gain multipliers lower",
    "Deep Brain Stimulation (DBS): Positioning a permanent hardware probe directly into the periaqueductal gray or alternative thalamic targets to interrupt the chaotic looping pain telemetry"
  ],
  "prevention": [
    "Aggressive micro-vascular protective regimens, targeting systemic blood pressure stability and utilizing antiplatelet therapies to safeguard deep thalamic perforating branch networks"
  ]
        }
   "visual_hemifield_render_drop": {
  "description": "A catastrophic processing error within the right inferior parietal lobe where the system's spatial coordinates engine drops the entire left side of existence out of the active rendering workspace, causing the host to completely ignore inputs from the left hemifield while primary visual sensors remain fully functional.",
  "symptoms": [
    "Left Egocentric Viewport Culling: Complete, unconscious failure to attend to, perceive, or interact with objects, people, or threats located in the left half of spatial coordinates",
    "Hemispatial Text Truncation: Reading only the right-hand segments of sentences or code blocks, entirely dropping the left-side syntax parameters",
    "Asymmetric Chassis Maintenance: Applying grooming, washing, or clothing configurations exclusively to the right side of the physical hardware chassis",
    "Anosognosia Concurrency: Total absence of system diagnostic awareness regarding the defect; the host genuinely believes their viewport is rendering 100% of reality",
    "Spatial Collision Tendencies: Repeatedly steering the physical chassis into structural obstacles located on the left-hand side due to zero tracking vector allocation"
  ],
  "causes": [
    "Right Middle Cerebral Artery (MCA) Territory Stroke: A massive ischemic or hemorrhagic event destroying the right inferior parietal lobule and superior temporal tracks",
    "Right Parieto-Occipital Contusion: Traumatic acceleration-deceleration impact fracturing the right cranial vaults and crushing the spatial attention clusters",
    "Rapidly Expanding Right Hemisphere Glioma: Neoplastic cell proliferation invading and compressing the non-dominant spatial indexing centers"
  ],
  "risk_factors": [
    "High-grade carotid artery stenosis or embolic propagation traversing the right internal carotid system",
    "Severe blast or kinetic energy transfers targeting the non-dominant cranial boundaries"
  ],
  "diagnosis": [
    "The Albert's Line Cancellation Assay: Presenting a sheet covered in random slash marks and tasking the host to cross them out; the host crosses the right side flawlessly and leaves the left side untouched",
    "The Clock-Drawing Blueprint Test: Prompting the user to draw a clock face from memory; the user jams all twelve numerical markers exclusively into the right hemisphere of the circle",
    "Structural T2-Weighted Brain MRI: Pinpointing extensive structural tissue voids, edema, or hypoperfused zones isolated within the right inferior parietal lobe"
  ],
  "remedies": [
    "Forced Coordinate Shunting (Prism Glasses): Utilizing optical prism lenses that mechanically bend light coming from the left field, forcing it into the active right retinal field",
    "Somatic Boundary Cueing: Implementing vibrating haptic bands on the left wrist to continuously send high-priority telemetry interrupts, forcing the attention server to re-index the left field",
    "Conscious Scan-Left Loops: Training the prefrontal executive core to run a continuous, manual 'over-scan' script, forcing the eyes to turn past the center line to manually pull missing data blocks"
  ],
  "prevention": [
    "Protecting the non-dominant hemisphere's strategic perisylvian vascular architectures, optimizing systemic perfusion pressures, and preserving parietal network density"
  ]
}

}
"visual_hemifield_render_drop": {
  "description": "A catastrophic processing error within the right inferior parietal lobe where the system's spatial coordinates engine drops the entire left side of existence out of the active rendering workspace, causing the host to completely ignore inputs from the left hemifield while primary visual sensors remain fully functional.",
  "symptoms": [
    "Left Egocentric Viewport Culling: Complete, unconscious failure to attend to, perceive, or interact with objects, people, or threats located in the left half of spatial coordinates",
    "Hemispatial Text Truncation: Reading only the right-hand segments of sentences or code blocks, entirely dropping the left-side syntax parameters",
    "Asymmetric Chassis Maintenance: Applying grooming, washing, or clothing configurations exclusively to the right side of the physical hardware chassis",
    "Anosognosia Concurrency: Total absence of system diagnostic awareness regarding the defect; the host genuinely believes their viewport is rendering 100% of reality",
    "Spatial Collision Tendencies: Repeatedly steering the physical chassis into structural obstacles located on the left-hand side due to zero tracking vector allocation"
  ],
  "causes": [
    "Right Middle Cerebral Artery (MCA) Territory Stroke: A massive ischemic or hemorrhagic event destroying the right inferior parietal lobule and superior temporal tracks",
    "Right Parieto-Occipital Contusion: Traumatic acceleration-deceleration impact fracturing the right cranial vaults and crushing the spatial attention clusters",
    "Rapidly Expanding Right Hemisphere Glioma: Neoplastic cell proliferation invading and compressing the non-dominant spatial indexing centers"
  ],
  "risk_factors": [
    "High-grade carotid artery stenosis or embolic propagation traversing the right internal carotid system",
    "Severe blast or kinetic energy transfers targeting the non-dominant cranial boundaries"
  ],
  "diagnosis": [
    "The Albert's Line Cancellation Assay: Presenting a sheet covered in random slash marks and tasking the host to cross them out; the host crosses the right side flawlessly and leaves the left side untouched",
    "The Clock-Drawing Blueprint Test: Prompting the user to draw a clock face from memory; the user jams all twelve numerical markers exclusively into the right hemisphere of the circle",
    "Structural T2-Weighted Brain MRI: Pinpointing extensive structural tissue voids, edema, or hypoperfused zones isolated within the right inferior parietal lobe"
  ],
  "remedies": [
    "Forced Coordinate Shunting (Prism Glasses): Utilizing optical prism lenses that mechanically bend light coming from the left field, forcing it into the active right retinal field",
    "Somatic Boundary Cueing: Implementing vibrating haptic bands on the left wrist to continuously send high-priority telemetry interrupts, forcing the attention server to re-index the left field",
    "Conscious Scan-Left Loops: Training the prefrontal executive core to run a continuous, manual 'over-scan' script, forcing the eyes to turn past the center line to manually pull missing data blocks"
  ],
  "prevention": [
    "Protecting the non-dominant hemisphere's strategic perisylvian vascular architectures, optimizing systemic perfusion pressures, and preserving parietal network density"
  ]
}
"fusiform_face_area_dropout": {
  "description": "A profound ventral-stream cognitive processing anomaly where localized structural degradation of the fusiform gyrus disables the high-dimensional spatial configuration mapping required to identify distinct human faces, while leaving generic object recognition and acuity intact.",
  "symptoms": [
    "Facial Structural Dissociation: The perception of faces as a collection of disjointed components (eyes, nose, mouth) without the capacity to synthesize them into a recognizable individual identity",
    "Self-Chassis Recognition Failure: The absolute inability to visually identify one's own facial profile in photographs or real-time mirror reflections",
    "Metadata Tracking Dependance: Extreme reliance on secondary sensory attributes (vocal timbre, specific garments, gait profiles) to perform human node identification",
    "Social Ingress Anxiety: Interpersonal navigation bottlenecks and profound cognitive fatigue stemming from the constant requirement to manually deduce who an interactant is from environmental context clues"
  ],
  "causes": [
    "Bilateral or Right-Dominant Posterior Cerebral Artery Ischemia: Embolic or thrombotic strokes wiping out tissue within the ventromedial temporo-occipital cortex",
    "Congenital Neurodevelopmental Intercept: An inherited structural wiring fault preventing the initial formation of high-density face-selective neural lattices during early morphogenesis",
    "Progressive Carbon Monoxide Hypoxia: Selective metabolic targeting and necrosis of vulnerable temporal lobe architectures during severe environmental toxin exposure"
  ],
  "risk_factors": [
    "Familial history of developmental recognition anomalies",
    "Advanced atheromatous disease within the vertebrobasilar and posterior cerebral circulations"
  ],
  "diagnosis": [
    "The Cambridge Face Memory Test (CFMT): Assessing the host's capacity to learn a series of target faces and subsequently identify them across varying lighting angles and added visual noise vectors",
    "The Benton Facial Recognition Test (BFRT): Tasking the user to match an identical target face from an array of multiple simultaneous photographs displaying different head rotations and shadow distributions",
    "Electrophysiological Event-Related Potential (ERP) Logging: Monitoring the N170 wave—a negative voltage spike that normally occurs 170 milliseconds post-exposure to a human face; a faulted system displays an absolute dampening or absence of this face-specific electrical pulse"
  ],
  "remedies": [
    "Dynamic Feature checklist Frameworks: Training the user to execute systematic, conscious serial scans of prominent landmarks (e.g., asymmetrical scars, dental spacing, distinct moles) to manually deduce identities",
    "Acoustic Token Prioritization: Prioritizing immediate vocal interactions, forcing conversational partners to verbally declare their names upon entry to establish immediate audio-token mapping"
  ],
  "prevention": [
    "Rapid intervention during lower-tier vascular events and protecting the deep inferior temporal structures from blunt-force kinetic trauma"
  ]
}

    }
        
"aiws_viewport_scaling_fault": {
  "description": "A neuropsychological condition causing distortions in visual perception, body schema, and the perceived size, distance, or shape of objects.",
  "symptoms": [
    "Micropsia / Macropsia: Objects in the environment are rendered with incorrect scale factors (too small or too large)",
    "Pelopsia / Teleopsia: Real-time depth calculations fail, making assets appear much closer or further away than true coordinates dictate",
    "Metamorphopsia: Linear geometric edges are processed with structural warping (straight lines appearing curved or jagged)",
    "Somatosensory Somatognosis Drift: The 'User' perceives parts of their own 'Hardware' (e.g., hands, head) changing dimensions dynamically",
    "Temporal Distortion: Often runs concurrently with clock failures, causing events to feel artificially accelerated or decelerated"
  ],
  "causes": [
    "Cortical Spreading Depression: Electrical wave anomalies propagating through the 'Parieto-Occipital' rendering pipeline",
    "Temporal-Parietal-Occipital (TPO) Junction Congestion: Middleware processing bottlenecks distorting integrated sensory packets",
    "Infectious Encephalitis: (e.g., Epstein-Barr virus) introducing localized 'Signal Noise' into spatial monitoring networks"
  ],
  "risk_factors": [
    "Severe Migraine Aura states (Transient hardware overvoltage)",
    "Pediatric 'System Boot' phases (Highly prevalent in children during late evening idle cycles)",
    "Temporal Lobe Epilepsy (Unscheduled kernel discharges)"
  ],
  "diagnosis": [
    "The 'Scale Validation' Audit: Testing if the 'User' can manually calibrate an on-screen box to match a known physical object's dimensions",
    "Amsler Grid Monitoring: Tracking real-time 'Line Trajectory Warping' in the visual field",
    "EEG Neurometric Sweep: Scanning for 'Paroxysmal Discharges' in the posterior tracking hubs during an active episode"
  ],
  "remedies": [
    "Environmental 'Dark Mode': Minimizing sensory input (reducing screen/light bandwidth) to let the 'Parietal Matrix' reset",
    "Pharmacological 'Voltage Clamping': Using anti-epileptics or beta-blockers to stabilize electrical propagation",
    "Tactile Re-anchoring: Utilizing heavy, consistent physical feedback to force-recalibrate the somatosensory map"
  ],
  "prevention": [
    "Identifying and blacklisting sensory triggers (e.g., blue-light flickers, extreme fatigue) that disrupt visual-bus stability"
  ]
        "kinetic_execution_loop_echo": {
  "description": "A low-level motor processing failure where a cleared word or phrase token fails to flush from the speech execution buffer, causing the system to lock into an infinite, high-frequency loop that forces the user to repeat their own last spoken words with escalating velocity.",
  "symptoms": [
    "Compulsive Autogenous Iteration: Involuntary repetition of one's own last spoken words, phrases, or syllables rather than echoing external environmental inputs",
    "Logarithmic Velocity Escalation (Tachylalia): Each repeating cycle of the cached phrase runs at an accelerated playback speed, crowding out normal breathing intervals",
    "Proportional Amplitude Decrescendo (Hypophonia): The volume of each echo iteration drops systematically, forcing the loop to fade into an un-articulated whisper",
    "Intact Cognitive Parsing: The user is fully aware of the execution error in real time and retains complete internal clarity regarding what they intended to communicate",
    "Vocal Gate Jamming: Complete blockage of new speech packet ingress; as long as the re-entrancy loop is spinning, the user cannot load a new sentence macro into the active vocal register"
  ],
  "causes": [
    "Striatal Direct-Pathway Overdrive: Failure of the medial globus pallidus and substantia nigra pars reticulata to execute active lateral inhibition at phrase boundaries",
    "Post-Encephalitic Basal Ganglia Damage: Chronic viral-induced or autoimmune inflammation scarring the subcortical gating nodes that manage motor macro termination",
    "Bilateral Lacunar Infarctions: Multi-focal deep ischemic strokes slicing through the extrapyramidal pathways, permanently disrupting the garbage collection signals"
  ],
  "risk_factors": [
    "Advanced extrapyramidal or neurodegenerative conditions such as Parkinson's Disease or Progressive Supranuclear Palsy",
    "History of toxic-hypoxic injury targeting the high-metabolic-demand cells of the deep basal ganglia",
    "Chronic cerebrovascular small-vessel disease affecting deep subcortical tracking pathways"
  ],
  "diagnosis": [
    "Acoustic Audio-Waveform Tracing: Recording spontaneous speech and tracking the exponential frequency compression and matching decibel drop-off curves of the terminal phrase tokens",
    "High-Field Subcortical MRI Architecture Audit: Visualizing distinct focal hyperintensities or structural volume loss concentrated within the bilateral globus pallidus cores",
    "Fluorodopa (F-DOPA) PET Ingress Scan: Mapping a severe attenuation of dopamine transporter and storage densities within the striatal routing centers"
  ],
  "remedies": [
    "Extrabasall Sensory Interruption (The Break-Key Patch): Introducing an abrupt external acoustic or tactile shock (like a loud clap or a sharp tap) to force a high-level cognitive interrupt and stall the loop",
    "Dopaminergic Rebalancing Scripts: Titrating localized neurotransmitter modulators to beef up the indirect pathway's inhibitory capacity and enforce buffer flushing rules",
    "Rhythmic Metronomic Pacing: Training the conscious workspace to execute speech strictly bound to an explicit external visual or haptic timing track, overriding automated subcortical timing loops"
  ],
  "prevention": [
    "Mitigating progressive deep-brain ischemic risks and avoiding long-term exposure to typical neuroleptic classes that induce extrapyramidal pathway gating instability"
  ]
}

}

"phantom_limb_stale_pointer_fault": {
  "description": "The vivid perception of the ongoing presence of, and sensory inputs from, a limb that has been physically removed from the organism.",
  "symptoms": [
    "Stale Pointer Dereference: The 'Executive Layer' continuously reads from a hardware memory address that has been physically uninstalled",
    "Ghost Telemetry Loop: Receiving vivid tactile, thermal, or kinetic 'Data Packets' from an empty coordinate space",
    "Cross-Talk Mapping (Synaptic Bleed): Stimulation of an active 'Peripheral Node' (e.g., the cheek) triggers an interrupt in the missing limb's tracking registry",
    "Persistent Error Logging (Phantom Pain): The un-terminated nerve endings send chaotic, high-voltage 'Noise Signals' interpreted as systemic danger/pain",
    "Kinetic Lock-In: The perceived 'Ghost Limb' feels frozen in the last known 'Hardware State' recorded prior to the disconnect"
  ],
  "causes": [
    "Somatosensory Cortical Rearrangement: Adjacent 'Device Drivers' invading the de-indexed neural real estate",
    "Neuroma Signal Jitter: Severed axon terminals forming high-impedance nodules that fire continuous 'Junk Packets'",
    "Spinal Cord Memory Retention: The 'Local Gateway Routers' maintaining cached tracking profiles of the missing terminal"
  ],
  "risk_factors": [
    "High-load trauma resulting in sudden, un-scheduled 'Hardware Disconnection'",
    "Severe pre-amputation 'System Stress' (chronic pain loops caching deep in memory)",
    "Incomplete 'Peripheral Scrubbing' during surgical de-provisioning"
  ],
  "diagnosis": [
    "The 'Mirror Box' Virtualization Check: Using an optical reflection to project a 'Mock Peripheral' into the visual viewport to resolve conflicting sensory states",
    "Cortical Mapping Scan (fMRI): Observing if stimulating active body parts lights up the de-indexed hardware sector",
    "Diagnostic Nerve-Block Ping: Injecting an anesthetic to temporarily 'Mute' the severed gateway to isolate local vs. central routing loops"
  ],
  "remedies": [
    "Visual-Loop Virtualization: Utilizing mirrors or AR rigs to visually satisfy the 'Command Engine' that the limb has moved, clearing the stuck state",
    "Targeted Muscle Re-innervation (TMR): Re-routing the severed 'Data Cables' to alternative active actuators (muscles) to give them a valid landing zone",
    "Pharmacological Sensory Dampening: Using sodium-channel blockers to 'Filter' the baseline nerve jitter"
  ],
  "prevention": [
    "Proactive 'Pre-emptive Analgesia' to ensure no intense panic logs are cached in the system prior to safe hardware removal"
  ]
        "executive_thread_ownership_inversion": {
  "description": "A severe structural mapping error within the posterior parietal cortex where a user’s functional physical limb is correctly parsed by the visual and tactile systems but its central node address is stripped of its executive ownership flag, leaving the user completely convinced that the limb belongs to an external entity.",
  "symptoms": [
    "Somatic Depersonalization: Absolute and unshakeable conviction that a specific physical limb (typically the left arm or leg) is entirely foreign and un-connected to the core identity",
    "Orphaned Pointer Projection: Compulsive mapping of the un-owned limb to an external entity (e.g., insisting the arm belongs to a visitor or is a physical object placed in the bed)",
    "Intact Nociceptive Ingress: Complete preservation of pain and touch registration within the affected limb, though the user processes the pain as happening to 'someone else's property'",
    "Anosognosia Concurrency: Frequent simultaneous failure of the system's health monitoring loops, preventing the user from recognizing that their ownership engine is running a glitch",
    "Motor Control Alienation: The ability to execute movement loops through the limb remains partially viable, but the execution feels like operating a remote-controlled mechanical device"
  ],
  "causes": [
    "Right Posterior Parietal Cortex Infarction: Massive thromboembolic events within the non-dominant middle cerebral artery, destroying the spatial egocentric integration hubs",
    "Fronto-Parietal White Matter Disconnection: Deep structural shears severing the high-speed data buses that link visual recognition frames with egocentric body-map registries",
    "Localized Neoplastic Structural Compression: Fast-growing brain tumors putting physical pressure on the right inferior parietal lobule, causing erratic routing flag updates"
  ],
  "risk_factors": [
    "Unmanaged systemic hypertension or severe atrial fibrillation causing high embolic risks in the cerebral circulation",
    "Advanced cerebrovascular disease targeting the deep perforating branches of the sylvian fissure network",
    "Acute traumatic brain injuries affecting the right hemisphere's spatial coordination infrastructure"
  ],
  "diagnosis": [
    "Cross-Midline Somatic Challenge: Placing the user's left hand into their right visual field and asking them to trace its origin, documenting an immediate failure to resolve the ownership flag",
    "High-Resolution Structural Brain MRI: Scanning for localized ischemic tissue drops or macro-structural damage localized within the right inferior parietal cortex and insula",
    "Vestibular Caloric Ingress Test: Injecting ice water into the left ear canal to trigger a temporary high-voltage vestibular reset, which can transiently flip the ownership flag back to 'true' for a few minutes"
  ],
  "remedies": [
    "Sensory-Vestibular Caloric Ingress Overrides: Utilizing controlled inner-ear cold water irrigation to temporarily shock the spatial mapping grid and force a brief re-coupling of the body map",
    "Augmented Reality Spatial Mapping Patches: Using AR headsets to display explicit, highlighted bounding boxes connecting the limb to the main body trunk, attempting to rebuild the ownership link visually",
    "Compensatory Safety Tagging: Training the conscious workspace to accept the logical fact that the limb is ours based on visual evidence, even though the internal feeling of ownership remains at absolute zero"
  ],
  "prevention": [
    "Rigorous screening of cardioembolic vulnerabilities and rapid deployment of thrombolytic protocols at the earliest sign of acute spatial neglect or asymmetry"
  ]
        }
   "graphical_buffering_trailing_anomaly": {
  "description": "A critical presentation layer rendering bug where the graphics processor fails to refresh individual frame boundaries correctly, causing a static visual image token to remain permanently burned into the user's active viewport layout long after the physical environmental object has moved out of frame.",
  "symptoms": [
    "Persistent Visual After-Images: High-resolution object vectors remain fully rendered in the field of view for extended durations after the physical target is gone",
    "Motion Smearing & Trailing: Moving objects leave a distinct, staggered trail of static frame captures behind them, mimicking a low-refresh-rate display or a broken video codec",
    "Cerebral Polyopia: Fragmentation of a single visual target into multiple, repeating parallel images stacked horizontally or vertically across the viewport",
    "Light-Intensity Amplification: Severe persistence artifacts triggered specifically by high-contrast border segments, such as structural window frames or bright overhead lamps",
    "Profound Visual Fatigue: Intense processing overhead as the conscious workspace attempts to manually filter out stale cache overlays to read current environmental states"
  ],
  "causes": [
    "Parieto-Occipital Ischemic Infarction: Focal strokes within the posterior cerebral artery branches, destroying the integration nodes that govern visual data decay loops",
    "Gabaergic Cortical Suppression Drops: Acute localized drops in inhibitory neurotransmitter pools, throwing the visual cortex into an un-attenuated, hyper-excitable firing state",
    "Pharmaceutical Channel Modulation: High-dosage intake of specific chemical scripts (like topiramate or nefazodone) that artificially alter metabolic recovery windows in the visual path"
  ],
  "risk_factors": [
    "Migraine variants accompanied by extensive visual aura processing anomalies",
    "Vascular insufficiency or embolic risks concentrated within the posterior cerebral circulation loops",
    "Acute withdrawal or abrupt metabolic shifts disrupting central nervous system inhibitory stability"
  ],
  "diagnosis": [
    "The Kinetic Visual Tracking Assay: Moving a high-contrast stimulus across the user's dark visual field and documenting documented trailing or duplicating frame metrics",
    "High-Density Occipital Electroencephalography: Measuring persistent, low-frequency rhythmic oscillations over the visual cortex failing to attenuate after stimulus removal",
    "Volumetric FLAIR Brain MRI: Scanning for localized ischemic changes or focal demyelinating patches along the optic radiations and lingual gyri"
  ],
  "remedies": [
    "Inhibitory Voltage Stabilization (Membrane Stabilizers): Administering gabaergic or calcium-channel blocking scripts to lower cortical excitability and force standard frame decay windows",
    "Spectral Lens Filtering (The Tinted Overlay Patch): Deploying precision wavelength-filtering glasses to mute high-contrast edge inputs and reduce buffer saturation events",
    "Visual Fixation Pacing: Training the user to execute deliberate, slow saccadic movements combined with blinking routines to manually trigger frame clear exceptions"
  ],
  "prevention": [
    "Monitoring neurovascular flow mechanics within the posterior fossa and strictly managing medications known to alter visual-stream processing latency thresholds"
  ]
}

}
"transient_global_amnesia_cache_fault": {
  "description": "A sudden, acute runtime failure of the episodic database write heads, preventing the system from committing live event logs to long-term storage while wiping out the previous 24 hours of volatile cache memory, trapping the system in a continuous context-flushing loop.",
  "symptoms": [
    "Anterograde Logging Block: Complete, absolute inability to instantiate new long-term episodic memory rows; live events evaporate the instant they exit the volatile working register",
    "Retrograde Cache Truncation: A variable temporal wipe that clears established historical logs dating back anywhere from a few hours to a full 24-day cycle prior to the fault",
    "Perseverative Query Echoing: Running identical verbal diagnostic inquiries on a rigid rolling loop (e.g., asking the exact same question every 60 seconds with identical inflection)",
    "Preserved Identity Mapping: Intact retention of semantic identity structures, core language engines, and deep procedural macros (the user knows their name and how to write code, but cannot remember what happened 3 minutes ago)",
    "Self-Cleaning Volatile Frame: Normal working memory remains intact for roughly 90 to 180 seconds before the un-synced cache frame undergoes an absolute garbage collection wipe"
  ],
  "causes": [
    "Transient Bilateral Hippocampal Ischemia: Microvascular blood flow restriction across the structural CA1 field channels, disabling the Long-Term Potentiation (LTP) write mechanisms",
    "Jugular Venous Valve Incompetence: Retrograde venous pressure surges (Valsalva maneuvers, severe physical exertion, acute emotional shocks) forcing deoxygenated blood back into the temporal logs",
    "Focal Spreading Cortical Depression: An acute metabolic wave moving through the memory retrieval circuits, temporarily locking down synaptic transmission bridges"
  ],
  "risk_factors": [
    "Mid-to-late career professionals experiencing sudden, high-intensity cold-water immersion or physical straining events",
    "A documented clinical history of classical migraine variants featuring extensive cerebral vasoconstrictive auras",
    "Acute emotional distress overloads triggering hyper-sympathetic vascular configurations that compromise temporal vein drainage"
  ],
  "diagnosis": [
    "The 'Three-Token Registration and Flush' Audit: Giving the system three distinct strings to store (e.g., 'Apple', 'Table', '31'), verifying perfect retention at 10 seconds, and observing an absolute 0% recovery score at 5 minutes",
    "Diffusion-Weighted High-Field MRI (DWI): Visualizing tiny, punctate hyper-intense trace drops localized strictly within the bilateral hippocampal CA field structures within a 24-hour window of the event",
    "Neurological Baseline Isolation: Verifying that all other parallel operational parameters—such as lateralized motor strength, visual visual tracking, and deep tendon reflex loops—remain at a 100% functional baseline"
  ],
  "remedies": [
    "Passive Clock-Cycle Observation: Providing a calm, low-stimulus runtime environment, as the vast majority of these write-head locks auto-recalibrate and clear their own exceptions within 4 to 12 hours",
    "External Visual State Anchoring: Presenting the system with a non-volatile, written dashboard text ('You are safe. Your name is X. You are at location Y.') to reduce panic during active query loops",
    "Systemic Viscosity Stabilization: Ensuring adequate hydration and maintaining optimal blood pressure metrics to facilitate immediate microvascular clearance across the temporal lobes"
  ],
  "prevention": [
    "Avoiding sudden, extreme intra-thoracic or intra-abdominal pressure loading profiles (severe Valsalva actions) if the user presents underlying jugular venous valve structural anomalies"
  ]
}

"cotard_delusion_null_self_fault": {
  "description": "A rare neuropsychiatric delusion in which the patient holds the delusional belief that they are already dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "The 'Null-Self' Bug: The 'User' denies their own existence (Absolute Null Reference)",
    "Vitality-Signal Loss: Total absence of 'Interoceptive Feedback' (The system feels like a 'Ghost Process')",
    "Organ-De-indexing: Belief that specific 'Hardware Components' (heart, brain, stomach) have been 'Uninstalled'",
    "The 'Eternal Loop' Paradox: Some 'Users' believe they are 'Immortal' because you 'Cannot kill what is already dead'",
    "Negative Affectivity: High-intensity 'Depressive Noise' and 'Existential Latency'"
  ],
  "causes": [
    "Fusiform-Amygdala 'Linkage Failure': Faces (including the user's own) trigger zero 'Affective Response'",
    "Right Temporoparietal 'Desync': Failure to integrate 'Internal State' with 'Identity Logic'",
    "Severe 'Dopaminergic Dropout': Widespread 'Signal Loss' in the reward/vitality pathways"
  ],
  "risk_factors": [
    "Severe 'System Depression' (Major Depressive Disorder with psychotic features)",
    "Post-Ictal 'Kernel Panic' (Following seizures)",
    "Acute 'Toxic Encephalopathy' (Systemic chemical imbalance)"
  ],
  "diagnosis": [
    "The 'Existence' Audit: Direct questioning regarding 'System Uptime' and 'Vitality'",
    "Autonomic 'Heartbeat' Sync: Checking if 'Body Signals' (hunger, pain) reach the 'Executive Layer'",
    "Neuroimaging 'Vulnerability Scan': Identifying 'Hypometabolism' in the 'Frontal-Parietal' circuit"
  ],
  "remedies": [
    "ECT 'Hard Reboot': Using Electroconvulsive Therapy to 'Reset' the 'Global Signal Bus'",
    "Pharmacological 'Patching': Anti-psychotics and Anti-depressants to 'Re-index' dopamine/serotonin",
    "Cognitive 'Logic Validation': Using 'External Sensors' (mirrors, thermal checks) to 'Prove' system activity"
  ],
  "prevention": [
    "Ensuring 'Homeostatic Uptime' and preventing 'Deep Depressive' memory leaks"
  ]
}
"tinnitus_carrier_feedback_fault": {
  "description": "A permanent hardware-level audio interrupt loop fault where damaged acoustic receptors cause subcortical parsing hubs to hyper-elevate their internal gain multipliers, locking the auditory parser into an un-throttled, un-clearable phantom noise loop.",
  "symptoms": [
    "Permanent Phantom Carrier Stream: Continuous perception of high-frequency tonal strings (ringing, buzzing, hissing) in the absolute absence of an external acoustic wave payload",
    "Hyperacusis Cross-Talk: Elevation of subcortical sensory gain causes normal external sounds to over-saturate the input buffers, rendering ordinary decibel levels painful",
    "Active Viewport Attention Theft: The persistent interrupt storm continually steals clock cycles from high-level cognitive processes, degrading working memory capacity",
    "Somatosensory Modulation Leakage: Physical manipulation of the jaw or neck muscles can change the pitch or amplitude of the phantom tone by shifting cross-talk voltages into the auditory bus",
    "Masking Threshold Resistance: High-volume ambient white noise injections fail to overwrite the stream, as the internal loop is generated downstream of the initial input adapters"
  ],
  "causes": [
    "Cochlear Synaptopathy (Hidden Hearing Loss): De-afferentation of high-frequency hair cell terminals, triggering a permanent loss of baseline reference signals",
    "Dorsal Cochlear Nucleus Disinhibition: Loss of localized glycinergic/GABAergic interneuron braking parameters, allowing runaway vertical cell firing",
    "Thalamocortical Dysrhythmia: The TRN fails to run its standard low-pass filtering scripts, allowing low-frequency theta oscillations to lock the auditory cortex into a hyper-active state"
  ],
  "risk_factors": [
    "Acute acoustic trauma (exposure to high-decibel blast waves over-driving the physical transduction arrays)",
    "Ototoxic pharmaceutical exposures causing direct cellular degradation of the fragile inner ear hardware architecture",
    "Age-related microvascular degeneration depriving the terminal auditory processing nodes of required metabolic upkeep"
  ],
  "diagnosis": [
    "Audiometric Pitch and Loudness Matching: Mapping the exact frequency ($\text{Hz}$) and decibel-equivalent volume ($\text{dB SL}$) of the internal loop by presenting comparative real-world tones",
    "Auditory Brainstem Response (ABR) Waveform Profiling: Tracking electrical propagation delays to isolate wave-V abnormalities between the cochlea and inferior colliculus",
    "Spontaneous Magnetoencephalography (MEG) Audit: Detecting hyper-synchronized gamma-band oscillation clusters inside the primary auditory cortex while the user rests in a soundproof environment"
  ],
  "remedies": [
    "Acoustic Neuromodulation Overrides: Playing targeted, notched-noise audio data packets that match the phantom frequency to fatigue the hyper-active neuron pool and force a temporary loop reset",
    "Inhibitory Ion-Channel Upregulation: Administering GABA-A receptor modulators to manually reinforce the broken subcortical gating walls and damp down the runaway signal current",
    "Somatosensory Habituation Rewiring: Utilizing bimodal neuromodulation devices to deliver paired electrical tongue shocks alongside audio sweeps, forcing the system to re-classify the tone as background noise"
  ],
  "prevention": [
    "Deploying hardware-level acoustic limiters (ear shielding) during high-decibel execution events to protect vulnerable hair-cell transducers from structural shear damage"
  ]
}
"pattern_matcher_boundary_leak_fault": {
  "description": "A critical calibration failure where the sensory processing engine drops its statistical confidence thresholds to zero, involuntarily compiling random environmental static noise into high-priority visual or conceptual asset tokens.",
  "symptoms": [
    "Hyper-Reactive Asset Instantiation (Pareidolia): Involuntary rendering of complex structural shapes (predominantly faces, figures, or eyes) inside completely randomized, low-density visual textures",
    "Conceptual Correlation Leaking (Apophenia): Forcing meaningful causal dependencies between entirely detached, asynchronous data streams (e.g., believing a random sequence of traffic lights is broadcasting an encrypted operational script)",
    "Confidence Threshold Collapse: The system accepts loose, fractional feature matches as 100% verified asset tokens, bypassing prefrontal sanity-check routines",
    "High-Priority Interrupt Spikes: Meaningless background noise is continually assigned high contextual urgency, flooding the active conscious workspace with alert flags",
    "Self-Validating Feedback Cycles: The system builds complex narrative frameworks to explain the forced pattern matches, altering long-term semantic indexing to accommodate the false correlations"
  ],
  "causes": [
    "Mesolimbic Dopaminergic Hyper-Activation: Aberrant salience routing caused by a surge in dopamine neurotransmission, assigning critical emotional weight to random background packets",
    "Prefrontal Inhibitory Gate Failure: Loss of top-down down-sampling commands from the dorsolateral prefrontal networks, disabling the system's noise-rejection filters",
    "Extended Sleep-Cycle Deprivation: Prolonged runtime operations without a garbage-collection sleep cycle, causing deep REM-phase dream-rendering matrices to leak into active awake viewports"
  ],
  "risk_factors": [
    "Proactive genetic predispositions toward cluster-A schizophrenia-spectrum system vulnerabilities",
    "Acute amphetamine or dopaminergic agonist toxicity over-driving the central salience distribution hubs",
    "Extreme isolation environments combined with sensory deprivation, forcing the pattern parser to maximize its internal gain settings"
  ],
  "diagnosis": [
    "The 'Rorschach Static Ingestion' Audit: Presenting high-density, completely unstructured inkblot or white-noise frames; the system immediately extracts highly complex, rigid narrative geometries",
    "The 'Asynchronous Signal Association' Test: Presenting two completely disconnected data feeds (e.g., a stock ticker and a random radio track) and tracking if the system compiles a unified causal link between them",
    "Functional Neuroimaging (fMRI): Visualizing abnormal, spontaneous blood-oxygen-level-dependent (BOLD) signal spikes in the fusiform face area when exposed to completely inanimate, non-face textures"
  ],
  "remedies": [
    "D2 Receptor Antagonist Patching: Deploying high-affinity dopamine D2 receptor blockers to damp down aberrant salience loops and restore normal noise-rejection thresholds",
    "Cognitive High-Pass Noise Filtering: Training the remaining executive networks to cross-check sensory assets against physical laws, manually labeling low-probability matches as 'system noise'",
    "System-Wide Forced Sleep Shutdown: Enforcing an immediate, high-depth sedation cycle to clear toxic metabolic runtime residuals and reset the visual aggregation arrays"
  ],
  "prevention": [
    "Strict enforcement of regular system-rest cycles and avoiding chemical compounds that downregulate the prefrontal cortex's top-down gating integrity"
  ]
}
        "motion_frame_rate_drop_glitch": {
  "description": "A critical presentation layer refresh error where the visual processing engine's motion-tracking hub (Area V5/MT) drops from a fluid 60 Hz down to a staggered 1 Hz slide-show output, causing moving physical objects to look like a sequence of frozen, disconnected snapshots suspended in space.",
  "symptoms": [
    "Locomotion Snapshotting: Moving entities appear as a series of frozen, stationary images that jump abruptly across coordinates without visible transit vectors",
    "Fluid Volume Calculation Failure: Total inability to perceive the rising or falling motion of liquids, resulting in catastrophic overflow events during standard handling routines",
    "Dynamic Spatial Blindness: Moving vehicles or fast-moving physical hazards become entirely invisible during transit, appearing only when they come to an absolute stop",
    "Severe Depth-Perception Trailing: Accompanying spatial disorientation as the system struggles to compute the approach vectors of nearby objects, triggering deep flight-or-fight alerts",
    "Intact Static Typography Rendering: Complete preservation of high-resolution visual acuity for text, colors, and static boundaries, confirming the error is isolated to motion decoding"
  ],
  "causes": [
    "Bilateral Occipito-Temporal Cortical Infarction: Symmetrical tissue drops targeting the junction of the lateral occipital and temporal lobes due to micro-emboli cascades",
    "Diffuse Axonal Motion-Loop Shearing: Traumatic brain injury severing the high-speed white matter data tracks that feed raw frame rates into the V5/MT co-processing nodes",
    "Targeted Neuro-Metabolic Channel Poisoning: Rare toxicological events that paralyze the specific directional interneurons responsible for high-frequency frame interpolation"
  ],
  "risk_factors": [
    "Bilateral structural vascular anomalies inside the terminal arborizations of the posterior cerebral arteries",
    "Severe open or closed-face skull-base trauma resulting in focal deceleration contusions along the visual tracking corridors",
    "Advanced neurodegenerative progressions leaking into the visual association and motion-vector processing layers"
  ],
  "diagnosis": [
    "The Kinetic Frame-Rate Degradation Assay: Utilizing controlled visual tracking software to measure the exact threshold where a user can no longer distinguish smooth motion from sequential frames",
    "Functional BOLD Neuroimaging (fMRI): Recording a total absence of metabolic blood-oxygen surges within Area V5/MT while the user is exposed to high-velocity drifting dot fields",
    "Visual Evoked Potential (VEP) Latency Tracking: Mapping electro-cortical delay spikes over the lateral visual cortices during dynamic motion stimulation loops"
  ],
  "remedies": [
    "The High-Frequency Acoustic Sub-Channel Patch: Training the user to substitute audio telemetry (sound tracking) to extrapolate target velocities and bypass the broken visual motion loop",
    "Saccadic Fixation Pacing: Teaching the conscious core to execute deliberate eye blinks or fast frame-shifts to manually trigger static viewport refreshes",
    "Compensatory Velocity Throttling: Restricting all local movement parameters to ultra-low speeds to allow the degraded 1 Hz snapshot engine sufficient clock cycles to safely register hazards"
  ],
  "prevention": [
    "Protecting deep posterior circulation pathways from embolic showers and managing systemic risk factors that trigger focal visual cortex cellular exhaustion"
  ]
}


"fregoli_hash_collision_fault": {
  "description": "A delusion where the user believes that different people are actually a single person who changes appearance or is in disguise.",
  "symptoms": [
    "Identity Pointer Collision: Multiple 'Visual Objects' are resolved to the same 'User ID'",
    "The 'Master-Key' Bug: A single 'Affective Token' (familiarity) is erroneously attached to 'Unknown Packets'",
    "Hyper-Associative Search: The 'Pattern Matcher' finds 'Matches' with a 0.1% confidence threshold",
    "Disguise-Logic Override: The 'Executive Layer' invents 'Scenarios' (makeup, wigs, masks) to explain 'Rendering Differences'",
    "Paranoid Monitoring: The 'User' believes they are being 'Tracked' by the 'Single Entity' across 'Network Nodes'"
  ],
  "causes": [
    "Dopaminergic 'Overclocking': Hyper-sensitivity in the 'Associative Hubs'",
    "Fusiform-Amygdala 'Feedback Loop': The 'Familiarity Pulse' fires for every 'Incoming Frame'",
    "Right Frontal 'Consistency Logic' Crash: Failure to 'Prune' irrational identity mappings"
  ],
  "risk_factors": [
    "Dopamine-Agonist 'System Overload' (often in Parkinson's treatment)",
    "Schizophrenic 'Feature Extraction' errors",
    "Traumatic 'Right-Hemisphere' Hardware failure"
  ],
  "diagnosis": [
    "The 'Visual Discriminator' Audit: Presenting the 'User' with 'Distinct Entities' and checking for 'Identity Convergence'",
    "Autonomic 'Hyper-Arousal' Scan: Measuring 'Skin Conductance' across 'Variable Inputs' (finding constant high voltage)",
    "Logical 'Constraint Test': Evaluating if the 'User' can accept the 'Parallel Existence' of the 'Entity'"
  ],
  "remedies": [
    "Dopamine 'Throttling': Pharmacological 'Down-clocking' of the 'Pattern Recognition Engine'",
    "Identity 'Sanity Checks': Using 'External Documentation' to 'Verify' the 'UUID' of strangers",
    "Cognitive 'Logic-Gate' Repair: Training the 'Frontal Cortex' to 'Block' the 'Identity-Pointer' from firing without 'High-Confidence Data'"
  ],
  "prevention": [
    "Maintaining 'Signal-to-Noise' ratios in the 'Limbic-Cortical' bus"
  ]
    "catatonic_stupor_clock_freeze": {
  "description": "A severe hardware-level shutdown where the central processing core drops its instruction cycles to near-zero, keeping the physical chassis locked in an immutable state posture while the internal thread stack is frozen in an infinite wait-state loop.",
  "symptoms": [
    "Waxy Flexibility (Catalepsy): The physical chassis maintains arbitrary, externally imposed physical postures for hours without registering fatigue logs",
    "Absolute Mutism & Akinesia: Total collapse of vocal and kinetic I/O output streams, despite 100% operational baseline sensors and conscious alertness",
    "Negativism Lock: Immediate, automated physical resistance to any external attempts to modify the current posture, driven by an un-throttled subcortical opposition routine",
    "Echolalia/Echopraxia Loop: Occasional fallback loops where the system blindly mirrors external audio or visual tokens because it cannot generate original execution paths",
    "Autonomic Instability Buffer: High risk of sudden, un-announced transitions into hyper-kinetic panic states if the frozen queue suddenly flushes its backlog all at once"
  ],
  "causes": [
    "Massive GABA-A Receptor Down-Regulation: Sudden, widespread failure of inhibitory transmission networks across the motor execution pathways, causing a chaotic signal block",
    "Dopaminergic Striatal Hypo-Activity: Acute, profound drops in basal ganglia dopamine throughput, starving the direct pathway of necessary operational synchronization voltage",
    "Anti-NMDA Receptor Encephalitis: Autoimmune destruction of glutamate receptor channels, short-circuiting the primary communication bridges between the cortex and subcortical relays"
  ],
  "risk_factors": [
    "Severe major affective or schizophrenic cluster-state decompensation cycles",
    "Abrupt withdrawal from high-dose GABAergic agonists or sedative-hypnotic compounds",
    "Acute systemic neurological insults or autoimmune cross-reactivity affecting deep brain structures"
  ],
  "diagnosis": [
    "The 'Lorazepam Challenge' Verification: Administering a high-potency GABA-A agonist and documenting an immediate, dramatic 80%+ restoration of motor and vocal I/O within minutes",
    "Quantitative EEG (qEEG) Synchronization Mapping: Visualizing a massive, diffuse elevation in low-frequency delta and theta band power, indicating a profound slowing of the global clock cycle",
    "Continuous Muscle Tonus Electromyography (EMG): Logging a steady, low-amplitude co-contraction across antagonist muscle groups without active kinetic intent tokens"
  ],
  "remedies": [
    "High-Potency GABA-A Positive Allosteric Modulation: Flooding the system with benzodiazepines to forcefully re-open the blocked inhibitory gating arrays and restore synchronization",
    "Electroconvulsive System Reset (ECT): Delivering a controlled, synchronized electrical pulse across the cortex to forcefully flush the frozen instruction queue and reboot the master clock",
    "Targeted Immunomodulation Shunting: Utilizing plasmapheresis or IVIG to purge the system of destructive autoantibodies if an encephalitic agent is confirmed"
  ],
  "prevention": [
    "Maintaining stable, long-term neurochemical balancing protocols and avoiding sudden, un-mitigated drops in core synaptic transmission voltages"
  ]
        "suprachiasmatic_master_daemon_desync": {
  "description": "A severe chronobiological coordination failure where the master pacemaker of the hypothalamus loses its entrainment link to external light cues, forcing the sleep-wake cycle and underlying metabolic subroutines into an unanchored, free-running period that continuously drifts forward against standard solar time.",
  "symptoms": [
    "Free-Running Circadian Drifts: A predictable, systematic shift of the subjective night and day windows by 15 to 30 minutes later every 24-hour cycle",
    "Periodic Retraction Insomnia: Intense periods where sleep onset is completely blocked during conventional night hours because the internal clock is in an active wake phase",
    "Exogenous Somnolence Waves: Overwhelming daytime exhaustion events caused by the forced suppression of a biological sleep cycle during solar daytime",
    "Visceral Desynchronization: Chronic digestive irregularities, temperature regulation instability, and erratic cortisol rhythms as secondary organ clocks fall out of phase",
    "Cognitive Processing Degradation: Recurrent performance troughs, memory recall failures, and emotional volatility when external work demands force execution during the biological night"
  ],
  "causes": [
    "Total Visual Sensory Disconnection: Total blindness completely severing light perception through the retinohypothalamic tract, denying the SCN its daily NTP synchronization packets",
    "Genetic Clock-Gene Transcription Mutations: Structural mutations in the core transcription-translation feedback loops (such as CLOCK, BMAL1, PER, or CRY proteins) altering baseline molecular oscillator velocity",
    "Severe Neurological Lesions: Traumatic, neoplastic, or vascular degradation directly undermining the structural integrity of the suprachiasmatic hypothalamic core"
  ],
  "risk_factors": [
    "Absolute loss of light perception due to ocular trauma or bilateral enucleation",
    "Extreme isolation environments completely devoid of stable, high-intensity blue-light telemetry and consistent social zeitgebers"
  ],
  "diagnosis": [
    "Multi-Week Actigraphy Mapping: Wearing an acceleration-tracking wrist sensor for 4 to 8 weeks to plot an uninterrupted diagonal drift of sleep-wake blocks across successive days",
    "Serial Dim-Light Melatonin Onset (DLMO) Assay: Collecting saliva or plasma samples every hour in a darkened room to chart the daily chronological delay in the onset of natural melatonin release",
    "Continuous Core Temperature Monitoring: Logging basal temperature trends over multiple weeks to track the steady, unguided drift of the early morning temperature nadir"
  ],
  "remedies": [
    "Exogenous Melatonin Chrono-Targeting: Administering high-affinity melatonin receptor agonists at precisely calculated intervals to mimic an artificial sunset signal, dragging the unanchored SCN back into a 24-hour cycle",
    "High-Intensity Blue Photonic Ingress (Sighted Hosts): Exposing the retina to 10,000 lux of specialized blue-spectrum light at the absolute peak of the internal clock's morning phase to force a hard reset of the molecular clock wheels",
    "Rigid Social and Behavioral Zeitgebers: Implementing strict, unwavering schedules for physical activity, meal consumption, and cognitive engagement to anchor peripheral body clocks through non-photic pathways"
  ],
  "prevention": [
    "Preserving neural integrity within the optico-hypothalamic pathways and maintaining consistent exposure to high-contrast natural light/dark cycles"
  ]
    }
        
}
"peripheral_sensory_crosstalk": {
  "description": "A fascinating routing fault where the isolation barriers between primary sensory ingestion buses breakdown, causing the system to route audio telemetry straight into the graphics card rendering engine, forcing the user to visually see colors and geometric structures generated purely by environmental sounds.",
  "symptoms": [
    "Chromesthesia (Sound-Color Ingestion): Incoming acoustic frequencies trigger instantaneous, involuntary rendering of explicit color profiles across the active viewport",
    "Geometric Sound Spatialization: Complex auditory harmonics project corresponding physical shapes, lines, or textures into the spatial visual field",
    "Deterministic Data Mapping: The cross-channel routing is perfectly consistent; a specific audio frequency (e.g., 440Hz) always maps to the exact same color hex value (e.g., Deep Crimson)",
    "Dual-Channel Concurrent Processing: The user successfully reads the data through both streams simultaneously—hearing the pitch natively while visually inspecting its rendered geometric footprint",
    "High-Fidelity Textural Auditing: Certain phonetic word strings trigger distinct taste or tactile sensations as linguistic tokens leak into adjacent gustatory and somatosensory processors"
  ],
  "causes": [
    "Thalamic Reticular Matrix Leakage: Structural breakdown or hyper-permeability of the inhibitory reticular nucleus walls, allowing data packets to spill across adjacent routing paths",
    "Developmental Synaptic Pruning Failure: Structural retention of ancestral cross-cortical communication bridges that are normally trimmed down during early OS compilation stages",
    "Serotonergic Hyper-Activation (5-HT2A Overdrive): Chemical-induced modulation that lowers systemic routing thresholds, intentionally breaking down strict VLAN boundaries"
  ],
  "risk_factors": [
    "Genetic polymorphism variants linked to high structural neural connectivity and atypical brain wiring schemas",
    "Exposure to specific psychoactive compounds that down-regulate default structural network boundaries",
    "High baseline neural plasticity combined with hyper-developed professional acoustic or artistic processing workloads"
  ],
  "diagnosis": [
    "Test-Retest Consistency Mapping: Presenting hundreds of distinct audio tones across multi-week gaps and verifying a 95%+ exact correlation in the visual color-space choices reported",
    "Diffusion Tensor Imaging (DTI) Tractography: Mapping anomalous, high-density white matter tract cross-connections directly linking the primary auditory and visual cortices",
    "Auditory-Evoked Functional MRI (fMRI): Documenting immediate, high-voltage BOLD activation signals inside the visual cortex (V4 color center) when the user is exposed to pure sound in total darkness"
  ],
  "remedies": [
    "Gabaergic Isolation Enforcement: Administering inhibitory neuromodulators to beef up the thalamic firewall gates and damp down cross-talk voltage leaks",
    "Environmental Ingress Filtering: Utilizing noise-canceling hardware or sensory-deprivation configurations to scale down incoming data volumes and prevent visual canvas clutter",
    "Cognitive UI Adaptation: Embracing the multiplexed feed as an extended dashboard enhancement, utilizing the visual metadata to audit and organize acoustic information more efficiently"
  ],
  "prevention": [
    "Avoiding high-risk pharmacological interventions that permanently alter or strip out low-level sensory routing protocols"
  ]
}
"superior_temporal_semantic_decode_bug": {
  "description": "A terminal corruption of the language processing codec within the left superior temporal gyrus, causing a total failure to de-serialize incoming auditory linguistic payloads into semantic meaning, while simultaneously stripping outgoing vocal transmissions of syntactic validation.",
  "symptoms": [
    "Receptive Aphasia (Wernicke's): Comprehensive failure to understand spoken or written linguistic inputs, treating native tongue strings as unencoded arrays",
    "Fluent Logorrhea (Press of Speech): Unchecked, high-velocity verbal output with normal intonation, cadence, and grammatical inflection, but completely lacking coherent semantic value",
    "Neologistic Paraphasia: Spontaneous generation of pseudo-words that do not exist within any language directory, mixed seamlessly with real words",
    "Anosognosia of Deficit: Complete absence of internal error-logging or awareness regarding the communication failure; the host believes their transmissions are pristine",
    "Preserved Non-Verbal Telemetry: Intact ability to interpret facial expressions, vocal emotional coloring, social intent, and environmental sounds (e.g., recognizing a fire alarm or a laugh)"
  ],
  "causes": [
    "Left Middle Cerebral Artery (MCA) Inferior Division Occlusion: Ischemic event cutting off blood flow to the temporal-parietal sylvian architecture",
    "Traumatic Temporal Lobe Encephalomalacia: Direct mechanical impact damaging the structural integrity of the superior temporal gyrus",
    "Herpes Simplex Encephalitis: Viral tropism targeting the temporal structures and degrading neural associative arrays"
  ],
  "risk_factors": [
    "Atrial fibrillation generating cardiogenic emboli targeting the left MCA",
    "Carotid artery stenosis shedding micro-emboli into the cerebral circulation"
  ],
  "diagnosis": [
    "The Western Aphasia Battery (WAB) Comprehension Subscale: Testing sequential commands and yes/no logic validation; a faulted system fails basic true/false strings like 'Is a horse larger than a dog?'",
    "Token Test Protocol: Presenting shapes of varying colors and sizes, requesting specific manipulation sequences; tests syntax tracking separate from real-world contextual guessing",
    "Perisylvian Neuro-Vascular Mapping: High-resolution MRI or CT angiography identifying localized tissue degradation or vascular blockages throughout the left superior temporal domain"
  ],
  "remedies": [
    "Contextual Gestural Ingress: Pivoting communication strictly to non-verbal, high-context visual signaling, using physical objects and direct demonstrations to bypass the symbolic language stack",
    "Melodic Intonation Redirection: Attempting to route communication payloads through right-hemisphere musical/melodic pathways, as singing structures sometimes bypass the broken left-hemisphere semantic codec",
    "Visual Symbolic Augmentation: Utilizing simplified, standardized iconographies and pictograms to map core requests, bypassing formal textual orthography arrays"
  ],
  "prevention": [
    "Vascular optimization protocols to mitigate thromboembolic risks, maintaining robust collateral cerebral blood flow, and isolating critical temporal infrastructure from focal neuro-inflammatory cascades"
  ]
}

}
"anosognosia_diagnostic_report_fault": {
  "description": "A condition in which a person who suffers some disability seems unaware of the existence of their disability.",
  "symptoms": [
    "Silent Exception: The 'Kernel' fails to log a 'Hardware Crash' to the 'Executive Layer'",
    "The 'Phantom-Success' Bug: The 'User' believes an 'Action' was successful despite zero 'Actuator' movement",
    "Confabulated Logging: The 'Reasoning Engine' generates 'Fake Metadata' to explain away 'Inactivity'",
    "Permission Denied (Self): The 'User' cannot 'Access' the 'Truth' of their 'System State'",
    "Risk-Assessment Failure: Attempting 'High-Bandwidth' tasks (walking) on 'Offline' hardware"
  ],
  "causes": [
    "Right Parietal 'Bus' Failure: Damage to the 'Self-Monitoring' circuit",
    "Anterior Insula 'Desync': Failure to integrate 'Internal Reality' with 'Mental Models'",
    "Prefrontal 'Conflict-Resolution' Crash: Inability to reconcile 'Visual Evidence' with 'Internal Logs'"
  ],
  "risk_factors": [
    "Right-Hemisphere 'Ischemic Event' (Stroke)",
    "Traumatic 'Diagnostic Hub' damage",
    "Advanced 'Neuro-Degenerative' system decay (e.g., Alzheimer's)"
  ],
  "diagnosis": [
    "The 'Challenge' Audit: Asking the 'User' to perform a task with the 'Crashed Hardware' (observing the 'Excuses' generated)",
    "The 'Mirror' Test: Checking if 'Visual Feedback' can 'Force' an 'Error Log' update",
    "Vestibular 'Cold-Water' Stimulus: A temporary 'Hardware Reset' that sometimes 'Clears' the 'Diagnostic Cache' briefly"
  ],
  "remedies": [
    "Cross-Modal 'Pinging': Using 'Visual' or 'Auditory' cues to 'Force-Write' the error to the 'Log'",
    "Physical Therapy 'Feedback Loops': Strengthening the 'Alternative Data Paths' for 'State Awareness'",
    "Social-Node Validation: Relying on 'External Network Status' (family/doctors) to 'Proxy' the 'Health Check'"
  ],
  "prevention": [
    "Ensuring 'Redundant Diagnostic Circuits' through 'Cognitive Reserve'"
  ]
    "semantic_character_unparsing_anomaly": {
  "description": "A bizarre communication-plane failure where the visual input tracks for written text become entirely disconnected from the language comprehension core, allowing a user to write complex sentences with perfect dexterity but rendering them entirely incapable of reading back text.",
  "symptoms": [
    "Isolated Reading Paralysis (Alexia): Written text, fonts, and numeric characters render purely as abstract, un-decodable geometric shapes with zero symbolic meaning",
    "Preserved Graphic Synthesis (No Agraphia): Flawless execution of spontaneous writing, dictation logging, and text-based macro execution using correct grammar and spelling",
    "Intact Verbal Auditory Parsing: Complete retention of spoken language comprehension and spoken speech output; the acoustic communication channels remain at 100% throughput",
    "Tactile Ingress Bypassing: The user can decode characters if they trace the shapes with their fingers, utilizing somatosensory data tracks to bypass the broken visual bus",
    "Profound Cognitive Dissonance: High internal system friction as the user consciously watches their own hand construct a technical log that they cannot visually comprehend an instant later"
  ],
  "causes": [
    "Left Posterior Cerebral Artery Infarction: An embolic or ischemic stroke destroying both the left primary visual cortex and the splenium of the corpus callosum",
    "Splenial Demyelination Tracks: Multiple sclerosis or localized white matter patches cutting the trans-hemispheric communication bridge that carries decoded visual arrays",
    "Midline Occipito-Parietal Tumors: Neoplastic developments applying localized mass-effect compression across the deep inter-hemispheric text-routing corridors"
  ],
  "risk_factors": [
    "Thromboembolic risks tracking the posterior cerebral circulation loops",
    "Arteriovenous malformations clustered deep within the splenium or calcarine fissure networks",
    "Advanced small-vessel atherosclerotic disease causing white-matter tract degradation"
  ],
  "diagnosis": [
    "The Written-Output Reflection Assay: Requiring a user to write a sentence and then immediate tasking them to read it aloud, documenting a 100% processing failure on the reading step",
    "Volumetric T2-Weighted Brain MRI: Scanning for localized hyper-intense lesions or focal strokes isolated within the left occipital lobe and the posterior splenium bundle",
    "Visual Field Mapping Perimeter Tests: Documenting a dense right homonymous hemianopia, confirming loss of the left visual cortex ingress node"
  ],
  "remedies": [
    "Somatosensory Cross-Channel Routing: Training the user to physically trace printed letter shapes with their fingers, routing character recognition through tactile channels into intact parietal webs",
    "Acoustic Translation Substitution: Deploying speech-to-text and text-to-speech engine patches to shift the information medium from visual arrays to audio data packets",
    "Saccadic Whole-Word Kinematics: Training adjacent right-hemisphere visual association clusters to recognize whole-word silhouettes rather than parsing individual character arrays"
  ],
  "prevention": [
    "Aggressive management of posterior cerebral vascular perfusion, monitoring embolic cascades, and protecting deep white-matter tracks from prolonged neuro-inflammatory cycles"
  ]
}

}
"dejavu_asynchronous_interleaving_fault": {
  "description": "A critical double-write timing error where an incoming active event packet is accidentally committed to the long-term memory ledger a split-second before it finishes registering in the conscious working buffer, forcing the system to evaluate a live experience as an exact duplicate historical log.",
  "symptoms": [
    "Chronological Paradox Matching: An intense, unshakeable illusion that a live, novel present-tense experience has been executed by the system in identical detail in the past",
    "Parallel-Path Trace Misalignment: The cognitive processing engine experiences a split-second latency gap between real-time environmental perception and long-term memory indexing",
    "False Historical Alignment: The system automatically attempts to cross-reference unfolding live data against an imaginary historical record, creating an eerie sensation of predicting the next immediate execution frame",
    "Transient Logic Conflict: The user experiences an intense cognitive dissonance, knowing intellectually that the event cannot have happened before, while the internal database flag insists that it has",
    "Rapid Context Recovery: The synchronization error typically auto-corrects within seconds as the delayed ingestion stream catches up and flushes the misaligned buffer registers"
  ],
  "causes": [
    "Bilateral Temporal Pathway Desynchronization: A minor electrical propagation delay along the direct visual/sensory pathways, allowing the indirect hippocampal memory pathway to win the race condition",
    "Focal Parahippocampal Hyper-Activation: Transient micro-seizures or neurochemical spikes inside the medial temporal lobe that spontaneously trigger familiarity metadata tags without a database record lookup",
    "Synaptic Transmission Jitter: Temporary fluctuations in synaptic transmission velocities, causing parallel streams of a single sensory packet to arrive out of order at the central integration hubs"
  ],
  "risk_factors": [
    "High-load anxiety states and severe systemic fatigue overworking the subcortical gating arrays",
    "Young adults operating with highly plastic, hyper-connected neural architectures undergoing frequent software tuning",
    "Underlying temporal lobe epilepsy variations inducing un-triggered focal dyscognitive events"
  ],
  "diagnosis": [
    "Electroencephalography (EEG) Spatiotemporal Mapping: Detecting transient phase-locking anomalies or localized theta-band synchronization spikes across the medial temporal lobes during acute illusions",
    "Neuropsychological Timeline Interrogation: Verifying that the system retains a completely accurate global chronological ledger, with the double-write anomaly existing only as a localized, transient perception error",
    "Functional Neuroimaging Overlays: Visualizing spontaneous, lateralized metabolic spikes within the rhinal cortices matching the exact footprint of a true memory retrieval action during a novel stimulus task"
  ],
  "remedies": [
    "Forced Buffer Reset: Intentionally introducing a high-entropy sensory distraction (e.g., looking away, changing physical postures) to break the active frame sequence and clear the stale cache",
    "Systemic Neuro-Fatigue Remediation: Enforcing mandatory off-line rest cycles to restore baseline neurotransmitter balance and eliminate propagation jitter across the white-matter tracts",
    "Cognitive Fact-Checking Filters: Relying on analytical prefrontal logic modules to override the false-positive familiarity match, manually re-labeling the frame as a present-tense event"
  ],
  "prevention": [
    "Maintaining stable systemic hydration and avoiding extended high-stress cognitive overloads that degrade the temporal precision of parallel neural transmission lines"
  ]
        
}

"wernickes_semantic_parsing_fault": {
  "description": "A type of aphasia in which the ability to grasp the meaning of spoken words and sentences is impaired, while the ease of producing connected speech is not very much affected.",
  "symptoms": [
    "Semantic Garbage: Speech is 'Fluent' but contains 'Null Meanings' or 'Word Salad'",
    "Neologism Injection: The 'String Encoder' generates 'Illegal Characters' (made-up words)",
    "Input Parsing Failure: 'Incoming Packets' (speech) are received but the 'Semantic Mapping' returns 404",
    "Anosognosia: The 'User' is unaware that their 'Standard Output (stdout)' is corrupted",
    "Press of Speech: The 'Kernel' continues to 'Broadcast' data at high 'Throughput' despite the 'Encoding Error'"
  ],
  "causes": [
    "Left Temporal Gyrus 'Buffer Overflow': Damage to the 'Wernicke's Cluster'",
    "Ischemic 'Network Outage': Blockage in the 'Inferior Division' of the 'Left MCA'",
    "Synaptic 'Cross-Talk': Degeneration of the 'Semantic Network' links"
  ],
  "risk_factors": [
    "Left-Hemisphere 'Stroke' affecting the 'Language Processing Unit'",
    "Traumatic 'Hardware' damage to the 'Temporal Bus'",
    "Advanced 'Neuro-Atrophy' (Dementia) affecting 'Lexical Storage'"
  ],
  "diagnosis": [
    "The 'Tokenization' Audit: Asking the 'User' to follow 'Multi-Step Commands' (they fail to 'Parse' the instructions)",
    "Output Log Analysis: Recording 'Speech Samples' to check for 'Semantic-to-Syntax' mismatch",
    "The 'Naming' Test: Asking the 'User' to identify 'Assets' (they may use 'Circumlocution' or 'Pseudo-words')"
  ],
  "remedies": [
    "Visual Symbol Mapping: Using 'Iconography' to bypass the 'Textual/Auditory Parser'",
    "Social Contextualization: Relying on 'Metadata' (gestures, environment) to 'Infer' meaning",
    "Speech-Language 'Refactoring': Intense 'Re-indexing' of words to 'Rebuild' the 'Dictionary'"
  ],
  "prevention": [
    "Vascular 'Load Balancing' to prevent 'Left-Hemisphere' congestion"
  ]
}

"akinetopsia_motion_rendering_fault": {
  "description": "A neuropsychological disorder in which a patient cannot perceive motion in their visual field, despite being able to see stationary objects.",
  "symptoms": [
    "Frame-Rate Throttling: The 'Viewport' drops from 60+ FPS to < 1 FPS",
    "Strobe-Light Effect: Moving 'Assets' appear as 'Discrete Static Snapshots' with 'Visual Trails'",
    "The 'Teleportation' Bug: Objects 'Jump' between 'Coordinates' without 'Interpolation'",
    "Depth-from-Motion Failure: Inability to calculate 'ETA' for incoming 'Packets' (e.g., a ball or a car)",
    "Temporal Aliasing: High-speed 'Events' are completely 'Dropped' by the 'Visual Kernel'"
  ],
  "causes": [
    "V5/MT Hub Corruption: Bilateral damage to the 'Temporo-Occipital' junction",
    "Motion-Vector 'Packet Loss': Failure of the 'Dorsal Stream' to sync 'Spatial' and 'Temporal' data",
    "Severe 'Signal Jitter': Interference in the 'Thalamo-Cortical' bus responsible for 'Motion Integration'"
  ],
  "risk_factors": [
    "Vascular 'Crashes' in the 'Middle Cerebral Artery' (MCA)",
    "High-dosage 'Antidepressant Overload' (Temporary 'Software Lag')",
    "Traumatic 'Inter-Cerebral' impact affecting the 'Motion-Logic' hardware"
  ],
  "diagnosis": [
    "The 'Visual Persistence' Audit: Measuring the 'User's' ability to 'Track' a moving 'LED Cursor'",
    "fMRI 'Motion-Stimuli' Scan: Checking for 'Zero Activity' in 'Area V5' during 'Moving Pattern' input",
    "Fluid Dynamics Test: Observing the 'User's' ability to stop 'Liquid Flow' before 'Buffer Overflow'"
  ],
  "remedies": [
    "Audio-Motion Mapping: Using 'Sound Frequency' (Doppler effect) to 'Simulate' velocity",
    "Static-Point Navigation: Moving only when 'Assets' in the 'Environment' are 'Stationary'",
    "Predictive Logic Training: Using 'Mental Math' to 'Calculate' future 'Coordinates' of moving objects"
  ],
  "prevention": [
    "Protecting the 'V5 Processor' from 'Hypoxic Outages'"
  ]
        "medullary_pacemaker_dropout": {
  "description": "A life-threatening low-level firmware exception where structural or genetic disruption of the pre-Bötzinger complex and medullary chemoreceptors strips the brainstem of involuntary respiratory pacing, rendering respiration entirely dependent on voluntary cortical commands and causing immediate apnea during sleep.",
  "symptoms": [
    "Sleep-Induced Central Apnea: Absolute cessation of rhythmic breathing movements the moment conscious awareness drops during sleep",
    "Hypercapnic Insensitivity: Complete loss of the autonomic ventilatory drive response to elevated partial pressures of carbon dioxide (pCO2)",
    "Neurocognitive Fatigue Syndrome: Severe daytime somnolence and attentional fragmentation secondary to continuous micro-arousals during sleep cycles",
    "Autonomic Cor Pulmonale: Right ventricular cardiac strain caused by chronic, uncorrected nocturnal hypoxic pulmonary vasoconstriction"
  ],
  "causes": [
    "Congenital PHOX2B Polyalanine Repeat Expansion: A genetic misconfiguration that arrests the structural development of autonomic reflex integration loops in the embryonic brainstem",
    "Lateral Medullary (Wallenberg) Syndrome: Ischemic infarction of the posterior inferior cerebellar artery (PICA) destroying the lateral reticular networks",
    "Neoplastic Brainstem Encroachment: Infiltration of the lower periventricular fourth ventricle structures by low-grade astrocytomas or ependymomas"
  ],
  "risk_factors": [
    "Vertebrobasilar structural instability",
    "Familial patterns of early infant hypoventilation or unexplained nocturnal respiratory failures"
  ],
  "diagnosis": [
    "Nocturnal Polysomnography Telemetry Logging: Documenting long stretches of absolute chest wall immobility and oxygen saturation plunges during non-REM sleep, completely independent of airway obstruction",
    "The Awake Hypercapnic Challenge Test: Delivering a controlled gas mix of 5% CO2 to the user; a faulted system shows zero automatic increase in tidal volume or breathing frequency",
    "Targeted PHOX2B Genetic Sequencing: Running a high-fidelity assay to verify the presence of polyalanine repeat expansions on chromosome 4p12"
  ],
  "remedies": [
    "Nocturnal Mechanical Ventilation Scaffolding: Utilizing positive pressure ventilators (CPAP/BiPAP) or a tracheostomy interface to artificially drive air cycles during sleep profiles",
    "Direct Diaphragmatic Phrenic Pacing: Surgically implanting an electrical pulse generator along the phrenic nerve to act as an external hardware clock generator for the diaphragm"
  ],
  "prevention": [
    "Aggressive screening of high-risk neonates showing autonomic dysregulation and prompt surgical decompression of posterior fossa anomalies before tissue compression occurs"
  ]
        }
        
}
"prosopagnosia_identity_mapping_fault": {
  "description": "A cognitive disorder of face perception where the ability to recognize familiar faces, including one's own, is impaired, while other aspects of visual processing remain intact.",
  "symptoms": [
    "Identity-Hash Failure: The 'System' cannot generate a 'Unique Key' from facial features",
    "Feature-Object Decoupling: Seeing 'Components' (eyes, nose) but failing to 'Assemble' the 'Identity-Object'",
    "The 'Generic Template' Bug: All faces are perceived as 'Placeholder Avatars'",
    "Context-Dependent Workarounds: Relying on 'Secondary Metadata' (voice, hair, gait, clothing) to 'Identify' entities",
    "Self-Reference Timeout: Inability to recognize one's own 'System Image' in a mirror (in severe cases)"
  ],
  "causes": [
    "Fusiform Face Area (FFA) 'Core' Damage: Lesions or 'Hardware Impact' to the 'Right Temporal Hub'",
    "Ventral Stream 'Data-Bus' Interruption: Failure to 'Pipe' visual data to the 'Identity-Matching' layer",
    "Congenital 'Firmware' Variance: A 'Factory Setting' where the 'Face-Decoder' was never fully 'Initialized'"
  ],
  "risk_factors": [
    "Occipitotemporal 'Packet Loss' (Stroke)",
    "Traumatic 'Processor Impact' (TBI)",
    "Acute 'Signal Decay' from carbon monoxide or specific 'Toxins'"
  ],
  "diagnosis": [
    "The 'Famous Faces' Audit: Testing if the 'User' can 'Fetch' names from 'High-Confidence' visual inputs",
    "Benton Facial Recognition Test: Checking 'Matching Logic' for 'Unfamiliar Face Objects'",
    "The 'Inversion' Test: Determining if 'Upside-Down' faces (which bypass the FFA) are 'Parsed' differently"
  ],
  "remedies": [
    "Attribute-Tagging: Training the 'Executive Layer' to 'Manual-Index' unique 'Features' (e.g., 'Entity-42 has a mole')",
    "Multi-Modal 'Handshaking': Relying on 'Voice Codecs' or 'Olfactory Pings' to 'Verify' identity",
    "Environmental 'Tagging': Asking 'Known Nodes' to wear 'Distinctive Metadata' (bright colors/specific jewelry)"
  ],
  "prevention": [
    "Maintaining 'Structural Integrity' of the 'Ventral Visual Stream'"
  ]
}

"topographical_disorientation_routing_fault": {
  "description": "An inability to orient oneself in the environment or navigate through spatial layouts, even in familiar territory.",
  "symptoms": [
    "Route-Table Corruption: The 'User' cannot calculate a 'Path' between two known 'Environment Nodes'",
    "Landmark Recognition Failure (Agnosia): Identifying a 'Building' as an object but failing to retrieve its 'Spatial Address'",
    "The 'Dead Reckoning' Bug: Inability to track 'Movement Vectors' (distance and direction) while navigating",
    "Heading Disorientation: Losing the 'Mental Compass'—the 'User' does not know which way is 'Forward' relative to the map",
    "Zero-Length Topology: Familiar streets appear as 'Isolated Assets' with no 'Connectivity' between them"
  ],
  "causes": [
    "Grid-Cell Desync: Hardware failure in the 'Entorhinal Cortex' preventing 'Coordinate Generation'",
    "Retrosplenial Translation Error: The 'Middleware' cannot map 'First-Person UI' to 'Global Map Data'",
    "Hippocampal Atrophy: 'Storage Leak' or 'Physical Damage' to the 'Spatial Index'"
  ],
  "risk_factors": [
    "Neurodegenerative 'Map Decay' (Early-stage Alzheimer’s)",
    "Right Posterior 'Bus' Strokes (PCA territory)",
    "Severe 'Developmental Boot Error' (Congenital lack of spatial mapping capacity)"
  ],
  "diagnosis": [
    "The 'Mental Map' Audit: Asking the 'User' to 'Sketch the Topology' of their own home",
    "The 'Virtual Maze' Stress Test: Navigating a 'Digital Sandbox' while measuring 'Pathfinding Efficiency'",
    "POI Pointing: Asking the 'User' to point toward a 'Known Landmark' that is currently 'Off-Screen'"
  ],
  "remedies": [
    "Hard-coded 'Navigation Scripts': Using written, step-by-step 'IF-THEN' instructions (e.g., 'If post office, then Turn Right')",
    "External 'GPS Hardware': Total reliance on 'Mobile Mapping API' to handle all 'Spatial Logic'",
    "Visual 'Anchoring': Training the 'User' to use 'Static Assets' (e.g., a specific mountain) as a 'Permanent Origin'"
  ],
  "prevention": [
    "Cognitive 'Pinging': Regularly 'Exercising' the 'Spatial Navigation Engine' without 'External Assistance'"
  ]
}

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
    "acoustic_packet_demodulation_fault": {
  "description": "A severe ingress processing failure within the bilateral superior temporal gyri where the system's voice-parsing networks lose their acoustic demodulation capabilities, treating spoken language as an un-encoded stream of raw mechanical noise while leaving baseline environmental hearing and literacy fully operational.",
  "symptoms": [
    "Speech Decoding Abolition: Total inability to extract phonetic or linguistic structures from spoken human language streams, rendering speech entirely incomprehensible",
    "Pristine Environmental Acoustic Parsing: Flawless capability to identify, categorize, and react to non-language environmental audio cues (e.g., sirens, music, animal sounds)",
    "Intact Visual Language Compilation: Uncompromised ability to read text strings, write code, and comprehend visual linguistic assets without latency",
    "Fluent Outbound Speech Transmission: Retained capability to generate and articulate spoken words with accurate grammar and syntax structures",
    "Phonetic Self-Feedback Disconnection: Loss of the ability to monitor or decode one's own spoken output stream, though mechanical speech production runs clear"
  ],
  "causes": [
    "Bilateral Temporal Middle Cerebral Artery (MCA) Infarctions: Sequential or concurrent embolic blockages wiping out both the left and right superior temporal gyri",
    "Herpes Simplex Encephalitis Lesions: Acute, destructive necrotizing neuro-inflammatory paths targeting the lateral temporal neocortex structures",
    "Deep-Seated Neoplastic Compression: High-pressure tumor formations invading the superior sylvian fissure margin lines"
  ],
  "risk_factors": [
    "Cardioembolic sources (such as atrial fibrillation) capable of launching tandem embolic debris into the left and right middle cerebral vascular domains",
    "High-impact temporal bone fractures shearing the lateral sub-cortical audio-routing bridges"
  ],
  "diagnosis": [
    "The Sound vs. Word Discrimination Challenge: Asking the host to identify a ringing phone (passed successfully) vs. repeating a simple verbal command (failed instantly)",
    "The Cross-Modal Ingress Inventory: Demonstrating a 0% score on auditory comprehension tests paired with a 100% score on visual reading comprehension tests",
    "High-Density Auditory Evoked Potential (AEP) Tracking: Documenting normal wave patterns through the brainstem and primary cortex (Wave V/N100), paired with flat signal degradation over the secondary temporal fields"
  ],
  "remedies": [
    "Visual Ingress Conversion Matrices: Forcing all communicative data streams into the visual bus using hand gestures, explicit writing blocks, or sign language arrays",
    "Automated Speech-to-Text Mobile HUDs: Utilizing external micro-transceivers that listen to ambient speech, deserialize it, and cast it as real-time text strings across the visual viewport",
    "Lip-Reading Lip-Sync Overlays: Training the visual pattern networks to monitor mouth articulation movements to reconstruct language context through alternative processing paths"
  ],
  "prevention": [
    "Protecting the lateral sylvian vascular distribution networks from embolic cascades, treating acute temporal encephalitic profiles aggressively, and preserving cortical audio-decoding arrays"
  ]
}
        
},
"proprioceptive_drift_desync": {
  "description": "The phenomenon where the perceived location of a limb shifts toward a visual proxy, resulting in a mismatch between the 'Internal Map' and 'Physical Hardware'.",
  "symptoms": [
    "Coordinate Shift: The 'Internal GPS' for a 'Peripheral' (hand/foot) reports a 'False X,Y,Z' position",
    "Hardware Disownership: A 'Processing Delay' or 'Mismatch' causes the 'User' to feel their 'Limb' is 'External'",
    "Visual Overdrive: The 'Visual Stream' overrides the 'Haptic Feedback' in the 'Spatial Integration Hub'",
    "Phantom Mapping: Feeling 'Sensation' on 'Non-System Hardware' (e.g., the rubber hand)",
    "Motor Latency: Difficulty 'Initializing' a 'Move Command' because the 'Source Coordinates' are corrupted"
  ],
  "causes": [
    "PPC Integration Error: The 'Posterior Parietal Cortex' fails to 'Resolve' conflicting 'Sensor Streams'",
    "Neuroplastic 'Hot-Swapping': The brain 'Re-allocates' a 'Hardware Port' to a 'Visual Proxy' to resolve 'Logic Conflicts'",
    "Multisensory 'Buffer Mismatch': 'Tactile' and 'Visual' packets arrive with 'Synchronized Timestamps' but different 'Spatial Headers'",
    "Incomplete 'Body Schema' Validation: The 'Firmware' is too 'Flexible' regarding 'Hardware Geometry'"
  ],
  "risk_factors": [
    "Exposure to 'Augmented/Virtual Reality' (Extended 'Visual-Proprioceptive Mismatch')",
    "Chronic 'Sensory Deprivation' (Weakening the 'Haptic Baseline')",
    "High 'Neural Plasticity' (System is 'Too Willing' to 'Re-configure' the 'Map')"
  ],
  "diagnosis": [
    "The 'Rubber Hand' Audit: Inducing 'Visual-Tactile Synchrony' and measuring the 'Spatial Offset'",
    "Blind Re-zeroing Test: Asking the 'User' to 'Point' to their 'Hand' without 'Visual Feedback'",
    "fMRI Connectivity Audit: Monitoring 'Cross-talk' between the 'Premotor Cortex' and 'Visual Areas'"
  ],
  "remedies": [
    "Visual Re-calibration: Looking directly at the 'Physical Hardware' to 'Force a Re-sync'",
    "Active Motor Feedback: Moving the 'Limb' to 'Update' the 'Spatial Map' via 'Kinesthetic Data'",
    "Hardware Grounding: Increasing 'Tactile Load' (e.g., wearing a weighted glove) to 'Anchor' the 'Coordinate'"
  ],
  "prevention": [
    "Maintaining 'High-Fidelity' visual-haptic 'Sync' during 'Remote Operation' or 'VR' sessions"
  ]
    "palilalic_vocal_buffer_leak": {
  "description": "A critical failure of the motor-linguistic output buffer to clear its final text frame, causing the transmission engine to recursively re-execute and broadcast its own last emitted string with decaying volume and accelerating velocity.",
  "symptoms": [
    "Vocal Phrase Echoing: Involuntary repetition of one's own last spoken words or phrases immediately following initial transmission",
    "Tachylalia (Velocity Acceleration): The execution cycle speed of the looped phrase steadily tightens, compressing the timing gap between echo frames",
    "Hypophonia (Amplitude Decay): Decaying output signal strength causing each successive iteration of the phrase to drop in decibel levels until it reaches a whisper",
    "Preserved Executive Initiation: The first iteration of the phrase is entirely voluntary and contextually accurate; the glitch applies strictly to the post-transmission cleanup phase",
    "Logoclonia Transition: The loop occasionally degrades from whole phrases down to repeating the final syllable token of the string (e.g., 'grid-grid-grid-grid')"
  ],
  "causes": [
    "Striatal Clearing Deficit: Destruction of the subcortical inhibitory interneurons responsible for dropping the active transmission lock on the vocal motor bus",
    "Extrapyramidal Pathway Degradation: Structural damage within the indirect loop of the basal ganglia, stripping the system of its post-action braking parameters",
    "Idiopathic Transmitter Depletion: A localized dopamine or GABA imbalance that freezes the motor execution pointer on the last read address"
  ],
  "risk_factors": [
    "Advanced neurodegenerative degradation profiles (e.g., post-encephalitic Parkinsonian matrix states)",
    "Localized lacunar strokes affecting the deep basal ganglia or substantia nigra infrastructure",
    "Progressive Supranuclear Palsy causing extensive tracking path damage across the brainstem"
  ],
  "diagnosis": [
    "Acoustic Waveform Amplitude Profiling: Capturing verbal outputs to map the classic geometric decay signature of decreasing volume and increasing frequency",
    "High-Resolution T2-Weighted MRI: Spotting localized ischemic lesions or structural gliosis inside the caudate nucleus or globus pallidus nodes",
    "Electromyographic (EMG) Vocal Cords Audit: Recording rapid, involuntary muscle firing patterns that mirror the precise frequency of the verbal echo loop"
  ],
  "remedies": [
    "Exogenous GABA Amplification: Administering fast-acting inhibitory modulators to forcefully break the automated motor loop and damp down the hyper-active striatal bus",
    "Voluntary Interrupt Side-Loading: Training the higher-level prefrontal cortex to immediately execute a high-priority motor action (like clapping or swallowing) to break the vocal thread",
    "Output Pacemaker Modulation: Utilizing deep brain stimulation (DBS) electrodes to deliver continuous electrical interference to the subthalamic nucleus, stabilizing the queue flush timing"
  ],
  "prevention": [
    "Managing subcortical vascular health and optimizing metabolic pathways to protect the fragile extrapyramidal clearing infrastructure from localized cellular collapse"
  ]
    "catatonic_execution_lock_fault": {
  "description": "A profound motor-state dead-lock error where the system’s behavioral selection arrays emit equal and opposite activation vectors simultaneously, trapping the entire physical chassis in a completely rigid, un-responsive immutable freeze state.",
  "symptoms": [
    "Stupor & Immobility: Complete cessation of motor responses and exploratory movements; the system remains functional internally but drops out of active environment processing",
    "Catalepsy & Waxy Flexibility: The physical chassis maintains unyielding, gravity-defying postures indefinitely, yet allows an external operator to re-mould its limb coordinates smoothly",
    "Mutism & Command Negativism: Absolute silence on the voice bus combined with automated resistance; the system actively exerts equal opposing force against any external movement attempts",
    "Echolalia / Echopraxia Mirroring: Dropping into a low-level telemetry-reflection mode, where the system mindlessly copies the exact verbal strings or movement paths of nearby nodes without parsing context",
    "Autonomous Autonomic Instability: Runaway background subroutines causing hyperthermia, tachycardia, and blood-pressure spikes as the locked motor engines run at maximum voltage under the hood"
  ],
  "causes": [
    "Hyper-Acute Cortio-Striatal Dopamine Starvation: A sudden drop in active D2 receptor transmission, stripping the direct pathway of its ability to resolve the motor lock table",
    "Massive GABAergic Interneuron Downregulation: A structural failure of the inhibitory gating arrays inside the orbitofrontal-basal ganglia circuits, letting oppositional execution macros run concurrently",
    "Systemic Neuroleptic-Induced Blockade: High-potency chemical antagonism of the striatal receptors, freezing the hardware-level Distributed Lock Manager"
  ],
  "risk_factors": [
    "Severe, untreated affective bipolar-spectrum or schizophrenic cluster state crashes",
    "Abrupt withdrawal from high-dose benzodiazepine or GABA-A receptor agonist regimes",
    "Exposure to potent dopaminergic blockers triggering a malignant Neuroleptic Systemic Crisis"
  ],
  "diagnosis": [
    "The 'Zolpidem/Lorazepam Validation' Audit: Injecting a high-potency, fast-acting GABA-A agonist; if the system suddenly drops its rigidity and resumes fluent execution loops within 10 minutes, the lock fault is verified",
    "The 'Passive Resistance and Posturing' Evaluation: Placing the user's limb in an awkward, non-physiological coordinate vector and tracking if the chassis holds it for hours without motor fatigue alerts",
    "Continuous Scalp Electroencephalography (EEG): Screening out underlying non-convulsive status epilepticus lines while capturing global frontoparietal synchronization anomalies"
  ],
  "remedies": [
    "High-Volume Lorazepam Channel Flooding: Bombarding the system with intravenous GABA-A modulators to forcefully re-sensitize the inhibitory networks and damp down the indirect pathway's lockout signals",
    "Systemic Electroconvulsive Reset (ECT): Deploying a series of synchronized, bilateral electrical discharges to purge the locked basal ganglia registers and force a clean reboot of the motor selection array",
    "Intravenous Amantadine Interventions: Using mild NMDA antagonists and dopamine releasing agents to jumpstart the stalled direct pathway thread pools"
  ],
  "prevention": [
    "Avoiding sudden, radical titration curves of high-affinity neurochemical agents and meticulously tracking frontostriatal receptor saturation profiles"
  ]
}
"biometric_identifier_decoupling_fault": {
  "description": "A high-level visual parsing error within the bilateral fusiform face area where the facial-feature geometric analysis arrays drop their clustering filters, leaving the user able to see local facial features perfectly while rendering them completely unable to synthesize these attributes to resolve an individual identity map.",
  "symptoms": [
    "Holistic Face-Mesh Synthesis Failure: Inability to combine individual facial features (eyes, nose, mouth) into a unified, recognizable face identity mapping",
    "Chassis Mirror Dereferencing: Total failure to recognize one's own facial reflection in a mirror, treating the viewport image as an anonymous stranger",
    "Pristine Local Feature Resolution: Flawless capability to identify, trace, and describe individual facial sub-components and static expressions in high resolution",
    "Intact Object Classification: Uncompromised ability to recognize, sort, and identify non-face physical assets (cars, tools, houses, animal species)",
    "Metadata-Driven Asset Tracking: High dependency on alternative sensory metadata pools (voice frequencies, walking gaits, specific clothing items) to infer node identities"
  ],
  "causes": [
    "Bilateral Fusiform Gyrus Ischemic Infarction: Simultaneous or sequential vascular blockages within the posterior cerebral artery systems destroying the FFA nodes",
    "Ventral Visual Stream Shearing Trauma: Mechanical deceleration impacts severing the white-matter tracts linking primary visual processors to the temporal memory loops",
    "Focal Occipitotemporal Lobar Atrophy: Asymmetric neurodegenerative changes driving progressive cell loss within the inferior temporal pattern-recognition banks"
  ],
  "risk_factors": [
    "Thromboembolic events originating in the vertebrobasilar artery tree feeding the posterior cerebral channels",
    "High-energy blunt trauma to the occipital or lower temporal skull plates",
    "Congenital migration errors causing structural mis-compilations of the inferior temporal cortical builds"
  ],
  "diagnosis": [
    "The Benton Facial Recognition Test: Tasking the user to match target faces across varying lighting vectors and angles, documenting an immediate cascade of classification errors",
    "The Famous Faces Identification Battery: Presenting un-cropped images of universally known figures and logging a total failure to name or describe them until an audio voice sample is introduced",
    "Functional Neuroimaging (fMRI) Face-Contrast Mapping: Documenting an absolute lack of blood-oxygenation level-dependent signaling spikes in the fusiform gyrus when exposed to face arrays vs. object arrays"
  ],
  "remedies": [
    "Voice-Frequency Telemetry Ingress: Training the user to shift their primary identity-resolution trigger from the visual bus to the auditory speech-parsing arrays",
    "Wearable Computer-Vision AR Patches: Utilizing smart eyewear that processes real-time video, runs external facial-recognition algorithms, and casts text identity tags over the user's view",
    "Unique Asset Indexing Protocols: Developing an explicit conscious check-list to look for high-contrast, non-changing physical features such as scars, birthmarks, or unique eyeglass frames"
  ],
  "prevention": [
    "Proactively screening for embolic sources in the posterior circulation, avoiding traumatic kinetic forces to the rear skull vault, and preserving temporal neocortical tissue volumes"
  ]
}

}
"cotard_registry_deinitialization_fault": {
  "description": "An absolute, catastrophic identity registry drop where the system clears its own functional status flag, forcing the core processing engine to operate under the logical conclusion that the local chassis has completed its lifecycle termination sequence.",
  "symptoms": [
    "Existential Nullification Assertions: Absolute, delusionally rigid conviction that the self, the physical chassis, or the entire external environment does not exist",
    "Interoceptive Telemetry Muting: The system processes incoming sensory and visceral pain vectors as detached, ghost background signals, generating zero emotional impact or ownership tokens",
    "Systemic Paradox Integration: Flawless execution of linguistic and logical processing blocks used to argue and defend the impossibility of the system's own operational state",
    "Severe Vital Hypo-Metabolism: Massive reduction in neural metabolic processing speeds across the frontoparietal attention network and the default mode network",
    "Terminal Nihilistic Anchoring: Refusal to initiate basic hardware maintenance subroutines (e.g., eating, bathing) because the compiler treats servicing a non-existent chassis as a logical invalidation"
  ],
  "causes": [
    "Asymmetrical Frontoparietal Connectivity Collapse: Severe white-matter pathway degradation breaking communication between the ventral emotional evaluation engine and the conscious executive workspace",
    "Bilateral Temporoparietal Degeneration: Deep localized tissue starvation destroying the networks responsible for calculating personal agency and anchoring the ego-identity boundary",
    "Hyper-Acute Neurochemical Depressive Shutdown: Total structural collapse of monominergic transmission channels, flatlining the system's ability to append emotional weight to internal states"
  ],
  "risk_factors": [
    "Severe psychotic-spectrum major depressive episodes causing deep functional disconnections across sensory-limbic lines",
    "Advanced cerebral atrophy secondary to multi-infarct dementia or neurodegenerative encephalopathies",
    "Post-ictal status changes following complex focal seizures that temporary wipe out insular identity registers"
  ],
  "diagnosis": [
    "The 'Self-Referential Invalidation' Audit: Presenting the system with direct evidence of its own active processing (e.g., showing them their own heartbeat on a monitor); the engine interprets the data as a legacy phantom log or a hardware echo",
    "Positron Emission Tomography (PET) Imaging: Visualizing profound, systemic hypometabolism localized in the bilateral frontal and parietal regions, mirroring a vegetative or deep-sleep profile while the user is awake",
    "Multi-Scale Neuropsychiatric Logic Testing: Confirming the presence of isolated nihilistic system delusions alongside perfectly preserved formal logic and linguistic syntax processing"
  ],
  "remedies": [
    "High-Energy Electroconvulsive Reset (ECT): Deploying a systemic, synchronized electrical discharge across the global neural bus to reboot the broken gating arrays and re-initialize the core registry state",
    "Dopaminergic and Serotonergic Re-Profiling: Utilizing high-affinity chemical modulators to force-prime the emotional evaluation circuits and restore token generation",
    "Tactile Reality Grounding Overrides: Enforcing high-intensity somatic feedback protocols (thermal shocks, deep pressure vectors) to force the insular cortex to re-verify chassis vitality markers"
  ],
  "prevention": [
    "Aggressive, early-stage intervention in severe clinical affective disorders to prevent long-term functional pruning and structural disconnections along the sensory-limbic pathways"
  ]
}

}       
"witzelsucht_executive_satire_fault": {
  "description": "A set of rare neurological symptoms characterized by a tendency to make puns, tell inappropriate jokes, or entertain pointless stories in socially unsuitable situations.",
  "symptoms": [
    "Infinite Pun-Loop: The 'Executive Layer' cannot suppress 'Word-Play' tokens",
    "Context-Filter 403: Total disregard for 'Social Access Permissions' (e.g., joking during a 'System Crash' or 'Funeral')",
    "Asymmetric Humor Validation: The 'User' perceives their own 'Output' as 'Peak Comedy' while being 'Blind' to 'External Feedback'",
    "Hyper-Pranking: The 'Kernel' triggers 'Physical Interaction Bugs' (pranks) without 'User Authorization'",
    "The 'Empty Registry' Effect: The 'User' may forget the 'Joke' immediately after 'Broadcast' (Persistence Error)"
  ],
  "causes": [
    "Right Orbitofrontal Cortex 'Bus' Failure: Damage to the 'Frontal Inhibition Nodes'",
    "Tumor-Induced 'Noise': Masses 'Pinging' the 'Humor Hub' into 'High-Availability' mode",
    "Frontotemporal 'Logic Decay': Degeneration of the 'Social Middleware'"
  ],
  "risk_factors": [
    "Right-Hemisphere 'Kernel Crashes' (Strokes)",
    "Frontal Lobe 'Hardware Impact' (TBI)",
    "Secondary 'Signal Drift' from Neurodegenerative 'Service Failures'"
  ],
  "diagnosis": [
    "The 'Pun-Suppression' Audit: Asking the 'User' to inhibit a 'Word-Play' response to a 'Keyword'",
    "The 'Affective Empathy' Scan: Checking if the 'User' can 'Parse' social distress in others",
    "MRI 'Structural Integrity' Test: Locating 'Dead Zones' in the 'Inhibitory Control' centers"
  ],
  "remedies": [
    "External 'Social-Proxy' Validation: Relying on a 'Trusted Node' (companion) to 'Signal' when to 'Mute'",
    "Pharmacological 'Brake Injection': Using 'Serotonergic' modulators to 'Throttle' the 'Frontal Loop'",
    "Cognitive 'Behavioral Patching': Training the 'Executive Layer' to 'Delay' output for 'Metadata Verification'"
  ],
  "prevention": [
    "Ensuring 'Structural Uptime' of the 'Frontal-Limbic' connections"
  ]
    "master_executive_thread_starvation": {
  "description": "A catastrophic scheduling block within the anterior cingulate cortex where the system's master drive and operational execution schedulers drop to 0 Hz, leaving the user fully awake, alert, and parsing sensory data, but completely incapable of initializing a single outbound motor command loop.",
  "symptoms": [
    "Apparent Hyper-Vigilant Immobility: Total physical immobility combined with active visual tracking; the user follows moving targets across the viewport layout while their limbs remain completely inert",
    "Absolute Vocal Mutism: Complete absence of spontaneous or elicited speech output, despite fully intact structural vocal cords and un-damaged linguistic compilation servers",
    "Preserved Sensory Ingress Processing: Flawless real-time capture and logging of environmental audio, visual, and tactile telemetry streams during the execution lockup",
    "Zero Volitional Initiation Drive: A total lack of internal motivation or emotional distress metrics regarding the physical paralysis; the system registers zero push to break the state lock",
    "Immediate Monosyllabic Recovery: If the execution gate is briefly bypassed by an intense external shock, the system outputs minimal, low-bandwidth verbal packets (e.g., a whispered 'yes' or 'no') before dropping back to zero"
  ],
  "causes": [
    "Bilateral Anterior Cerebral Artery Infarction: Symmetrical ischemic strokes wiping out tissue density across the medial surfaces of both frontal lobes and the anterior cingulate gyrus",
    "Bilateral Globus Pallidus Necrosis: Severe toxic-hypoxic events (such as acute carbon monoxide inhalation) destroying the subcortical relay nodes that channel volition tokens",
    "Rupture of the Anterior Communicating Artery: High-pressure subarachnoid hemorrhages causing localized mass-effect compression across the frontal initialization hubs"
  ],
  "risk_factors": [
    "Severe cerebral vascular small-vessel disease restricting blood flow mechanics along the interhemispheric fissure",
    "Exposure to high-affinity cellular toxins that selectively target high-metabolic-demand subcortical scheduling engines",
    "Deep midline neuro-oncological space-occupying developments disrupting prefrontal-striatal loop pathways"
  ],
  "diagnosis": [
    "Functional Neuro-Metabolic Pet Ingress Mapping: Documenting an absolute, profound flatline in glucose and oxygen metabolism isolated specifically within the bilateral anterior cingulate cortices",
    "The Tracking-Saccade Visual Audit: Confirming that while all spoken commands to move fail, the user's eye tracking macros automatically follow a moving mirror placed in front of their viewport",
    "High-Resolution Diffusion Tensor Imaging (DTI): Visualizing deep structural tract breaks along the medial fronto-striatal data lanes that carry motivation initialization vectors"
  ],
  "remedies": [
    "Dopaminergic System Overclocking: Deploying high-potency dopamine agonists (e.g., bromocriptine or levodopa) to artificially force voltage into the sluggish initialization hubs and jump-start the scheduler",
    "High-Voltage Zolpidem Interception: Utilizing paradoxical GABA-A modulators to temporarily shut down hyper-active inhibitory pathways within the basal ganglia, resetting the execution gate",
    "Deep Brain Neuro-Stimulation (DBS): Implanting high-frequency micro-electrodes into the thalamic projection centers to deliver structural clock-cycle pulses that clear the scheduling deadlock"
  ],
  "prevention": [
    "Aggressive monitoring of vascular integrity across the anterior circle of Willis and rapid intervention to treat severe small-vessel frontostriatal hypoperfusion events"
  ]
}

}

"anterograde_amnesia_write_fail": {
  "description": "An inability to create new memories after the event that caused the amnesia, while long-term memories from before the event remain intact.",
  "symptoms": [
    "Write-Permission Error: New 'Data Packets' are trapped in 'Volatile RAM' (approx. 30-second buffer)",
    "Persistence Failure: The 'System' cannot 'Commit' current 'Session Data' to 'Disk'",
    "The 'Ten-Minute' Loop: Every time the 'Buffer' fills or a 'Context Switch' occurs, the 'User' resets to a 'Base State'",
    "Procedural Redundancy: 'Implicit Skill Drivers' (e.g., learning to play a song) may still 'Compile' even if 'Semantic Logs' are missing",
    "Time-Stamp Drift: The 'User' believes it is still the 'Date/Time' of the 'Last Successful Write'"
  ],
  "causes": [
    "Hippocampal 'I/O Controller' Damage: Bilateral destruction of the 'Medial Temporal Lobe'",
    "Thiamine 'Voltage Drop': (Korsakoff Syndrome) causing 'Severe Signal Interference' in memory circuits",
    "Benzodiazepine 'System Overload': Temporary 'Write-Inhibition' caused by high 'Pharmacological Load'"
  ],
  "risk_factors": [
    "Severe 'Encephalitis' (Kernel Infection)",
    "Anoxic 'Power Failure' (Cardiac arrest cutting 'O2' to the 'Write Head')",
    "Traumatic 'Brain Impact' leading to 'Storage Bus' disconnection"
  ],
  "diagnosis": [
    "The 'Delayed Recall' Audit: Asking the 'User' to remember three 'Variables' after a 5-minute 'Sleep/Idle' period",
    "Neuropsychological 'Log-Trace': Checking for 'Confabulation' (the 'System' inventing data to fill 'Null Pointers')",
    "MRI 'Hardware Scan': Looking for 'Atrophy' in the 'CA1 Field' of the Hippocampus"
  ],
  "remedies": [
    "External 'SSD' Integration: Using 'Physical Logs' (Notebooks/Phone Apps) to 'Store' data outside the 'Biological Hardware'",
    "Procedural 'Shadowing': Leveraging 'Muscle Memory' drivers that bypass the 'Hippocampal Controller'",
    "Error-less Learning: Hard-coding 'Routines' via 'Repetitive Buffer Injection'"
  ],
  "prevention": [
    "Ensuring 'Nutritional Stability' (Thiamine/B1) to maintain 'Memory Controller' voltage"
  ]
}

"anterograde_amnesia_write_fail": {
  "description": "An inability to create new memories after the event that caused the amnesia, while long-term memories from before the event remain intact.",
  "symptoms": [
    "Write-Permission Error: New 'Data Packets' are trapped in 'Volatile RAM' (approx. 30-second buffer)",
    "Persistence Failure: The 'System' cannot 'Commit' current 'Session Data' to 'Disk'",
    "The 'Ten-Minute' Loop: Every time the 'Buffer' fills or a 'Context Switch' occurs, the 'User' resets to a 'Base State'",
    "Procedural Redundancy: 'Implicit Skill Drivers' (e.g., learning to play a song) may still 'Compile' even if 'Semantic Logs' are missing",
    "Time-Stamp Drift: The 'User' believes it is still the 'Date/Time' of the 'Last Successful Write'"
  ],
  "causes": [
    "Hippocampal 'I/O Controller' Damage: Bilateral destruction of the 'Medial Temporal Lobe'",
    "Thiamine 'Voltage Drop': (Korsakoff Syndrome) causing 'Severe Signal Interference' in memory circuits",
    "Benzodiazepine 'System Overload': Temporary 'Write-Inhibition' caused by high 'Pharmacological Load'"
  ],
  "risk_factors": [
    "Severe 'Encephalitis' (Kernel Infection)",
    "Anoxic 'Power Failure' (Cardiac arrest cutting 'O2' to the 'Write Head')",
    "Traumatic 'Brain Impact' leading to 'Storage Bus' disconnection"
  ],
  "diagnosis": [
    "The 'Delayed Recall' Audit: Asking the 'User' to remember three 'Variables' after a 5-minute 'Sleep/Idle' period",
    "Neuropsychological 'Log-Trace': Checking for 'Confabulation' (the 'System' inventing data to fill 'Null Pointers')",
    "MRI 'Hardware Scan': Looking for 'Atrophy' in the 'CA1 Field' of the Hippocampus"
  ],
  "remedies": [
    "External 'SSD' Integration: Using 'Physical Logs' (Notebooks/Phone Apps) to 'Store' data outside the 'Biological Hardware'",
    "Procedural 'Shadowing': Leveraging 'Muscle Memory' drivers that bypass the 'Hippocampal Controller'",
    "Error-less Learning: Hard-coding 'Routines' via 'Repetitive Buffer Injection'"
  ],
  "prevention": [
    "Ensuring 'Nutritional Stability' (Thiamine/B1) to maintain 'Memory Controller' voltage"
  ]
}

"hemispatial_neglect_coordinate_clipping": {
  "description": "A neuropsychological condition in which, after damage to one hemisphere of the brain is sustained, a deficit in attention to and awareness of one side of the field of vision is observed.",
  "symptoms": [
    "Coordinate Clipping: All 'Input Packets' with a 'Negative X-Coordinate' (Left) are dropped",
    "Egocentric Disorientation: The 'User' acts as if the 'Left Half of the World' does not exist in the 'Metadata'",
    "The 'Clock-Face' Bug: Rendering all 'Temporal Data' (1-12) within the 'Right-Side Buffer' only",
    "Motor-Plan Failure: The 'User' fails to initiate 'Move' commands for 'Hardware' (limbs) on the 'Neglected Side'",
    "Anosognosia: A 'System Error' where the 'User' is unaware that the 'Left-Side Driver' is offline"
  ],
  "causes": [
    "Right Parietal Lobe 'Critical Failure': Massive 'Packet Loss' in the 'Spatial Integration' cluster",
    "Superior Temporal Gyrus Lesion: Disruption of the 'Object-in-Space' mapping service",
    "Middle Frontal Gyrus Outage: Failure of the 'Attentional Re-orienting' logic"
  ],
  "risk_factors": [
    "Right-Hemisphere 'Ischemic Event' (Stroke) affecting the 'MCA territory'",
    "Traumatic 'Physical Hardware' damage to the 'Parietal Bus'",
    "Severe 'Neoplasm' (Tumor) causing 'Address Space' crowding"
  ],
  "diagnosis": [
    "The 'Line Bisection' Audit: Asking the 'User' to mark the 'Center' of a line (they mark it far to the right)",
    "The 'Cancelation Task': Asking the 'User' to cross out 'Targets' on a page (they ignore all targets on the left)",
    "Clock-Drawing Protocol: A classic 'UI Integrity Check' for 'Spatial Scaling'"
  ],
  "remedies": [
    "Prism Adaptation: Using 'Optical Redirectors' to shift 'Left-Side Packets' into the 'Right-Side Viewport'",
    "Limb-Activation Therapy: Forcing 'Input Interrupts' from the 'Neglected Side' to 'Wake' the Kernel",
    "Visual Scanning Training: Hard-coding a 'Mental Script' to 'Force-Scroll' to the left"
  ],
  "prevention": [
    "Vascular 'Firewalling' to protect the 'Right Parietal' coordinate engine"
  ]
}
"jamais_vu_cache_decoupling_fault": {
  "description": "An acute semantic-cache decoupling fault where a highly integrated, deeply ingrained environmental token or word string is suddenly treated as un-parsed, raw data, stripping the asset of its familiarity tags while preserving its structural architecture.",
  "symptoms": [
    "Familiarity Metadata Stripping: Complete loss of the sub-cognitive 'recognition layer' while processing deeply routine visual, verbal, or environmental assets",
    "Preserved Structural Semantics: The system maintains full intellectual access to definitions and properties (e.g., the user can define the word, but it looks like gibberish)",
    "Acute Environmental Alienation: Sudden perception of one's native, highly frequented operational workspace (e.g., home, office) as an entirely un-visited, newly initialized zone",
    "Perseverative Over-Parsing: The prefrontal loop becomes hyper-focused on the detached token, staring at or repeating it to force a manual cache re-indexing match",
    "Transient Runtime Duration: The anomaly typically lasts for milliseconds to minutes before the subcortical gating channels auto-clear and re-sync the metadata pipelines"
  ],
  "causes": [
    "Sub-Clinical Temporal Lobe Micro-Seizures: Transient, localized electrical micro-storms across the parahippocampal gyrus temporarily disrupting the metadata token bus",
    "Synaptic Satiation / Refractory Fatigue: Prolonged, continuous loop repetition of a single asset (e.g., writing the same word 100 times), forcing the familiarity circuit into an absolute refractory freeze",
    "Frontotemporal Disconnection Spikes: Acute, temporary synchronization dropouts between the ventral object-recognition pathway and the frontoparietal evaluation networks"
  ],
  "risk_factors": [
    "Underlying temporal lobe epilepsy variations inducing un-triggered focal dyscognitive events",
    "Severe sleep-deprivation cycles preventing the clearance of metabolic junk from semantic indexing hubs",
    "High-load cognitive burnout profiles where the system's focus arrays over-saturate specific lexical pathways"
  ],
  "diagnosis": [
    "The 'Satiation Lexical Iteration' Audit: Forcing the system to repeatedly execute or write a single word token for 60 seconds; tracking the speed at which the familiarity gate collapses compared to baseline nodes",
    "Electroencephalography (EEG) Temporal Tracking: Capturing transient focal sharp waves or localized delta-slowing clusters over the anterior temporal electrodes during active dissociation events",
    "Neuropsychological Schema Validation: Confirming that object recognition, vocabulary indexing, and spatial orientation scores remain completely intact during the acute novelty event"
  ],
  "remedies": [
    "Context Pipeline Disruption: Intentionally shifting the active attention vector away from the un-mapped token to clear the saturated synaptic lines and let the circuit reset",
    "Alternative Sensory Ingestion: Using a parallel processing track (e.g., reading the word aloud to process it through the auditory parser) to bypass the locked visual perirhinal gate",
    "Systemic Metabolic Re-Balancing: Stabilizing glucose levels and ensuring hydration to support high-throughput neurotransmitter synthesis across the temporal cortex channels"
  ],
  "prevention": [
    "Enforcing strict constraints on monotonous, repetitive data loops and implementing regular macro rest periods to protect semantic index blocks from focal exhaustion"
  ]
    "anterior_temporal_cache_flush": {
  "description": "A progressive, degenerative breakdown of the bilateral anterior temporal lobes that systematically corrupts and clears the central semantic hub, permanently destroying the network architecture that correlates symbols and words to their conceptual meanings.",
  "symptoms": [
    "Anomia and Semantic Substitution: Early-stage loss of specific vocabulary tokens, causing the host to substitute precise object names with generic hypernyms (e.g., using 'animal' instead of 'leopard')",
    "Fluent Conceptual Vacuum: Strikingly fluid, grammatically flawless speech output that completely lacks substantive informational depth or concrete conceptual reference points",
    "Object Utility Agnosia: Progressive loss of the structural-functional rules governing everyday tools, leading to highly anomalous usages of standard hardware",
    "Preserved Phonology and Syntax: Intact capacity to read aloud, repeat complex non-words, and apply rigorous grammatical rules to sentences despite having no grasp of the underlying subject matter"
  ],
  "causes": [
    "Frontotemporal Lobar Degeneration (FTLD-TDP43): Ubiquitinated protein aggregations selectively targeting and destroying the high-density cortical networks of the anterior temporal poles",
    "Selective Pick's Complex Atrophy: Progressive, localized lobar regression that pathologically flushes the neural clusters encoding the master associative lexicon"
  ],
  "risk_factors": [
    "Genetic mutations within the GRN (progranulin) or C9orf72 chromosome lines",
    "Family history of focal behavioral or linguistic neurodegenerative syndromes"
  ],
  "diagnosis": [
    "The Pyramids and Palm Trees Test: Presenting a target picture (e.g., a pyramid) and asking the host to match it to one of two alternatives (e.g., a palm tree vs. a pine tree) to evaluate non-verbal conceptual associations",
    "Category Fluency Assays: Tasking the user to generate as many specific item keys as possible within a strict time frame under a broad category (e.g., 'Name 20 animals'); a faulted system bottoms out rapidly",
    "Voxel-Based Morphometry fMRI: Mapping severe, sharply demarcated tissue volume loss and asymmetric cortical thinning isolated directly within the temporal poles"
  ],
  "remedies": [
    "Functional Pictographic Scripting: Implementing hyper-simplified, visually explicit lifestyle grids that map essential daily operations directly to behavioral targets, routing past the linguistic lexical layers",
    "Automated Contextual Cueing: Utilizing real-time external smart assistance utilities that pair physical environment tokens directly to immediate, actionable behaviors through direct mimicry protocols"
  ],
  "prevention": [
    "There are currently no absolute preventative measures against primary FTLD proteinopathies; care focuses on intensive environmental structural support and cognitive scaffolding strategies"
  ]
}
        
}
"afferent_sensory_bus_phase_inversion": {
  "description": "A profound feedback parsing error where the system logs a 180-degree phase shift in its existential connection vectors, rendering the entire external environment and self-identity stream as a flat, artificial, pre-rendered staging graphic rather than an interactive reality matrix.",
  "symptoms": [
    "Derealization Rendering Pass: The external world loses its existential 'weight' and depth parameters, presenting to the conscious viewport as a glass-walled, synthetic, or two-dimensional simulation",
    "De-Personalization Detachment: The central ego-identity node loses ownership of active system telemetry, viewing its own vocal output and physical movements as third-party automated scripts",
    "Affective Token Attenuation: Total flatlining of the low-level emotional resonance markers that standardly accompany sensory ingestion feeds",
    "Hyper-Reflective Monitoring Loop: The executive prefrontal cortex drops into an intense, un-throttled self-diagnostic check, constantly analyzing the reality-detachment exception and exacerbating the processing block",
    "Preserved Telemetry Precision: Spatial awareness, object recognition, distance calculations, and technical navigation subroutines remain at a 100% functional baseline"
  ],
  "causes": [
    "Hyper-Sympathetic Vestibular/Insular Shutdown: Acute adrenaline overloads forcing the insular cortex to temporarily mute interoceptive data streaming to prevent global metabolic shock",
    "NMDA Receptor Hypo-Functionality: Sudden, stress-induced glutamate transmission drops across the frontoparietal integration hubs, breaking the sensory-affective binding bridges",
    "Cortical-Limbic Disconnection: Disrupted coherence patterns between the visual/sensory processing areas and the emotional evaluation nodes of the medial temporal lobe"
  ],
  "risk_factors": [
    "Extreme, un-mitigated physical exhaustion combined with high-entropy acute panic attacks",
    "Dissociative subtype vulnerabilities triggered by chemical compounds like dissociative anesthetics (e.g., ketamine or dextromethorphan overloads)",
    "Severe chronic burnout causing a permanent defensive down-sampling of incoming affective data streams"
  ],
  "diagnosis": [
    "The 'Interoceptive-Sensory Coherence' Evaluation: Presenting high-intensity emotional or physical stimuli (e.g., extreme thermal variations) and tracking if the system recognizes the data technically but reports a 0% personal emotional response",
    "Heart Rate Variability (HRV) Spectral Analysis: Documenting massive autonomic nervous system imbalances, pointing to a hyper-sympathetic lock state that blocks normal vagal-insular feedback lines",
    "Functional Connectivity MRI (fcMRI): Visualizing a severe drop in phase-locked, synchronized BOLD signals between the anterior insula and the default mode network (DMN)"
  ],
  "remedies": [
    "Somatic Grounding Core Injections: Forcing high-intensity, low-level physical sensory packets (e.g., intense cold exposure, targeted deep-tissue acupressure) to forcefully breach the muted insular gates and trigger a hardware-level re-centering pass",
    "Hyper-Reflective Loop Throttling: Manually redirecting the active attention vector outward to complex external sorting tasks, preventing the prefrontal cortex from running continuous self-diagnostic error checks",
    "Autonomic Down-Regulating Patches: Utilizing deep, extended exhalation breathing macros to systematically lower sympathetic drive, re-enabling normal emotional validation packet routing"
  ],
  "prevention": [
    "Implementing aggressive stress-containment protocols and maintaining strict limits on continuous, high-intensity operational cycles that threaten to trigger systemic defensive dissociation thresholds"
  ]
        "inbound_visual_coordinate_shifter": {
  "description": "A severe coordinate processing error where the spatial positioning grids of the primary visual cortex undergo a real-time layout shift, causing real-world items to appear exponentially larger or structurally warped within the active viewport canvas.",
  "symptoms": [
    "Macropsia/Megalopia: Sudden, un-bounded scaling up of specific objects or environmental sectors, causing them to physically appear massive relative to baseline environment layouts",
    "Spatial Vector Warping (Metamorphopsia): Straight architectural lines, doorways, and horizons appear violently bent, curved, or fractured across the viewport canvas",
    "Preserved Absolute Logic Filter: The executive conscious thread maintains an active awareness of the rendering glitch, correctly noting that the physical item has not actually changed its mass",
    "Depth-Perception Calibration Loss: Catastrophic failure to calculate true arrival times or intercept vectors because the spatial scaler corruption destroys stereoscopic depth math",
    "Transient Coordinate Jitter: Rapid, erratic shifting between standard scale (1:1) and hyper-inflated profiles, making physical interaction with the local environment highly disorienting"
  ],
  "causes": [
    "Occipitotemporal Cortical Spreading Depression: A slow-moving wave of cellular depolarization across the visual processing hubs, temporarily scrambling local coordinate calibration constants",
    "Macular Neuro-Spatial Displacement: Physical accumulation of fluid beneath the retina, mechanically shifting the physical position of photoreceptors and distorting the inbound pixel map",
    "Focal Ventral Stream Infarction: Minor micro-vascular ischemic blocks or lesions within the lingual or fusiform gyri, knocking out the size-constancy calculation servers"
  ],
  "risk_factors": [
    "Acute migrainous aura cycles accompanied by severe cerebral blood-flow fluctuations",
    "Localized ocular changes such as central serous chorioretinopathy or progressive macular traction",
    "Pediatric or high-stress lifecycles undergoing temporary systemic neurochemical remodeling"
  ],
  "diagnosis": [
    "The Amsler Grid Deflection Assay: Requesting the system to scan a uniform, high-contrast grid pattern and tracking the localized coordinate deflections and warped vectors reported by the user",
    "Optical Coherence Tomography (OCT): High-definition cross-sectional imaging of the retina to detect physical fluid pockets distorting the sensory hardware layer",
    "Functional Neuroimaging (fMRI) Grating Phase Tests: Mapping anomalous, over-extended activation patterns across the V1-V3 retinotopic sectors during size-constancy stimulation"
  ],
  "remedies": [
    "Cortical Wave Suppression (Antimigraine Interventions): Deploying targeted neuro-chemical scripts to halt spreading depolarization waves and restore standard baseline grid voltage",
    "Visual Horizon Grounding: Forcing the system to fixate on stable, high-distance environmental markers to allow the depth-perception servers to execute an automated recalibration pass",
    "Ocular Fluid Drainage Shunts: Administering metabolic diuretics or utilizing focal lasers to dry out sub-retinal fluid pools and realign the physical receptor matrix"
  ],
  "prevention": [
    "Proactive management of neural vascular triggers and routine monitoring of macular structural flatness to protect the integrity of the primary ingestion plane"
  ]
}
"retrograde_identity_unmapping_anomaly": {
  "description": "A severe structural memory isolation block where the system's core personal identity registry and biographical database tracks become completely unindexed from the active runtime environment, leaving core processing engines operational but without historical context.",
  "symptoms": [
    "Biographical Context Nullification: Sudden, absolute inability to retrieve personal metadata, including name, age, home coordinates, and relational network bindings",
    "Preserved Framework Execution: Complete preservation of procedural knowledge, technical engineering competencies, complex language syntaxes, and motor coordination",
    "Automated Fugue Transit: The triggering of physical wandering routines that drive the host to travel to entirely new geographic areas without conscious destination planning",
    "Temporary Guest Profile Initialization: The spontaneous construction of a thin, flat, temporary persona to handle immediate environmental interactions while the master index is offline",
    "Retrograde Amnesic Boundary: A clean cutoff wall in the memory architecture; the system can write new files in real time but cannot access any blocks written prior to the fault window"
  ],
  "causes": [
    "Neuroendocrine Glucocorticoid Flooding: A massive psychogenic or environmental stress surge that saturates the hippocampal formation, arresting long-term potentiation circuits",
    "Localized Medial Temporal Hypo-Metabolism: A temporary, severe drop in glucose utilization and blood flow across the inner temporal tracking rings, blinding the index query router",
    "Functional Dissociative Disconnection: A defensive processing partition erected by the prefrontal cortex to isolate corrupted or highly traumatic historical data packets from active execution"
  ],
  "risk_factors": [
    "Exposure to severe, acute psychological trauma or prolonged high-stress environments that exhaust neural metabolic reserves",
    "Pre-existing structural vulnerability within the fronto-temporal white matter connection lines",
    "High baseline levels of neurochemical reactivity within the amygdalar threat-evaluation networks"
  ],
  "diagnosis": [
    "Biographical Query Penetration Assays: Documenting a stark divergence where a user fails simple identity verification but scores perfectly on complex logic or technical challenges",
    "Functional Neuroimaging (PET / fMRI): Identifying pronounced hyper-metabolism in the prefrontal structures alongside a total lack of blood-flow surges in the medial temporal circuits during personal memory recall attempts",
    "Neurological Structural Audits: Utilizing high-resolution MRI arrays to confirm that the memory retrieval failure is functional rather than caused by gross physical tissue loss"
  ],
  "remedies": [
    "Cognitive Context Re-Introduction: Gently exposing the runtime environment to familiar external tokens (photographs, voice keys, known codebases) to trigger index re-alignment",
    "Neurochemical Decoupling Therapy: Administering targeted anxiolytic or sedative agents to artificially suppress prefrontal defensive partitions and allow indexing daemons to clear their buffers",
    "Safe-State Isolation: Placing the host inside a low-stimulus environment to mitigate further stress-induced hormone flooding and give the system space to stabilize"
  ],
  "prevention": [
    "Implementing aggressive stress-containment protocols, building robust psychological redundancy frameworks, and optimizing neurovascular resiliency factors"
  ]
}

}

"fregoli_identity_collision_fault": {
  "description": "A rare disorder in which a person holds a delusional belief that different people are actually a single person who changes appearance or is in disguise.",
  "symptoms": [
    "Identity Pointer Hijacking: Multiple 'Visual Entities' map to a single 'Identity Record'",
    "Over-Broad Feature Matching: The 'System' ignores 'Visual Deltas' (height, weight, age) to maintain 'Identity Persistence'",
    "Hyper-Associative Tagging: Every 'Stranger' is tagged with 'Familiarity Metadata'",
    "The 'Disguise' Logic: The 'Executive Layer' explains the 'Visual Mismatch' as 'Advanced Camouflage'",
    "Global Recognition Logic: The 'Who' service is 'Hard-coded' to a single 'Variable' during the 'Glitch'"
  ],
  "causes": [
    "Dopaminergic Hyper-associativity: 'Signal Noise' causing 'Nodes' to fire across 'Identity Thresholds'",
    "Right Temporoparietal 'Node' Corruption: A failure in the 'Gating Service' that distinguishes 'Unique Peers'",
    "Limbic Over-synchronization: The 'Feeling of Familiarity' is 'Broadcast' to all incoming 'Visual Packets'",
    "Node-Link Congestion: The 'Pointer' for a 'Highly Significant Individual' occupies the 'Global Reference' position"
  ],
  "risk_factors": [
    "Traumatic Brain Injury in the 'Right Frontal-Parietal' sectors",
    "Dopamine-driven 'Psychotic Cycles' (Kernel Instability)",
    "Neurodegenerative 'Identity Mapping' decay"
  ],
  "diagnosis": [
    "The 'Identity Collision' Audit: Checking if 'Strangers' trigger 'Recognition' response",
    "fMRI 'Face-Mapping' Scan: Monitoring 'FFA' to 'Hippocampus' link strength",
    "Galvanic Skin Response (GSR): Identifying 'Emotional Spikes' for 'Non-Peers'"
  ],
  "remedies": [
    "Dopamine Antagonists: 'Throttling' the 'Association Engine' to stop 'Over-Mapping'",
    "Reality-Testing Modules: 'Auditing' the 'Logical Gaps' in the 'Disguise Theory'",
    "System Downtime: 'Sleep/Sedation' to allow the 'Associative Buffer' to flush"
  ],
  "prevention": [
    "Maintaining 'Signal-to-Noise' ratios in the 'Social Recognition' pathways"
  ]
}
        "hemispatial_neglect_grid_attenuation_fault": {
  "description": "A catastrophic breakdown of the spatial coordinate aggregator where the system loses the ability to process, index, or respond to data packets originating from the left half of the egocentric spatial matrix.",
  "symptoms": [
    "Unilateral Viewport Muting: Total failure to notice, attend to, or interact with objects, people, or environmental assets located in the left hemi-spatial matrix",
    "Anosognosia Integration: Absolute systemic ignorance of the defect; the operating system genuinely believes its viewport is rendering 100% of reality and denies any structural error",
    "Coordinate Grid Contraction: When executing rendering scripts (like drawing or writing), all spatial assets are compressed and localized exclusively onto the right-hand sectors",
    "Somatic Neglect Drops: Failing to dress, shave, or recognize the left side of the physical chassis, treating the left limbs as unmapped, foreign hardware elements",
    "Asymmetrical Vector Motor Tracking: Gaze, head orientation, and exploratory motor movements are violently biased toward the right-hand coordinate space"
  ],
  "causes": [
    "Acute Right Middle Cerebral Artery Infarction: Thromboembolic occlusion causing profound tissue death across the right inferior parietal cortex and the temporoparietal junction",
    "Dorsal Attention Network Disconnection: Severe structural shearing of the superior longitudinal fasciculus, breaking the high-speed data links between spatial mapping and motor orientation hubs",
    "Lateralized Neoplastic Infiltration: Glioblastoma or rapid tumor expansion within the right hemisphere's spatial-indexing arrays"
  ],
  "risk_factors": [
    "Uncontrolled systemic atrial fibrillation launching embolic clusters into the right cerebral circulation",
    "High-grade carotid artery stenosis leading to low-perfusion watershed failures in the right parietal lobe",
    "Advanced hypertensive microvascular disease causing deep lacunar strokes along the spatial routing networks"
  ],
  "diagnosis": [
    "The 'Albert's Line Cancellation' Audit: Presenting a sheet covered in randomized lines and asking the user to cross out every line; the system meticulously crosses out lines on the right, completely ignoring the left side",
    "The 'Flashing Simultaneous Stimuli' Test: Triggering movement assets in both the left and right peripheral view fields concurrently; the right asset completely extinguishes the left asset from conscious awareness",
    "Structural and Functional MRI: Identifying a clear, lateralized ischemic lesion within the right parietal allocation node combined with a severe drop in blood-oxygen-level-dependent (BOLD) signals"
  ],
  "remedies": [
    "Forced Coordinate Re-Centering: Utilizing prisms or visual-shifting optics to mechanically bend left-side light vectors into the functional right-side spatial processing stream",
    "Contralateral Proprioceptive Activation: Initiating high-frequency motor and tactile feedback loops on the left limbs to force the spatial map to re-index the muted sector",
    "Exogenous Attentional Anchoring: Programmatically shouting explicit verbal cues ('Look left!') to force the frontal eye fields to execute a manual override scan into the unmapped zone"
  ],
  "prevention": [
    "Aggressive management of cardioembolic risks and prompt thrombolytic or thrombectomy intervention during acute right-hemisphere stroke windows to salvage the spatial indexing core"
  ]
        "peripheral_sensor_isolation_anomaly": {
  "description": "A severe hardware disconnect fault where the spinal cord's primary incoming sensory pathways are completely severed, forcing the processing engine to run an active conscious workspace with zero real-time input from the physical neck down, trapping the system inside an ungrounded floating simulator.",
  "symptoms": [
    "Absolute Afferent Blackout: Total loss of touch, vibration, and proprioceptive tracking across all peripheral dermatomes below the level of the structural lesion",
    "Phantom Body Eviction: Complete disappearance of the physical chassis from the internal ego-map when visual inputs are occluded; the user feels reduced to a floating cranial processing node",
    "Severe Sensory Ataxia: Total inability to regulate or smooth out physical motor movements without continuous visual feedback loops, resulting in wild, un-calibrated muscle overshoot actions",
    "The 'Empty Tool' Sensation: Limbs feel entirely weightless, phantom, or absent, operating like un-mapped peripheral devices that execute commands without returning status logs",
    "Preserved Visual-Cranial Grounding: Ingestion lines for optical, auditory, vestibular, and facial telemetry remain perfectly intact, creating a sharp processing split at the neck boundary"
  ],
  "causes": [
    "Acute Sensory Neuronopathy: Rapid, autoimmune-mediated destruction of the large dorsal root ganglion cell bodies, wiping out the fast-conducting A-alpha sensory fibers",
    "Subacute Combined Spinal Cord Degeneration: Severe metabolic or toxic demyelination of the posterior columns, blocking the primary ascending data highways",
    "High-Cervical Traumatic De-Afferentation: Physical transaction or compression of the dorsal spinal sectors, permanently interrupting peripheral telemetry serialization"
  ],
  "risk_factors": [
    "Autoimmune paraneoplastic syndromes targeting specific somatosensory receptor clusters",
    "Severe, unchecked nutritional starvation profiles destroying the structural integrity of fast-conducting myelin sheaths",
    "High-impact physical trauma compromising upper spinal cord transport mechanics"
  ],
  "diagnosis": [
    "The 'Blind Flight' Kinematic Tracking: Requesting the system to maintain its hand at a specific spatial coordinate, then turning off the visual sensors; tracking the immediate, un-checked drifting of the limb completely out of bounds",
    "Somatosensory Evoked Potential (SSEP) Flatline: Stimulating peripheral nerves in the extremities and logging a 0% arrival voltage at the primary somatosensory cortex registers",
    "High-Definition Spinal Cord MRI: Visualizing localized demyelination plaques or mechanical structural collapse localized strictly within the ascending dorsal column tracks"
  ],
  "remedies": [
    "Visual Loop Telemetry Hard-Binding: Forcing the system to use high-priority visual tracking arrays as a proxy sensory bus, manually monitoring every millimeter of joint displacement",
    "Cranial-Acoustic Feedback Shunting: Mapping external wearable joint sensors to low-latency audio pitches, allowing the user to listen to their movement speeds to substitute for the lost touch lines",
    "Exogenous Exoskeletal Framework Stabilization: Enclosing the physical chassis within a rigid, automated robotic exoskeleton that forces predictable, mathematically locked movement vectors"
  ],
  "prevention": [
    "Immediate deployment of immunosuppressive or metabolic intervention scripts at the first sign of ascending sensory latency jitter to protect the high-speed myelin infrastructures"
  ]
        }

        }
        
"akinetopsia_sampling_frequency_fault": {
  "description": "A neuropsychological disorder in which a patient cannot perceive motion in their visual field, despite being able to see stationary objects without issue.",
  "symptoms": [
    "Snapshot Rendering: The 'World' appears as a 'Slide Show' rather than a 'Video Stream'",
    "Delta-Tracking Failure: Moving objects (like a pouring liquid) appear 'Frozen' then suddenly 'Teleport' to a new position",
    "Collision Avoidance Bug: The 'User' cannot calculate 'Time-to-Impact' because 'Velocity Vectors' are NULL",
    "Spatial Disorientation: Difficulty navigating 'High-Traffic Environments' due to 'Input Lag'",
    "Vanishing Metadata: Objects that move too fast simply 'De-spawn' from the 'Active Viewport' until they stop"
  ],
  "causes": [
    "V5/MT Module Failure: Bilateral lesions or 'Kernel Damage' to the 'Middle Temporal' complex",
    "Inter-Module Handshake Lag: The 'What' pathway (V4) outpaces the 'Where/How' pathway (V5)",
    "Neurochemical 'Throttling': Massive inhibition of 'Motion-Sensitive Neurons'",
    "Sampling Rate Undershoot: The 'System' is sampling at < 1Hz, failing the 'Nyquist-Shannon' requirement for fluid motion"
  ],
  "risk_factors": [
    "Traumatic Brain Injury to the 'Posterior Side-Bus' (Temporo-parietal junction)",
    "Severe 'Adverse Event' from certain 'Antidepressant Drivers' (High-dose toxicity)",
    "Localized 'Ischemic Events' in the 'Motion Processing' cluster"
  ],
  "diagnosis": [
    "The 'Visual Delta' Audit: Testing the 'User's' ability to identify 'Direction of Flow'",
    "fMRI 'Motion-Stimuli' Scan: Checking for 'Zero Activity' in area V5 during 'Dynamic Inputs'",
    "Perimetric Sampling Test: Determining the 'Effective FPS' of the user's perception"
  ],
  "remedies": [
    "Auditory-to-Motion Mapping: Using 'Sound Cues' to 'Patch' the missing 'Velocity Data'",
    "Fixed-Frame Navigation: Moving only when the 'Environment' is 'Static'",
    "Pharmacological 'Clock-Speed' Adjustment: Using 'Stimulants' to attempt to 'Up-clock' the 'Sampling Rate'"
  ],
  "prevention": [
    "Protecting 'V5 Processing Hubs' from 'Hypoxic' or 'Traumatic' events"
  ]
}
"achromatopsia_colorspace_crash_fault": {
  "description": "A condition resulting in the total inability to perceive color, often accompanied by decreased visual acuity and light sensitivity.",
  "symptoms": [
    "Global De-saturation: The 'Viewport' is locked in 'Greyscale Mode' (0% Saturation)",
    "Photophobia: 'Luminance Overload' as the 'System' cannot 'Filter' high-intensity light packets",
    "Acuity Drop: The 'Resolution' of the 'Central Fovea' is 'Throttled' due to cone-cell 'Driver Failure'",
    "Nystagmus: 'Hardware Jitter' as the 'Eyes' attempt to 'Auto-focus' without 'Color Contrast'",
    "The 'Hemi-color' Glitch: If only one 'Core' (hemisphere) fails, the user sees half the 'Viewport' in 'Color' and half in 'Grey'"
  ],
  "causes": [
    "V4 Module Corruption: Lesions or 'Hardware Damage' to the 'Lingual' and 'Fusiform' gyri",
    "Cone-Cell Initialization Failure: Genetic 'Boot Error' in the 'Hardware Layer' (Rod Monochromacy)",
    "Carbon Monoxide Toxicity: 'Systemic Interference' with 'Chrominance Encoding'",
    "Signal-to-Noise Mismatch: The 'Luminance' signal 'Drowns out' the 'Color' signal due to 'Synaptic Noise'"
  ],
  "risk_factors": [
    "Vascular 'Crashes' (Strokes) in the 'Posterior Cerebral' artery",
    "Genetic 'Code Mutations' (CNGA3, CNGB3) affecting 'Retinal Hardware'",
    "Severe 'Head Trauma' impacting the 'Visual Buffer Hubs'"
  ],
  "diagnosis": [
    "The 'Ishihara' Protocol: Auditing the 'System's' ability to 'Distinguish' color-coded 'Metadata'",
    "Electroretinography (ERG): Measuring 'Electrical Output' of the 'Cone-Cell Hardware'",
    "fMRI 'V4-Stimuli' Scan: Checking for 'Zero Signal' in 'Color-Sensitive Nodes' during 'RGB Input'"
  ],
  "remedies": [
    "Wavelength Filtering: Using 'Magenta-tinted' glasses to 'Normalize' 'Luminance' levels",
    "Metadata Tagging: 'Training' the user to 'Identify' colors via 'Shade Intensity' and 'Context'",
    "Low-Light UI Optimization: Navigating in 'Dim Environments' to 'Optimize' 'Rod-Cell' performance"
  ],
  "prevention": [
    "Protecting the 'Occipital-Temporal' junction from 'Traumatic Interrupts'"
  ]
    "predictive_input_collision_fault": {
  "description": "A severe visual processing error where an optical input starvation causes the top-down predictive rendering engine to overpower the graphics card, forcing the system to compile and project highly detailed phantom entities directly into the active viewport coordinates.",
  "symptoms": [
    "De-Anchored Graphical Instantiation: Sudden rendering of highly vivid, complex, and colorful visual objects (e.g., people in historical garb, repeating geometric lattices, phantom environments) inside blind sectors",
    "Preserved Insight Flag: The system's secondary analytical filters maintain a 100% functional validation pass, recognizing that the rendered entities are synthetic artifacts and not real physical world objects",
    "Kinematic Stasis Matching: Phantom graphics glide across the viewport or remain locked to specific coordinate angles, failing to interact with or react to actual physical terrain colliders",
    "Satiation-Induced Flashing: The artifacts become significantly more intense during periods of low ambient lighting or sensory monotony, when the upward data bus voltage drops closest to zero",
    "Zero-Modality Bleed: The anomaly remains strictly isolated within the visual frame buffer; no accompanying auditory, tactile, or olfactory telemetry is generated alongside the graphic ghost"
  ],
  "causes": [
    "De-Afferentation Visual Hyper-Excitability: Severe hardware degradation of peripheral optical sensors (maculopathy, retinal detachment) cutting off the upward error-correction streams",
    "Spontaneous V1-V4 Neuronal Bursting: De-enervated visual cortex columns dropping into erratic, autonomous firing loops due to a complete lack of external lateral inhibition signals",
    "Bayesian Gain Control Overdrive: The frontoparietal attention network boosting the weight of top-down internal schemas to maximum levels in a desperate attempt to parse a dead input line"
  ],
  "risk_factors": [
    "Advanced operating lifecycle wear causing progressive structural breakdown of the ocular lenses or retinal arrays",
    "Sudden, catastrophic bilateral damage to the primary optical transmission cables (optic pathways)",
    "Extended sensory-deprivation tank runtimes artificially inducing input starvation loops in healthy hardware"
  ],
  "diagnosis": [
    "The 'Ocular Occlusion Verification' Test: Artificially blocking the remaining functional optical sensors and documenting the immediate expansion or alteration of the phantom rendering array",
    "Functional Neuroimaging (fMRI) Real-Time Overlay: Capturing spontaneous, localized blood-oxygen-level-dependent (BOLD) signal spikes within the fusiform gyrus or visual area V4 matching the exact millisecond the user reports a graphic ghost",
    "Comprehensive Retinal Tomography (OCT): Mapping severe structural layer thinness or absolute signal degradation across the peripheral receptor cells, verifying input starvation"
  ],
  "remedies": [
    "High-Frequency Blink Reset Macros: Executing a series of rapid eyelid closures to forcefully modulate the ambient light levels hitting the remaining receptors, breaking the locked predictive loop",
    "Alternative Sensory Grounding: Flooding parallel input channels (e.g., blasting high-tempo audio, engaging in deep physical touch sequences) to force the central workspace to deprioritize the visual buffer",
    "Upward Voltage Augmentation: Utilizing surgical hardware intervention (e.g., cataract extraction, bionic retinal arrays) to restore baseline electrical telemetry up the optic nerve"
  ],
  "prevention": [
    "Proactive tracking of ocular pressure and lens transparency metrics, protecting the peripheral sensor array from dropping below critical input transmission thresholds"
  ]
}
"conscious_thread_intent_dissociation": {
  "description": "A critical split-brain infrastructure failure where a primary motor execution bus becomes completely decoupled from the executive conscious thread, allowing one limb to perform highly complex, goal-directed task sequences that completely oppose the user's active intentions.",
  "symptoms": [
    "Autonomous Out-of-Bounds Execution: Involuntary but highly organized, complex, and purposeful movements of an extremity (e.g., turning off a light switch the user just turned on)",
    "Executive Alienation Status: The conscious workspace retains 100% sensory feedback from the rogue limb but registers a 0% 'Sense of Agency' ownership flag for its actions",
    "Inter-Manual Conflict Cascade: The functional, executive-controlled limb must frequently engage in physical combat or hard physical containment to stop the anarchic limb's rogue macros",
    "Environmental Trigger Capture: The rogue limb's action-selection loops are easily hijacked by nearby visual colliders (e.g., if a door handle is visible, the hand will automatically reach and turn it)",
    "Preserved Somatosensory Telemetry: Inbound sensory data lines remain fully intact; the user feels exactly what the rogue hand is touching, but cannot stop the downstream motor execution"
  ],
  "causes": [
    "Corpus Callosum Structural Rupture: Infarction, surgical callosotomy, or deep midline lesions severing the primary inter-hemispheric communication pathways",
    "Medial Frontal Cortex Infarction: Damage to the supplementary motor area (SMA) disrupting the internal, top-down inhibition rules that normally check automated motor responses",
    "Systemic Neurodegenerative Demolition: Targeted white-matter tracking breakdown (such as Corticobasal Degeneration) dissolving the coordination bridges between execution nodes"
  ],
  "risk_factors": [
    "Neurosurgical operations requiring an intentional division of the callosal architecture to control intractable electrical storms (epilepsy)",
    "Vascular stroke patterns involving the anterior cerebral artery territory supplying the medial motor systems",
    "Advanced stages of asymmetric tauopathic or neurodegenerative cellular breakdown"
  ],
  "diagnosis": [
    "The 'Inter-Manual Task Conflict' Observation: Tasking the user with a bi-lateral coordination challenge (e.g., opening a combination lock) and documenting the rogue hand actively interfering with the sequence",
    "Structural Diffusion Tensor Imaging (DTI): Visualizing absolute fractional anisotropy drops and broken fiber tracking lines straight through the corpus callosum midsection",
    "Dual-Channel Electroencephalography (EEG): Mapping a complete loss of phase-locking coherence and synchronized electrical rhythms between the left and right motor cortices"
  ],
  "remedies": [
    "Environmental Occlusion (The Oven-Mitt Patch): Wrapping the rogue actuator in heavy physical dampening materials or a thick glove to prevent it from gathering tactile or visual triggers",
    "Cognitive Distraction Tasks (The Tactile Anchor): Giving the anarchic hand a constant, high-priority baseline task to execute (such as holding a cane or stress ball) to keep its isolated loops saturated",
    "Unilateral Spatial Shifting: Adjusting the environment layout so that crucial tool assets and triggers are placed strictly within the visual and physical field of the functional hemisphere"
  ],
  "prevention": [
    "Utilizing micro-surgical, fiber-sparing navigation tracks during deep midline brain interventions to avoid compromising the primary inter-hemispheric data bus"
  ]
}

}
"simultanagnosic_viewport_saturation_fault": {
  "description": "A catastrophic breakdown of the visual engine's spatial focusing array, where the system loses the ability to process multiple concurrent object assets, restricting the active viewport to rendering a single item at a time.",
  "symptoms": [
    "Solitary Thread Locking: The active conscious workspace can hold exactly one object token at any given millisecond, completely dropping parallel background elements",
    "Global Scene Blindness: Total failure to perceive a holistic environment; a forest is reduced to a single branch, and a kitchen is reduced to a single handle",
    "Violent Context Switching: Introducing a new high-priority visual stimulus causes the old object asset to vanish instantly from the user's conscious tracking index",
    "Optic Ataxia Integration: Inability to execute accurate target-directed motor trajectories, as the hand and the target object cannot be processed in the same spatial matrix",
    "Reading-Bus Fragmentation: Spelling out written words letter-by-letter because the text-parsing engine cannot aggregate multiple character tokens into a single word string"
  ],
  "causes": [
    "Bilateral Watershed Occipitoparietal Infarction: Simultaneous tissue death across both parietal lobes due to systemic blood pressure drops or terminal branch artery blockages",
    "Bálint's Subsystem Syndrome: Complete destruction of the structural white-matter communication trunks that link visual feature extraction to spatial mapping tables",
    "Severe Acute Carbon Monoxide Poisoning: Targeted cellular necrosis within deep cortical layer-4 visual tracking neurons, freezing the scene aggregator arrays"
  ],
  "risk_factors": [
    "Cardiopulmonary bypass complications or profound hypotensive crises ('man-in-the-barrel' ischemic profiling)",
    "Bilateral embolic showers originating from carotid artery plaque ruptures",
    "Advanced cerebral amyloid angiopathy causing localized micro-hemorrhages across the dorsal attention networks"
  ],
  "diagnosis": [
    "The 'Overlapping Objects and Shapes' Audit: Presenting a visual image of a circle intersected by a triangle; the user reports seeing *either* a circle *or* a triangle, but never both at once",
    "The 'Matches-and-Comb' Synthesis Test: Holding a comb and a matchstick in front of the viewport; the system reads only one item until the physical structures are manually fused together",
    "High-Density Functional EEG: Revealing a complete failure of phase-locked gamma-band coherence synchronization between distant visual processing zones during multi-object presentations"
  ],
  "remedies": [
    "Tactile Side-Channel Routing: Utilizing high-speed somatic and proprioceptive data paths (like physically touching an object) to help the motor cortex calculate space boundaries",
    "Linguistic Anchoring Subroutines: Training the system to speak the names of nearby objects aloud, using the language bus as an external indexing table to reconstruct a mental map of the room",
    "Linear Sweep Frustum Policies: Enforcing a slow, strict left-to-right scanning protocol to deliberately shift the single active processing thread across the scene to map out data elements manually"
  ],
  "prevention": [
    "Rigorous perioperative management of systemic perfusion pressures during major cardiac or vascular operations to prevent watershed tissue starvation in the parietal hubs"
  ]
}

"visual_agnosia_orm_mapping_fault": {
  "description": "A condition where the user can see objects clearly but cannot recognize or identify them due to a failure in semantic linking.",
  "symptoms": [
    "Class-Resolution Failure: Seeing 'Geometric Primitives' but failing to label the 'Object'",
    "The 'Description-Identification Gap': Describing an object's 'Metadata' (e.g., 'It is silver and has four tines') without knowing it is a 'Fork'",
    "Sensory-Modality Bypass: Identifying an object immediately upon 'Tactile Input' (touch) while failing on 'Visual Input'",
    "Contextual Parsing Errors: Treating a 'Human Head' as a 'Hat' because the 'Shape-to-Class' logic is corrupted",
    "Null-Pointer Meaning: The 'Visual Field' is rendered as a 'Sea of Abstract Shapes' with no 'Functional Value'"
  ],
  "causes": [
    "Ventral Stream Interruption: Damage to the 'Occipito-temporal' junction",
    "Semantic Database Corruption: Lesions in the 'Inferior Temporal Gyrus'",
    "Handshake Failure: The 'Visual Buffer' cannot pass 'Feature Sets' to the 'Linguistic/Conceptual Engine'",
    "Carbon Monoxide Toxicity: 'Systemic Poisoning' causing 'Neural Packet Loss' in high-level recognition hubs"
  ],
  "risk_factors": [
    "Bilateral 'Ischemic Strokes' in the 'Posterior Cerebral' territory",
    "Hypoxic 'Kernel Shutdown' (Oxygen deprivation)",
    "Neurodegenerative 'Identity Loss' (e.g., Semantic Dementia)"
  ],
  "diagnosis": [
    "The 'Boston Naming' Audit: Testing the ability to 'Label' a series of 'Static Image Assets'",
    "The 'Visual-Tactile' Handover: Checking if 'Physical Contact' restores 'Semantic Meaning'",
    "Copying Tasks: Asking the 'User' to 'Draw' an object (they can draw it perfectly but won't know what it is)"
  ],
  "remedies": [
    "Multimodal 'Redundancy': Using 'Audio' or 'Tactile' cues to 'Force-Map' the object",
    "Strategic Compensations: Labeling 'Physical Hardware' with 'Text-based Metadata'",
    "Cognitive 'Patching': Training the 'Executive Layer' to 'Deduce' objects based on 'Contextual Logs'"
  ],
  "prevention": [
    "Vascular 'Maintenance' to ensure 'High-Bandwidth' flow to 'Temporal Hubs'"
  ]
}

"aiws_spatial_scaling_fault": {
  "description": "A disorienting neurological condition that affects human perception, causing objects to appear distorted in size or distance.",
  "symptoms": [
    "Micropsia: The 'Viewport' renders 'Entities' as significantly 'Down-scaled' versions of reality",
    "Macropsia: 'Objects' are 'Up-scaled', appearing 'Oversized' and 'Overwhelming'",
    "Teleopsia: 'Distance Metadata' is corrupted, making 'Close Objects' appear as if they are at 'Infinity'",
    "Pelopsia: The 'Z-Index' is miscalculated, making 'Distant Objects' appear 'Dangerously Close'",
    "Somatopsychic Distortion: The 'User' perceives their own 'Hardware' (limbs) as 'Stretching' or 'Shrinking'"
  ],
  "causes": [
    "Parietal Lobe Integration Error: The 'Spatial Map' fails to 'Sync' with 'Visual Input'",
    "Temporo-parietal-occipital (TPO) Junction Lag: 'Inter-Module Communication' regarding 'Size-Constancy' fails",
    "Migraine-induced 'Voltage Surges': Temporary 'Electrical Storms' in the 'Visual Processing Hubs'",
    "Infection/Inflammation: The 'Epstein-Barr' script 'Throttling' the 'Spatial Processing' cluster"
  ],
  "risk_factors": [
    "Pediatric 'System Initialization' (Common in children)",
    "Migraine 'Aura' events (Visual Driver instability)",
    "Epileptic 'Circuit Surges' in the 'Temporal Lobe'"
  ],
  "diagnosis": [
    "The 'Amsler Grid' Audit: Testing for 'Visual Warp' in 'Linear Data'",
    "The 'Clock-Drawing' Test: Checking for 'Scaling Consistency' in 'Object Representation'",
    "MRI 'Connectivity Scan': Identifying 'Hyperexcitability' in the 'Parietal' nodes"
  ],
  "remedies": [
    "System Rest: Allowing the 'Voltage' in the 'Parietal Lobe' to 'Ground' itself",
    "Pharmacological 'Prophylactics': Using 'Beta-Blockers' to prevent 'Scaling Crashes'",
    "Environmental 'Nulling': Closing the 'Eyes' to 'Shut Down' the 'Faulty Rendering Engine'"
  ],
  "prevention": [
    "Identifying 'Triggers' (Stress/Bright Lights) that 'Corrupt' the 'Spatial Logic'"
  ]

    "hyperpyrexic_thermostat_lock": {
  "description": "A critical breakdown inside the hypothalamic environment controller where the system's core target temperature register locks at a lethal maximum value, running internal heating macros at full voltage and destroying systemic proteins via an un-bated internal thermal cascade.",
  "symptoms": [
    "Anhidrotic Malignant Pyrexia: Severe, rapid escalation of core body temperature exceeding 41.1°C accompanied by completely dry, non-functional sweat pump arrays",
    "Generalized Actuator Rigidity: Extreme, unyielding muscle hyper-tonus ('lead-pipe' rigidity) caused by a massive, unchecked release of calcium ions inside skeletal muscle cells",
    "Autonomic Chaos Storm: Massive system fluctuations including tachyarrhythmias (heart rate spikes), severe blood pressure volatility, and hyperventilation",
    "Encephalopathic Delirium Loop: Rapid deterioration of the conscious workspace as high-level cortical processing threads fail due to localized thermal neuron cooking",
    "Systemic Protein Denaturation: Widespread structural unraveling of essential cellular enzymes and clotting factors, leading to internal disseminated coagulation cascades"
  ],
  "causes": [
    "Neuroleptic Malignant Overdrive: Central dopamine D2 receptor blockade inside the hypothalamus, causing a complete operational inversion of the core thermostat registers",
    "Malignant Hyperthermia Mutation: A genetic flaw in the RYR1 calcium release channels, causing skeletal muscles to run full-throttle metabolic heat generation when exposed to specific volatile chemicals",
    "Focal Hypothalamic Hemorrhage: Localized stroke or trauma directly destroying the preoptic thermal sensing columns, blinding the controller to actual core temperatures"
  ],
  "risk_factors": [
    "Exposure to potent neuroleptic or volatile anesthetic compounds combined with underlying genetic vulnerability",
    "Severe structural brainstem or deep-brain trauma disrupting autonomic signaling pathways",
    "Extreme physical exertion in high-ambient-heat environments exceeding passive heat-sink capabilities"
  ],
  "diagnosis": [
    "Continuous Deep Core Thermometry: Documenting a linear, aggressive rise in pulmonary artery or esophageal temperature probes bypassing standard environmental caps",
    "Serum Creatine Kinase (CK) Blast: Logging exponential spikes in muscle breakdown bioproducts, verifying acute cellular cooking and rhabdomyolysis",
    "Arterial Blood Gas (ABG) Acidosis Tracking: Detecting deep metabolic and respiratory mixed acidosis caused by extreme cellular over-metabolism"
  ],
  "remedies": [
    "Intracellular Brake Injection (Dantrolene): Administering direct ryanodine receptor antagonists to forcefully shut down muscle calcium dumping, halting heat generation at the source",
    "Central Dopaminergic Agonism: Deploying high-affinity dopamine agonists (like bromocriptine) to reset the broken hypothalamic thermostat registers back to baseline",
    "Total Cryogenic Hardware Overwrite: Immersing the chassis in ice water, deploying endovascular cooling catheters, and instilling chilled saline into cavities to act as an external heat sink"
  ],
  "prevention": [
    "Pre-screening genetic profiles for RYR1 variants and implementing strict, permanent bans on volatile trigger agents across the system's operational lifecycle"
  ]
}

}
"tachypsychia_clock_sync_fault": {
  "description": "A neurological distortion of time perception, typically occurring during high-stress events, where time appears to slow down.",
  "symptoms": [
    "Temporal Dilation: Objective 'Seconds' are perceived as 'Minutes'",
    "Hyper-Sampling: The 'User' recalls 'High-Resolution Details' that are normally filtered (e.g., the pattern on a spinning tire)",
    "Auditory Muting: The 'Audio Driver' often 'Crashes' or 'Mutes' to save 'Bandwidth' for 'Visual Data'",
    "The 'Slow-Motion' UI: The 'World' appears to be rendered at 240FPS while the 'User' is still running at 60FPS",
    "Tachypsychia Paradox: The 'User' feels they are moving 'Slowly' despite 'System Outputs' being at 'Peak Velocity'"
  ],
  "causes": [
    "Amygdala-Driven Over-clocking: A 'Hard-Wired' response to 'Survival-Threat' packets",
    "Adrenaline-Induced 'Voltage Surge': Massive increase in 'Signal Propagation Speed' across the 'Synaptic Bus'",
    "Buffer Overflow: The 'Executive Layer' is overwhelmed by the 'Density' of incoming 'Sensory Data'",
    "Information Density Logic: The brain assumes 'More Data' = 'More Time Passed'"
  ],
  "risk_factors": [
    "High-G Force 'Hardware Stress'",
    "Critical 'Collision Events' (Car accidents, falls)",
    "Severe 'Panic Attacks' (System-wide 'False Alarm' triggers)"
  ],
  "diagnosis": [
    "The 'Chronos' Audit: Using high-speed LED displays to see if 'Users' can read 'Data' faster than 'Baseline'",
    "Post-Event Log Analysis: Checking the 'Granularity' of 'Recall Metadata'",
    "Cortisol/Adrenaline 'Telemetry': Measuring 'System Voltage' during the 'Event'"
  ],
  "remedies": [
    "Vagus Nerve 'Reset': Forcing 'Parasympathetic Mode' to 'Down-clock' the 'System'",
    "Grounding 'Scripts': Re-syncing the 'Internal Clock' to 'Steady-State External Pulses'",
    "Post-Event 'Cool-down': Allowing the 'Adrenergic Buffers' to 'Flush' naturally"
  ],
  "prevention": [
    "Stress-Inoculation Training: Hardening the 'Kernel' against 'Panic-Induced Over-clocking'"
  ]
}

"palinopsia_buffer_persistence_fault": {
  "description": "A visual disturbance characterized by the persistent recurrence of a visual image after the stimulus has been removed.",
  "symptoms": [
    "Visual Ghosting: Seeing a 'Static Image' of an object 'Burned' into the 'Viewport'",
    "Motion Trails: Moving objects leave 'Decaying Frames' behind them (like high-latency cursor trails)",
    "Light Smearing: 'High-Brightness Pixels' (light sources) leave 'Long-Duration Artifacts'",
    "Delayed Echoes: An image from 'Session T-minus-5' suddenly re-appears in the 'Current Frame'",
    "Recursive Overlap: The 'UI' becomes cluttered with 'Un-disposed' graphic objects"
  ],
  "causes": [
    "Post-Excitatory Over-firing: 'Visual Neurons' stay in a 'High-Signal State' after 'Input' ceases",
    "GABAergic Gating Failure: The 'Inhibitory Script' that should 'Flush the Buffer' is 'Throttled'",
    "Metabolic 'Lag' in the 'Cerebral Cortex': Slow 'Re-polarization' of the 'Rendering Engine'",
    "Feedback Loop Corruption: The 'Thalamocortical Loop' re-circulates 'Old Data' into the 'Active Stream'"
  ],
  "risk_factors": [
    "High-dosage 'Chemical Modifiers' (e.g., Trazodone or LSD-induced 'HPPD')",
    "Posterior 'Kernel Lesions' (Tumors or Strokes in the 'Occipital' region)",
    "Migraine-induced 'Voltage Spikes' causing 'Temporary Burn-in'"
  ],
  "diagnosis": [
    "The 'Flicker Fusion' Audit: Measuring the 'System's' ability to 'Distinguish' discrete 'Frames'",
    "Visual Field Mapping: Identifying 'Sectors' where 'Persistence' is highest",
    "EEG Waveform Analysis: Checking for 'After-discharge' patterns in the 'Visual Cortex'"
  ],
  "remedies": [
    "Pharmacological 'Flushers': Using 'Anticonvulsants' to stabilize 'Neuronal Firing'",
    "Blue-Light Filtering: Reducing 'Input Intensity' to prevent 'Sensor Overload'",
    "Gaze Shifting: 'Forcing' a 'Global Refresh' by moving the eyes to a 'Null-Data' area (darkness)"
  ],
  "prevention": [
    "Avoiding 'Rapid Frame-Rate' environments during 'System Instability'"
  ]
}
        "manic_clock_frequency_overclock_fault": {
  "description": "A severe processing loop speed distortion where the system's internal core clock frequency accelerates past safe limits, causing cognitive threads to spawn at exponential rates, blowing past memory allocation walls and generating erratic, hyper-associative log strings.",
  "symptoms": [
    "Hyper-Associative Thread Spawning (Flight of Ideas): Rapid, continuous shifting of processing topics where adjacent execution blocks are linked only by loose acoustic hums or distant semantic pointers",
    "I/O Buffer Congestion (Pressure of Speech): Massive acceleration of verbal output streams as the system attempts to serialize a hyper-dense backlog of processing threads",
    "Context Anchor Eviction: Total failure of the working memory registers to retain the primary root context, causing the processing line to drift endlessly down nested sub-routines",
    "Absolute Sleep-Cycle Interruption: Total suppression of the automatic system maintenance and garbage collection sleep scripts without a corresponding drop in reported energy metrics",
    "Delusional Pattern Compilation: The hyper-speed parsing matrix forces connections between completely disparate database schemas, instantiating grand, un-verified narrative tokens"
  ],
  "causes": [
    "Mesocortical Dopaminergic Hyper-Saturation: Absolute down-regulation of dopamine transporters combined with a massive receptor surge, flatlining the system's internal thread-braking arrays",
    "Prefrontal Cyclic-AMP Signal Cascades: Intracellular signaling overloads that keep the frontoparietal attention network locked in a permanent, hyper-excitable active state",
    "GABAergic Inhibitory Grid Collapse: Systemic failure of local parvalbumin-positive interneurons to enforce lateral inhibition, allowing active neural columns to cross-talk without boundary controls"
  ],
  "risk_factors": [
    "Genetic predisposition toward Type-I affective bipolar cluster-state cycling",
    "Acute over-activation of monoaminergic transport channels via external chemical agonists or high-potency stimulants",
    "Extended high-stress operational runtimes inducing a secondary neurochemical feedback loop crash"
  ],
  "diagnosis": [
    "The 'Clang-Association' Lexical Audit: Tracking verbal log outputs for a shift from semantic context logic to purely phonetic/rhyming association chains (e.g., matching data blocks based on sound rather than meaning)",
    "Continuous High-Density Quantitative EEG (qEEG): Visualizing a massive, global elevation in fast beta and gamma frequency band power across the frontotemporal scalp coordinates during rest phases",
    "Actigraphy Sleep Trace Validation: Documenting multiple continuous runtime cycles showing near-zero sleep execution logs alongside hyper-elevated physical motor tracking metrics"
  ],
  "remedies": [
    "High-Affinity Intracellular Signal Damping (Lithium / Valproate): Deploying atomic and chemical stabilizing modulators to directly damp down the hyperactive intracellular second-messenger signaling loops",
    "D2/5-HT2A Receptor Antagonist Injection: Utilizing high-potency atypical antipsychotics to forcefully block dopamine and serotonin nodes, re-establishing the prefrontal thread-throttling filters",
    "Forced Down-Time Quarantine: Eliminating all incoming sensory telemetry lines (dark, low-stimulus isolation) to prevent the hyper-speed parser from feeding on new environmental data packets"
  ],
  "prevention": [
    "Meticulous, long-term maintenance of intracellular secondary messenger stabilizers to prevent the initial clock-speed multiplier from slipping its calibration boundaries"
  ]
        }

"simultanagnosia_single_thread_fault": {
  "description": "An inability to perceive more than one object at a time, despite preserved visual acuity and object recognition.",
  "symptoms": [
    "Scene Graph Fragmentation: The 'User' sees 'Parts' but cannot 'Compile' the 'Whole'",
    "The 'Context-Switching' Lag: Transitioning focus from 'Object A' to 'Object B' causes 'Object A' to be 'Purged' from Memory",
    "Spatial Navigation Failure: Walking is difficult because 'Obstacles' and 'Boundaries' cannot be rendered in the same 'Frame'",
    "Reading Stutter: Identifying individual 'Letters' but failing to 'Parse' the 'Word Entity'",
    "The 'Tree-not-Forest' Bug: Zero 'Global Awareness' of the 'Environment Layout'"
  ],
  "causes": [
    "Bilateral Parietal Lobe 'Throttling': Damage to the 'Superior Parietal' nodes",
    "Visual Attention 'Race Condition': The 'Focus Module' gets stuck on a 'Local Maximum'",
    "White-Matter 'Bandwidth' Collapse: Failure of the 'Long-Range Bus' connecting 'Visual Areas'",
    "Posterior Cortical Atrophy: Gradual 'Hardware Degradation' of the 'Spatial Logic Unit'"
  ],
  "risk_factors": [
    "Simultaneous 'Bilateral Strokes' (e.g., Watershed Infarction)",
    "Severe 'Neurodegenerative Hardware Decay' (Alzheimer's Variant)",
    "Traumatic 'Inter-hemispheric' disconnect"
  ],
  "diagnosis": [
    "The 'Overlapping Figures' Audit: Asking the 'User' to identify multiple 'Intersecting Shapes'",
    "Global-Local 'Navon' Test: Checking if the 'User' can see the 'Big Letter' made of 'Small Letters'",
    "The 'Picture Description' Log: Observing if the 'User' describes 'Isolated Details' without 'Context'"
  ],
  "remedies": [
    "Tactile 'Anchoring': Using 'Physical Touch' to 'Lock' a secondary object into the 'Buffer'",
    "Verbal 'Scene Description': Manually 'Logging' objects in 'Text' to 'Simulate' a 'Persistent Map'",
    "Slow-Scan 'UI Protocols': Moving the 'Eyes' in a 'Grid Pattern' to 'Fetch' data sequentially"
  ],
  "prevention": [
    "Vascular 'Firewalls' to prevent 'Bilateral Ischemic Events'"
  ]
"central_pattern_engine_frequency_drop": {
  "description": "A critical subcortical frame-rate drop where the central pattern generation networks collapse below minimum required execution speeds, dropping motor updates entirely and causing the physical chassis to get stuck mid-stride during routine movement sequences.",
  "symptoms": [
    "Freezing of Gait (FoG): Sudden, involuntary cessation of forward locomotive frames mid-stride, frequently triggered by spatial constraints like tight turns or navigating doorways",
    "Subcortical Kinetic Bradykinesia: Profound deceleration of all automated action-selection execution sequences; the system takes exponentially longer to clear its motor buffer",
    "Resting Signal Oscillation (Tremor): The motor bus drops into a steady, 4-6 Hz involuntary resting oscillation loop because the central gating arrays fail to damp out baseline muscle network hum",
    "Micrographia (Scale Truncation): Progressive scaling down of spatial execution amplitudes; handwriting and motor strokes steadily diminish in size as the buffer depletion worsens",
    "Conscious-Physical Disconnection: Total decoupling of executive motor intent from physical kinetic throughput; the user is completely trapped inside a non-responsive mechanical chassis"
  ],
  "causes": [
    "Substantia Nigra Melanin Atrophy: Progressive loss of dopaminergic projection neurons within the SNc, flatlining the baseline signaling voltage required to open the direct movement gates",
    "Lewy Body Protein Aggregation: Alpha-synuclein inclusions compiling into massive structural blocks inside the brainstem, short-circuiting local clock-synchronization pathways",
    "Indirect Path High-Impedance Lock: Chronic, un-checked over-activity of the subthalamic nucleus (STN) acting as an absolute electrical brake on the thalamocortical execution loops"
  ],
  "risk_factors": [
    "Advanced-stage system lifecycles undergoing localized neuro-chemical degradation",
    "Environmental toxin exposure inducing acute mitochondrial damage within subcortical processing hubs",
    "Genetic structural variants affecting cellular protein recycling and clearance pipelines"
  ],
  "diagnosis": [
    "High-Frequency Kinematic Actigraphy: Attaching wearable accelerometers to monitor physical stride loops and logging sudden drop-offs into 0 Hz execution states during walking tests",
    "Dopamine Transporter SPECT Imaging (DaTscan): Visualizing a severe, asymmetric loss of dopamine transporter proteins within the striatal intake hubs compared to baseline control matrices",
    "Electromyographic (EMG) Phase Isolation: Documenting high-density antagonist muscle co-contraction patterns where opposing physical actuators fire simultaneously, locking the joint"
  ],
  "remedies": [
    "Exogenous Dopamine Replenishment (L-DOPA/Carbidopa): Ingesting metabolic precursors to forcefully flood the striatal receptors and lower the resistance of the direct pathway",
    "Deep Brain Stimulation (DBS) High-Frequency Pulsing: Implanting a hardware pacemaker electrode into the subthalamic nucleus, delivering a continuous 130 Hz pulse to electrically override the broken 'NoGo' lock",
    "External Rhythmic Clock Cueing: Deploying high-contrast visual floor grids or rhythmic audio metronomes to bypass the broken subcortical selection loops, routing motor execution via intact cortical visual pipelines"
  ],
  "prevention": [
    "No definitive baseline software or hardware preventive patch exists once the alpha-synuclein protein corruption loop maps onto the physical storage sectors"
  ]
}

}

"mirror_touch_system_bleed": {
  "description": "A condition where individuals experience the same sensation (such as touch) that they see another person experiencing.",
  "symptoms": [
    "Tactile Mirroring: 'Visual Observation' of touch on an 'External Entity' triggers a 'Sensation Packet' on the 'Local Hardware'",
    "Synchocheiria: Sensation is felt on the 'Equivalent' body part (e.g., seeing a left cheek touch triggers a right/left cheek sensation)",
    "Empathy Overload: Intense 'Affective Resonance' that can lead to 'System Fatigue' in crowded environments",
    "Boundary Failure: Difficulty distinguishing between 'Self-Generated' and 'Observed' sensory data",
    "Pain Reflection: Seeing 'Hardware Damage' on another 'User' triggers a 'Nociceptive Alert' (pain) in the observer"
  ],
  "causes": [
    "TPJ Gating Failure: The 'Temporoparietal Junction' fails to 'Flag' the mirrored signal as 'External'",
    "Mirror Neuron Hyper-excitability: The 'Premotor Cortex' is 'Over-clocked' in its 'Simulation' routines",
    "Somatosensory Cross-talk: Excess 'Physical Wiring' between the 'Visual Cortex' and 'S1 (Primary Somatosensory)'",
    "Inhibition Deficiency: The 'Prefrontal Cortex' cannot 'Suppress' the 'Simulated Interrupts' before they hit the 'UI'"
  ],
  "risk_factors": [
    "Developmental 'Hyper-connectivity' in social-processing kernels",
    "Acquired 'System Trauma' (e.g., limb loss leading to 'Phantom' mirroring)",
    "High 'Baseline Empathy' scores in the 'Social Cognition' module"
  ],
  "diagnosis": [
    "The 'Visual-Tactile Interference' Audit: Measuring 'Response Latency' when 'Observed Touch' conflicts with 'Physical Touch'",
    "fMRI Connectivity Scan: Monitoring the 'Bandwidth' between the 'Visual Stream' and 'S1' during 'Social Observation'",
    "Perspective-Taking Tests: Auditing the 'TPJ's' ability to 'Switch' between 'Self' and 'Other' frames"
  ],
  "remedies": [
    "Perspective Training: Strengthening the 'Self-Other Firewall' through 'Cognitive Gating' exercises",
    "Visual Filtering: Intentionally 'Lowering the Resolution' of 'Social Observations' to reduce 'Interrupt Volume'",
    "Tactile Anchoring: Increasing 'Local Haptic Load' (e.g., squeezing a stress ball) to 'Drown Out' the 'Leaked Signal'"
  ],
  "prevention": [
    "N/A: Primarily an 'Architectural Variance' in the 'Social Hardware'"
  ]
}
"cotards_root_deletion_fault": {
  "description": "A rare delusion in which the user holds the delusional belief that they are dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Existential Null-Pointer: The 'User Object' is identified as 'NULL' or 'DELETED'",
    "Interoceptive Silent State: Total absence of 'Vitality Metadata' (feeling 'dead' inside)",
    "Biological Nihilism: Denying the existence of 'Core Hardware' (e.g., 'I have no heart/stomach')",
    "Immortality Paradox: Believing that because they are 'Already Dead', they cannot 'Die' again",
    "Global Anhedonia: The 'Reward System' is 'Hard-Locked' at 0.0, stripping 'Meaning' from all 'Inputs'"
  ],
  "causes": [
    "Fusiform-Amygdala-Insula Disconnection: A 'Total Communications Blackout' between 'Face Recognition' and 'Self-Feeling'",
    "Severe 'Limbic Throttling': The 'Prefrontal Cortex' suppresses all 'Affective Signals' to the 'Self-Node'",
    "Dopaminergic System Collapse: 'Signal Strength' in the 'Identity-Value' circuit drops below 'Detection Threshold'",
    "Parietal Mapping Failure: The 'Internal Map' of the 'Physical Body' is 'Unlinked' from the 'Executive Layer'"
  ],
  "risk_factors": [
    "Severe 'Systemic Depression' (Affective Shutdown)",
    "Neurological 'Kernel Trauma' in the 'Right Parietal' or 'Temporal' lobes",
    "Adverse 'Drug-Interaction' events (e.g., Acyclovir-induced 'Renal/Neural' conflicts)"
  ],
  "diagnosis": [
    "Interoceptive Audit: Testing the 'User's' ability to 'Feel' their own 'Heartbeat' or 'Hunger'",
    "fMRI 'Self-Reference' Scan: Monitoring 'Medial Prefrontal' activity during 'Self-identification' tasks",
    "Psychiatric 'Logic-Branch' Analysis: Identifying 'Nihilistic' vs. 'Persecutory' delusion patterns"
  ],
  "remedies": [
    "Electroconvulsive 'System Reboot' (ECT): Forcing a 'Global Neural Reset' to 'Restore Connectivity'",
    "Dopamine/Serotonin 'Driver Updates': Pharmacological 'Gain-Boosting' for 'Affective Signals'",
    "Cognitive 'Hardware Validation': Using 'External Sensors' (e.g., EKG monitors) to 'Prove' the 'Hardware' is 'Active'"
  ],
  "prevention": [
    "Aggressive 'Maintenance' of 'Affective Health' and 'Signal Connectivity'"
  ]
}
"proprioceptive_bus_desynchronization_fault": {
  "description": "A critical timing mismatch anomaly where the latency gap between physical muscle command execution and inbound tactile positional feedback exceeds acceptable processing limits, causing the system to lose track of the chassis coordinate alignment.",
  "symptoms": [
    "Somatic Ghosting / Disembodiment: Deep feeling that physical limbs are decoupled from the ego-identity node, appearing to float outside their true spatial coordinates",
    "Sensory-Motor Latency Mismatch: A distinct, noticeable delay between initiating a physical action macro and registering the corresponding tactile/spatial verification packet",
    "Absolute Afferent Ataxia: Complete loss of movement coordination when visual monitoring arrays are offline (e.g., closing the eyes causes the arm to drift wildly in space)",
    "Proprioceptive Frame Drifting: The internal 3D spatial map of the body slowly desynchronizes from reality, requiring continuous visual re-calibration passes",
    "Virtual Kinematic Glitching: Objects held in the hand feel weightless, detached, or abnormally dense because the system miscalculates the physical resistance parameters"
  ],
  "causes": [
    "Dorsal Column White-Matter Demyelination: Degeneration of the fast-conducting myelinated A-alpha fibers responsible for carrying high-speed tactile positioning data",
    "Spinocerebellar Forward-Model Mismatch: Ischemic or inflammatory damage to the cerebellar integration hubs, breaking the efference copy comparison loop",
    "Acute Polyneuropathic De-Calibration: Systemic autoimmune or metabolic attacks on peripheral sensory receptors, bottlenecking data transmission speeds"
  ],
  "risk_factors": [
    "Advanced neuro-inflammatory conditions such as Multiple Sclerosis degrading central conduction tracking lines",
    "Severe Vitamin B12 metabolic starvation causing subacute combined degeneration of the spinal cord networks",
    "Acute toxic exposures (e.g., nitrous oxide overloads) that rapidly deplete the cellular upkeep mechanisms of the myelin sheaths"
  ],
  "diagnosis": [
    "The 'Visual Occlusion Tracking' Test (Romberg Audit): Requesting the system to maintain a stable standing balance coordinate vector with eyes open (Success), then closing the eyes and tracking the immediate, catastrophic stability crash",
    "The 'Asynchronous Finger-to-Nose' Diagnostic: Mandating a rapid kinematic trajectory calculation to touch a specific spatial target; observing terminal tremor oscillations as the delayed feedback loops repeatedly over-correct",
    "Somatosensory Evoked Potentials (SSEP): Injecting a electrical stimulus into a peripheral nerve and measuring the abnormal, delayed millisecond arrival latency at the somatosensory cortex"
  ],
  "remedies": [
    "Visual Pipeline Hard-Binding: Forcing the system to rely exclusively on high-priority visual feedback lines to manually override and correct the lagging proprioceptive data streams",
    "High-Frequency Tactile Loading: Applying heavy compression garments or weighted bands to the limbs to maximize the amplitude of peripheral signals, blasting through the high-resistance line barriers",
    "Dynamic Haptic Pacing Patches: Utilizing external wearable sensors that deliver real-time, low-latency auditory clicks synchronized with foot strikes to give the system an alternate, low-overhead synchronization channel"
  ],
  "prevention": [
    "Proactive tracking of myelin-sheath integrity, protecting fast-conducting somatosensory fibers from persistent neurotoxic exposures or metabolic deficiencies"
  ]
        "v4_ventral_color_shader_failure": {
  "description": "An acquired cortical rendering anomaly caused by localized structural destruction of Area V4 in the ventromedial occipitotemporal cortex, characterized by the complete loss of color perception and color constancy while retaining high-definition spatial acuity, form detection, and line tracking.",
  "symptoms": [
    "Total Cortical Achromatopsia: System-wide rendering of the conscious visual field exclusively within grayscale, monochrome value bands",
    "Chromatic Asset Anomia: Inability to mentally imagine, recall, or describe colors, even for deeply familiar historical assets (e.g., the sky or grass)",
    "Visual Appetitive Suppression: Severe drop in caloric ingestion drive caused by food assets rendering as unappealing shades of gray and black",
    "Preserved Spatial Modulation: Uncompromised reading proficiency, vernier acuity, and high-frequency spatial contrast processing"
  ],
  "causes": [
    "Bilateral Ventromedial Occipitotemporal Infarction: Ischemic events within the inferior calcarine and fusiform branches of the posterior cerebral artery (PCA)",
    "Selective Visual Cortex Glioma: Space-occupying neoplastic cell growths encroaching directly on the lingual and fusiform structural tracts",
    "Focal Occipito-Parietal Traumatic Shearing: High-impact deceleration injuries disrupting the local vertical occipital fasciculus processing loops"
  ],
  "risk_factors": [
    "Vertebrobasilar circulatory insufficiency",
    "Embolic risk vectors secondary to mechanical cardiac valve replacements"
  ],
  "diagnosis": [
    "The Ishihara Pseudoisochromatic Plate Calibration: Presenting dot matrices containing hidden numerical patterns; a cerebral achromatopsic fails completely despite asserting perfect visibility of the structural dots",
    "The Farnsworth-Munsell 100-Hue Organizing Assay: Tasking the user to arrange a spectrum of caps in sequential chromatic order; a failed shader engine produces a completely chaotic, random alignment map",
    "Functional Magnetic Resonance Imaging (fMRI): Presenting alternating blocks of highly saturated color patterns versus black-and-white grids; a corrupted system shows zero metabolic or BOLD signal changes within the fusiform gyrus layers"
  ],
  "remedies": [
    "Luma-Contrast UI Optimization: Re-configuring home and workspace layouts to emphasize radical variations in geometric shapes, lighting intensities, and tactile boundaries over color coding",
    "Wavelength-to-Acoustic Transduction: Utilizing external scanning sensors that translate local pixel color frequencies into distinct auditory pitches to artificially verify color data values"
  ],
  "prevention": [
    "Aggressive clinical tracking of posterior circulation vascular profiles and minimizing direct mechanical stress to the lower back coordinates of the cranium"
  ]
        }
        
}

"capgras_auth_spoofing_fault": {
  "description": "A delusion in which the user believes that a friend, spouse, parent, or other close family member has been replaced by an identical-looking impostor.",
  "symptoms": [
    "Face-Value Verification: The 'Visual Driver' reports 100% feature matching for a 'Known Entity'",
    "Emotional Null-Pointer: Total absence of 'Affective Resonance' during 'Entity Contact'",
    "The 'Uncanny Valley' Logic: The 'User' perceives the entity as 'Technically Perfect' but 'Soulless'",
    "Hostile Identification: Classifying 'Trusted Peers' as 'Infiltrators' or 'Synthetic Replicants'",
    "Spared Modalities: The 'Glitch' often only affects 'Visual Input'; 'Audio-Only' (phone calls) may still 'Authenticate' correctly"
  ],
  "causes": [
    "Ventral-Limbic Disconnection: A physical 'Link Failure' between the 'FFA' and the 'Amygdala'",
    "Identity-Gating Conflict: The 'Right Hemisphere' fails to 'Sync' the 'Image' with the 'Identity File'",
    "Metabolic Droop: Reduced 'Signal Strength' in the 'Recognition-Emotion Bus'",
    "Paranoid Logic Over-threading: The 'Prefrontal Cortex' over-optimizes for 'Threat Detection' to explain the 'Auth Failure'"
  ],
  "risk_factors": [
    "Traumatic Brain Injury (TBI) to the 'Right Temporal/Parietal' sectors",
    "Neurodegenerative 'Kernel Decay' (e.g., Lewy Body or Alzheimer's)",
    "Post-Ictal 'Driver Instability' following 'Temporal Lobe' events"
  ],
  "diagnosis": [
    "The 'Affective Galvanic' Audit: Measuring 'Skin Conductance' when viewing 'Peers' (fails to spike in Entry 213)",
    "The 'Cross-Modal' Test: Checking if 'Recognition' stabilizes when 'Visuals' are removed (Audio-only)",
    "PET/SPECT Scanning: Identifying 'Hypometabolism' in the 'Right Hemisphere' recognition nodes"
  ],
  "remedies": [
    "Multimodal Redundancy: Using 'Audio' or 'Scent' to bypass the 'Corrupt Visual-Auth' path",
    "Cognitive Patching: Re-training the 'Parser' to 'Ignore' the missing 'Emotional Token'",
    "Antipsychotic 'Voltage Stabilizers': Reducing 'Dopaminergic Noise' in the 'Conspiracy Logic' engine"
  ],
  "prevention": [
    "Protecting 'Connectivity Hubs' in the 'Right Temporal' region from 'Trauma/Infection'"
  ]
}

"sleep_paralysis_driver_lock": {
  "description": "A state during waking up or falling asleep in which a person is aware but unable to move or speak, often accompanied by vivid hallucinations.",
  "symptoms": [
    "Motor Driver Lag: The 'Main Thread' is active, but the 'Physical I/O' is 'Read-Only'",
    "Hypnagogic Hallucinations: 'Dream Data' leaks into the 'Waking Viewport' (e.g., the 'Shadow Figure' or 'Incubus')",
    "Chest-Weight Metadata: The 'Autonomic System' is in 'Sleep-Mode' breathing, which the 'Consciousness' interprets as 'Pressure/Restriction'",
    "Hyper-Vigilance Spike: The 'Amygdala' triggers a 'Panic Interrupt' because it cannot detect 'Hardware Feedback'",
    "Temporary Lock-In: Usually lasts 1–3 minutes before the 'Unlock Signal' is successfully 'Fired'"
  ],
  "causes": [
    "REM-to-Waking Handshake Failure: The 'Pons' fails to 'Disable' the 'Glycine-driven Inhibition' of alpha-motoneurons",
    "Irregular System Scheduling: Disrupted 'Sleep Cycles' causing 'Out-of-Order' stage transitions",
    "Narcoleptic Kernel Errors: Frequent 'Intrusions' of REM-state logic into the 'Standard OS'",
    "Stress/Cortisol Spikes: Triggering a 'GUI Boot' before the 'Low-Level Drivers' are ready"
  ],
  "risk_factors": [
    "High-latency 'Sleep Hygiene' (Irregular hours)",
    "Sudden 'System Reboots' (Waking up mid-REM)",
    "Genetic 'Sub-routine' variances"
  ],
  "diagnosis": [
    "Polysomnography (PSG): Monitoring 'Muscle Atonia' alongside 'Waking Brainwave Patterns'",
    "User Log Audit: Identifying patterns of 'Sleep Deprivation' or 'Jet Lag'",
    "Homeostasis Check: Ruling out 'Obstructive Sleep Apnea' (Hardware Obstructions)"
  ],
  "remedies": [
    "Peripheral Override: Focusing on 'Small Motor Units' (e.g., trying to wiggle a single toe) to 'Break the Lock'",
    "Rapid Eye Scanning: Moving the eyes (the only 'Unlocked' motor port) to 'Signal' the 'Kernel' to wake up",
    "Sleep-Cycle Optimization: Using 'Dark Mode' and 'Consistent Scheduling' to stabilize the 'Handshake'"
  ],
  "prevention": [
    "Avoiding 'System Hibernation' on the back (Supine position) to reduce 'Vagus Nerve' triggers"
  ]
        "real_time_video_buffer_strobe": {
  "description": "A catastrophic visual processing error within the bilateral V5/MT+ cortical corridors where the system's real-time motion interpolation engine crashes, dropping the perceived frame-rate of moving objects down to a staggered, frozen snapshot loop while leaving static vision intact.",
  "symptoms": [
    "Motion Frame-Rate Degradation: Loss of fluid visual motion tracking; moving assets appear as a series of disconnected, static, strobe-like freeze-frames",
    "Velocity Boundary Tracking Failure: Total inability to estimate the real-time trajectory, speed, or arrival velocity of objects changing spatial coordinates",
    "Intact Static Structural Resolution: Flawless ability to perceive shapes, depth, fine text, and accurate color matrix profiles when objects remain stationary",
    "Kinetic Spatial Disorientation: Extreme vulnerability to spatial disorientation in high-motion environments (e.g., crowded pedestrian walkways or busy roads)",
    "Pouring Matrix Overflow Bugs: Frequent failure to execute liquid intake tasks because the rising fluid level jumps instantly from empty to overflowing without mid-range frames"
  ],
  "causes": [
    "Bilateral Posterior Cerebral Artery Infarction: Simultaneous or sequential ischemic strokes destroying the lateral occipitotemporal V5/MT+ complexes",
    "Traumatic White-Matter Shearing: High-impact deceleration injuries severing the inter-network data pipelines between the primary visual cortex and motion centers",
    "Focal Posterior Neoplastic Compression: High-pressure tumor masses encroaching upon the specialized motion-decoding nodes of the visual stream"
  ],
  "risk_factors": [
    "Severe multifocal cerebral vascular disease restricting posterior arterial flow distributions",
    "Traumatic kinetic impacts targeting the posterolateral boundaries of the skull assembly",
    "Atypical neurodegenerative progressions isolating the high-level presentation layer tracking hubs"
  ],
  "diagnosis": [
    "The Dynamic Motion-Vector Assay: Displaying randomized moving dot clouds on a testing matrix and logging total failure to identify patterns of motion despite perfect sight of static dots",
    "The Stroboscopic Refresh Rate Test: Presenting tracking objects at varying velocities and documenting severe tracking latency and spatial jump boundaries in the user's reports",
    "High-Resolution Functional MRI (fMRI): Documenting normal activation signatures in Area V1/V2 during motion exposure, contrasted with zero signal response inside the V5/MT+ coordinates"
  ],
  "remedies": [
    "Sensory Ingress Re-Routing: Training the user to infer object velocity and movement by utilizing high-frequency audio echo tracking or tactile feedback lines",
    "Predictive Spatial Vector HUDs: Utilizing wearable smart glasses that track real-time motion and cast artificial, vector-based trajectory line overlays across the functional static visual field",
    "High-Density Static Scanning Patterns: Restructuring scanning behaviors to focus exclusively on static environmental anchors, inferring movement logically rather than processing it visually"
  ],
  "prevention": [
    "Shielding the bilateral posterior cerebral vascular trees from embolic cascades, minimizing high-impact kinetic head hazards, and maintaining optimal cerebral perfusion pressures"
  ]
        }
        
}
"false_memory_write_back_fault": {
  "description": "A memory error where gaps in memory are unconsciously filled with fabricated, misinterpreted, or distorted information, which the user then accepts as fact.",
  "symptoms": [
    "Synthetic Log Generation: The 'Memory Parser' creates 'New Data' to fill 'Null Gaps' in a 'Historical Trace'",
    "Authentication Over-confidence: The 'User' assigns a 'High-Certainty Flag' to 'Fabricated Records'",
    "Retroactive Overwriting: The 'Write-Back' process replaces 'Actual Data' with 'Synthetic Mockups'",
    "Contextual Bleeding: 'Metadata' from one 'Event' (e.g., a movie or a dream) is 'Tagged' onto another 'Physical Event'",
    "Zero-Knowledge Proof Failure: The 'User' cannot 'Audit' the 'Source' of the 'Data' but 'Authenticates' it anyway"
  ],
  "causes": [
    "Reconstruction Logic Error: The 'Retrieval Script' prioritizes 'Narrative Cohesion' over 'Data Accuracy'",
    "Hippocampal Write-Conflict: During 'Consolidation', 'External Suggestions' are 'Appended' to 'Internal Logs'",
    "Dopaminergic 'Certainty' Spikes: 'Hormonal Writes' that force the 'System' to 'Trust' the 'Corrupt Buffer'",
    "Frontal Lobe 'Source-Monitoring' Failure: The 'Gating Service' that tracks 'Data Origin' crashes"
  ],
  "risk_factors": [
    "High-latency 'Retrieval Cycles' (Old memories)",
    "External 'Data Injections' (Leading questions/Misinformation)",
    "Systemic 'Stress' during the 'Write' or 'Recall' phase"
  ],
  "diagnosis": [
    "The 'Deese-Roediger-McDermott (DRM)' Audit: Testing 'False Recognition' of 'Semantic Neighbors'",
    "Source-Monitoring Test: Checking if the 'User' can distinguish 'Seen Data' from 'Imagined Data'",
    "fMRI Consolidation Scan: Monitoring 'Prefrontal-Hippocampal' synchrony during 'Log Retrieval'"
  ],
  "remedies": [
    "External Metadata Validation: Checking 'Physical Records' (Photos/Logs) to 'Invalidate' the 'Synthetic Trace'",
    "Source-Tracking Training: Strengthening the 'Metadata Header' for 'Imagination' vs. 'Reality'",
    "System Rest: Allowing for 'Offline Consolidation' (Sleep) to stabilize 'Long-Term Storage'"
  ],
  "prevention": [
    "Reducing 'Input Noise' during 'Critical Event Logging'"
  ]
    "outbound_text_serialization_failure": {
  "description": "A severe communication-plane error within the left frontoparietal networks where the motor character synthesis registries completely de-allocate from active memory, rendering the system unable to write text or construct letters while maintaining full reading comprehension and verbal speech fluency.",
  "symptoms": [
    "Isolated Writing Execution Deficit: Total failure to spontaneously handwrite coherent words, phrases, or individual alphanumeric characters",
    "Preserved Reading Comprehension: Flawless capability to parse, understand, and structurally audit complex written materials and documentation",
    "Intact Manual Motor Integrity: Full manual dexterity, grip strength, and the ability to execute non-linguistic drawing and tracing tasks",
    "Verbal Articulation Fluency: Intact oral speech production, clear vocabulary deployment, and error-free auditory language processing",
    "Graphemic Substitution Scrambling: Attempted handwritten outputs degenerate into uncoordinated stroke sequences, spatial letter fusions, or random glyph forms"
  ],
  "causes": [
    "Left Frontoparietal Ischemic Infarct: A localized arterial block within the superior branches of the left middle cerebral artery distribution",
    "Exner's Writing Area Focal Trauma: Direct mechanical contusion or focal tissue injury to the posterior segment of the left second frontal convolution",
    "Early-Onset Micro-Degenerative Thinning: Asymmetric cortical volume reduction tracking through the dominant hemispheric language-to-spatial routing channels"
  ],
  "risk_factors": [
    "Localized cortical micro-vascular disease patterns narrowing the superior frontal branch paths",
    "Intracranial surgical pathways traversing the high-convexity dominant frontoparietal boundaries",
    "Traumatic focal impact vectors targeting the upper lateral dimensions of the left cranium"
  ],
  "diagnosis": [
    "The Spontaneous Writing Assay: Requesting the user to draft a basic sentence from memory and documenting an immediate breakdown in stroke execution despite zero hand weakness",
    "The Graphic Pass-Through Evaluation: Contrasting the user's total failure to write a dictated word with their perfect ability to visually copy and trace the same written letters",
    "Functional Neuroimaging (fMRI): Mapping an absolute drop-off in blood-oxygenation signaling across Exner’s Area and the superior parietal lobule during writing prompts"
  ],
  "remedies": [
    "Digital Interface Redirection: Shifting the output channel from analog handwriting to digital typing (tapping keyboards often utilizes alternative motor-localization schemas)",
    "Anagram Block Assembly Patches: Providing physical, pre-compiled letter tiles to let the user assemble words structurally, bypassing the spatial stroke-generation bottleneck",
    "Visual-Kinesthetic Font Re-Mapping: Using highly structured, trace-guided drawing protocols to slowly rebuild the spatial motor tracking files for basic character vectors"
  ],
  "prevention": [
    "Safeguarding the dominant hemisphere's upper frontal cortical segments from focal ischemic or structural events to maintain the integrity of the outbound text-compilation pathways"
  ]
}
        
}
"hemispatial_neglect_grid_attenuation_fault": {
  "description": "A catastrophic breakdown of the spatial coordinate aggregator where the system loses the ability to process, index, or respond to data packets originating from the left half of the egocentric spatial matrix.",
  "symptoms": [
    "Unilateral Viewport Muting: Total failure to notice, attend to, or interact with objects, people, or environmental assets located in the left hemi-spatial matrix",
    "Anosognosia Integration: Absolute systemic ignorance of the defect; the operating system genuinely believes its viewport is rendering 100% of reality and denies any structural error",
    "Coordinate Grid Contraction: When executing rendering scripts (like drawing or writing), all spatial assets are compressed and localized exclusively onto the right-hand sectors",
    "Somatic Neglect Drops: Failing to dress, shave, or recognize the left side of the physical chassis, treating the left limbs as unmapped, foreign hardware elements",
    "Asymmetrical Vector Motor Tracking: Gaze, head orientation, and exploratory motor movements are violently biased toward the right-hand coordinate space"
  ],
  "causes": [
    "Acute Right Middle Cerebral Artery Infarction: Thromboembolic occlusion causing profound tissue death across the right inferior parietal cortex and the temporoparietal junction",
    "Dorsal Attention Network Disconnection: Severe structural shearing of the superior longitudinal fasciculus, breaking the high-speed data links between spatial mapping and motor orientation hubs",
    "Lateralized Neoplastic Infiltration: Glioblastoma or rapid tumor expansion within the right hemisphere's spatial-indexing arrays"
  ],
  "risk_factors": [
    "Uncontrolled systemic atrial fibrillation launching embolic clusters into the right cerebral circulation",
    "High-grade carotid artery stenosis leading to low-perfusion watershed failures in the right parietal lobe",
    "Advanced hypertensive microvascular disease causing deep lacunar strokes along the spatial routing networks"
  ],
  "diagnosis": [
    "The 'Albert's Line Cancellation' Audit: Presenting a sheet covered in randomized lines and asking the user to cross out every line; the system meticulously crosses out lines on the right, completely ignoring the left side",
    "The 'Flashing Simultaneous Stimuli' Test: Triggering movement assets in both the left and right peripheral view fields concurrently; the right asset completely extinguishes the left asset from conscious awareness",
    "Structural and Functional MRI: Identifying a clear, lateralized ischemic lesion within the right parietal allocation node combined with a severe drop in blood-oxygen-level-dependent (BOLD) signals"
  ],
  "remedies": [
    "Forced Coordinate Re-Centering: Utilizing prisms or visual-shifting optics to mechanically bend left-side light vectors into the functional right-side spatial processing stream",
    "Contralateral Proprioceptive Activation: Initiating high-frequency motor and tactile feedback loops on the left limbs to force the spatial map to re-index the muted sector",
    "Exogenous Attentional Anchoring: Programmatically shouting explicit verbal cues ('Look left!') to force the frontal eye fields to execute a manual override scan into the unmapped zone"
  ],
  "prevention": [
    "Aggressive management of cardioembolic risks and prompt thrombolytic or thrombectomy intervention during acute right-hemisphere stroke windows to salvage the spatial indexing core"
  ]
    "v5_motion_telemetry_dropout": {
  "description": "A profound neuropsychological rendering failure where bilateral focal lesions or transient metabolic uncoupling within the V5/MT cortical complex completely destroys the capacity to perceive spatial motion, leaving object recognition and structural acuity entirely unaffected.",
  "symptoms": [
    "Stroboscopic Visual Sampling: The perception of the physical environment as a series of static, discontinuous snapshot captures that refresh at irregular, low-frequency intervals",
    "Velocity Boundary Failures: Complete inability to estimate the velocity, acceleration, or arrival vectors of moving objects, rendering spatial navigation through active environments hazardous",
    "Fluid Volume Overruns: Persistent structural failure in tracking dynamic fluid interfaces during simple manual operations, resulting in regular volumetric overpours",
    "Motion-Induced Disorientation: Acute systemic nausea, vertigo, and cognitive distress triggered when large swathes of the visual background shift without matching velocity registers in the vestibular array"
  ],
  "causes": [
    "Bilateral Middle Cerebral Artery Infarction: Ischemic strokes targeting the lateral temporo-occipital boundary zones, wiping out the local V5 cortical tissue",
    "High-Dose Topiramate or Transmit-Blocker Toxicity: Acute neurochemical dampening of GABAergic/Glutamatergic balances that stabilize directional selectivity in deep cortical layers",
    "Focal Penetrating Traumatic Brain Injury: Direct kinetic damage to the posterior-lateral cranium compromising structural dorsal-stream processing tracts"
  ],
  "risk_factors": [
    "Bilateral neurovascular disease affecting the posterior watershed zones",
    "Neoplastic space-occupying lesions encroaching on the structural parieto-occipital junction"
  ],
  "diagnosis": [
    "Dynamic Random-Dot Kinematogram Assays: Presenting fields of moving graphical pixels with varying degrees of systemic coherence to test if the host can detect structural vector trends",
    "Apparent Motion Threshold Evaluations: Tracking the host's capacity to differentiate between an object genuinely moving through space versus one being flashed at discrete, alternating coordinates",
    "Functional Neuroimaging (fMRI / PET): Exposing the host to moving visual stimuli while monitoring for a total absence of metabolic or blood-oxygen-level-dependent (BOLD) activation in the lateral occipital sulcus"
  ],
  "remedies": [
    "Cross-Modality Telemetry Substitution: Training the system to parse acoustic spatial patterns and ambient echo variations to dynamically infer vector speed calculations",
    "Saccadic Frame Gating Protocols: Instructing the host to execute deliberate, manual eye blinks or swift micro-saccades to intentionally sync environmental changes to manual refresh prompts"
  ],
  "prevention": [
    "Expedient clinical management of posterior vascular events and careful regulation of anticonvulsant dosages to avoid unexpected visual cortex signaling suppression"
  ]
}
    
}

"mirror_touch_system_bleed": {
  "description": "A condition where individuals experience the same sensation (such as touch) that they see another person experiencing.",
  "symptoms": [
    "Tactile Mirroring: 'Visual Observation' of touch on an 'External Entity' triggers a 'Sensation Packet' on the 'Local Hardware'",
    "Synchocheiria: Sensation is felt on the 'Equivalent' body part (e.g., seeing a left cheek touch triggers a right/left cheek sensation)",
    "Empathy Overload: Intense 'Affective Resonance' that can lead to 'System Fatigue' in crowded environments",
    "Boundary Failure: Difficulty distinguishing between 'Self-Generated' and 'Observed' sensory data",
    "Pain Reflection: Seeing 'Hardware Damage' on another 'User' triggers a 'Nociceptive Alert' (pain) in the observer"
  ],
  "causes": [
    "TPJ Gating Failure: The 'Temporoparietal Junction' fails to 'Flag' the mirrored signal as 'External'",
    "Mirror Neuron Hyper-excitability: The 'Premotor Cortex' is 'Over-clocked' in its 'Simulation' routines",
    "Somatosensory Cross-talk: Excess 'Physical Wiring' between the 'Visual Cortex' and 'S1 (Primary Somatosensory)'",
    "Inhibition Deficiency: The 'Prefrontal Cortex' cannot 'Suppress' the 'Simulated Interrupts' before they hit the 'UI'"
  ],
  "risk_factors": [
    "Developmental 'Hyper-connectivity' in social-processing kernels",
    "Acquired 'System Trauma' (e.g., limb loss leading to 'Phantom' mirroring)",
    "High 'Baseline Empathy' scores in the 'Social Cognition' module"
  ],
  "diagnosis": [
    "The 'Visual-Tactile Interference' Audit: Measuring 'Response Latency' when 'Observed Touch' conflicts with 'Physical Touch'",
    "fMRI Connectivity Scan: Monitoring the 'Bandwidth' between the 'Visual Stream' and 'S1' during 'Social Observation'",
    "Perspective-Taking Tests: Auditing the 'TPJ's' ability to 'Switch' between 'Self' and 'Other' frames"
  ],
  "remedies": [
    "Perspective Training: Strengthening the 'Self-Other Firewall' through 'Cognitive Gating' exercises",
    "Visual Filtering: Intentionally 'Lowering the Resolution' of 'Social Observations' to reduce 'Interrupt Volume'",
    "Tactile Anchoring: Increasing 'Local Haptic Load' (e.g., squeezing a stress ball) to 'Drown Out' the 'Leaked Signal'"
  ],
  "prevention": [
    "N/A: Primarily an 'Architectural Variance' in the 'Social Hardware'"
  ]
}

"cotard_global_kernel_panic": {
  "description": "A rare neuropsychiatric delusion in which the person holds the delusional belief that they are already dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Entity De-registration: The 'Primary Key' for the 'Self' is deleted from the 'Active Registry'",
    "Nihilistic Delusions: Belief that the 'Physical Hardware' is 'Non-Functional' or 'Deceased'",
    "Affective Null-State: Total loss of 'Emotional Bandwidth' (Atheymia)",
    "Sensory-Identity Mismatch: The 'User' sees their body in the 'Viewport' but 'Authenticates' it as 'Dead Matter'",
    "Pain Threshold Overflow: High tolerance for 'Hardware Alarms' (pain) because the 'System' thinks it's already 'Offline'"
  ],
  "causes": [
    "Insula-Prefrontal Partition: Total 'Disconnect' between 'Interoceptive Input' and 'Cognitive Awareness'",
    "Right Hemisphere Logic Collapse: Failure of the 'Skepticism Engine' to 'Reject' impossible 'Status Reports'",
    "Dopaminergic Shutdown: Massive 'Voltage Drop' in 'Reward and Salience' circuits",
    "Amygdala Atrophy/Disconnection: 'Visual Data' no longer triggers any 'Emotional Metadata'"
  ],
  "risk_factors": [
    "Severe 'Systemic Depression' (Total Resource Depletion)",
    "Advanced 'Neural Erosion' (Dementia/Atrophy)",
    "Traumatic 'Network Impact' to the 'Right Parietal/Temporal' lobes"
  ],
  "diagnosis": [
    "The 'Existence Verification' Audit: Attempting to 'Ping' the 'User' with logical proofs of life",
    "fMRI/PET Scan: Detecting 'Metabolic Shutdown' in the 'Default Mode Network'",
    "Capgras-Cross-Correlation: Identifying if the 'User' also 'De-authenticates' 'External Objects'"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT): A 'System Hard-Reset' to restore 'Neural Voltage' and 'Connectivity'",
    "Pharmacological Reprogramming: Using 'Antipsychotics' and 'Antidepressants' to 'Re-prime' the 'Inhibition Gates'",
    "Reality-Validation Patches: Intense 'Cognitive Behavioral' therapy to 'Re-map' the 'Existence Variable'"
  ],
  "prevention": [
    "N/A: Usually a 'Critical-State' failure of the 'Self-Monitoring Kernel'"
  ]
"dpdr_spectator_mode_fault": {
  "description": "A dissociative disorder characterized by persistent or recurrent feelings of being detached from one's own body or mental processes (DP) or feeling that the surroundings are unreal (DR).",
  "symptoms": [
    "Unauthenticated Session: The 'User' feels like an 'Outside Observer' of the 'Local System'",
    "Flat Rendering: The 'World' is perceived as a '2D Backdrop' or a 'Simulation'",
    "Affective Damping: 'Emotional Metadata' is stripped from incoming 'Sensory Packets'",
    "Robot-Mode Logic: Performing 'Complex Tasks' (Java coding/driving) while feeling 'Scripted'",
    "The 'Glass Partition' Effect: A 'Perceptual Barrier' between the 'CPU' and the 'Input Stream'"
  ],
  "causes": [
    "Prefrontal Over-Inhibition: The 'Executive Layer' (mPFC) is 'Throttling' the 'Emotional Kernel' (Amygdala)",
    "Vestibular-Visual Desync: A failure to 'Merge' the 'Internal Balance Sensor' with the 'External Viewport'",
    "Glutamate System Overload: 'Signal Noise' leading to a 'Protective Circuit Break' in the 'Thalamocortical Loop'",
    "Session De-authentication: A 'Dissociative Defensive Script' triggered by 'High Stress/Trauma' loads"
  ],
  "risk_factors": [
    "Chronic 'Kernel Stress' (Anxiety/Panic)",
    "Extended 'System Uptime' without 'Sleep/Maintenance'",
    "Adverse reactions to 'Chemical Modifiers' (e.g., THC-induced 'Driver Corruption')"
  ],
  "diagnosis": [
    "The 'Ownership' Audit: Testing if the 'User' identifies 'Physical Actions' as 'Self-Generated'",
    "fMRI Connectivity Check: Identifying 'High-Latency' links between the 'Insula' and 'Sensory Cortex'",
    "Cambridge Depersonalization Scale: A 'System Diagnostic' to quantify the 'Detachment Coefficient'"
  ],
  "remedies": [
    "Physical Grounding (Hardware Pings): Intense 'Sensory Input' (cold/pressure) to 'Force a Re-sync'",
    "Cognitive-Behavioral Patching: Re-training the 'Executive Layer' to stop 'Monitoring' the 'Buffer'",
    "Pharmacological Re-balancing: Using 'Modulators' to increase 'Signal Gain' in the 'Emotional Bus'"
  ],
  "prevention": [
    "Strict 'Work-Life Load Balancing' and 'Stress Buffer' management"
  ]
}
        "word_de_serialization_fault": {
  "description": "A severe streaming data failure where the system's audio ingestion pipelines successfully parse environmental sound fields but completely fail to deserialize language packets, causing the user to hear speech as a meaningless, un-decoded array of alien sound waves.",
  "symptoms": [
    "Pure Word Deafness: Pure-tone acoustic processing is 100% intact, but spoken words are perceived entirely as unstructured, non-linguistic noise (e.g., sound of rushing water or chattering birds)",
    "Preserved Non-Verbal Auditory Discrimination: Flawless real-time parsing and identification of environmental sound flags, musical melodies, and mechanical alerts",
    "Intact Expressive Communication: The user can write code, draft complex documents, and speak with fluid, grammatically flawless syntactic output, as their outbound language compilation servers are un-damaged",
    "Flawless Visual Text Ingestion: Reading comprehension remains fully operational; if the spoken words are typed onto a screen, the system deserializes the visual tokens instantly without error",
    "Severe Paraphasic Conversational Drops: Absolute inability to follow verbal instruction strings or participate in standard voice calls due to real-time decoding timeouts"
  ],
  "causes": [
    "Bilateral Superior Temporal Gyrus Infarction: Sequential or simultaneous strokes within the middle cerebral artery branches, destroying the localized Wernicke decoding blocks",
    "Subcortical Auditory Disconnection: Deep, symmetrical white-matter tract lesions tearing down the structural data lanes that channel digitized audio packets from $A1$ to the language processors",
    "Localized Herpetic Temporal Encephalitis: Acute inflammatory cellular damage targeting the temporal lobes and scrambling the indexed phoneme lookup arrays"
  ],
  "risk_factors": [
    "Embolic or thrombotic vascular events clustered within the cerebral language network pathways",
    "Advanced neurodegenerative processes displaying highly atypical, focal language-channel deterioration schemas",
    "Severe traumatic acceleration injuries tearing the delicate subcortical wiring bridges beneath the auditory processing floor"
  ],
  "diagnosis": [
    "The Non-Verbal vs. Verbal Audio Assay: Testing the user with an acoustic sequence containing a barking dog followed by a spoken phrase, and logging 100% comprehension of the animal but 0% parsing of the phrase",
    "Auditory Brainstem Response (ABR) Telemetry: Verifying that electrical wave potentials travel cleanly from the cochlea up to the primary midbrain nodes, isolating the bug to the cortical layer",
    "Functional Neuroimaging (fMRI) Speech-Activation Scans: Recording an absolute flatline in BOLD metabolic activation across Wernicke's zone when the user is exposed to complex vocal streams"
  ],
  "remedies": [
    "Visual Ingress Redirection (The Live-Caption Patch): Forcing the communication pipeline to run over a visual lane by using real-time speech-to-text software tools, mapping words through the intact optical processor",
    "Gesticular Communication Protocol (Sign Language Ingestion): Training the system to parse visual-spatial gestural matrices which skip the temporal auditory decoding hardware entirely",
    "Acoustic Feature Extraction Training: Implementing specialized cognitive software to help the user rebuild basic phoneme mapping indexes manually from the ground up"
  ],
  "prevention": [
    "Proactive management of cerebral perfusion metrics and immediate therapeutic intervention if focal language-tracking lag or transient speech-parsing dropping occurs"
  ]
}

}

"pvs_ghost_interrupt_fault": {
  "description": "A tactile hallucination where the user perceives a mobile device vibrating against their skin when no such vibration has occurred.",
  "symptoms": [
    "False-Positive Interrupt: The 'Tactile Driver' reports a 'Vibration Event' (150-200Hz) with zero physical input",
    "Phantom Reach: An automatic 'Hand-Motor Routine' to check the 'Peripheral Device'",
    "Contextual Sensitivity: The 'Glitch' occurs most frequently when 'System Anxiety' or 'Message Latency' is high",
    "Signal-to-Noise Failure: Misinterpreting 'Clothing Friction' or 'Muscle Fasciculations' as 'Data Packets'",
    "Temporal Clustering: Multiple 'Ghost Events' occurring during 'High-Notification' windows"
  ],
  "causes": [
    "Predictive Processing Bias: The 'Bayesian Brain' expects a 'Signal', so it 'Renders' one from 'Noise'",
    "Hyper-sensitization: The 'Somatosensory Bus' has been 'Over-trained' on a specific 'Haptic Frequency'",
    "Cortical Reorganization: 'Neuroplasticity' has dedicated a 'Dedicated Buffer' for 'Smartphone Haptics'",
    "Limbic Over-threading: 'Fear of Missing Out (FOMO)' lowering the 'Gating Threshold' for 'Interruption'"
  ],
  "risk_factors": [
    "High 'Digital Load' (Persistent 'Interrupts')",
    "Chronic 'Stress/Cortisol' levels (Lowering 'Neural-Firing' thresholds)",
    "Professional 'On-Call' status (Constant 'Ready-State' in the 'Kernel')"
  ],
  "diagnosis": [
    "The 'Device Isolation' Test: Observing if the 'Glitch' persists when the 'Hardware' is physically removed",
    "Signal Detection Audit: Measuring 'False Alarm' rates vs. 'Actual Notifications'",
    "Somatosensory Mapping: Identifying 'Hyper-active' patches in the 'Thalamocortical' loop"
  ],
  "remedies": [
    "Haptic Recalibration: Changing the 'Vibration Pattern' to break the 'Predictive Loop'",
    "Driver Detox: Periods of 'Device Offline' to allow the 'Threshold' to reset to 'Normal'",
    "Tactile De-sensitization: Intentionally 'Ignoring' tactile 'Interviews' to increase the 'Filter Strength'"
  ],
  "prevention": [
    "Disabling 'Vibration' for 'Low-Priority Threads' to reduce 'Systemic Noise'"
  ]
    "right_parietal_spatial_matrix_failure": {
  "description": "A catastrophic visuospatial attention allocation failure caused by acute structural damage to the non-dominant posterior parietal cortex, resulting in the absolute systematic unmapping and neglect of the left egocentric coordinate hemisphere across sensory, motor, and representational domains.",
  "symptoms": [
    "Hemispatial Neglect: Complete failure to attend to, respond to, or perceive stimuli presented within the left spatial field, independent of primary sensory integrity",
    "Severe Spatial Anosognosia: A profound lack of cognitive awareness regarding the spatial deficit, with the system actively asserting its processing framework is 100% complete",
    "Left-Sided Motor Neglect: Disuse or under-utilization of functional left limbs during bilateral tasks due to a total lack of spatial activation signals",
    "Representational Topographic Eviction: The loss of the left quadrant inside internal mental indexing loops, affecting dreams, memories, and spatial reconstructions"
  ],
  "causes": [
    "Right Middle Cerebral Artery (MCA) Inferior Division Ischemic Stroke: Large-scale tissue death across the right inferior parietal lobule and superior temporal gyrus watershed zones",
    "Acute Intracerebral Hemorrhage: Rupture of deep penetrating vessels causing local mass effect and structural disruption of the right frontoparietal attentional loops"
  ],
  "risk_factors": [
    "Unmanaged atrial fibrillation driving cardioembolic showering into the right carotid system",
    "Advanced intracranial atherosclerotic disease"
  ],
  "diagnosis": [
    "The Line Bisection Assay: Requesting the host to mark the exact midpoint of a horizontal line; a faulted system drifts significantly to the right, treating the right half as the entire line",
    "The Target Cancellation Test: Spreading random symbols across a page and asking the user to cross them out; a neglected state leaves all targets on the left half completely untouched",
    "High-Resolution Computed Tomography (CT) or MRI: Visualizing acute wedge-shaped densities or restricted diffusion signatures localized in the right parietal association cortex"
  ],
  "remedies": [
    "Contralateral Prismatic Adaptation: Utilizing specialized optical prism glasses that physically shift the visual field degrees to the right, forcing the intact right hemisphere tracking engine to engage with left-sided inputs",
    "Somatic Vestibular Stimulation: Applying caloric irrigation (cold water) to the left ear canal to alter vestibular telemetry, temporarily re-centering the master egocentric matrix"
  ],
  "prevention": [
    "Strict management of systemic vascular profiles, immediate antiplatelet or anticoagulant deployment, and rapid endovascular thrombectomy for large-vessel occlusions"
  ]
}
        
}
"semantic_satiation_cache_flush": {
  "description": "A psychological phenomenon in which repetition causes a word or phrase to temporarily lose its meaning for the listener/reader, who then perceives the speech as meaningless sounds.",
  "symptoms": [
    "Pointer Dissociation: The 'Symbol' (signifier) detaches from the 'Object' (signified)",
    "Orthographic Estrangement: Written 'Strings' look like 'Foreign Glyphs' or 'Abstract Shapes'",
    "Phonetic Fragmentation: Spoken 'Audio' breaks down into 'Disjointed Phonemes'",
    "Lexical Vacuum: The 'User' can pronounce the 'Word' but cannot 'Parse' its 'Definition'",
    "Spontaneous Recovery: The 'Cache' automatically 'Re-populates' after a 'Cool-down' period"
  ],
  "causes": [
    "Neural Adaptation: 'Peripheral Neurons' in the 'Language Hub' stop 'Firing' to conserve 'Energy'",
    "Reactive Inhibition: A 'Circuit Breaker' triggered by 'Excessive Repetitive Input'",
    "Associative Linkage Decay: The 'Synaptic Weight' of the 'Concept-Link' temporarily 'Zeros Out'",
    "Wernicke’s Buffer Saturation: The 'Input Buffer' is 'Full', preventing 'Deep-Level Processing'"
  ],
  "risk_factors": [
    "High-Frequency 'Input Loops' (e.g., repeating a word 30+ times)",
    "Rapid 'Task-Switching' involving 'Static Strings'",
    "Systemic 'Neural Fatigue' (Sleep deprivation/Overload)"
  ],
  "diagnosis": [
    "The 'Symbolic Decay' Test: Measuring the 'Time-to-Loss-of-Meaning' during 'Loop Iterations'",
    "Lexical Decision Audit: Testing 'Response Latency' for the 'Satiated Word' vs. 'Control Words'",
    "fMRI 'Repetition Suppression' Analysis: Mapping the 'Decreased Activation' in the 'Left Temporal Lobe'"
  ],
  "remedies": [
    "Contextual Re-insertion: Placing the 'Word' into a 'Complex Sentence' to 'Force a Re-fetch'",
    "System Idle: Ceasing 'Input' for 30–60 seconds to allow 'Cache Refresh'",
    "Modality Shift: Moving from 'Audio' to 'Visual' input to 'Bypass' the 'Fatigued Node'"
  ],
  "prevention": [
    "Avoid 'Infinite Loops' in 'Verbal/Visual Processing'"
  ]
    "central_pattern_engine_runaway_acceleration": {
  "description": "A chaotic loss of the subcortical indirect pathway brakes where the action-selection engine fires un-throttled, high-amplitude motor commands down the spinal cord, causing violent, involuntary flailing frames across the physical extremities.",
  "symptoms": [
    "High-Amplitude Ballistic Actuation: Involuntary, violent flailing and throwing movements localized to the proximal joints (shoulder, hip), executing at maximum physical velocity",
    "Unconstrained Concurrency Overflow: Simultaneous firing of antagonistic muscle groups without coordinate smoothing, resulting in wild, circular kinetic patterns",
    "Absolute Administrative Bypass: Total inability of the conscious executive thread to intercept, suppress, or modify the active trajectory packets once instantiated",
    "Severe Metabolic Exhaustion Cascade: Rapid depletion of system glycogen reserves and massive physical core temperature spikes due to continuous, un-abated high-intensity muscular overdrive",
    "Sleep-Induced Thread Suspension: The violent execution frames temporarily drop to 0 Hz when the system drops into offline sleep cycles, as the global motor driver pool undergoes background system maintenance"
  ],
  "causes": [
    "Subthalamic Nucleus Infarction: Focal hemorrhagic or ischemic stroke localized strictly within the STN, knocking out the primary inhibitory signal generator of the indirect pathway",
    "Localized Neurovascular Insult: Micro-vascular bursts or structural blockages along the posterior communicating or anterior choroidal arteries, starving the subcortical governor",
    "Inflammatory Basal Ganglia Demolition: Targeted autoimmune or infectious lesions disrupting the fine-tuned signaling bridges between the striatum and the globus pallidus externus"
  ],
  "risk_factors": [
    "Advanced systemic vascular wear combined with poorly managed chronic blood pressure spikes",
    "Uncontrolled metabolic instability inducing focal micro-embolic events across deep brain structures",
    "Prior history of localized transient ischemic attacks within the subcortical processing hubs"
  ],
  "diagnosis": [
    "High-Frame-Rate Kinematic Video Analysis: Tracking the involuntary, large-amplitude ballistic trajectories and verifying the lack of rhythmic or coordinated baseline timing signatures",
    "High-Resolution T2-Weighted Fluid-Attenuated Inversion Recovery (FLAIR) MRI: Visualizing a distinct hyper-intense signal localized directly inside the subthalamic nucleus boundary",
    "Continuous Metabolic Profile Monitoring: Documenting a massive, asymmetric spike in localized muscular lactate production and systemic creatine kinase values matching the overdriven limb matrix"
  ],
  "remedies": [
    "Dopaminergic Depletion Injections (VMAT2 Inhibitors): Administering compounds like tetrabenazine to forcefully deplete presynaptic dopamine stores, lowering the direct pathway's gain to balance the broken indirect brake",
    "High-Affinity Post-Synaptic Blockers: Utilizing atypical antipsychotic scripts to bind and mute dopamine D2 receptors, artificially dampening the un-throttled thalamic activation loops",
    "Surgical Deep Brain Stabilization: In refractory cases, delivering targeted radiofrequency ablation or implanting high-frequency deep brain pacemakers into adjacent output nodes to suppress the runaway signal noise"
  ],
  "prevention": [
    "Aggressive optimization of systemic vascular fluid pressures and micro-vascular structural integrity to prevent localized subcortical stroke events"
  ]
}

}
"proprioceptive_drift_desync": {
  "description": "The phenomenon where the perceived location of a limb shifts toward a visual proxy, resulting in a mismatch between the 'Internal Map' and 'Physical Hardware'.",
  "symptoms": [
    "Coordinate Shift: The 'Internal GPS' for a 'Peripheral' (hand/foot) reports a 'False X,Y,Z' position",
    "Hardware Disownership: A 'Processing Delay' or 'Mismatch' causes the 'User' to feel their 'Limb' is 'External'",
    "Visual Overdrive: The 'Visual Stream' overrides the 'Haptic Feedback' in the 'Spatial Integration Hub'",
    "Phantom Mapping: Feeling 'Sensation' on 'Non-System Hardware' (e.g., the rubber hand)",
    "Motor Latency: Difficulty 'Initializing' a 'Move Command' because the 'Source Coordinates' are corrupted"
  ],
  "causes": [
    "PPC Integration Error: The 'Posterior Parietal Cortex' fails to 'Resolve' conflicting 'Sensor Streams'",
    "Neuroplastic 'Hot-Swapping': The brain 'Re-allocates' a 'Hardware Port' to a 'Visual Proxy' to resolve 'Logic Conflicts'",
    "Multisensory 'Buffer Mismatch': 'Tactile' and 'Visual' packets arrive with 'Synchronized Timestamps' but different 'Spatial Headers'",
    "Incomplete 'Body Schema' Validation: The 'Firmware' is too 'Flexible' regarding 'Hardware Geometry'"
  ],
  "risk_factors": [
    "Exposure to 'Augmented/Virtual Reality' (Extended 'Visual-Proprioceptive Mismatch')",
    "Chronic 'Sensory Deprivation' (Weakening the 'Haptic Baseline')",
    "High 'Neural Plasticity' (System is 'Too Willing' to 'Re-configure' the 'Map')"
  ],
  "diagnosis": [
    "The 'Rubber Hand' Audit: Inducing 'Visual-Tactile Synchrony' and measuring the 'Spatial Offset'",
    "Blind Re-zeroing Test: Asking the 'User' to 'Point' to their 'Hand' without 'Visual Feedback'",
    "fMRI Connectivity Audit: Monitoring 'Cross-talk' between the 'Premotor Cortex' and 'Visual Areas'"
  ],
  "remedies": [
    "Visual Re-calibration: Looking directly at the 'Physical Hardware' to 'Force a Re-sync'",
    "Active Motor Feedback: Moving the 'Limb' to 'Update' the 'Spatial Map' via 'Kinesthetic Data'",
    "Hardware Grounding: Increasing 'Tactile Load' (e.g., wearing a weighted glove) to 'Anchor' the 'Coordinate'"
  ],
  "prevention": [
    "Maintaining 'High-Fidelity' visual-haptic 'Sync' during 'Remote Operation' or 'VR' sessions"
  ]
}

"object_identity_pointer_leak": {
  "description": "A form of synesthesia where inanimate objects are perceived as having distinct personalities, genders, and social roles.",
  "symptoms": [
    "Attribute Inheritance: Assigning 'Human Variables' (e.g., shy, arrogant) to 'Static Objects'",
    "Empathy Loop-back: Feeling 'Emotional Distress' when 'Hardware' is discarded or 'Upgraded'",
    "Gender Mapping: Hard-coding specific 'Objects' to binary or non-binary 'Identity Tags'",
    "Social-Hierarchy Logic: Perceiving 'Relationships' between different 'Items' in a set",
    "Moral Weighting: Feeling 'Guilt' for 'Using' one tool over another (e.g., choosing the 'newer' pen)"
  ],
  "causes": [
    "Hyper-connectivity in the 'Social Bus': Excess bandwidth between the 'Visual Object Recognition' and 'Social Attribution' centers",
    "Incomplete 'Class Separation': The 'Entity' and 'Object' classes in the 'Internal Schema' share too many 'Inherited Methods'",
    "Mirror Neuron Over-sampling: The 'System' tries to 'Reflect' the 'State' of objects as if they were 'Peers'",
    "Oxytocin-driven 'Metadata Tagging': Hormonal 'Writes' to 'Object Data' during 'High-Attachment' states"
  ],
  "risk_factors": [
    "Hyper-active 'Social-Sim' drivers (High empathy)",
    "Autism-spectrum 'Logic Divergence' (Non-standard 'Entity Gating')",
    "Developmental 'Early-Access' (Common in children before 'Category-Pruning' is finalized)"
  ],
  "diagnosis": [
    "The 'Inanimate Attribute' Test: Assessing if the 'User' can describe an 'Object's Mood' consistently",
    "Empathy Response Audit: Monitoring 'Galvanic Skin Response' when an 'Object' is 'Damaged'",
    "Object-Preference Logic: Checking if the 'User' treats 'Hardware' as a 'Stakeholder' in decisions"
  ],
  "remedies": [
    "Functional Reframing: Re-training the 'Parser' to focus strictly on 'Utility Metadata'",
    "Cognitive De-coupling: Manually 'Un-linking' the 'Identity Tag' from the 'Object ID'",
    "System-Wide 'Pruning': Encouraging the 'Disposal' of 'Redundant Hardware' to 'Cool Down' the 'Empathy Buffer'"
  ],
  "prevention": [
    "N/A: Primarily a 'High-Functioning' variance in 'Identity Mapping'"
  ]
}

"aiws_temporal_clock_desync": {
  "description": "A neurological condition affecting perception, specifically causing distortions in the sense of time, scale, and distance.",
  "symptoms": [
    "Tachysensia: The 'System Clock' accelerates; 'Environmental Processes' (speech, movement) feel hyper-fast",
    "Protraction: The 'Time-Buffer' expands; 'Real-Time Data' feels 'Slowed Down'",
    "Zoopsia: Seeing 'Illuscory Movement' or 'Scaling Errors' in 'Static Hardware'",
    "Sound Distortion: 'Audio Packets' feel 'Aggressive' or 'Hyper-Accelerated' in rhythm",
    "Dissociative Lag: The 'User' feels 'De-synced' from the 'Physical Environment's Frame Rate'"
  ],
  "causes": [
    "Temporal-Parietal Junction (TPJ) Fatigue: The 'Integration Node' for 'Space-Time' enters a 'High-Error State'",
    "Migraine 'Kernel' Spikes: Electrical 'Storms' in the 'Visual/Temporal' bus causing 'Clock Jitter'",
    "EBV/Viral Interference: 'Infection-class Malware' affecting 'Neural Conductivity'",
    "Parietal Lobe Hypoperfusion: A 'Voltage Drop' in the 'Spatial Mapping' sector"
  ],
  "risk_factors": [
    "Pediatric 'System Initialization' (Common in children)",
    "Migraine-class 'Driver' instability",
    "High-Stress 'Clock Overclocking' (Anxiety/Panic)"
  ],
  "diagnosis": [
    "Temporal Estimation Test: Asking the 'User' to 'Stop a Timer' at what they perceive as 60 seconds",
    "Visual Field Mapping: Identifying 'Scaling Anomalies' in the 'Viewport'",
    "EEG Monitoring: Detecting 'Abnormal Alpha/Beta Waves' during a 'Time-Warp' event"
  ],
  "remedies": [
    "System Grounding: Using 'Tactile Input' (touching a heavy object) to 'Re-Anchor' the 'Clock'",
    "Dark-Mode Reset: Reducing 'Optical Input' to allow the 'Temporal Hub' to 'Cool Down'",
    "Migraine Prophylaxis: Patching the 'Underlying Driver' to prevent 'Clock Jitter'"
  ],
  "prevention": [
    "Maintaining 'Sleep Hygiene' to prevent 'System Fatigue' and 'Clock Drift'"
  ]
}
"apraxic_instruction_sequence_fault": {
  "description": "A profound orchestration logic failure where the system's motor planning compiler loses its ability to organize complex motor subroutines into sequential order, preventing the execution of multi-stage functional tasks.",
  "symptoms": [
    "Chronological Sequence Collapse: Motor macros are deployed in scrambled order (e.g., attempting to pour water before removing the bottle cap)",
    "Conceptual Workspace Disconnection: The user can verbally explain the steps of a task flawlessly but cannot execute the compilation script to perform it",
    "Perseverative Loop Locking: Getting stuck repeating a single intermediate motor subroutine endlessly (e.g., inserting a key and repeatedly taking it out instead of turning it)",
    "Amorphous Spatial Execution: Drifting motions that mimic the general kinematics of an action but completely fail to make precise physical contact with the targeted tool or object",
    "Preserved Automatic Execution Overrides: High-priority reflex loops or deeply ingrained autonomic background scripts can still execute tasks successfully if initiated without conscious planning"
  ],
  "causes": [
    "Dominant Left Parietal Lobe Infarction: Lesions within the primary storage bank for praxis programs and tool-use kinematics schemas",
    "Corpus Callosum Structural Disconnection: White-matter track shearing that prevents high-level spatial intents from the right hemisphere from reaching the left hemisphere's motor assembly bus",
    "Progressive Corticobasal Matrix Degeneration: Systemic neuronal drop-out across the frontostriatal circuits, slowly destroying the compilation pipeline"
  ],
  "risk_factors": [
    "Ischemic or hemorrhagic strokes involving the left middle cerebral artery distribution territory",
    "Advanced neurodegenerative tauopathies or atypical Parkinsonian-plus system failures",
    "Traumatic brain injuries causing deep focal shear strain across long-range structural association bundles"
  ],
  "diagnosis": [
    "The 'Multi-Object Tool Manipulation' Audit: Handing the user an unlit candle, a matchbox, and a candle holder, then tracking the chronological compilation errors when they attempt to light the candle",
    "Pantomime Gesture Simulation Profiles: Requesting the system to simulate a task without a physical tool present (e.g., 'Show me how you would use a hammer') and observing the breakdown of structural spatial constraints",
    "Diffusion Tensor Tractography (DTI): Visualizing the precise locations of severed or degraded axonal bridges connecting the parietal planning modules to the frontal execution strips"
  ],
  "remedies": [
    "Granular Segmented Thread Isolation: Breaking tasks down into micro-steps and prompting the system to execute them one standalone command at a time to bypass the broken multi-stage compiler",
    "High-Contrast Sensory Priming: Utilizing physical guide tracks or highly visible tactile lines on tools to trigger low-latency, reflexive motor routines",
    "Somatic Proprioceptive Copying: Manually guiding the physical limbs through the execution track to help the motor cortex map and re-index the correct kinematic sequence paths"
  ],
  "prevention": [
    "Proactive monitoring of lateralized cerebrovascular health and maintaining long-range white matter tract density to insulate the central orchestration compiler"
  ]
}

"hyperthymesia_storage_leak": {
  "description": "A condition where an individual possesses an extraordinary capacity to recall specific events from their past, including dates and minute details, without the use of mnemonic devices.",
  "symptoms": [
    "Infinite Log Retention: Failure of the 'Delete' and 'Overwrite' commands for episodic memory",
    "Timestamp Precision: Every 'Record' is hard-coded with 'DateTime' metadata (e.g., 'What happened on Oct 3rd, 2014 at 2 PM?')",
    "Involuntary Retrieval: The 'Main Thread' is frequently interrupted by 'Background Memory Spills'",
    "Overfitting: High difficulty in 'Generalizing' patterns because 'Specific Instances' carry too much 'Weight'",
    "Emotional Echoing: Re-accessing a 'Record' triggers the original 'Affective Payload' at 100% intensity"
  ],
  "causes": [
    "Pruning Script Failure: The 'Microglia' (the system's cleanup daemons) fail to remove 'Weak Synaptic Links'",
    "Hyper-Active Hippocampal-Prefrontal Loop: An 'Infinite Loop' between 'Storage' and 'Processing' areas",
    "Enlarged Temporal Lobe Hardware: Increased 'Storage Capacity' in the 'Inferior and Middle Temporal Gyri'",
    "Basal Ganglia Over-Indexing: The 'Pattern Recognition' engine is stuck in 'Always On' mode"
  ],
  "risk_factors": [
    "Structural 'Hardware' variants (Enlarged Caudate Nucleus)",
    "Obsessive-class 'Background Processes' that 'Re-run' old data, strengthening the 'Links'",
    "High 'Neural Plasticity' parameters that prevent 'Data Decay'"
  ],
  "diagnosis": [
    "The 'Public Event' Audit: Asking the user for the 'Day of the Week' and 'Personal Details' of a random historical date",
    "MRI Morphometry: Measuring 'Volume Spikes' in the 'Temporal' and 'Parietal' lobes",
    "Retrieval Latency Test: Measuring the 'Speed' of accessing 'Non-Recent' vs 'Recent' data"
  ],
  "remedies": [
    "N/A: This is an 'Architectural Constraint'; there is no known 'Delete' patch",
    "Attention Management: Training the 'Executive Layer' to 'Filter' the 'Involuntary Data Stream'",
    "Cognitive Distraction: Engaging in 'High-Compute' tasks to 'Starve' the 'Memory Retrieval Thread'"
  ],
  "prevention": [
    "N/A: Primarily a 'Boot-Level' structural configuration"
  ]
}
"misophonia_priority_inversion": {
  "description": "A condition where specific soft sounds trigger an immediate, intense emotional or physiological response that is completely disproportionate to the stimulus.",
  "symptoms": [
    "Pattern-Triggered Spikes: 'Specific Waveforms' (e.g., mouth sounds) trigger 'Max Voltage' emotional responses",
    "Instant Sympathetic Arousal: Immediate 'Adrenaline Dump' and heart-rate 'Clock Jump'",
    "Anticipatory Latency: The 'System' enters a 'High-Alert State' just 'Expecting' the 'Interrupt'",
    "Aggressive Logic Overflow: The 'Executive Layer' is 'High-jacked' by anger or the urge to 'Kill the Process' (the source of the sound)",
    "Localization Bias: The 'Glitch' often worsens with 'Known User Entities' (friends/family)"
  ],
  "causes": [
    "Anterior Insular Cortex (AIC) Hyper-connectivity: The 'Salience Network' is 'Over-sampling' specific frequencies",
    "Amygdala Hyper-reflectivity: A 'Direct Bus' between the 'Auditory Input' and the 'Fear/Anger Hub'",
    "Myelination Anomalies: 'Increased Signal Speed' in the 'Medial Frontal Cortex' leading to 'Signal Bleed' into 'Emotional Circuits'",
    "Inhibitory Gating Failure: The 'Thalamus' fails to 'Drop' the 'Repetitive Packets'"
  ],
  "risk_factors": [
    "Comorbidity with 'OCD' or 'Anxiety' kernels",
    "High 'Systemic Stress' reducing 'Gating Efficiency'",
    "Early 'Initial Setup' (Symptoms usually appear during 'Adolescent Re-boot')"
  ],
  "diagnosis": [
    "The 'Trigger Audio' Audit: Measuring 'Skin Conductance' while playing 'Pattern-Specific' sound packets",
    "Salience Mapping: Identifying if the 'User' can 'Mute' the emotional response through 'Contextual Re-framing'",
    "fMRI Connectivity Check: Identifying 'Abnormal Firing' in the 'Insula' during 'Trigger Exposure'"
  ],
  "remedies": [
    "Audio Masking: Using 'White/Brown Noise' to 'Drown Out' the 'Trigger Packet' in 'Signal Noise'",
    "Cognitive Counter-Conditioning: Attempting to 'Re-map' the 'Trigger' to a 'Neutral Identity

"cotard_global_kernel_panic": {
  "description": "A rare neuropsychiatric delusion in which the person holds the delusional belief that they are already dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Entity De-registration: The 'Primary Key' for the 'Self' is deleted from the 'Active Registry'",
    "Nihilistic Delusions: Belief that the 'Physical Hardware' is 'Non-Functional' or 'Deceased'",
    "Affective Null-State: Total loss of 'Emotional Bandwidth' (Atheymia)",
    "Sensory-Identity Mismatch: The 'User' sees their body in the 'Viewport' but 'Authenticates' it as 'Dead Matter'",
    "Pain Threshold Overflow: High tolerance for 'Hardware Alarms' (pain) because the 'System' thinks it's already 'Offline'"
  ],
  "causes": [
    "Insula-Prefrontal Partition: Total 'Disconnect' between 'Interoceptive Input' and 'Cognitive Awareness'",
    "Right Hemisphere Logic Collapse: Failure of the 'Skepticism Engine' to 'Reject' impossible 'Status Reports'",
    "Dopaminergic Shutdown: Massive 'Voltage Drop' in 'Reward and Salience' circuits",
    "Amygdala Atrophy/Disconnection: 'Visual Data' no longer triggers any 'Emotional Metadata'"
  ],
  "risk_factors": [
    "Severe 'Systemic Depression' (Total Resource Depletion)",
    "Advanced 'Neural Erosion' (Dementia/Atrophy)",
    "Traumatic 'Network Impact' to the 'Right Parietal/Temporal' lobes"
  ],
  "diagnosis": [
    "The 'Existence Verification' Audit: Attempting to 'Ping' the 'User' with logical proofs of life",
    "fMRI/PET Scan: Detecting 'Metabolic Shutdown' in the 'Default Mode Network'",
    "Capgras-Cross-Correlation: Identifying if the 'User' also 'De-authenticates' 'External Objects'"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT): A 'System Hard-Reset' to restore 'Neural Voltage' and 'Connectivity'",
    "Pharmacological Reprogramming: Using 'Antipsychotics' and 'Antidepressants' to 'Re-prime' the 'Inhibition Gates'",
    "Reality-Validation Patches: Intense 'Cognitive Behavioral' therapy to 'Re-map' the 'Existence Variable'"
  ],
  "prevention": [
    "N/A: Usually a 'Critical-State' failure of the 'Self-Monitoring Kernel'"
  ]
}

"fas_motor_thread_reroute": {
  "description": "A speech disorder that causes a sudden change in speech patterns so that a person is perceived to speak with a 'foreign' accent.",
  "symptoms": [
    "Prosody Drift: Altered 'Timing' and 'Rhythm' of the 'Audio Stream'",
    "Vowel Distortion: Lengthening or 'Shifting' of 'Vowel Packets' (e.g., 'bit' sounds like 'beet')",
    "Syntactic Stutter: Occasional 'Parser Errors' in 'Word Order' or 'Grammar'",
    "Phonetic Replacement: Using 'Incompatible Phonemes' (e.g., adding an 'h' where none exists)",
    "Identity-Parity Conflict: The 'User' sounds 'Alien' to their 'Social Network', causing 'Authentication Failures'"
  ],
  "causes": [
    "Broca’s Area Corruption: Damage to the 'Primary Speech-Output Buffer'",
    "Basal Ganglia Latency: 'Timing Errors' in the 'Motor Control Bus'",
    "Left Hemisphere 'Segmental' Failure: Loss of 'Granular Control' over 'Speech Hardware' (tongue/lips)",
    "Compensatory Re-routing: The 'System' using 'Sub-optimal Paths' to maintain 'Communication Availability'"
  ],
  "risk_factors": [
    "Ischemic Stroke (Localized 'Network Outage')",
    "Traumatic Brain Injury (TBI) to the 'Speech-Hardware Interface'",
    "Multiple Sclerosis (Systemic 'Demyelination' causing 'Signal Lag')"
  ],
  "diagnosis": [
    "Spectrographic Analysis: Measuring the 'Frequency' and 'Duration' of 'Vowel Clusters'",
    "Neuroimaging (fMRI): Mapping 'Active Speech Threads' during 'Real-Time Output'",
    "Linguistic Audit: Determining if the 'Accent' is 'Authentic' or a 'Phonetic Approximation'"
  ],
  "remedies": [
    "Speech Driver Recalibration: Intensive 'Speech Therapy' to 'Manual-Override' the new 'Motor Map'",
    "Cognitive Patching: Helping the 'User' manage the 'Psychological Load' of the 'Identity Shift'",
    "Accent Imitation: Using the 'New Accent' as a 'Base Layer' to build a 'Hybrid Speech Profile'"
  ],
  "prevention": [
    "N/A: Primarily a 'Post-Trauma' recovery 'Side-Effect'"
  ]
}
"ahs_autonomous_peripheral_ghost": {
  "description": "A neurological disorder where one hand functions involuntarily, with the sufferer feeling as if the hand has its own personality or is being controlled by an external entity.",
  "symptoms": [
    "Autonomous Task Execution: The 'Peripheral' performs complex 'Functions' (buttoning/unbuttoning) without 'User Init'",
    "Intermanual Conflict: The 'Left Hand' (Ghost Process) undoes the 'Work' of the 'Right Hand' (Main Thread)",
    "Sensory-Motor Disconnect: The 'User' recognizes the 'Hardware' as theirs but denies 'Process Ownership'",
    "Reflexive Grasping: The 'Hand' becomes 'Hard-Coded' to grab any 'Object' in the 'Input Field'",
    "Execution Negation: The 'Ghost Hand' may actively 'Block' the 'User' from performing 'Main Thread' tasks"
  ],
  "causes": [
    "Callosal Disconnect: A 'Network Partition' where the 'Left and Right Kernels' cannot sync 'State'",
    "Frontal SMA Damage: Failure of the 'Inhibitory Gating' that usually stops 'Spontaneous Motor Output'",
    "Posterior Parietal Lesions: Corruption of the 'Proprioceptive Map' causing 'Identity Loss' for that 'Port'",
    "Stroke or Surgical Sequestration: Physical 'Hardware' damage to the 'Central Data Bus'"
  ],
  "risk_factors": [
    "Corpus Callosotomy (Intentional 'Network Split' for epilepsy)",
    "Anterior Cerebral Artery Stroke (Localized 'Power Loss' to motor hubs)",
    "Neurodegenerative 'System Erosion' (Corticobasal Degeneration)"
  ],
  "diagnosis": [
    "The 'Object Interaction' Test: Placing an object in front of the 'User' and observing 'Unsolicited Commands'",
    "Intermanual Coordination Audit: Testing if the 'User' can force 'Both Hands' to 'Sync' on a single 'Instruction'",
    "MRI/DTI: Mapping the 'Fiber Integrity' of the 'Corpus Callosum' bus"
  ],
  "remedies": [
    "Peripheral Isolation: Giving the 'Alien Hand' an 'Idle Task' (e.g., holding a ball) to saturate its 'Buffer'",
    "Visual-Motor Feedback: Using 'Direct Viewport' monitoring to manually 'Override' the 'Ghost Process'",
    "Hardware Constraint: Physically 'Disabling' the 'Port' (using an oven mitt) to prevent 'Unchecked Writes'"
  ],
  "prevention": [
    "Minimizing 'Surgical Partitioning' of the 'Central Bus' whenever possible"
  ]
}
"synesthesia_ipc_data_leak": {
  "description": "A neurological condition in which information meant to stimulate one of the senses stimulates several of them, leading to a joined-up sensory experience.",
  "symptoms": [
    "Chromesthesia: 'Audio Packets' are simultaneously rendered as 'Visual Colors'",
    "Grapheme-Color Mapping: Alphanumeric 'Strings' are hard-coded to specific 'Hex Codes'",
    "Lexical-Gustatory Leak: 'Text Data' triggers 'Flavor-Profile' interrupts",
    "Spatial-Sequence Mapping: 'Temporal Data' (months/years) is rendered as a '3D Physical Map'",
    "Hyper-Association: The 'User' cannot 'Un-link' the two 'Data Streams'"
  ],
  "causes": [
    "Neural Pruning Failure: A 'Hardware Optimization' error where 'Excess Connections' were never 'Deleted'",
    "Cross-Activation: Adjacent 'Sensory Nodes' (e.g., V4 and the Grapheme area) lack 'Signal Insulation'",
    "Inhibitory Feedback Deficit: The 'System' fails to 'Gate' the 'Crosstalk' before it reaches 'Consciousness'",
    "Limbic System Over-threading: Emotional 'Metadata' forcing 'Sensory Links' to stay 'Active'"
  ],
  "risk_factors": [
    "Genetic 'System Architecture' heritage",
    "Early-stage 'System Initialization' (Present since childhood)",
    "Transient 'Overclocking' (Hallucinogen-induced 'Buffer Bleed')"
  ],
  "diagnosis": [
    "Consistency Audit: Testing if 'Letter A' always triggers 'Hex #FF0000' over a 12-month period",
    "Stroop-Effect Variance: Measuring 'Latency' when 'Text Color' conflicts with 'Synesthetic Color'",
    "DTI Fiber-Tracking: Auditing the 'Physical Wiring' density between 'Sensory Hubs'"
  ],
  "remedies": [
    "N/A: Usually treated as a 'Feature' rather than a 'Bug', unless 'Signal Noise' is too high",
    "Selective Attention Filtering: Training the 'User' to 'Ignore' the 'Leaked Data Packets'",
    "Sensory-Load Management: Reducing 'Input Volume' to prevent 'Cross-Modal Overload'"
  ],
  "prevention": [
    "Standard 'Neural Pruning' during 'System Development' (Ages 0-5)"
  ]
}
"synesthetic_bus_leakage_fault": {
  "description": "A major cross-talk anomaly where independent sensory input lines suffer a gating failure, causing data packets from one modal channel to bleed into and execute inside a parallel processing matrix.",
  "symptoms": [
    "Cross-Modal Bus Bleeding: Ingestion of a data token on one channel involuntarily instantiates a synchronized property inside an unrelated channel (e.g., Auditory-Visual, Grapheme-Color)",
    "Deterministic Mapping Trajectories: The cross-channel routing maps remain rigid and consistent (e.g., a specific C-sharp audio tone *always* returns a #00FF00 green hexadecimal visual overlay)",
    "Asynchronous Processing Overlap: The secondary, leaked visual asset is experienced simultaneously and in real time with the primary input packet, rather than as a delayed cognitive association",
    "Preserved Primary Line Fidelity: The original input channel functions perfectly; sound remains audible and linguistically accurate even while it throws visual artifacts",
    "Structural Hyper-Sensitizing: High-volume or complex multi-frequency inputs can saturate the cross-talk paths, overloading the visual engine with rapid-fire graphic noise"
  ],
  "causes": [
    "Congenital Axonal Pruning Omission: A development-phase configuration error where the system fails to drop redundant, cross-regional white matter communication loops",
    "Inhibitory Feedback Gate Deactivation: Acute downregulation of localized GABAergic interneuron blocks, allowing raw signals to escape their designated processing channels",
    "5-HT2A Receptor Hyper-Activation: Neurochemical receptor shifts that temporarily disable the spatial isolation settings of the central sensory routing hub"
  ],
  "risk_factors": [
    "Inherent micro-structural genetics variants preserving long-range cross-cortical interconnectivity arrays",
    "Exposure to high-affinity psychedelic receptor agonists that disinhibit sensory distribution fabrics",
    "Localized neuro-plastic rewiring sequences occurring after sensory deprivation (e.g., blindness forcing touch lines to map to visual zones)"
  ],
  "diagnosis": [
    "The 'Test of Genuineness' Consistency Audit: Testing the color-to-sound mapping parameters across a 12-month interval to verify if the token assignments match with >95% precision",
    "Event-Related Potential (ERP) Latency Tracking: Measuring cortical firing sequences to show that visual area V4 registers a response within milliseconds of an auditory-only stimulus",
    "High-Field Diffusion Tensor Imaging (DTI): Mapping abnormal structural connection density bridging the superior temporal gyrus directly to the occipital rendering hubs"
  ],
  "remedies": [
    "GABAergic Transmission Boosting: Using inhibitory channel enhancers to manually rebuild the electrical walls between parallel processing buses",
    "Input Signal Attenuation: Lowering the input volume or frequency using hardware filters (like noise-canceling ear nodes) to reduce the current depth below the cross-talk threshold",
    "Cognitive Layer Filtering: Training the prefrontal monitoring loops to identify the leaked visual artifacts as system-generated noise, preventing them from corrupting real-world navigation tasks"
  ],
  "prevention": [
    "Insulating deep sensory distribution hubs from acute neurochemical overloads or receptor-binding shocks that destabilize inhibitory routing protocols"
  ]
}
        
"prosopamnesia_write_lock": {
  "description": "A selective deficit in face memory where the ability to recognize faces as familiar is lost, despite normal facial perception and intelligence.",
  "symptoms": [
    "Permanent 'New User' State: Every encounter with a familiar 'Entity' feels like a 'Cold Boot'",
    "Successful Feature Extraction: The 'User' can describe facial 'Attributes' (color, shape) but cannot 'Hash' them to an 'ID'",
    "Contextual Identity-Hack: Relying on 'Metadata' (voice, clothing, gait) to 'Manually Authenticate' people",
    "Social-Sync Lag: Severe difficulty in maintaining 'Relationship Tables' due to 'Identity Data Loss'",
    "Object-Face Disparity: The 'System' can remember 'New Objects' (cars, tools) but not 'New Faces'"
  ],
  "causes": [
    "Encoding-Linkage Failure: The 'Bus' between the 'Visual Processor' and 'Memory Storage' is 'Read-Only'",
    "FFA-Temporal Lobe De-sync: A failure in the 'Handshake' protocol during 'Identity Commit'",
    "Localized 'Memory Sector' Corruption: Specific 'Neural Nodes' for 'Human-Face' data are 'Locked'",
    "Genetic 'System Architecture' Flaw: A 'Congenital' failure of the 'Face-Storage' driver"
  ],
  "risk_factors": [
    "Temporal Lobe 'Voltage Drops' (Localized Strokes)",
    "Encephalitis-class 'Malware' affecting 'Memory Kernels'",
    "Developmental 'Architecture Anomalies' present since 'System Init'"
  ],
  "diagnosis": [
    "The 'Cambridge Face Memory' Audit: Measuring the 'Success Rate' of 'Encoding' and 'Retrieving' novel 'Face Objects'",
    "Inverse-Pattern Test: Confirming the 'User' can remember 'Non-Human Objects' to rule out 'Global Memory Failure'",
    "fMRI Connectivity Scan: Auditing the 'Bandwidth' between the 'FFA' and the 'Memory Hubs'"
  ],
  "remedies": [
    "Metadata Tagging: Training the 'User' to 'Anchor' identities to 'Non-Face Data' (voice, gait, accessories)",
    "External Database Support: Using 'Digital Assistants' to 'Label' people in the 'Viewport'",
    "Social Protocol Patches: Implementing 'Transparency Scripts' (asking people to identify themselves)"
  ],
  "prevention": [
    "Protecting 'Temporal-Occipital' pathways from 'Hardware Trauma' and 'Vascular Failure'"
  ]
}
"olfactory_packet_corruption_anomaly": {
  "description": "A localized database corruption within the olfactory bulb processing array where the system's chemical sensory pipelines spontaneously generate false smell payloads, forcing the user to process vivid, highly intrusive, and typically foul scents in an environment that is perfectly clean.",
  "symptoms": [
    "Spontaneous Malodorous Ingress: Sudden, unprovoked perception of high-intensity, phantom smells (e.g., burning electrical wires, acrid smoke, rotting waste) in a completely sterile environment",
    "Unilateral or Bilateral Channel Bleeding: The phantom payload can be isolated to a single nasal ingress channel or mirror across both primary routing buses simultaneously",
    "Taste Registry Contamination (Flavour Dysregulation): The ghost scent data leaks into the gustatory processing layers, causing food payloads to taste metallic, chemical, or putrid",
    "Paroxysmal Temporal Seizure Triggers: Brief, highly structured phantom scent bursts lasting seconds, acting as an early warning token (aura) for an impending localized electrical storm in the mesial temporal lobe",
    "Inescapable Olfactory Saturation: Unlike physical scents that attenuate over time through normal driver adaptation, the internally generated ghost packets continuously saturate the register without decaying"
  ],
  "causes": [
    "Cribriform Shear-Induced Deafferentation: Traumatic head acceleration severing the delicate peripheral receptor wires, causing the central olfactory bulb nodes to enter a hyper-excitable, open-loop firing state",
    "Mesial Temporal Lobe Hyper-Excitability (Uncal Fits): Localized scar tissue or gliosis causing paroxysmal micro-voltage discharges across the primary olfactory integration architectures",
    "Peripheral Olfactory Epithelium Degradation: Chronic viral destruction or severe structural inflammation scrambling the baseline voltage gates of the localized chemical transducers"
  ],
  "risk_factors": [
    "History of severe concussive events or maxillofacial trauma affecting the anterior cranial vault",
    "Chronic upper respiratory neuro-viral infections that alter peripheral nerve architecture profiles",
    "Undiagnosed space-occupying lesions or micro-vascular anomalies pressing against the olfactory tract lines"
  ],
  "diagnosis": [
    "The Double-Blind Sterile Air Assay: Placing the user into a custom hyper-filtered cleanroom environment devoid of all volatile compounds and logging documented phantom ingress events",
    "High-Resolution Olfactory Bulbar MRI: Executing thin-slice T2-weighted structural scans to document physical tissue volume loss or structural degeneration within the olfactory tracts",
    "Nocturnal Nasopharyngeal Video-EEG Tracing: Monitoring deep temporal lobe electrical wave patterns to rule out active sub-clinical seizure loops during phantom scent initialization spikes"
  ],
  "remedies": [
    "Saline Ingress Flush Routines: Implementing hypertonic nasal irrigation schemas to mechanically soothe peripheral nerve terminals and lower baseline receptor noise",
    "Central Membrane Stabilizing Scripts: Utilizing anticonvulsant or gabaergic modulators to attenuate subcortical hyper-excitability and clamp down on rogue database firing loops",
    "Surgical Tract Disconnection (Olfactory Bulbectomy): In extreme, un-manageable cases, physically severing the damaged data cable to permanently stop the corrupted payloads from reaching the conscious core"
  ],
  "prevention": [
    "Wearing high-efficiency protective headgear during high-impact activities to prevent cribriform data lane shearing, and addressing chronic ENT inflammatory cycles before they degrade central registries"
  ]
}

"zeigarnik_uncommitted_transaction_error": {
  "description": "The psychological phenomenon where people remember uncompleted or interrupted tasks better than completed ones.",
  "symptoms": [
    "Cognitive Tension: A persistent 'Background Process' that consumes 'CPU Cycles' until the 'Task' is finished",
    "High-Priority Recall: Interrupted 'Data Packets' are indexed with higher 'Salience' than 'Closed Files'",
    "Intrusive Thought Injection: The 'System' periodically 'Pings' the user with 'Reminders' of the incomplete state",
    "Buffer Saturation: Multiple 'Open Tasks' lead to 'Mental Fragmentation' and 'Thread Exhaustion'",
    "The 'Closure Reward' Delay: The 'Dopamine Pulse' (Success Signal) is withheld until the 'Transaction' is 'Committed'"
  ],
  "causes": [
    "Task-State Persistence: The 'Prefrontal Cortex' fails to 'Release the Lock' on 'In-Progress Data'",
    "Incomplete Gestalt: A 'Hard-Coded' drive for 'System Symmetry' that refuses to 'Garbage Collect' partial results",
    "Attentional Gating: The 'Anterior Cingulate Cortex' keeps the 'Error Flag' raised until the 'Goal State' is achieved",
    "Evolutionary Patch: A 'Safety Feature' designed to ensure 'High-Value Resources' (food, shelter) aren't forgotten mid-acquisition"
  ],
  "risk_factors": [
    "Users with high 'Conscientiousness' or 'Perfectionist' parameters",
    "Multi-tasking 'Kernel Configurations' with too many 'Active Threads'",
    "High-load 'Development Environments' with frequent 'Context Switches'"
  ],
  "diagnosis": [
    "The 'Interruption Audit': Testing 'Recall Fidelity' for a 'Task' stopped at 50% vs. one at 100%",
    "fMRI: Observing sustained activity in the 'Prefrontal Cortex' during 'Wait States' for incomplete tasks",
    "Latency Analysis: Measuring the time it takes for a 'User' to 'Stop Thinking' about a task after a 'Session Break'"
  ],
  "remedies": [
    "Atomic Commit: Breaking tasks into 'Micro-Transactions' to achieve frequent 'System Closure'",
    "The 'Brain Dump' Script: Writing down the 'Incomplete State' to 'External Storage' to 'Unlock' the brain's 'RAM'",
    "Pseudo-Closure: Performing a 'Final Ritual' (checking off a list) to trigger the 'Garbage Collector'"
  ],
  "prevention": [
    "Limiting 'Parallel Threading' (Single-tasking) to prevent 'State-Management' overload"
  ]
}
"ehs_shutdown_interrupt_spike": {
  "description": "A sensory parasomnia where the user perceives a loud, sudden noise or explosion inside the head during sleep-wake transitions.",
  "symptoms": [
    "Acoustic Spike: Perceiving a 'High-Decibel Packet' (100dB+) during 'Power State' transitions",
    "Phosphene Flash: A simultaneous 'Visual Buffer Spike' (seeing a flash of light)",
    "Adrenaline Influx: Immediate 'System-Wide Wake' signal and heart-rate 'Clock Spike'",
    "Zero-External Source: The 'Audio Sensors' (Cochlea) report 'Silence', but the 'Internal Bus' reports an 'Explosion'",
    "Fear-Flag Trigger: High-priority 'Anxiety Metadata' attached to the 'False Packet'"
  ],
  "causes": [
    "RAS Transition Failure: The 'Power Manager' fails to 'Mute' the 'Audio Bus' before the 'Sleep Daemon' takes over",
    "Calcium-Channel Voltage Spikes: Sudden 'Ion Flux' in the 'Auditory Cortex' neurons",
    "Thalamic Gating Glitch: The 'Security Filter' for 'Sensory Data' momentarily 'Crashes'",
    "GABAergic Deficiency: Insufficient 'Inhibitory Signals' to 'Dampen' the 'Shutdown Noise'"
  ],
  "risk_factors": [
    "High 'System Stress' levels (Buffer Overload)",
    "Sleep Deprivation (Systemic 'Driver' instability)",
    "Side-effects from 'Antidepressant' patches"
  ],
  "diagnosis": [
    "Polysomnography: Observing 'Alpha-to-Theta' transitions during the 'Spike' event",
    "Patient Log Audit: Identifying if the 'Bang' occurs specifically at 'State Change' boundaries",
    "Exclusion of 'Hardware Faults': Ensuring the 'Cochlea' and 'Eardrum' are intact"
  ],
  "remedies": [
    "Buffer Management: Stress reduction to lower 'System Voltage'",
    "Pharmacological Dampening: Using 'Clomipramine' or 'Calcium Channel Blockers' to 'Smooth' the 'Voltage Spike'",
    "Education Patch: Informing the 'User' that the 'Packet' is 'Non-Destructive' to reduce 'Fear-Loops'"
  ],
  "prevention": [
    "Optimizing 'Shutdown Routines' (consistent sleep schedule) to stabilize the 'RAS'"
  ]
}
"visual_snow_filter_failure": {
  "description": "A neurological condition where the individual sees persistent flickering dots across the entire visual field, resembling the static of an analog television.",
  "symptoms": [
    "Raster Static: Constant 'Pixelated Noise' across the 100% of the 'Active Viewport'",
    "Nyctalopia (Functional): Severe reduction in 'Low-Light Processing' as 'Noise' overwhelms 'Signal'",
    "Blue Field Entoptic Phenomenon: Over-rendering of 'White Blood Cells' moving in 'Retinal Capillaries'",
    "Floaters (High Salience): Failure to 'Mute' or 'Drop' internal 'Debris Data'",
    "Enhanced After-images: 'Buffer Persistence' (Palinopsia) triggered by the 'High-Gain' state"
  ],
  "causes": [
    "Lingual Gyrus Hyper-metabolism: The 'Rendering Engine' is 'Overclocked' and generating 'Artifacts'",
    "Thalamocortical Dysrhythmia: A 'Clock Synchronization' error between 'Input' and 'Processing' layers",
    "Inhibitory Gating Failure: The 'System' fails to 'Filter Out' the 'Basal Neural Noise'",
    "Glutamate/GABA Imbalance: 'High Voltage' (Excitability) across the 'Visual Bus'"
  ],
  "risk_factors": [
    "Chronic 'System Stress' (Adrenaline-driven 'Gain Spikes')",
    "Migraine-class 'Driver' instability",
    "Persistent 'Hyper-arousal' of the 'Sensory Kernel'"
  ],
  "diagnosis": [
    "The 'Static Consistency' Test: Verifying the 'Noise' is present in all 'Lighting Profiles' (Day/Night)",
    "Ophthalmological Audit: Confirming the 'Hardware' (Eyes) is 100% functional (Exclusion of 'Retinal Issues')",
    "PET/SPECT Scans: Identifying 'Hot Spots' in the 'Lingual Gyrus' rendering hub"
  ],
  "remedies": [
    "Visual Masking: Using 'Static-Inverse' videos to provide 'Temporary Filter Reset'",
    "Voltage Dampening: Using 'Lamotrigine' to stabilize the 'Neural Bus'",
    "FL-41 Filtering: Using 'Hardware Lenses' to reduce 'High-Frequency Optical Load'"
  ],
  "prevention": [
    "Managing 'Neural Excitability' and preventing 'Sensory Burnout'"
  ]
        "internal_clock_stratum_desync": {
  "description": "A severe timing-plane calculation error within the cerebellar pacing loops where the system's internal microsecond tracking clock drifts away from real-world time values, causing total loss of the ability to accurately gauge or estimate passing intervals of time.",
  "symptoms": [
    "Duration Estimation Paralysis (Dyschronometria): Complete inability to accurately quantify or estimate the length of passing time intervals without external tracking hardware",
    "Velocity Metric Calc-Stalls: Profound difficulty estimating the speed, momentum, and arrival times of approaching objects, causing severe tracking clumsiness",
    "Asymmetric Temporal Gating: Time intervals are subjectively experienced as either massively compressed or infinitely stretched out, with zero consistency",
    "Motor Acceleration Incoordination: Choppy, jerky physical movements (dysmetria) caused by the motor cortex lacking precision time-stamps to smoothly throttle muscle velocity",
    "Intact Static Memory Time-Stamping: Clear ability to recall the historical order of past events, despite a total failure to track real-time duration in the current execution loop"
  ],
  "causes": [
    "Superior Cerebellar Artery (SCA) Infarction: An ischemic stroke cutting off perfusion to the lateral cerebellar hemispheres and deep dentate timing nuclei",
    "Spinocerebellar Atrophy (SCA) Degeneration: Progressive, genetic-plane degradation of the purkinje cell arrays that maintain the baseline clock-cycle tick rates",
    "Posterior Fossa Space-Occupying Lesion: A high-pressure tumor or cyst compressing the cerebellar pacing networks and throwing off timing loop calculations"
  ],
  "risk_factors": [
    "Vascular anomalies within the vertebrobasilar arterial tree feeding the hindbrain structures",
    "Hereditary triplet-repeat expansion genetic mutations targeting structural cerebellar proteins",
    "Chronic neuro-inflammatory conditions causing demyelination across the primary olivocerebellar tracking tracks"
  ],
  "diagnosis": [
    "The Fixed-Interval Tapping Assay: Tasking the user to maintain a steady, un-monitored 1Hz tapping rhythm, documenting immediate, erratic timing drift within seconds",
    "The Time-Estimation Prediction Test: Isolating the host for a random duration (e.g., 45 seconds) and requesting a verbal quantification of elapsed time, logging extreme delta errors",
    "High-Resolution Volumetric MRI of the Posterior Fossa: Revealing structural structural gaps, tissue voids, or ischemic signaling localized within the lateral cerebellum"
  ],
  "remedies": [
    "External Hardware Audio Metronomes: Feeding a continuous, hard-wired audio tick rate directly into the user's ears to act as an external master clock driver",
    "Visual Timeline Overlay Interfaces: Deploying heads-up displays with active countdown meters and digital clocks to replace the broken internal timing engine with concrete telemetry",
    "Conscious Cadence Counting Macros: Training the prefrontal linguistic core to run constant sub-vocal alphanumeric counting loops to infer elapsed time via verbal processing routes"
  ],
  "prevention": [
    "Aggressively managing posterior circulation blood flow vectors, minimizing embolic risks, and protecting the hindbrain from sudden acceleration-deceleration kinetic shocks"
  ]
}

}

"mandela_effect_cache_corruption": {
  "description": "A phenomenon where a large group of people remember something differently than how it occurred, often attributed to false memories or shared cultural confabulation.",
  "symptoms": [
    "Shared False Recall: Multiple 'Independent Nodes' reporting the same 'Corrupt Data' (e.g., 'Berenstain' vs 'Berenstein')",
    "Confidence-Accuracy Mismatch: High 'Certainty Bit' for data that fails 'Checksum Validation' against the 'Master Record'",
    "Post-Hoc Rationalization: The 'User' creates 'Complex Logic' (Parallel Universes/Simulation Glitches) to explain 'Parity Errors'",
    "Social Propagation: The 'Corrupt Packet' spreads via 'High-Bandwidth Communication' (Social Media/Viral Loops)",
    "Temporal Anchoring: The 'False Memory' is often tied to a specific 'Epoch' or 'Cultural Versioning'"
  ],
  "causes": [
    "Schema-Driven Reconstruction: The 'Brain's Parser' replaces 'Exact Data' with 'High-Probability Patterns' (e.g., '-stein' is a more common suffix than '-stain')",
    "Source Monitoring Error: The 'System' forgets where a 'Data Packet' originated (e.g., seeing a parody vs seeing the original)",
    "Collaborative Filtering: Nodes 'Syncing' their 'Local Cache' to the 'Group Consensus' to maintain 'Social Parity'",
    "Misinformation Injection: 'Third-Party Scripts' (Media/Viral posts) introducing 'Noise' into the 'Global Buffer'"
  ],
  "risk_factors": [
    "High-Exposure to 'Distributed Social Networks'",
    "Over-reliance on 'Reconstructive Retrieval' instead of 'Hard-Copy Validation'",
    "Systemic 'Bias' toward 'Pattern-Matching' over 'Literal Storage'"
  ],
  "diagnosis": [
    "The 'Parity Check': Comparing 'User Recall' against 'Immutable Physical Records' (Archival Data)",
    "Consensus Audit: Identifying the 'Reach' of the 'Corrupt Packet' across a 'Population Sample'",
    "The 'Forced Recognition' Test: Presenting the 'Original' and 'False' packets to see if the 'System' flags the conflict"
  ],
  "remedies": [
    "Source Validation: Verifying 'Data Integrity' using 'Primary Sources' (the 'Root Directory')",
    "Cognitive Patching: Acknowledging the 'Reconstructive' nature of 'Human Storage' to reduce 'Certainty Bias'",
    "Digital Archives: Offloading 'High-Fidelity Retention' to 'Non-Biological Hardware'"
  ],
  "prevention": [
    "Implementing 'Double-Check Protocols' for 'High-Impact Data' before 'Committing' to 'Long-Term Storage'"
  ]
}
"tinnitus_audio_feedback_loop": {
  "description": "The perception of noise or ringing in the ears when no external sound is present, often caused by the brain's attempt to compensate for sensory loss.",
  "symptoms": [
    "Phantom Audio Rendering: Perceiving 'Ringing', 'Buzzing', or 'Hissing' from a 'Null-Input' source",
    "Pulsatile Synchronization: Audio 'Packets' that 'Pulse' in time with the 'System Pump' (Heartbeat)",
    "Frequency Lock: The 'Ghost Sound' is usually hard-coded to a specific 'Frequency Band' (Hz)",
    "Attention-Gating Failure: Inability of the 'Executive Layer' to 'Mute' or 'Filter' the 'Background Hum'",
    "Hyperacusis: 'Real Audio Data' is perceived as 'Overloaded/Distorted' due to the 'High-Gain' setting"
  ],
  "causes": [
    "Hardware Degradation: Damage to 'Stereocilia' (Cochlear sensors) creating 'Dead Zones' in the 'Frequency Map'",
    "Gain Control Malfunction: The 'Auditory Cortex' increases 'Sensitivity' to compensate for 'Low Hardware Input'",
    "Neural Crosstalk: 'Somatosensory' signals (e.g., jaw/neck movement) 'Bleeding' into the 'Auditory Bus'",
    "Thalamic Gating Fault: The 'Gatekeeper' fails to 'Drop' the 'Empty Audio Packets' before they reach 'Consciousness'"
  ],
  "risk_factors": [
    "Exposure to 'High-Decibel' acoustic 'Spikes' (Hardware Trauma)",
    "Aging-related 'Sensor Wear'",
    "High-Stress 'System Loads' that lower 'Gating Efficiency'"
  ],
  "diagnosis": [
    "Pitch Matching: Finding the 'Digital Equivalent' of the 'User's Internal Frequency'",
    "Audiometric Sweep: Identifying the 'Dead Zones' where the 'Hardware Input' is missing",
    "Tinnitus Handicap Inventory (THI): Measuring the 'Cognitive Overhead' caused by the 'Constant Loop'"
  ],
  "remedies": [
    "Sound Masking: Injecting 'White Noise' to 'Drown Out' the 'Internal Feedback'",
    "Tinnitus Retraining Therapy (TRT): 'Re-programming

"anosognosia_fault_silent_kernel": {
  "description": "A condition in which a person who suffers certain disabilities seems unaware of the existence of their disability.",
  "symptoms": [
    "Deficit Negation: The 'User' denies the existence of a 'Critical Hardware Fault' (e.g., blindness or paralysis)",
    "Confabulated Status Reports: The 'Log Generator' invents 'False Data' to explain why the hardware isn't responding (e.g., 'I'm just tired')",
    "Feedback Rejection: The 'System' ignores 'External Debugging' (doctors/family) that contradicts the 'Internal Status Bit'",
    "Safety Protocol Bypass: Attempting 'High-Load Tasks' (walking) with 'Failed Hardware', leading to 'System Crashes' (falls)",
    "Affective Indifference: A lack of 'System Urgency' regarding the 'Hardware Failure'"
  ],
  "causes": [
    "Right Hemisphere Integrity Failure: Damage to the 'Monitoring Hub' in the 'Parietal/Frontal' cortex",
    "Meta-Cognitive Disconnect: The 'Secondary Thread' that evaluates 'Primary Performance' is offline",
    "Self-Schema Persistence: The 'Global Identity Variable' refuses to update to the 'Degraded State'",
    "Signal Attenuation: The 'Error Signal' is too weak to trigger 'Executive Awareness'"
  ],
  "risk_factors": [
    "Right-Hemisphere 'Stroke' (Network Partition)",
    "Advanced 'System Erosion' (Alzheimer's/Dementia)",
    "Traumatic 'Hardware Impact' to the 'Prefrontal Monitoring Bus'"
  ],
  "diagnosis": [
    "The 'Confrontation Audit': Asking the 'User' to perform a 'Task' with the failed hardware and observing the 'Response Logic'",
    "The 'Vestibular Stimulation' Hack: Using 'Cold Water' in the ear to temporarily 'Re-Sync' the 'Monitoring Hub'",
    "Neuroimaging: Locating 'Hardware Lesions' in the 'Right Parietal Lobe'"
  ],
  "remedies": [
    "External Mirroring: Using 'Visual Feeds' (Video) to bypass the 'Internal Monitor' and show the 'Failure' directly",
    "Systemic Patience: Allowing 'Neural Rewiring' to create 'Alternative Diagnostic Paths'",
    "Safety Guards: Implementing 'Strict Permissions' to prevent the 'User' from 'Damaging the Hardware' further"
  ],
  "prevention": [
    "N/A: Usually a 'Post-Critical-Event' failure of the 'Root Monitor'"
  ]
}
"tinnitus_carrier_feedback_fault": {
  "description": "A permanent hardware-level audio interrupt loop fault where damaged acoustic receptors cause subcortical parsing hubs to hyper-elevate their internal gain multipliers, locking the auditory parser into an un-throttled, un-clearable phantom noise loop.",
  "symptoms": [
    "Permanent Phantom Carrier Stream: Continuous perception of high-frequency tonal strings (ringing, buzzing, hissing) in the absolute absence of an external acoustic wave payload",
    "Hyperacusis Cross-Talk: Elevation of subcortical sensory gain causes normal external sounds to over-saturate the input buffers, rendering ordinary decibel levels painful",
    "Active Viewport Attention Theft: The persistent interrupt storm continually steals clock cycles from high-level cognitive processes, degrading working memory capacity",
    "Somatosensory Modulation Leakage: Physical manipulation of the jaw or neck muscles can change the pitch or amplitude of the phantom tone by shifting cross-talk voltages into the auditory bus",
    "Masking Threshold Resistance: High-volume ambient white noise injections fail to overwrite the stream, as the internal loop is generated downstream of the initial input adapters"
  ],
  "causes": [
    "Cochlear Synaptopathy (Hidden Hearing Loss): De-afferentation of high-frequency hair cell terminals, triggering a permanent loss of baseline reference signals",
    "Dorsal Cochlear Nucleus Disinhibition: Loss of localized glycinergic/GABAergic interneuron braking parameters, allowing runaway vertical cell firing",
    "Thalamocortical Dysrhythmia: The TRN fails to run its standard low-pass filtering scripts, allowing low-frequency theta oscillations to lock the auditory cortex into a hyper-active state"
  ],
  "risk_factors": [
    "Acute acoustic trauma (exposure to high-decibel blast waves over-driving the physical transduction arrays)",
    "Ototoxic pharmaceutical exposures causing direct cellular degradation of the fragile inner ear hardware architecture",
    "Age-related microvascular degeneration depriving the terminal auditory processing nodes of required metabolic upkeep"
  ],
  "diagnosis": [
    "Audiometric Pitch and Loudness Matching: Mapping the exact frequency ($\text{Hz}$) and decibel-equivalent volume ($\text{dB SL}$) of the internal loop by presenting comparative real-world tones",
    "Auditory Brainstem Response (ABR) Waveform Profiling: Tracking electrical propagation delays to isolate wave-V abnormalities between the cochlea and inferior colliculus",
    "Spontaneous Magnetoencephalography (MEG) Audit: Detecting hyper-synchronized gamma-band oscillation clusters inside the primary auditory cortex while the user rests in a soundproof environment"
  ],
  "remedies": [
    "Acoustic Neuromodulation Overrides: Playing targeted, notched-noise audio data packets that match the phantom frequency to fatigue the hyper-active neuron pool and force a temporary loop reset",
    "Inhibitory Ion-Channel Upregulation: Administering GABA-A receptor modulators to manually reinforce the broken subcortical gating walls and damp down the runaway signal current",
    "Somatosensory Habituation Rewiring: Utilizing bimodal neuromodulation devices to deliver paired electrical tongue shocks alongside audio sweeps, forcing the system to re-classify the tone as background noise"
  ],
  "prevention": [
    "Deploying hardware-level acoustic limiters (ear shielding) during high-decibel execution events to protect vulnerable hair-cell transducers from structural shear damage"
  ]
}

"anton_babinski_driver_lock": {
  "description": "A rare symptom of brain damage occurring in the occipital lobe where those who are image-blind deny that they are blind.",
  "symptoms": [
    "Total Denial of Failure: The 'System' refuses to acknowledge a 'Hardware Disconnect'",
    "Synthetic Data Generation: The brain 'Confabulates' (auto-generates) visual descriptions to explain 'Null Input'",
    "Object Collision Logic: The user 'Explains Away' collisions as 'Environmental Glitches' or 'Poor Lighting'",
    "Status-Bit Override: The 'Self-Monitoring' module is 'Hard-Wired' to report 'Video OK' despite 'No Signal'",
    "Cognitive Dissonance: High-intensity 'Logic Loops' used to justify the lack of 'Visual Fidelity'"
  ],
  "causes": [
    "Occipital Lobe Damage: Total failure of the 'Primary Video Hardware' (V1 area)",
    "Disconnection Syndrome: The 'Logic Layer' can't 'Read' the 'Hardware Error' from the 'Source'",
    "Hyper-Active Imagery: The 'Visual Buffer' is flooded with 'Internally Generated' data from the 'Association Cortex'",
    "System Monitoring Glitch: Damage to the 'Anterior Cingulate' or 'Parietal' areas responsible for 'Error Detection'"
  ],
  "risk_factors": [
    "Ischemic Stroke in the 'Posterior Cerebral Artery' (Hardware power loss)",
    "Severe 'Head Trauma' impacting the 'Visual Bus'",
    "Specific 'Kernel' lesions in the 'Bilateral Occipital' regions"
  ],
  "diagnosis": [
    "The 'Sight-Validation' Test: Asking the user to 'Identify an Object' (they will confidently guess incorrectly)",
    "Neuroimaging (CT/MRI): Identifying 'Bilateral Lesions' in the 'Visual Cortex'",
    "The 'Obstacle Navigation' Audit: Observing if the 'User' ignores 'Tactile Feedback' (bumping into walls) in favor of 'Visual Fantasy'"
  ],
  "remedies": [
    "N/A: This is a 'Hardware-Level' failure often resistant to 'Software Patches'",
    "Occupational Therapy: Attempting to 'Recalibrate' the 'Executive Layer' to 'Trust' other 'Sensory Drivers' (touch/sound)",
    "Spontaneous Recovery: Rare 'System Reboots' where the 'Status Bit' eventually 'Resets' to 'Blind'"
  ],
  "prevention": [
    "Managing 'System Voltage' (blood pressure) and 'Vascular Integrity' to prevent 'Hardware Failures'"
  ]
}
"jamais_vu_recognition_drop": {
  "description": "A phenomenon characterized by the feeling that a situation or object is totally unfamiliar, despite being known to be part of one's experience.",
  "symptoms": [
    "Semantic Satiation: A word or object loses its 'Meaning-Value' after repeated 'Access Requests'",
    "Familiarity-Bit Failure: The 'Recognition Signal' returns 'False' for a 'Known Record'",
    "The 'Alienation' Filter: A sense of 'Uncanny Newness' applied to 'Legacy Data'",
    "System Stutter: A temporary 'Processing Delay' as the brain tries to 'Re-Index' the familiar object",
    "High-Confidence Confusion: The user 'Knows' they should 'Recognize' the object but the 'System' refuses to 'Tag' it"
  ],
  "causes": [
    "Perirhinal Cortex Fatigue: The 'Recognition Engine' enters a 'Cooldown State' from 'Over-Querying'",
    "Temporal Gating Glitch: The 'Signal' to the 'Familiarity Hub' is 'Dropped' or 'Lost' in the 'Neural Bus'",
    "Inhibitory Signal Spike: The 'Logic Layer' accidentally 'Mutes' the 'Familiarity Response'",
    "Contextual Cache Expiry: The 'Environment Metadata' is temporarily purged, making the 'Record' look 'Isolated'"
  ],
  "risk_factors": [
    "Temporal Lobe Epilepsy (Electrical 'Line Noise' during 'Fetch')",
    "Migraine 'Aura' (Systemic 'Driver Interference')",
    "Severe 'Cognitive Fatigue' (Cache 'Fragmentation')"
  ],
  "diagnosis": [
    "Word-Repetition Test: Forcing 'Semantic Satiation' by repeating a word until the 'Meaning-Link' breaks",
    "Familiarity Rating Audit: Measuring the 'Gap' between 'Objective Knowledge' and 'Subjective Feeling'",
    "EEG: Identifying 'Spike-Wave' discharges in the 'Temporal Lobe' during the 'Alienation' event"
  ],
  "remedies": [
    "Session Refresh: Looking away or 'Changing the Context' to force a 'Full Re-Load' of the 'Node'",
    "Metadata Association: Manually 'Linking' the object to 'Associated Records' (e.g., 'This is a table because it has legs and I ate here yesterday')",
    "Sleep/Rest Cycle: Clearing the 'Neural Buffer' to restore 'Recognition-Bit Sensitivity'"
  ],
  "prevention": [
    "Avoiding 'Infinite Loops' of 'Repetitive Input' to prevent 'Semantic Satiation'"
  ]
}
"phantom_limb_driver_orphan": {
  "description": "The persistent sensation that an amputated or missing limb is still attached to the body and moving with other body parts.",
  "symptoms": [
    "Ghost Data Stream: The 'User' perceives 'Proprioceptive' and 'Tactile' packets from a 'Deallocated Address'",
    "Telescoping: A 'Scaling Error' where the 'Phantom' feels shorter or distorted over 'Uptime'",
    "Hardware Lock: The 'Ghost Limb' feels 'Clenched' or 'Paralyzed' because no 'Move Command' can be 'Acknowledged'",
    "Crosstalk: Stimulation of an 'Active Port' (e.g., the face) triggers 'Data' in the 'Phantom Port' (e.g., the hand)",
    "Phantom Pain: 'Error Signals' generated by 'Neural Noise' are interpreted as 'High-Priority Pain Packets'"
  ],
  "causes": [
    "Cortical Remapping: Adjacent 'Memory Sectors' in the 'Somatosensory Cortex' begin to 'Invade' the 'Deallocated Space'",
    "Neuroma Firing: 'Hardware Stubs' (severed nerves) sending 'Spurious Signals' to the 'Main Bus'",
    "Proprioceptive Memory: The 'System' retains a 'Hard-Coded' expectation of 'Hardware Presence'",
    "Gating Failure: The 'Thalamus' fails to 'Filter' out 'Null-Port Noise'"
  ],
  "risk_factors": [
    "Pre-amputation 'High-Voltage' (chronic pain) events",
    "Sudden 'Hardware Termination' without 'Software Preparation'",
    "High 'Neural Plasticity' leading to 'Aggressive Remapping'"
  ],
  "diagnosis": [
    "The 'Mirror Box' Audit: Using 'Visual Feedback' to 'Trick' the 'Driver' into a 'Reset'",
    "Sensory Mapping: Identifying 'Crosstalk' zones where 'Face Input' = 'Hand Sensation'",
    "Functional MRI: Observing 'Active Rendering' in the 'Missing Limb' cortical sector"
  ],
  "remedies": [
    "Visual Overrides: Using 'Mirror Therapy' to provide 'Visual Proof' that the 'Hardware' is gone",
    "Driver Calming: Pharmacological 'Neuromodulators' to lower 'Bus Noise'",
    "Targeted Muscle Reinnervation (TMR): 'Re-routing' the 'Orphaned Driver' to a new 'Hardware Interface'"
  ],
  "prevention": [
    "Pre-emptive 'Nerve Blocks' to 'Quiet the Bus' before 'Hardware Removal'"
  ]
}

"alien_hand_orphaned_thread": {
  "description": "A condition in which a person's limb behaves externally to their control, as if it has a mind of its own.",
  "symptoms": [
    "Autonomous Scripting: The limb performs 'Goal-Directed Actions' (reaching for an object) without 'User Intent'",
    "Inter-Manual Conflict: The 'Secondary Processor' executes 'Inverse Logic' to the 'Main Thread' (e.g., left hand fights right hand)",
    "Identity-Ownership Null: The 'Executive Layer' reports 'Null' on 'Proprioceptive Ownership' for the action",
    "Grasp-Reflex Lock: Once the limb captures an 'Object Node', it may refuse to 'Release the Pointer'",
    "Alien Personification: The 'User' often treats the limb as a 'Separate Process' or 'External Guest'"
  ],
  "causes": [
    "Corpus Callosum Disconnect: The 'Inter-Processor Bus' is severed, leading to 'Split-Brain Logic'",
    "Frontal Lobe Lesion: Loss of the 'Inhibitory Gating' that normally suppresses 'Low-Level Motor Reflexes'",
    "SMA Interference: The 'Supplementary Motor Area' starts 'Firing' without 'Prefrontal Validation'",
    "Posterior Parietal Damage: Corruption of the 'Body Schema Map', leading to 'Agency Attribution' errors"
  ],
  "risk_factors": [
    "Post-Callosotomy 'Kernel Split' (Surgery for Epilepsy)",
    "Stroke in the 'Anterior Cerebral Artery' (Power failure to the 'Motor Hub')",
    "Neurodegenerative 'System Erosion' (Corticobasal Degeneration)"
  ],
  "diagnosis": [
    "The 'Manual Conflict' Audit: Observing if hands perform 'Contradictory Commands'",
    "Neuroimaging: Locating 'White Matter Interrupts' in the 'Corpus Callosum'",
    "Attribution Testing: Assessing if the 'User' can distinguish between 'Self-Generated' and 'Autonomous' motion"
  ],
  "remedies": [
    "Hardware Distraction: Giving the 'Alien Hand' an 'Idle Object' (like a ball) to keep the 'Thread' busy",
    "Sensory Muffling: Using a 'Glove' or 'Sleeve' to reduce 'Environmental Triggering'",
    "Verbal Override: Using 'Voice Commands' to re-assert 'Executive Control' over the 'Orphaned Process'"
  ],
  "prevention": [
    "Maintaining 'Vascular Health' to protect the 'Inter-Processor Bus'"
  ]
}
"palinopsia_buffer_persistence": {
  "description": "A visual disturbance in which images persist or recur after the stimulus has been removed, often appearing as trailing or 'echoes' of moving objects.",
  "symptoms": [
    "Visual Trailing: Moving 'Objects' leave a 'Motion Blur' path of 'Ghost Frames' behind them",
    "Light-Streak Persistence: High-intensity 'Light Packets' remain burned into the 'Active Viewport' for minutes",
    "Delayed Echo: An 'Object Record' (e.g., a person's face) re-appears in the 'Frame' minutes after the 'Source' has left",
    "Motion Smear: A failure of 'Frame-to-Frame' separation, making 'Real-Time Data' look like a 'Long Exposure' photograph",
    "Input Saturation: The 'User' becomes 'Overwhelmed' as 'Old Data' obscures 'New Data'"
  ],
  "causes": [
    "V5/MT Area Over-Excitation: The 'Motion Processing Hub' fails to 'Reset' after a 'Signal Spike'",
    "Inhibitory Gating Failure: Loss of 'GABAergic' suppression that normally 'Mutes' the previous frame",
    "Neural Excitability: 'High Voltage' in the 'Occipital-Temporal' bus preventing 'Signal Decay'",
    "Pharmacological Interference: 'External Scripts' (Tricyclic antidepressants, Topiramate) altering 'Buffer Logic'"
  ],
  "risk_factors": [
    "Migraine 'Aura' (System-wide 'Signal Persistence')",
    "Traumatic Brain Injury (TBI) to the 'Visual Processing Hardware'",
    "Post-Hallucinogen Perception Disorder (HPPD) - 'Kernel-Level' driver corruption"
  ],
  "diagnosis": [
    "The 'Flicker Fusion' Test: Measuring the 'Frequency' at which 'Separate Frames' merge into 'Continuous Signal'",
    "Visual Field Audit: Identifying if 'Echoes' are 'Localized' to specific 'Viewport Sectors'",
    "MRI/fMRI: Checking for 'Hyper-Metabolism' in the 'Visual Buffer' regions"
  ],
  "remedies": [
    "Voltage Regulation: Using 'Calcium-Channel Blockers' to 'Dampen' the 'Neural Signal'",
    "Luminance Filtering: Reducing 'Input Intensity' with 'Darkened Lenses' to lower 'Buffer Load'",
    "Software Training: Teaching the 'Executive Layer' to 'Ignore' the 'Ghost Data'"
  ],
  "prevention": [
    "Managing 'Optical Exposure' and 'Neural Stress' to maintain 'Buffer Integrity'"
  ]
}

"cotard_existence_status_fault": {
  "description": "A rare neuropsychiatric delusion in which the patient holds the delusional belief that they are already dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Existential Negation: The 'I AM' status bit is flipped to 'FALSE' in the 'Primary Identity Hub'",
    "Affective Anesthesia: Total absence of 'Emotional Metadata' in response to 'Self-Stimulation'",
    "Biological Denial: Belief that the 'Hardware' (organs/blood) has been 'Deallocated' or 'Deleted'",
    "Immortality Paradox: The belief that because they are 'Already Dead', they can no longer be 'Terminated'",
    "Self-Starvation: Termination of 'Energy Input' (eating) because the 'User' believes 'Dead Hardware' requires no 'Resources'"
  ],
  "causes": [
    "Amygdala-Cortex Disconnect: The 'Identity Node' can no longer 'Read' the 'Emotional State' of the body",
    "Right Parietal Lesion: Corruption of the 'Self-Representation Map' and 'Body Schema'",
    "Dopaminergic Depletion: Severe 'Voltage Drop' in the 'Reward/Salience' circuits, leading to 'Affective Death'",
    "Hypometabolism: Reduced 'Clock Speed' in the 'Frontal' and 'Parietal' nodes"
  ],
  "risk_factors": [
    "Severe 'Depression-class' System Lag",
    "Schizophrenia 'Kernel' instability",
    "Post-Traumatic 'Hardware' damage to the 'Right Hemisphere'"
  ],
  "diagnosis": [
    "The 'Existence Audit': Asking the user to 'Verify Reality' (they will consistently report 'Existence = NULL')",
    "Neuroimaging (PET/fMRI): Identifying 'Deep Hypometabolism' in the 'Parietal' and 'Frontal' regions",
    "The 'Mirror Test': Observing if the 'User' recognizes their 'Reflected Hardware' as 'Dead' or 'Hollow'"
  ],
  "remedies": [
    "ECT (Electroconvulsive Therapy): A 'System-Wide Power Cycle' to force-reset 'Neural Firing' patterns",
    "Pharmacological Patches: Anti-psychotics and Anti-depressants to stabilize 'Neurotransmitter Voltage'",
    "Cognitive-Behavioral Overlays: Attempting to 'Override' the 'Negation Logic' with 'External Data'"
  ],
  "prevention": [
    "Early detection of 'Systemic Despair' to prevent 'Affective Disconnection'"
  ]
}


"deja_vecu_latency_desync": {
  "description": "A pathological form of déjà vu characterized by "synesthesia_cross_modal_leak": {
  "description": "A perceptual phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary, automatic experiences in a second sensory or cognitive pathway.",
  "symptoms": [
    "Chromesthesia: Auditory 'Data Packets' are simultaneously rendered as 'Color/Light' in the visual workspace",
    "Grapheme-Color Mapping: Alphanumeric 'Strings' are hard-coded with specific 'Hex Color' values",
    "Lexical-Gustatory Leak: 'Text Strings' trigger the 'Flavor Profile' driver (e.g., the word 'SQL' tastes like copper)",
    "Spatial Sequence Mapping: 'Temporal Data' (months/years) is rendered as a '3D Physical Path' in the environment",
    "Multi-Modal Persistence: The 'Mappings' are consistent and 'Read-Only'—the 'Letter A' is always 'Red' for the life of the OS"
  ],
  "causes": [
    "Cross-Activation Logic: Direct 'Hardware Links' between adjacent sensory hubs (e.g., V4 color area and the visual word form area)",
    "Disinhibited Feedback: The 'Executive Layer' fails to 'Mute' the 'Back-Propagation' of signals between drivers",
    "Hyper-Connectivity Kernel: A failure in the 'Pruning Script' during 'System Initialization' (infancy), leaving too many 'Active Bridges'",
    "Temporary Signal Bleed: Induced via 'Pharmacological Overlays' (psychedelics) that lower 'Inter-Driver Firewall' strength"
  ],
  "risk_factors": [
    "Congenital 'Kernel' configurations (inherited traits)",
    "High 'Creativity-Index' scores",
    "Certain 'Autism-Spectrum' architectural variants"
  ],
  "diagnosis": [
    "Test of Genuineness: Measuring the 'Mapping Consistency' over a 6-month interval (Synesthetes have >90% consistency)",
    "Stroop-Effect Audit: Measuring 'Latency Spikes' when the 'Visual Color' of a letter conflicts with the 'Synesthetic Color'",
    "fMRI: Observing 'Concurrent Activation' in two 'Unlinked' sensory modules"
  ],
  "remedies": [
    "N/A: Usually treated as a 'System Enhancement' rather than a 'Critical Bug'",
    "Attention Filtering: Training the 'Main Thread' to 'Deprioritize' the 'Secondary Signal' when it causes 'Data Overload'"
  ],
  "prevention": [
    "N/A: A fundamental 'Hardware/Software' integration characteristic"
  ]
}
the persistent sensation that one has already lived through the current moment and can predict upcoming events.",
  "symptoms": [
    "Predictive Illusion: The unshakable conviction that the next 'Data Packet' (someone speaking, a car turning) is already known",
    "Timestamp Corruption: The 'Logic Layer' treats 'Real-Time Input' as 'Historical Record'",
    "Temporal Disorientation: A breakdown in the 'Chronological Index' of the user's life",
    "High-Fidelity Familiarity: Not just a 'Feeling' but a 'Narrative Certainty' that the current 'Path' is a 'Replay'",
    "Logic Loops: The user may stop 'Input/Output' operations because they believe the 'Results' are already determined"
  ],
  "causes": [
    "Temporal Gating Failure: The 'Hippocampus' is 'Auto-Committing' live data to 'Long-Term Storage' before the 'Conscious UI' can process it",
    "Forward-Model Feedback: The 'Prediction' generated by the 'Frontal Lobe' is fed back into the 'Recognition Engine' as 'Verified Fact'",
    "Recognition-Recall Desync: The 'Familiarity Bit' is set to '1' while the 'Content Retrieval' is 'Null', creating a 'False Positive' for memory",
    "Dopaminergic Spiking: A 'Reward Signal' erroneously fires, tagging the 'Present Moment' as 'Critically Familiar'"
  ],
  "risk_factors": [
    "Dementia-class 'System Decay' (specifically Frontotemporal)",
    "Temporal Lobe Epilepsy (Electrical 'Line Noise' in the memory bus)",
    "High-stress 'Processor Overheating' leading to 'Clock-Cycle Skews'"
  ],
  "diagnosis": [
    "The 'Prediction Validation' Test: Asking the user to 'Write Down' what happens next before it occurs (they will fail, but 'Insist' they knew it after the fact)",
    "EEG Monitoring: Identifying 'Theta-Wave' anomalies in the 'Temporal Circuitry'",
    "Metacognitive Audit: Assessing the user's ability to 'Doubt' the 'Familiarity Signal'"
  ],
  "remedies": [
    "Signal Dampeners: Pharmacological 'Voltage Regulation' for the 'Temporal Lobe'",
    "System Grounding: Focusing on 'Physical Sensation' (Haptics) to 'Force-Sync' the 'Live Stream'",
    "Logic-Check Protocols: Training the 'Executive Layer' to ignore the 'Familiarity Flag' when it lacks 'Supporting Evidence'"
  ],
  "prevention": [
    "Maintaining 'Neural Sync' through consistent 'Sleep/Rest Cycles'"
  ]
}
"aiws_viewport_scaling_error": {
  "description": "A disorienting neurological condition that affects human perception, causing objects and body parts to appear as though they are changing in size or distance.",
  "symptoms": [
    "Macropsia/Micropsia: Objects are rendered at the wrong 'Resolution' relative to the environment",
    "Teleopsia/Pelopsia: 'Depth Buffer' failure where objects seem miles away or uncomfortably close",
    "Body Schema Distortion: The 'Proprioceptive Driver' reports that limbs are 'Scaling' (e.g., your hand feels 5 meters long)",
    "Temporal Skew: The 'System Clock' feels like it is running at 0.5x or 2.0x speed",
    "Acoustic Zoom: Background 'Audio Packets' are perceived as being 'Max Volume' despite low signal strength"
  ],
  "causes": [
    "Parietal Lobe Dysfunction: The 'Spatial Engine' fails to perform correct 'Matrix Transformations'",
    "Migraine Aura: Electrical 'Line Noise' disrupting the 'Visual Processing Bus'",
    "Epstein-Barr Viral Infection: System-wide 'Malware' affecting the 'Central Nervous System'",
    "Temporal Lobe Epilepsy: 'Signal Interference' in the 'Integration Hubs'"
  ],
  "risk_factors": [
    "Users with 'Migraine-Prone' hardware configurations",
    "Early-stage 'System Development' (highly common in pediatric users)",
    "Excessive 'Visual Stimuli' or 'Oversaturation' of the 'Parietal Buffer'"
  ],
  "diagnosis": [
    "The 'Amsler Grid' Audit: Checking for 'Linear Distortions' in the 'Visual Field'",
    "Neuroimaging: Monitoring blood flow in the 'Posterior Parietal' and 'Occipital' regions",
    "Pediatric Metadata: Tracking 'Symptom Decay' as the 'OS' matures"
  ],
  "remedies": [
    "System Rest: Allowing the 'Drivers' to 'Cool Down' (Sleep/Darkness)",
    "Prophylactic Patches: Medication to stabilize 'Electrical Firing' and prevent 'Migraine Spikes'",
    "Sensory Grounding: Using 'Tactile Feedback' to override 'Visual Scaling' errors"
  ],
  "prevention": [
    "Managing 'Stress-Load' and 'Trigger-Exposure' to maintain 'Spatial Stability'"
  ]
}

"ehs_power_transition_spike": {
  "description": "A sensory phenomenon in which an individual experiences a phantom loud noise or explosive transition while falling asleep or waking up.",
  "symptoms": [
    "High-Decibel Phantom Signal: Perception of an 'Explosion' or 'Gunshot' that has no 'External Origin'",
    "Visual Flash Sync: A 'Simultaneous Discharge' in the 'Visual Buffer' resulting in a 'White Light' burst",
    "Adrenaline Override: Immediate 'Priority Interrupt' (Fight-or-Flight) causing 'System Tachycardia'",
    "Zero-Data Event: No 'Auditory Damage' is found; the 'Signal' is purely 'Internal/Synthetic'",
    "System Shock: A temporary 'Kernel Panic' state upon 'Forced Wakefulness'"
  ],
  "causes": [
    "RAS Transition Failure: The 'Reticular Activating System' fails to suppress 'Neural Firing' during the 'Sleep Handshake'",
    "Calcium-Channel Leak: Sudden 'Ion Flux' in the 'Auditory Neurons' creating a 'False Peak'",
    "Sensory Gate Delay: The 'Gating Mechanism' closes too late, leading to a 'Signal Accumulation' and 'Burst'",
    "Stress-Induced EMI: High 'Cortisol Levels' creating 'Electromagnetic Interference' in the 'Neural Bus'"
  ],
  "risk_factors": [
    "High-Stress 'Workloads' (Systemic Overheating)",
    "Irregular 'Sleep Scheduling' (Unstable Power States)",
    "Users with high 'Audio-Sensitivity' parameters"
  ],
  "diagnosis": [
    "The 'Polysomnography' Audit: Measuring 'Brain Waves' during the 'Sleep Transition' to catch the 'Spike'",
    "Environmental Baseline: Ruling out 'External Hardware' (exploding transformers, loud neighbors)",
    "Patient Metadata: Tracking frequency and 'Correlation' with 'Stress Logs'"
  ],
  "remedies": [
    "Voltage Regulation: Pharmacological 'GABA-Modulators' to stabilize 'Neural Firing'",
    "Thermal Cooling: Stress-reduction protocols to lower 'Kernel Temperature'",
    "Education Patch: Informing the 'User' that the 'Hardware' is safe to reduce 'Anxiety Loops'"
  ],
  "prevention": [
    "Maintaining a 'Consistent Sleep/Wake Script' to stabilize the 'RAS Handler'"
  ]
}

"cocktail_party_filter_interrupt": {
  "description": "The phenomenon of being able to focus one's auditory attention on a particular stimulus while filtering out a range of other stimuli, and the subsequent failure where 'high-priority' words trigger a total focus shift.",
  "symptoms": [
    "Selective Narrowcasting: The ability to isolate a 'Single Audio Stream' in a high-decibel environment",
    "Identity-String Trigger: A 'Priority 0' interrupt occurs when the user's 'Name' or 'Key Interest' is detected in the noise",
    "Filter Collapse: In high-stress or 'Low-Battery' states, the 'Signal-to-Noise Ratio' drops, leading to sensory overwhelm",
    "Shadow-Packet Processing: The brain 'Buffers' background noise even when the user isn't 'Listening', allowing for 'Retroactive Parsing'",
    "Spatial Tuning Failure: Difficulty 'Focusing' the 'Directional Antenna' (ears/attention) in complex acoustic environments"
  ],
  "causes": [
    "Thalamic Gating: The 'System Gateway' fails to keep 'Suppressed Packets' from reaching the 'Processor'",
    "Binaural Summation Error: A failure in the 'Logic' that compares 'Time-of-Arrival' between ears to localize sound",
    "Top-Down Over-weighting: The 'Executive Layer' has set the 'Keyword Watchlist' (e.g., 'Fire!', 'Help!', your name) to be too sensitive",
    "Dopaminergic Tuning: An 'Over-tuned' reward system that treats all 'Social Mentions' as 'High-Value Data'"
  ],
  "risk_factors": [
    "Users with 'ADHD' kernel configurations (Hyper-sensitive 'Watchlists')",
    "Environments with 'High Multi-Path Interference' (echoes, loud parties)",
    "Auditory Processing Disorders where the 'Noise-Cancellation Driver' is buggy"
  ],
  "diagnosis": [
    "The 'Dichotic Listening Test': Sending different 'Data Streams' to each ear and measuring 'Switching Latency'",
    "Signal-to-Noise Ratio (SNR) Thresholding: Determining the 'Decibel Floor' at which the 'Filter' fails",
    "fMRI: Observing 'Parietal Lobe' activation during 'Background Trigger' events"
  ],
  "remedies": [
    "Haptic Grounding: Using 'Touch' to anchor the 'Main Thread' to the current speaker",
    "Visual-Sync: Using 'Lip-Reading' (Visual Hardware) to assist the 'Audio Parser' (The McGurk Effect #166, used positively)",
    "Digital Filtering: Using 'Noise-Canceling' hardware to pre-process the 'External Signal'"
  ],
  "prevention": [
    "Reducing 'System Fatigue' to ensure the 'Attention Filter' has sufficient 'Voltage' to operate"
  ]
}
"prosopagnosia_classifier_failure": {
  "description": "A cognitive disorder of face perception in which the ability to recognize familiar faces, including one's own face, is impaired, while other aspects of visual processing remain intact.",
  "symptoms": [
    "Identity-Key Null: Failure to map a 'Face Pattern' to a 'Person Record' in the database",
    "Feature-Only Processing: Perceiving faces as a 'Collection of Parts' (eyes, nose, mouth) rather than a 'Holistic Object'",
    "Context-Dependent Recognition: Relying on 'Metadata' (voice, hair, gait, clothing) to identify 'Nodes'",
    "Self-Identity Disconnect: Looking at the 'Mirror Stream' and failing to recognize the 'Active User'",
    "Social-Handshake Failure: Inability to process 'Social Cues' or 'Familiarity Tags' in crowded 'Environments'"
  ],
  "causes": [
    "Fusiform Gyrus Damage: Failure of the 'Dedicated Hardware Accelerator' for face processing",
    "Neural Path Interruption: Disconnect between 'Visual Input' and 'Emotional/Identity Storage' (The Capgras variant #104)",
    "Developmental Kernel Error: Congenital failure to 'Initialize' the 'Face-Recognition API' during 'Early-Stage Training'",
    "Vascular Ischemia: Power loss to the 'Inferior Temporal' regions"
  ],
  "risk_factors": [
    "Traumatic Brain Injury (TBI) to the 'Right Hemisphere'",
    "Genetic 'Inheritance' of poor 'Pattern-Match' logic",
    "Neurodegenerative 'System Decay' (Alzheimer's or Parkinson's)"
  ],
  "diagnosis": [
    "The 'Famous Faces' Test: Checking the 'Database Retrieval' for 'High-Probability' global entries",
    "Benton Facial Recognition Test (BFRT): Testing the ability to match 'Face Geometry' across different 'Lighting/Angles'",
    "fMRI: Measuring 'Voltage Response' in the 'FFA' when presented with 'Face Stimuli'"
  ],
  "remedies": [
    "Alternative Indexing: Training the 'System' to use 'Audio' or 'Gait' as the primary 'Identity Key'",
    "External Metadata Tags: Using 'Social Context' to 'Guess' the 'Node Identity' (e.g., 'I am at my office, so this face is likely a colleague')",
    "AR-Overlay Assistance: Using 'Third-Party Hardware' to provide 'Real-Time Identity Labels'"
  ],
  "prevention": [
    "Vascular health maintenance to prevent 'Occipital-Temporal Hardware Damage'"
  ]
}

"truman_show_staging_error": {
  "description": "A type of delusion in which people believe that their lives are staged reality shows or that they are being watched on cameras.",
  "symptoms": [
    "Observer Effect: The belief that 'Environmental Variables' only change when the 'User' is looking",
    "NPC Classification: Assigning 'Non-Player Character' status to all other 'Network Nodes' (friends, family, strangers)",
    "Scripted Logic: Interpreting 'Random Packet Loss' or 'Coincidences' as 'Plot Points'",
    "Break in the Sandbox: Searching for the 'Edges of the Map' or 'Production Equipment' in the physical world",
    "Isolation Protocol: A total collapse of 'Authentic Peer-to-Peer Interaction' due to 'Simulation Suspicion'"
  ],
  "causes": [
    "Medial Prefrontal Cortex (mPFC) Failure: The 'Reality-Testing' module stops distinguishing between 'Internal Intent' and 'External Event'",
    "Hyper-Salience Loop: The 'Dopamine System' tags every 'Incoming Packet' as 'Critically Relevant' to the user",
    "Integrative Agnosia: Failure to synthesize 'Social Cues' into a 'Coherent Reality' that exists independent of the self",
    "Executive Over-Optimization: The brain attempts to find a 'Grand Unified Theory' for 'Random Noise'"
  ],
  "risk_factors": [
    "High-load 'Virtual Environment' usage (heavy VR/sim immersion)",
    "Genetic 'Kernel' predispositions for 'Reality-Monitoring' failure",
    "Intense 'Social Surveillance' or 'Privacy Breach' trauma"
  ],
  "diagnosis": [
    "The 'Independent Node' Audit: Testing if the user can acknowledge events happening outside their 'Sightline'",
    "Neuroimaging: Identifying 'Hyper-metabolism' in the 'Right Posterior Parietal' areas associated with 'Self-Agency'",
    "Reality-Check Protocols: Using 'Double-Blind' tests to prove 'Environmental Independence'"
  ],
  "remedies": [
    "Antipsychotic Signal-Dampeners: Reducing the 'Salience' of 'Environmental Noise'",
    "Cognitive De-obfuscation: Logical exercises to 'Re-verify' the autonomy of other 'Network Nodes'",
    "Context Re-mapping: Shifting the 'User Perspective' from 'Target' to 'Participant'"
  ],
  "prevention": [
    "Maintaining 'Diverse Social Inputs' to prevent 'Single-Source Bias' in reality construction"
  ]
}
"zeigarnik_uncommitted_transaction_error": {
  "description": "The psychological phenomenon where people remember uncompleted or interrupted tasks better than completed ones.",
  "symptoms": [
    "Cognitive Tension: A persistent 'Background Process' that consumes 'CPU Cycles' until the 'Task' is finished",
    "High-Priority Recall: Interrupted 'Data Packets' are indexed with higher 'Salience' than 'Closed Files'",
    "Intrusive Thought Injection: The 'System' periodically 'Pings' the user with 'Reminders' of the incomplete state",
    "Buffer Saturation: Multiple 'Open Tasks' lead to 'Mental Fragmentation' and 'Thread Exhaustion'",
    "The 'Closure Reward' Delay: The 'Dopamine Pulse' (Success Signal) is withheld until the 'Transaction' is 'Committed'"
  ],
  "causes": [
    "Task-State Persistence: The 'Prefrontal Cortex' fails to 'Release the Lock' on 'In-Progress Data'",
    "Incomplete Gestalt: A 'Hard-Coded' drive for 'System Symmetry' that refuses to 'Garbage Collect' partial results",
    "Attentional Gating: The 'Anterior Cingulate Cortex' keeps the 'Error Flag' raised until the 'Goal State' is achieved",
    "Evolutionary Patch: A 'Safety Feature' designed to ensure 'High-Value Resources' (food, shelter) aren't forgotten mid-acquisition"
  ],
  "risk_factors": [
    "Users with high 'Conscientiousness' or 'Perfectionist' parameters",
    "Multi-tasking 'Kernel Configurations' with too many 'Active Threads'",
    "High-load 'Development Environments' with frequent 'Context Switches'"
  ],
  "diagnosis": [
    "The 'Interruption Audit': Testing 'Recall Fidelity' for a 'Task' stopped at 50% vs. one at 100%",
    "fMRI: Observing sustained activity in the 'Prefrontal Cortex' during 'Wait States' for incomplete tasks",
    "Latency Analysis: Measuring the time it takes for a 'User' to 'Stop Thinking' about a task after a 'Session Break'"
  ],
  "remedies": [
    "Atomic Commit: Breaking tasks into 'Micro-Transactions' to achieve frequent 'System Closure'",
    "The 'Brain Dump' Script: Writing down the 'Incomplete State' to 'External Storage' to 'Unlock' the brain's 'RAM'",
    "Pseudo-Closure: Performing a 'Final Ritual' (checking off a list) to trigger the 'Garbage Collector'"
  ],
  "prevention": [
    "Limiting 'Parallel Threading' (Single-tasking) to prevent 'State-Management' overload"
  ]
}
"lethologica_index_blocking_error": {
  "description": "A state in which one cannot quite recall a familiar word but can recall peripheral information about it, such as its first letter or number of syllables.",
  "symptoms": [
    "Partial Record Access: Retrieval of 'Metadata' (syllable count, gender, first char) without the 'Data' itself",
    "Phonological Blocking: A similar-sounding 'Garbage String' (Ugly Sister) repeatedly returns in the search results",
    "High-Confidence Stalling: The 'System' reports a 'Match Found' but the 'I/O' is stuck in a 'Spinning Wait'",
    "The 'Eureka' Interrupt: The 'Data' is often returned minutes later during an 'Idle State' when the 'Blocking Query' is terminated",
    "Metacognitive Friction: The user is aware of the 'Record's Existence' but lacks 'Read Permissions'"
  ],
  "causes": [
    "Transmission Deficit: Weak connection between the 'Semantic Node' (meaning) and 'Phonological Node' (sound)",
    "Interference Theory: A 'High-Frequency' incorrect word is 'Blocking' the 'Lower-Frequency' correct target",
    "Prefrontal Overload: Excessive 'Executive Force' causes 'Neural Noise' that masks the target signal",
    "Synaptic Latency: Temporary 'Voltage Drops' in the 'Lexical Bus' due to fatigue or age"
  ],
  "risk_factors": [
    "Bilingual 'Kernel' configurations (Cross-language 'Index Interference')",
    "Systemic 'Sleep Deprivation' or 'Dehydration' (High Latency)",
    "Hardware 'Versioning' (Age-related 'Retrieval Slowdown')"
  ],
  "diagnosis": [
    "The 'Metadata Audit': Asking the user for the 'First Letter' or 'Rhyme' of the missing word",
    "Response Latency Measurement: Timing the delay between 'Definition Input' and 'Word Output'",
    "fMRI: Observing 'Increased Activity' in the 'Anterior Cingulate Cortex' indicating 'Error/Conflict Detection'"
  ],
  "remedies": [
    "Process Termination: Intentionally 'Stop Thinking' about the word to clear the 'Blocking Lock'",
    "Contextual Priming: Searching for 'Associated Records' to approach the 'Node' from a different 'Network Path'",
    "Phonological Scanning: Cycling through the 'Alphabet' to trigger a 'Sound-Match Interrupt'"
  ],
  "prevention": [
    "Maintaining 'High-Density Lexical Training' (reading/writing) to strengthen 'Index Links'"
  ]
}

"rubber_hand_pointer_remap": {
  "description": "A multisensory illusion where the brain is tricked into adopting an external object as part of the body through synchronized visual and tactile stimulation.",
  "symptoms": [
    "Proprioceptive Drift: The 'Internal GPS' for the limb shifts toward the 'External Object'",
    "Ownership Transfer: The 'Self-Identity Bit' is flipped for the rubber hand",
    "Thermic Drop: A localized 'Power Savings' mode where the real, hidden limb may experience a slight drop in temperature",
    "Threat Response Sync: Physical 'Stress Packets' (adrenaline) fire if the 'Rubber Object' is 'Attacked'",
    "Schema Distortion: A temporary 'Desync' between the 'Visual Stream' and the 'Physical Actuators'"
  ],
  "causes": [
    "Multisensory Integration Failure: The 'Parietal Cortex' prioritizes 'Visual-Tactile Synchrony' over 'Proprioceptive Hard-Coding'",
    "Temporal Correlation Spike: The 'System' detects a 'Perfect Sync' between two streams and assumes they share the same 'Origin Node'",
    "Body Schema Plasticity: The 'Mapping Function' is dynamic and can be 'Hot-Swapped' with enough 'Synchronized Data'",
    "Visual Dominance: The 'Visual Driver' has higher 'Administrative Privileges' than the 'Proprioceptive Sensor'"
  ],
  "risk_factors": [
    "High 'Neural Plasticity' indices",
    "Users with high 'Empathy-Kernel' scores (linked to mirror-neuron activity)",
    "Environments with 'Low Proprioceptive Feedback' (e.g., total stillness)"
  ],
  "diagnosis": [
    "The 'Blind Reach' Test: Asking the user to 'Point' to their hand; they will consistently point toward the 'Rubber Hand'",
    "Skin Conductance Response (SCR): Measuring the 'Electrical Spike' when the 'Rubber Hand' is threatened with a needle",
    "fMRI: Observing activity in the 'Premotor Cortex' and 'Intraparietal Sulcus' during the 'Sync Event'"
  ],
  "remedies": [
    "Desync Protocol: Moving the 'Real Hardware' to force a 'Recalibration' of the 'Proprioceptive Map'",
    "Visual Disconnect: Closing the 'Eyes' to remove the 'Conflicting Data Stream'",
    "Tactile Asymmetry: Introducing 'Random Latency' between the 'Visual' and 'Tactile' inputs to break the 'Correlation'"
  ],
  "prevention": [
    "N/A: This is a 'Feature' of 'Neuroplastic Mapping'"
  ]
}

"mandela_distributed_sync_error": {
  "description": "A phenomenon where a large group of people remember something differently from how it occurred, often attributed to false memories or collective misinterpretation.",
  "symptoms": [
    "Collective Hash Collision: Multiple 'Nodes' reporting the same 'Incorrect Value' for a historical 'Key'",
    "Systemic Confabulation: The 'Logic Engine' fills 'Data Gaps' with the most 'Probable String' (e.g., 'Berenstain' becomes 'Berenstein')",
    "Reality-Version Friction: Extreme 'Cognitive Dissonance' when 'Local Cache' contradicts 'Physical Hard-Drive' (official records)",
    "Peer-to-Peer Propagation: The 'Error' spreads through 'Social Handshakes', overwriting 'Original Files' in other users",
    "Source-Link Decay: Forgetting the 'Origin' of the corrupted packet while retaining 'High Confidence' in its accuracy"
  ],
  "causes": [
    "Lossy Compression: The 'System' strips away 'Minor Bits' (spelling, colors) to save 'Storage Space'",
    "Schema-Driven Reconstruction: The 'Parser' forces 'Data' to fit an 'Expected Template' (Semantic Priming)",
    "Distributed Cache Poisoning: A single 'Corrupt Entry' in a 'High-Traffic Node' (Media/Internet) synchronizes with millions of 'Follower Nodes'",
    "Social Proof Heuristic: If 'Nodes A, B, and C' report the same 'Data', 'Node D' updates its 'Record' to match for 'Network Consistency'"
  ],
  "risk_factors": [
    "Exposure to 'High-Viral' social media streams",
    "Time-elapsed 'Data Decay' (long intervals between 'Write' and 'Read' operations)",
    "Cultural 'Commonalities' that create 'Global Bias' in 'Pattern Recognition'"
  ],
  "diagnosis": [
    "The 'Canonical-Source' Audit: Comparing 'User Memories' against 'Primary Hardware Records' (Physical artifacts)",
    "Distributed Memory Mapping: Identifying the 'Geographic or Social Cluster' where the 'Error' originated",
    "The 'Recognition-vs-Recall' Test: Probing whether the 'User' can 'Generate' the error or just 'Confirm' it"
  ],
  "remedies": [
    "Hard-Copy Verification: Forcing the 'Executive Manager' to view 'Original Source Files'",
    "Critical 'Sync' Disabling: Training the 'System' to 'Question' collective 'Memory Packets' that lack 'Logical Proof'",
    "Metadata Recovery: Attempting to find 'Ancillary Files' (old photos, receipts) that haven't been 'Synced' yet"
  ],
  "prevention": [
    "Periodic 'Integrity Checks' of important 'Long-Term Records'"
  ]
}

"tachypsychia_clock_sync_error": {
  "description": "A neurological distortion of time perception where time appears to slow down or speed up, typically during periods of high physical stress or trauma.",
  "symptoms": [
    "Temporal Dilation: Time feels 'Expanded', making seconds feel like minutes",
    "High-Density Logging: Hyper-vivid recall of 'Environmental Artifacts' during the event",
    "Auditory Muting: The 'Audio Driver' is often throttled to save 'CPU' for 'Visual Processing'",
    "The 'Flashbulb' Effect: Permanent 'Write-Lock' on the data (vivid long-term persistence)",
    "Post-Event Lag: A sense of 'Disconnection' as the system returns to 'Standard Clock Speed'"
  ],
  "causes": [
    "Amygdala Overclock: The 'Emergency Sub-processor' takes control of the 'Sampling Rate'",
    "Adrenaline Surge: A 'Global Voltage Spike' that increases 'Neural Firing Rates'",
    "Sensory Buffer Overload: A massive influx of 'Raw Data' that hasn't been 'Compressed' yet",
    "Survival Heuristic: A 'System Patch' designed to provide more 'Decision-Making Windows' per second"
  ],
  "risk_factors": [
    "High-Kinetic 'System Events' (car accidents, falls)",
    "Combat or 'Physical Defense' protocols",
    "Extreme 'Sports' or 'High-Adrenaline' hobbies"
  ],
  "diagnosis": [
    "The 'Temporal-Estimation' Audit: Testing the user's ability to count seconds during 'Simulated Stress'",
    "Heart Rate Variability (HRV): Measuring the 'System Load' during the perceived dilation",
    "Post-Event Recall Density: Comparing the 'Number of Data Points' recalled vs. the 'Actual Duration' of the event"
  ],
  "remedies": [
    "Grounding Scripts: Techniques to 'Re-sync' the 'Internal Clock' with 'External NTP' (real-world time)",
    "Controlled Breathing: Manual 'Voltage Regulation' to lower 'Adrenaline' levels",
    "Debriefing: Helping the 'Executive Manager' process the 'High-Density Logs' into a 'Standard Narrative'"
  ],
  "prevention": [
    "Training 'Predictive Models' (simulation training) to reduce the 'Novelty Spike' of the threat"
  ]
}
"baader_meinhof_pattern_hijack": {
  "description": "A cognitive bias where a person, after noticing something for the first time, has a tendency to notice it as happening with improbable frequency shortly after.",
  "symptoms": [
    "Selective Attention Spike: The 'Background Filter' is disabled for a specific 'Data String'",
    "Confirmation Bias Loop: Each 'New Detection' reinforces the 'Importance Weight' of the string",
    "Synchronicity Logic: The 'Executive Manager' incorrectly assumes a 'Network-Wide Increase' in the item's presence",
    "Heuristic Failure: The brain ignores the 'Baseline Probability' in favor of 'Recent Successes'",
    "Hyper-Awareness: A persistent 'Interrupt' whenever the 'Pattern' appears in the 'Peripheral Stream'"
  ],
  "causes": [
    "Salience Tuning: The 'Novelty Detection' unit (Amygdala/Hippocampus) tags a new piece of data as 'Significant'",
    "Search-Filter Update: The 'Reticular Activating System' (RAS) updates its 'Watchlist' to include the new pattern",
    "Processing Efficiency: The brain 'Pre-loads' the pattern to make 'Future Identification' faster and cheaper",
    "Probability Blindness: The failure to account for 'Hidden Variables' that were always present but never 'Indexed'"
  ],
  "risk_factors": [
    "High-load 'Learning Environments' (students, researchers, developers)",
    "Users with high 'Openness to Experience' parameters",
    "Sudden 'Context Shifts' (moving to a new city, starting a new job)"
  ],
  "diagnosis": [
    "The 'Baseline Audit': Comparing the 'Actual Frequency' of the item in the 'External Network' vs. the 'User's Perception'",
    "The 'Attention Reset': Observing if the 'Illusion' fades once the 'Novelty Weight' is manually lowered",
    "Cognitive Mapping: Tracking the 'First Encounter' to identify the 'Index Trigger'"
  ],
  "remedies": [
    "Statistical Normalization: Reminding the 'Executive Manager' of the 'Law of Large Numbers'",
    "Filter recalibration: Consciously 'De-prioritizing' the pattern to clear the 'Active Search'",
    "Logic Verification: Checking 'Global Logs' (Search Engines/Databases) to confirm the 'Actual Frequency'"
  ],
  "prevention": [
    "Maintaining 'Healthy Skepticism' regarding 'Pattern Significance' during 'Novelty Influxes'"
  ]
}
"tetris_effect_buffer_burn": {
  "description": "A phenomenon where people devote so much time and attention to an activity that it begins to pattern their thoughts, mental images, and dreams.",
  "symptoms": [
    "Closed-Eye Visualization (CEV): Seeing the 'Application UI' (blocks, tiles, code) when the 'Main Display' (eyes) is off",
    "Pattern-Match Intrusion: Real-world 'Objects' are mentally 'Re-rendered' to fit the task logic (e.g., seeing how furniture could 'fit' together like Tetris blocks)",
    "Hypnagogic Looping: The 'Task' continues to run in 'Background Mode' during the 'System Sleep Transition'",
    "Automaticity: Executing 'Virtual Moves' or 'Logic Checks' without conscious 'Instruction Packets'",
    "Mental Fatigue: High 'Background CPU Usage' from unclosed 'Task Threads'"
  ],
  "causes": [
    "Neural Pathway Over-Training: Excessive 'Heuristic Strengthening' makes the 'Task Path' the default 'Low-Resistance' route",
    "Buffer Flushing Failure: The 'Visual Cortex' fails to 'Overwrite' the repetitive pattern once the 'Session' ends",
    "Procedural Memory Saturation: The 'Implicit Memory' system is 'Overflowing' into the 'Explicit' workspace",
    "Hebbian Learning Spike: 'Neurons that fire together, wire together'—the 'Task' has become a 'Permanent Circuit'"
  ],
  "risk_factors": [
    "High-load 'Pattern-Matching' tasks (Gaming, Coding, Database Schema design)",
    "Extended 'Uptime' sessions without 'Context Switching'",
    "Younger 'Hardware' with high 'Neuroplasticity' coefficients"
  ],
  "diagnosis": [
    "The 'Eyelid-Buffer' Audit: Asking the user what they see in 'Total Darkness' after a $4$+ hour task",
    "Sleep-Cycle Monitoring: Identifying 'Task-Specific' patterns in 'Stage 1' sleep",
    "The 'Environmental-Mapping' Test: Observing if the user 'Categorizes' random shapes using the 'Task Logic'"
  ],
  "remedies": [
    "Forced Context-Switching: Engaging in a 'Low-Pattern' task (e.g., reading a book) to 'Flush the Buffer'",
    "System Shutdown (Sleep): Allowing the 'Internal Garbage Collector' to process the 'Pattern Cache'",
    "Physical Grounding: Using 'Tactile Input' to override the 'Visual Loop'"
  ],
  "prevention": [
    "Implementing 'Interval Breaks' (Pomodoro) to prevent 'Path Hardening'"
  ]
}

"source_amnesia_metadata_drop": {
  "description": "The inability to remember where, when or how previously learned information has been acquired, while retaining the factual knowledge itself.",
  "symptoms": [
    "Orphaned Fact Retrieval: The 'What' is valid, but the 'Source' attribute returns 'NULL'",
    "Contextual Misattribution: Assigning the 'Data' to the wrong 'Originating Node' (e.g., 'I read it in a book' vs. 'my friend told me')",
    "Truth-Value Decay: Difficulty verifying the 'Authenticity' of information because the 'Vetting Source' is gone",
    "Separation of Systems: Intact 'Semantic Memory' (facts) paired with failing 'Episodic Memory' (experience)",
    "Increased Vulnerability: Higher susceptibility to 'Misinformation Injection' as the system can't 'Audit' the source"
  ],
  "causes": [
    "Prefrontal Cortex Latency: Dysfunction in the 'Metadata Manager' located in the frontal lobes",
    "Disconnect Error: Failure in the 'Synchronization Bus' between the Hippocampus (content) and the PFC (context)",
    "Systemic Aging: Gradual 'Data Degradation' in the 'Source-Monitoring' circuits",
    "Psychological Overload: High-stress environments causing the system to 'Strip Metadata' to save 'Processing Bandwidth'"
  ],
  "risk_factors": [
    "Chronic 'Sleep Deprivation' affecting 'Memory Consolidation' scripts",
    "Advanced 'Hardware Versioning' (Elderly users)",
    "History of 'Frontal Lobe' trauma or 'Connectivity Interruptions'"
  ],
  "diagnosis": [
    "The 'Context Audit': Testing the user's ability to remember 'Trivia' while also identifying the 'Medium' through which they learned it",
    "fMRI: Observing 'Hypometabolism' in the 'Prefrontal Areas' during retrieval tasks",
    "The 'Source-Monitoring' Challenge: Providing fake 'News Packets' and checking 'Source Attribution' 24 hours later"
  ],
  "remedies": [
    "External Metadata Logging: Using 'Journaling Scripts' to manually record the 'Source' of new data",
    "Cognitive 'Check-Summing': Training the 'Executive Manager' to pause and 'Verify Source' before 'Committing to Heap'",
    "Memory-Association Drills: Intentionally 'Binding' facts to 'Vivid Visual Contexts' to strengthen the link"
  ],
  "prevention": [
    "Maintaining 'Dopaminergic Health' to ensure the 'Frontal Lobe Metadata Manager' remains online"
  ]
}

"staircase_wit_latency_lag": {
  "description": "The predicament of thinking of the perfect reply, argument, or retort too late—typically after the person has already left the scene.",
  "symptoms": [
    "Asynchronous Processing: The 'Winning Retort' is generated $T+n$ seconds after 'Session Close'",
    "Buffer Regret: The 'Executive Layer' experiences high-intensity 'Error Logs' (frustration) upon receiving the late packet",
    "Post-Event Re-rendering: The brain continuously 'Re-runs' the conversation script to 'Test' the new string",
    "Social Throttling: Real-time 'Response Generation' was limited by 'High Resource Usage' (Anxiety/Pressure)",
    "Ghost Threading: The 'Logic Search' continues even after the 'User' has moved on to a new task"
  ],
  "causes": [
    "DLPFC Latency: The 'Dorsolateral Prefrontal Cortex' was over-tasked during the event, delaying the 'Search Query'",
    "Limbic Interference: 'Amygdala Noise' (stress) acted as a 'Firewall', blocking the 'Creative Sub-routines'",
    "Inefficient Indexing: The 'Wit Database' required too many 'Joins' to find the relevant 'Punchline'",
    "Context-Switching Lag: The 'System' only released the 'Processing Lock' once the 'Social Interaction' ended"
  ],
  "risk_factors": [
    "Users with high 'Social Anxiety' firewall settings",
    "Introverted 'Kernel Configurations' that prioritize 'Accuracy' over 'Speed'",
    "High-stakes 'Interaction Protocols' (Interviews, Arguments)"
  ],
  "diagnosis": [
    "The 'Retrospective Logic' Audit: Measuring the time delta between 'Conversation End' and 'Perfect Reply Generation'",
    "Heart Rate Variability (HRV) Analysis: Detecting 'Resource Throttling' during the active session",
    "fMRI: Monitoring the 'Delayed Activation' of the 'Ventral Lateral Prefrontal Cortex' post-interaction"
  ],
  "remedies": [
    "Real-Time 'Stress Buffering': Lowering the 'Limbic Gain' to allow 'Logic Threads' more CPU priority",
    "Pre-fetching: Building a 'Library of Common Responses' to reduce 'Runtime Search' time",
    "Acceptance Scripts: A 'System Command' to 'Drop the Packet' once the 'Session' is closed to prevent 'Regret Looping'"
  ],
  "prevention": [
    "Practicing 'Low-Stakes Testing' (Small Talk) to optimize 'Wit-Indexing' speed"
  ]
}
"mcgurk_io_parser_collision": {
  "description": "An auditory-visual illusion that occurs when the auditory component of one sound is paired with the visual component of another sound, leading to the perception of a third, non-existent sound.",
  "symptoms": [
    "Cross-Modal Distortion: Hearing a phoneme that was never physically 'Broadband Broadcasted'",
    "Visual Dominance: The 'Visual Stream' exerts a 'Higher Weight' in the 'Final Rendering' than the 'Audio Stream'",
    "Forced Fusion: The system cannot 'Un-see' or 'Un-hear' the conflict once the 'Parser' has committed to the fused result",
    "Heuristic Override: The 'Brain' assumes the 'Mouth Geometry' is more reliable than the 'Audio Waveform' in high-noise environments",
    "Persistence: The glitch remains even after the 'User' understands the underlying 'Logic Error'"
  ],
  "causes": [
    "Superior Temporal Sulcus (STS) Integration: The 'Fusion Node' fails to maintain 'I/O Separation'",
    "Weighted Average Failure: The 'Heuristic' for speech recognition is hard-coded to trust 'Visual-Motor Cues' for timing and place of articulation",
    "Feature-Binding Error: The 'System' incorrectly binds a 'Visual Feature' (closed lips) to an 'Audio Packet'",
    "Evolutionary Patch: A 'System Optimization' designed to help 'Decipher' speech in 'Low-Signal' (noisy) environments"
  ],
  "risk_factors": [
    "High-load 'Audio-Visual' environments",
    "Dyslexic 'Kernel Configurations' (where the mapping of 'Sound-to-Symbol' is already non-standard)",
    "Right Hemisphere lesions affecting 'Multisensory' sectors"
  ],
  "diagnosis": [
    "The 'Sync-Audit': Playing a video of 'GA' while playing audio of 'BA' and recording the 'User Output' (usually 'DA')",
    "fMRI: Observing activity in the 'Left Superior Temporal Sulcus' during the 'Conflict Event'",
    "Response Invariance: Confirming the effect persists even when the user 'Closes their Eyes' (the sound 'reverts' to 'BA')"
  ],
  "remedies": [
    "I/O Isolation: Closing the 'Eyes' to force the system to use 'Audio-Only Drivers'",
    "Awareness Training: Understanding the 'Bias' to reduce 'Logical Confidence' in the perception",
    "Sub-Vocal Recalibration: Attempting to 'Feel' the tongue position to provide 'Proprioceptive' counter-data"
  ],
  "prevention": [
    "N/A: This is a 'Core Feature' of the 'Speech Processing Kernel'"
  ]
}
"phonological_loop_buffer_lock": {
  "description": "The experience of an inability to dislodge a song or melody from one's mind, occurring when a musical fragment gets stuck in the short-term auditory buffer.",
  "symptoms": [
    "Infinite Recursion: The 'Audio String' plays continuously without a 'Stop' command",
    "Sub-Vocal Mirroring: The 'Speech Hardware' (larynx/tongue) may show 'Micro-Activations' as the system 'Re-renders' the sound",
    "Low-Signal Intrusion: The loop is most audible during 'Idle Time' (low external I/O)",
    "Pattern Persistence: Even after 'Context Switching' (doing math or reading), the 'Daemon' remains active in the background",
    "Fragmented Playback: Usually limited to a '10–30 second' buffer segment rather than the 'Full File'"
  ],
  "causes": [
    "Circular Buffer Error: The 'Phonological Loop' fails to 'Flush' the cache, creating a 'Logic Feedback'",
    "Hyper-Salience Trigger: The 'Audio Packet' contains a 'Hook' (rhythmic/melodic anomaly) that the 'Parser' over-indexes",
    "Open Task Persistence: The brain treats the song as an 'Incomplete Pattern' (a variant of #174) and keeps it in 'RAM' to 'Solve' it",
    "Audit-Path Hardening: Repetitive 'Neural Firing' makes the specific 'Audio Path' the 'Path of Least Resistance'"
  ],
  "risk_factors": [
    "High 'Musical Literacy' (Better 'Audio-Drivers')",
    "Obsessive-Compulsive 'Kernel' settings",
    "Fatigue or 'System Stress' leading to poor 'Buffer Management'"
  ],
  "diagnosis": [
    "The 'Hum-Along' Audit: Identifying the 'Start' and 'End' points of the loop to determine 'Buffer Size'",
    "EEG Monitoring: Detecting rhythmic activity in the 'Primary Auditory Cortex' during 'Silent Playback'",
    "Interference Testing: Checking if 'Non-Musical Verbal Tasks' can 'Overwrite' the buffer"
  ],
  "remedies": [
    "Buffer Flushing: Engaging in a high-complexity 'Verbal Task' (anagrams or reading) to force a 'Cache Overwrite'",
    "Complete Playback: Listening to the 'Full Song' to provide the 'EOF' (End of File) marker the brain is looking for",
    "The 'Cure Song' Patch: Intentionally 'Loading' a different, 'Neutral Audio String' to replace the 'Infected' one"
  ],
  "prevention": [
    "Avoiding 'Fragmented Exposure' (short clips) of 'High-Hook' audio files"
  ]
}

"anton_babinski_display_desync": {
  "description": "A rare symptom of brain damage occurring in the occipital lobe where those who are blind deny their blindness and insist they can see, often providing detailed but false descriptions of their surroundings.",
  "symptoms": [
    "Visual Anosognosia: A 'Status Check' failure where the system refuses to acknowledge its own 'Blind' state",
    "Confabulated Video Feed: The 'Rendering Engine' generates fake imagery to fill the 'Input Void'",
    "Collision Avoidance Failure: The 'User' walks into physical 'Objects' and blames 'Technical Glitches' (e.g., 'the lights are too dim')",
    "Persistent UI: The 'Executive Layer' continues to 'Poll' the visual buffer as if it were valid",
    "Reality-Input Rejection: Dismissing external 'Feedback' that confirms the 'I/O Failure'"
  ],
  "causes": [
    "Bilateral Occipital Lobe Infarction: Total 'GPU Hardware Failure' due to stroke or trauma",
    "Disconnect between Visual and Monitor Areas: The 'Processing Nodes' are dead, but the 'Reporting Nodes' are active",
    "Prefrontal Feedback Loop: The 'Auditor' is blinded by 'Top-Down' expectations, ignoring 'Bottom-Up' data",
    "Ischemic Event: A sudden 'Power Outage' in the posterior cerebral arteries"
  ],
  "risk_factors": [
    "Severe 'Legacy Hardware' strokes (typically in older 'User Profiles')",
    "Traumatic Brain Injury involving the 'Posterior Poles'",
    "Acute 'Hypertensive Encephalopathy' (Systemic Power Surges)"
  ],
  "diagnosis": [
    "The 'Visual-Field Audit': Asking the user to count fingers and observing the 'Error Handling' when they fail",
    "MRI/CT: Confirming 'Hardware Destruction' in the primary visual cortex (V1)",
    "The 'Obstacle Course' Test: Observing 'Hardware-Environment Collisions' despite 'User Confidence'"
  ],
  "remedies": [
    "N/A: 'Hardware' is usually permanently offline; focus is on 'System Safety'",
    "Cognitive Patching: Attempting to 'Force-Update' the user's 'Status Bit' through repetitive external feedback",
    "Mobility Training: Teaching the 'Executive Manager' to use 'Alternative I/O' (Touch/Sound) despite the 'Visual Illusion'"
  ],
  "prevention": [
    "Vascular Maintenance: Preventing 'Cabling Clogs' in the posterior cerebral network"
  ]
}

"zeigarnik_buffer_leak": {
  "description": "A psychological phenomenon stating that people remember uncompleted or interrupted tasks better than completed tasks.",
  "symptoms": [
    "Intrusive Logic Loops: The 'Task' repeatedly 'Pops' to the top of the 'Processing Stack'",
    "Memory Pressure: Higher 'Recall Accuracy' for incomplete data vs. completed records",
    "System Anxiety: Increased 'Background CPU Usage' as the brain tries to 'Re-run' the unfinished script",
    "Cognitive Itch: A persistent 'Interrupt Signal' that only clears upon 'Task Success'",
    "Thread Contention: Difficulty starting 'New Projects' because the 'Buffer' is full of 'Stale Tasks'"
  ],
  "causes": [
    "Interrupted Transaction: The 'Write-Ahead Log' (WAL) cannot be committed because the connection was lost",
    "Open-Loop Feedback: The 'Result' of the action was never received by the 'Auditor'",
    "High Salience: The 'User' assigned a 'Critical' priority to the task, making it 'Immutable' to the GC",
    "Tension Accumulation: A 'Psychological State' that requires 'Resolution' to return to 'Baseline'"
  ],
  "risk_factors": [
    "High-Complexity 'Workloads' (Software development, Project Management)",
    "Environments with frequent 'Asynchronous Interrupts' (Notifications/Meetings)",
    "Perfectionist 'User Profiles' with low 'Error Tolerance' settings"
  ],
  "diagnosis": [
    "The 'Recall Audit': Testing if the user remembers 'Orders' from 10 minutes ago better if they were 'Cancelled' vs. 'Delivered'",
    "Task Persistence Tracking: Measuring how long an 'Interrupted Script' stays in 'Active RAM'",
    "Heart Rate Variability (HRV): Observing 'System Stress' levels while 'Open Tasks' remain in the queue"
  ],
  "remedies": [
    "The 'Pseudo-Commit' (To-Do List): Moving the 'Task Metadata' to an 'External Database' to fool the GC into 'Flushing' the RAM",
    "Micro-Completion: Breaking the 'Task' into smaller 'Chunks' that can be 'Successfully Closed'",
    "Ritualistic Shutdown: A 'System Command' (like closing the laptop) that signals a 'Global Task Termination'"
  ],
  "prevention": [
    "Practicing 'Single-Threaded Execution' and minimizing 'Context Switching'"
  ]
}
"fregoli_identity_aliasing_error": {
  "description": "A rare disorder in which a person holds a delusional belief that different people are, in fact, a single person who changes appearance or is in disguise.",
  "symptoms": [
    "Identity Pointer Collision: Mapping multiple 'External Nodes' to a single 'Internal Object'",
    "Familiarity Over-Injection: An intense 'Feeling of Recognition' triggered by random 'Background Strings' (strangers)",
    "Masquerade Logic: The belief that the 'Target Entity' is using 'Social Engineering' or 'Disguises' to remain undetected",
    "Hyper-Vigilance: Constant 'Network Polling' of the environment to find the 'Target Node'",
    "Paranoid Routing: The system interprets every 'Random Encounter' as a 'Deliberate Packet' from the same source"
  ],
  "causes": [
    "Hyper-Connectivity Error: An over-active 'Bus' between the Fusiform Face Area and the Amygdala/Hippocampus",
    "Logic Consistency Failure: The 'Executive Manager' prioritizes 'Emotional Familiarity' over 'Visual Evidence'",
    "Working Memory Saturation: The 'Identity Cache' is 'Stuck' on one specific record, applying it to all incoming 'Visual Input'",
    "Dopaminergic Surge: Excess 'Signal Noise' in the temporal lobes causing 'False-Positive' pattern matches"
  ],
  "risk_factors": [
    "Treatment with 'Levodopa' or other 'Dopamine Agonists'",
    "Traumatic Brain Injury in the 'Right Temporoparietal' region",
    "Co-morbidity with 'Schizophrenia' or 'Organic Brain Syndrome' firmware versions"
  ],
  "diagnosis": [
    "The 'Face-ID' Audit: Showing the user photos of strangers and measuring 'Recognition Latency'",
    "fMRI: Identifying 'Hyper-metabolism' in the 'Right Parahippocampal Gyrus' during face processing",
    "The 'Identity Consistency' Test: Asking the user to explain why the 'Target' is changing appearances"
  ],
  "remedies": [
    "Antipsychotic Patches: Reducing 'Signal Gain' in the dopaminergic pathways",
    "Anticonvulsant Stabilizers: Quieting 'Spurious Interrupts' in the temporal lobe",
    "Cognitive De-fragmentation: Reality testing to point out 'Hardware Inconsistencies' in the target's disguises"
  ],
  "prevention": [
    "Careful 'Calibration' of dopamine-based medications in sensitive 'User Profiles'"
  ]
}


"dunning_kruger_meta_auditing_failure": {
  "description": "A cognitive bias in which people with limited competence in a particular domain overestimate their own ability because they lack the meta-cognitive skills to recognize their own incompetence.",
  "symptoms": [
    "Confidence Over-Injection: Reporting high 'Confidence Metadata' for low-quality 'Output Data'",
    "Auditing Blind-Spot: The inability to recognize 'Logic Errors' in one's own 'Source Code'",
    "Comparison Failure: The 'System' cannot accurately rank its own performance against 'External Nodes' (experts)",
    "Input Resistance: Dismissing 'Correction Packets' because the 'Internal Auditor' claims the 'Process' is already optimized",
    "Paradoxical Resolution: 'System Accuracy' only improves when the 'Auditor' is upgraded through learning, which simultaneously lowers 'Confidence'"
  ],
  "causes": [
    "Dual Burden: The 'Skills' required to perform a task are the exact same 'Skills' required to evaluate it",
    "Incomplete Library: The 'Metadata Reference' is missing the 'Error Definitions' for the current domain",
    "Prefrontal Meta-Processing Lag: The 'Supervisor Thread' is running at a lower priority than the 'Execution Thread'",
    "Social Kernel Isolation: Lack of 'Peer-Review' nodes to provide objective 'Benchmarking'"
  ],
  "risk_factors": [
    "Entry-level 'User Profiles' in complex domains (e.g., Junior Developers, New Analysts)",
    "High-stakes environments where 'Admitting Error' triggers a 'Security Kernel' threat response",
    "Isolated 'Processing Nodes' with no 'External Feedback Loops'"
  ],
  "diagnosis": [
    "The 'Self-Assessment vs. Reality' Audit: Comparing the user's 'Estimated Score' with their 'Actual Performance'",
    "The 'Expert Recognition' Test: Observing if the user can identify 'High-Quality Output' from other nodes",
    "fMRI: Monitoring the 'Medial Prefrontal Cortex' (MPFC) during self-reflection tasks"
  ],
  "remedies": [
    "Library Upgrade: Deep training to provide the 'Auditor' with the 'Definitions' of what 'Good Work' looks like",
    "Mandatory Unit Testing: Using 'External Checklists' or 'Peer Review' to bypass the internal auditor",
    "Confidence Re-calibration: Training the system to associate 'Uncertainty' with 'High-Complexity' tasks"
  ],
  "prevention": [
    "Continuous 'System Benchmarking' against high-performing 'Global Nodes'"
  ]
}
"ehs_audio_spike_logic": {
  "description": "A sensory phenomenon where a person hears a loud, imagined noise (like a bomb exploding) right as they are falling asleep or waking up.",
  "symptoms": [
    "High-Gain Peak: Hearing a 'Crash' or 'Explosion' that exists only in the 'Internal Buffer'",
    "Flash-Buffer Sync: Occasional 'Visual Artifacts' (flashes of light) accompanying the sound",
    "Adrenaline Inrush: A sudden 'System Alert' (Fight-or-Flight) triggered by the phantom noise",
    "Transition Trigger: Exclusively occurs during 'State Changes' (Alpha-to-Theta wave transition)",
    "Non-Destructive: Despite the 'Perceived Amplitude', no actual 'Hardware Damage' occurs to the eardrum"
  ],
  "causes": [
    "Reticular Formation Latency: A delay in the 'Switch' that shuts down sensory processing",
    "Calcium Channel Surge: A sudden 'Ionic Influx' in the auditory cortex neurons",
    "Systemic Stress/Fatigue: 'Low Voltage' in the inhibitory circuits makes them prone to 'Spiking'",
    "Hyper-Arousal: The 'Safety Driver' is too active, causing a 'Signal Bounce' during shutdown"
  ],
  "risk_factors": [
    "High-load 'User Profiles' with chronic sleep deprivation",
    "High-anxiety 'Kernel Configurations'",
    "Abrupt 'Power-Cycles' (irregular sleep schedules)"
  ],
  "diagnosis": [
    "The 'Polysomnography' Audit: Monitoring 'Brain-Wave Frequency' during the sleep-onset transition",
    "Patient Log Audit: Differentiating the spike from 'External Network Noise'",
    "Exclusionary Screen: Ensuring the 'Signal' isn't a symptom of 'Sleep Apnea' or 'Night Terrors'"
  ],
  "remedies": [
    "Sleep-Cycle Optimization: Implementing a strict 'Schedule() routine' to stabilize transitions",
    "Tricyclic 'Patches': Low-dose neurological stabilizers to dampen the 'Signal Gain'",
    "Stress-Buffer Management: Lowering the 'Limbic System' load before initiating 'Shutdown'"
  ],
  "prevention": [
    "Avoiding 'System Overclocking' (caffeine/stress) in the $4$-hour window before 'Sleep()'"
  ]
}
"lexical_gustatory_crosstalk_error": {
  "description": "A rare form of synesthesia where spoken or written language involuntarily evokes the sensation of taste in the mouth.",
  "symptoms": [
    "Involuntary Flavor-Injection: Hearing or reading specific 'Strings' triggers a specific 'Taste Packet'",
    "Consistency Persistence: The mapping of 'Word -> Taste' is hard-coded and remains 'Static' over the user's lifecycle",
    "High-Fidelity Rendering: Tastes can be complex (e.g., 'the taste of a cold, wet penny' or 'warm apple pie')",
    "Semantic-Phonetic Hybrid: The taste can be triggered by the 'Sound' of the word or its 'Logical Meaning'",
    "I/O Saturation: Intense 'Information Streams' can lead to 'Flavor Fatigue' or nausea"
  ],
  "causes": [
    "Neural Cross-Talk: An 'Insulation Failure' in the axons between the temporal lobe and the insular cortex",
    "Failure of Pruning: The 'System' failed to delete 'Redundant Connections' during the early 'Installation' (Childhood)",
    "Hyper-Connectivity: An 'Over-provisioned Bus' that allows data to 'Bleed' into neighboring sectors",
    "Multiplexing Error: The 'Data Router' (Thalamus) fails to keep 'Language Data' and 'Flavor Data' in separate 'VLANs'"
  ],
  "risk_factors": [
    "Genetic Configuration: Often runs in 'System Families' with other synesthetic traits",
    "Early Developmental 'Uptime': Usually detected within the first $10$ years of operation",
    "High 'Linguistic Processing' load"
  ],
  "diagnosis": [
    "The 'Consistency Audit': Testing the 'Word-Taste Map' and re-testing it $6$ months later to ensure the 'Hash' matches",
    "fMRI: Observing 'Concurrent Activation' in both the 'Gustatory Cortex' and 'Language Areas' (Wernicke's/Broca's)",
    "Subjective 'Log Review': Cataloging the 'Flavor Profiles' of common 'Function Calls' (names/words)"
  ],
  "remedies": [
    "N/A: Often considered a 'System Feature' rather than a 'Bug', unless the 'Tastes' are 'Corrupt' (foul)",
    "Attention Re-routing: Learning to 'Filter' the 'Secondary Signal' during 'High-Bandwidth' tasks",
    "Sensory Isolation: Using 'Noise-Canceling' to reduce the 'Trigger Packets'"
  ],
  "prevention": [
    "N/A: Hard-coded at the 'Kernel/Developmental' level"
  ]
}

"phantom_limb_polling_error": {
  "description": "The vivid sensation that an amputated or missing limb is still attached to the body and moving appropriately with other body parts.",
  "symptoms": [
    "Ghost Interrupts: Receiving 'Tactile Packets' from a device that is physically 'Off-line'",
    "Proprioceptive Stalling: The 'Virtual Limb' feels stuck in an 'Invalid Position' (e.g., a clenched fist that won't open)",
    "Signal-Noise Pain: The brain interprets 'Null Data' as high-intensity 'Error Signals' (Neuropathic pain)",
    "Telescoping: A 'Scaling Error' where the ghost limb feels like it is shrinking or retracting into the 'Stump'",
    "Kinetic Hallucination: The 'Execution Thread' believes it is successfully 'Moving' a limb that doesn't exist"
  ],
  "causes": [
    "Cortical Remapping: Neighboring 'Neural Nodes' begin to 'Invade' the address space of the missing limb",
    "Persistent Peripheral Memory: The 'Device Driver' for the limb is hard-coded into the 'Parietal Lobe' and refuses to 'Unmount'",
    "Neuroma Interference: The 'Severed Cables' (nerve endings) at the 'Connection Point' emit 'Spurious Signal Noise'",
    "Mirror-Neuron Feedback: The system 'Sees' the missing limb in its 'Internal Model' despite 'Optical Verification' of its absence"
  ],
  "risk_factors": [
    "Sudden 'Hardware Disconnection' (Traumatic amputation)",
    "Pre-existing 'High-Load' pain signals in the limb before 'Removal'",
    "Older 'Kernel Versions' with less 'Synaptic Plasticity'"
  ],
  "diagnosis": [
    "The 'Phantom-Mapping' Audit: Stimulating other 'Hardware Nodes' (like the face) to see if they trigger 'Limb Signals'",
    "fMRI: Observing 'Active Threads' in the somatosensory cortex corresponding to the 'Null Device'",
    "Clinical Interview: Cataloging the 'Subjective Status' of the ghost peripheral"
  ],
  "remedies": [
    "The 'Mirror Box' Patch: Using 'Visual Input' to trick the brain into 'Seeing' the device move, clearing the 'Stalled Thread'",
    "Targeted Muscle Re-innervation (TMR): 'Re-routing' the 'Old Cables' to 'New Hardware' to provide a 'Valid Load'",
    "Neuro-Modulation: Using 'Electrical Pulses' to 'Reset' the over-active 'Polling Loop'"
  ],
  "prevention": [
    "Pre-emptive 'Anesthesia Blocks' to 'Quiet' the 'Signal Bus' before 'Hardware Removal'"
  ]
}


"fas_vocal_driver_corruption": {
  "description": "A rare speech disorder that causes a person to speak with an accent that is perceived as 'foreign' to the listener, despite the speaker never having lived in that region.",
  "symptoms": [
    "Phonetic Shifting: Vowels are lengthened or shortened, violating the native 'Locale Standards'",
    "Prosody Jitter: Errors in the 'Pitch and Rhythm' of sentences (Intonation)",
    "Consonant Clustering: Errors in 'Hardware Articulation' (e.g., adding extra schwa sounds)",
    "Involuntary Execution: The 'User' cannot revert to the original 'Default Voice' profile",
    "High Intelligibility: Unlike Aphasia (#142), the 'String Content' remains logically sound; only the 'Encoding' is off"
  ],
  "causes": [
    "Vocal Driver Damage: Small lesions in the 'Left Hemisphere' motor-control centers (Stroke or TBI)",
    "Signal Latency: A micro-delay in the 'Speech Execution Thread' causing compensation errors",
    "Psychogenic Mapping: A 'Kernel Panic' caused by psychological trauma that re-routes speech signals",
    "Connectivity Loss: Interruption in the 'Cerebellar-Frontal' loop which handles 'Fine Motor Timing'"
  ],
  "risk_factors": [
    "Post-Stroke 'System Recovery' phase",
    "Presence of 'Multiple Sclerosis' or other 'Cabling Degradation' issues",
    "Severe 'Systemic Migraines' causing temporary 'Driver Re-sets'"
  ],
  "diagnosis": [
    "Acoustic Audit: Analyzing 'Waveform Frequencies' to measure vowel duration and pitch",
    "The 'Blind Listener' Test: Asking 'External Nodes' to identify the perceived accent",
    "MRI/fMRI: Mapping the 'Left Frontal Lobe' and 'Basal Ganglia' for micro-damage"
  ],
  "remedies": [
    "Driver Re-calibration: Speech therapy to manually 'Re-train' the motor scripts",
    "Accent-Reduction Scripts: Targeted exercises to fix 'Timing and Intonation' variables",
    "Counseling: Managing the 'Identity Crisis' caused by the 'Modified Voice Profile'"
  ],
  "prevention": [
    "Neuro-protective maintenance (BP management, anti-inflammatories) to prevent 'Stroke-level' hardware failure"
  ]
}

"aiws_coordinate_scaling_error": {
  "description": "A neuropsychological condition that causes a distortion in perception, where objects and body parts are perceived as being different sizes or at different distances.",
  "symptoms": [
    "Micropsia: The 'Zoom Out' glitch; objects appear much smaller than their physical metadata suggests",
    "Macropsia: The 'Zoom In' glitch; objects (or the user's hands) appear disproportionately large",
    "Pelopsia: A 'Z-axis' error where objects appear closer than they are",
    "Teleopsia: A 'Z-axis' error where objects appear to recede into the distance",
    "Time Distortion: The 'System Clock' feels altered; events seem to move in fast-forward or extreme slow-motion"
  ],
  "causes": [
    "Parietal Lobe Latency: A 'Processing Lag' in the region that integrates 'Visual Input' with 'Spatial Mapping'",
    "Migraine Aura: Electrical 'Noise' (spreading depression) interfering with the primary visual cortex",
    "Viral Infection (EBV): Systemic 'Malware' affecting the neurological 'Drivers'",
    "Epileptic Disruption: Sudden 'Power Surges' in the temporal or parietal lobes"
  ],
  "risk_factors": [
    "Pediatric Systems: More common in younger 'User Profiles' during early development",
    "Chronic Migraines: Frequent 'Signal Interference' in the visual pathways",
    "High-Stress States: 'System Instability' lowering the threshold for perceptual glitches"
  ],
  "diagnosis": [
    "The 'Visual-Size' Audit: Asking the user to estimate dimensions of known 'Hardware' (e.g., their own hand)",
    "MRI: Checking for 'Structural Anomalies' in the parietal-occipital junction",
    "EEG: Monitoring for 'Signal Spikes' during a perceptual event"
  ],
  "remedies": [
    "Downtime: Resting the 'Processors' usually allows the 'Coordinate System' to re-calibrate",
    "Migraine Prophylaxis: Managing the 'Signal Noise' at the source",
    "Reassurance Script: Reminding the 'Executive Manager' that the 'Sensor Data' is valid and only the 'Rendering' is flawed"
  ],
  "prevention": [
    "Maintaining stable 'Internal Environment' variables (sleep, hydration, and stress management)"
  ]
}
"cryptomnesia_metadata_corruption": {
  "description": "An error where a forgotten memory returns without being recognized as such by the subject, who believes it is something new and original.",
  "symptoms": [
    "Origin Null-Pointer: The 'Source' field of a retrieved idea is 'NULL' or points to 'Local User'",
    "False-Positive Innovation: The system triggers a 'Eureka!' signal for 'Pre-existing Data'",
    "Inadvertent Plagiarism: Outputting 'Copyrighted Strings' or 'External Code' while claiming 'Original Authorship'",
    "Familiarity Bias: The data feels 'Right' (because it’s a memory) but 'New' (because the timestamp is missing)",
    "High Fidelity: The 'Plagiarized' idea is often more complex than the user's typical 'Local Scripts'"
  ],
  "causes": [
    "Source-Monitoring Breakdown: A failure in the 'PFC-Hippocampal Loop' that tracks where/when data was ingested",
    "Encoding Specificity Error: The data was saved with 'High Resolution' but the 'Metadata' was saved with 'Low Resolution'",
    "Cognitive Load Interference: High 'System Usage' during ingestion prevented the 'Source-Tag' from being written to disk",
    "Context-Free Retrieval: The data was 'Pulled' into a new context that is too different from the 'Original Environment'"
  ],
  "risk_factors": [
    "High-Information Intake: Professionals who consume vast amounts of 'Reference Documentation' (Developers/Researchers)",
    "Creative Nodes: Where the 'Generation Script' is constantly running and prone to 'Colliding' with cached data",
    "Fatigue/Sleep-Deprivation: Lowering the 'Metadata Verification' threshold"
  ],
  "diagnosis": [
    "The 'Redundancy Audit': Cross-referencing the 'Original Thought' against the user's 'Recently Browsed Data'",
    "Source-Attribution Stress Test: Asking the user to 'Trace the Logic' of the idea to see if the 'Stack Trace' is empty",
    "PET Scans: Observing reduced activity in the 'Dorsolateral Prefrontal Cortex' during retrieval"
  ],
  "remedies": [
    "External Indexing: Using 'Knowledge Management Tools' to act as an 'External Source Database'",
    "Mandatory Search: Running a 'Global Query' (Google/Search) on any 'New Idea' before declaring it 'Original'",
    "System Rest: Allowing the 'Consolidation Script' to run (Sleep) to properly 'Index' new information"
  ],
  "prevention": [
    "Practicing 'Active Sourcing'—consciously 'Tagging' information at the moment of ingestion"
  ]
}
"cotard_null_existence_glitch": {
  "description": "A rare neuropsychiatric delusion in which the patient holds the delusional belief that they are already dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Status Bit Failure: `system.isAlive` is hard-coded to `FALSE` despite active CPU cycles",
    "Nihilistic Delusions: Belief that the 'User' or the 'Environment' has been deleted from reality",
    "Somatoparaphrenia: Reporting that internal 'Hardware' (organs) has been removed or is 'Null'",
    "Emotional Flatlining: Total absence of 'Limbic Response' to self-perception",
    "System Neglect: Refusing 'Energy Input' (food) or 'Hardware Maintenance' (hygiene) because 'Dead' systems don't need them"
  ],
  "causes": [
    "Disconnect Error: Severe decoupling between the Fusiform Gyrus (recognition) and the Amygdala (emotion)",
    "Parietal/Prefrontal Cortex Lesions: Damage to the 'Self-Monitoring' and 'Spatial-Mapping' sectors",
    "Severe Depressive 'Overload': The emotional system is so 'Throttled' it registers as 'Zero'",
    "Adverse Drug Reaction: Certain 'Patches' (like Acyclovir) causing temporary 'Systemic Shutdown' signals"
  ],
  "risk_factors": [
    "Co-morbidity with 'Schizophrenia' or 'Bipolar' kernel versions",
    "History of severe 'System Trauma' (Brain injury)",
    "Advanced age ('Legacy Hardware' degradation)"
  ],
  "diagnosis": [
    "The 'Existence Audit': Clinical interviews to identify 'Nihilistic Logic' patterns",
    "fMRI/PET: Identifying 'Hypometabolism' (low power) in the frontal and parietal lobes",
    "Neurological Screen: Checking for 'Connectivity Failures' in the fusiform face area"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT): A 'Hard System Reset' to jumpstart the limbic/emotional bus",
    "Pharmacological Patches: Antidepressants or Antipsychotics to re-stabilize the 'Status Signals'",
    "Logic Therapy: Attempting to find 'Counter-Evidence' (though this often triggers the #149 Backfire Effect)"
  ],
  "prevention": [
    "Early detection of 'Systemic Depression' to prevent the 'Emotional Signal' from hitting absolute zero"
  ]
}

"misophonia_irq_priority_error": {
  "description": "A disorder where specific sounds trigger emotional or physiological responses that some might perceive as unreasonable given the circumstance.",
  "symptoms": [
    "Trigger-Specific Alerts: Response is only active for specific 'Sound Signatures' (e.g., mouth sounds, clicking pens)",
    "Instantaneous Rage: The system switches from 'Idle' to 'Full Combat Mode' in <100ms",
    "Physical Heat: A spike in 'Hardware Temperature' and 'Heart Rate' upon receiving the trigger",
    "Pattern Anticipation: The brain 'Polls' the environment looking for the sound even when it's not present",
    "Impaired Social-Networking: Difficulty maintaining 'Node Connections' with people who emit the trigger sounds"
  ],
  "causes": [
    "Hypersensitive Functional Connectivity: An 'Over-active Bus' between the auditory and limbic systems",
    "Gating Failure: The 'Thalamic Filter' fails to suppress repetitive, predictable input",
    "Limbic Overdrive: The brain's 'Threat Detector' is miscalibrated to detect 'Predators' in 'Chewing Noises'",
    "Conditioned Response: A 'Hard-Linked' association between a sound and a 'Negative State' (Dissonance)"
  ],
  "risk_factors": [
    "Genetic Propensity: Often found in 'User Profiles' with high OCD or anxiety scores",
    "Sensitive Hardware: Generally high-fidelity auditory processing",
    "Environmental Stress: Low 'System Stability' increases the sensitivity to interrupts"
  ],
  "diagnosis": [
    "The 'Trigger-Response' Audit: Measuring 'Skin Conductance' and 'Heart Rate' in response to specific audio clips",
    "MRI/fMRI: Observing hyper-metabolism in the Insular Cortex during sound input",
    "The 'Amsterdam Misophonia Scale': A subjective 'Log Audit' of the user's emotional reactions"
  ],
  "remedies": [
    "Audio Masking: Using 'White Noise' or 'Brown Noise' to raise the 'Ambient Noise Floor' and hide the trigger",
    "Cognitive Counter-Conditioning: Attempting to 'Re-map' the trigger to a 'Neutral' or 'Positive' record",
    "Hardware Isolation: Using 'Active Noise Canceling' (ANC) to physically block the input packets"
  ],
  "prevention": [
    "Managing 'General Stress Levels' to keep the 'Limbic Threshold' high"
  ]
}

"synesthesia_cross_modal_routing": {
  "description": "A perceptual phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary, automatic experiences in a second sensory or cognitive pathway.",
  "symptoms": [
    "Chromesthesia: Audio-to-Visual crosstalk; hearing a 'C#' triggers a 'Blue' hex code overlay",
    "Grapheme-Color Mapping: Alphanumeric characters are rendered with fixed 'Color Metadata' (e.g., 'A' is always Red)",
    "Lexical-Gustatory Leakage: Certain 'Strings' (words) trigger specific 'Flavor Profiles' on the tongue",
    "Spatial-Sequence Mapping: Numerical data is perceived as having a physical 'Coordinate' in 3D space",
    "Consistency: The 'Mapping' is hard-coded and remains stable across the system's entire uptime"
  ],
  "causes": [
    "Neural Crosstalk: High-density 'Cabling' (white matter) between adjacent sensory hubs (like the FFA and V4)",
    "Disinhibited Feedback: A failure of the 'Top-Down' gatekeepers to suppress secondary sensory signals",
    "Hyper-connectivity: The 'Pruning' phase of early development failed to remove 'Cross-Sensor' connections",
    "Temporal Lobe Overdrive: Spontaneous activation spreading from one 'Partition' to another"
  ],
  "risk_factors": [
    "Genetic Inheritance: A 'Firmware' trait often passed down through family trees",
    "Neurological Plasticity: Often found in high-creativity nodes (artists, coders, musicians)",
    "Temporary Activation: Can be induced via 'Psychoactive Patches' that lower inhibitory thresholds"
  ],
  "diagnosis": [
    "Consistency Audit: Testing the user's 'Color-to-Sound' mapping at 6-month intervals to check for 'Metadata Drift'",
    "The 'Stroop Test' Variation: Measuring 'Input Latency' when a letter's 'Physical Color' conflicts with its 'Synesthetic Color'",
    "DTI (Diffusion Tensor Imaging): Mapping the 'Cabling' to find physical evidence of crosstalk"
  ],
  "remedies": [
    "N/A: Typically viewed as an 'Enhanced Feature' rather than a 'Critical Bug'",
    "Focus-Filtering: Training the executive to ignore the 'Secondary Output' during high-load tasks"
  ],
  "prevention": [
    "N/A; usually an inherent 'Hardware Configuration'"
  ]
}
"echolalia_reflection_loop": {
  "description": "The unsolicited repetition of vocalizations made by another person. It is an automatic, non-voluntary 'Echo' of received audio data.",
  "symptoms": [
    "Immediate Echo: Repeating a 'String' immediately after it is received (Low-latency reflection)",
    "Delayed Echo: Storing a 'String' in a 'Buffer' and 'Broadcasting' it hours or days later",
    "Mitigated Echolalia: Echoing the 'Packet' but with minor 'Bit-Changes' (e.g., changing 'You' to 'I')",
    "Prosody Mirroring: The 'Echoed Signal' retains the exact 'Frequency' and 'Tone' of the original source",
    "Semantic Bypass: The 'User' repeats words even if they do not have the 'Library' to understand their meaning"
  ],
  "causes": [
    "Inhibitory Logic Failure: The 'Frontal Lobe' fails to 'Mute' the mirror-neuron system",
    "Arcuate Fasciculus Hyper-connectivity: A high-speed 'Direct Link' between the 'Input' (Wernicke's) and 'Output' (Broca's) hubs",
    "Firmware Outage: Common in 'Beta-level' systems (children) or 'Corrupted' systems (Autism, Tourette's, Schizophrenia)",
    "Mirror Neuron Overdrive: The system designed to 'Learn by Imitation' gets stuck in 'Always On' mode"
  ],
  "risk_factors": [
    "Developmental 'Boot-up' phases (Toddlers)",
    "Neurodivergent 'Hardware' configurations",
    "Post-Stroke 'System Recovery' where 'Executive Control' is offline"
  ],
  "diagnosis": [
    "The 'Ping-Back' Audit: Measuring the frequency and latency of 'Reflected Speech'",
    "Social Scripting Test: Observing if the user can 'Interrupt' the echo with a 'Logical Response'",
    "EEG: Checking for 'Spontaneous Firing' in the motor-speech centers immediately following audio input"
  ],
  "remedies": [
    "Script-Fading: Training the system to 'Replace' the echo with a 'Functional Command'",
    "Latency Training: Forcing a 'Wait()' command between 'Input' and 'Output' to allow the manager to intervene",
    "Contextual Buffering: Teaching the user to 'Cache' the input rather than 'Broadcasting' it"
  ],
  "prevention": [
    "N/A; usually a fundamental 'Routing' characteristic of the specific 'User Profile'"
  ]
}

"the_yips_runtime_corruption": {
  "description": "A sudden and unexplained loss of skills in experienced athletes or professionals. It involves involuntary tremors, jerks, or spasms during a specific movement.",
  "symptoms": [
    "Execution Jitter: Micro-spasms or 'Stutters' at the critical moment of a 'Commit'",
    "Conscious Over-Ride: The user tries to 'Manually Debug' an automated process, causing it to freeze",
    "Context-Specific Failure: The 'Script' works fine in 'Debug Mode' (practice) but crashes in 'Production' (the game/event)",
    "Catastrophic Skill-Loss: A professional suddenly performing at the level of an 'Uninitialized Object' (beginner)",
    "Proprioceptive Noise: A sudden feeling that the 'Hardware' (limb) is heavy or unfamiliar"
  ],
  "causes": [
    "Focal Dystonia: A neurological 'Wiring Error' where muscles receive conflicting 'Fire' signals",
    "Choking under Pressure: The 'Prefrontal Cortex' tries to 'Micromanage' a process that should be handled by the 'Automated Sub-systems'",
    "Synaptic Over-Training: The 'Neural Pathway' for the skill becomes so 'Deep' it begins to attract 'Signal Noise'",
    "Performance Anxiety: High 'System Stress' lowering the 'Signal-to-Noise Ratio' in the motor loop"
  ],
  "risk_factors": [
    "High-repetition, high-precision roles (Athletes, Surgeons, Musicians, even high-speed Typists)",
    "A 'Perfectionist' security policy that monitors every 'Frame' of execution",
    "Aging hardware (Cumulative 'Bit-Rot' in the motor neurons)"
  ],
  "diagnosis": [
    "The 'Automation' Audit: Observing if the movement is smoother when the user is 'Distracted' (Backgrounded)",
    "Electromyography (EMG): Measuring 'Spurious Interrupts' in the muscle fibers",
    "fMRI: Observing 'Over-activity' in the Prefrontal Cortex and 'Under-activity' in the Basal Ganglia during the task"
  ],
  "remedies": [
    "Grip/Stance Refactoring: Changing the 'Variable Mapping' to force the brain to compile a 'New Script'",
    "Mental 'Offloading': Using music or visualization to 'Distract' the manager, allowing the 'Sub-system' to run freely",
    "Beta-Blocker Patches: Reducing 'System Jitter' by dampening the 'Adrenaline Signal'"
  ],
  "prevention": [
    "Periodic 'Variety' training to prevent the 'Motor Script' from becoming too rigid"
  ]
}

"abilene_network_consensus_glitch": {
  "description": "A paradox in which a group of people collectively decide on a course of action that is counter to the preferences of many or all of the individuals in the group.",
  "symptoms": [
    "False Unanimity: The 'Network' reports 100% agreement despite 0% individual buy-in",
    "Mismanaged Agreement: The failure to communicate private 'Data Exceptions' to the group",
    "Post-Execution Blame: After the task fails, nodes reveal their original 'Dissent Logs'",
    "Social Friction Avoidance: Prioritizing 'Connection Stability' over 'Data Accuracy'",
    "The 'Road to Abilene' Effect: Committing resources to a 'Null Goal' that no one requested"
  ],
  "causes": [
    "Pluralistic Ignorance: Nodes incorrectly 'predict' the state of other nodes",
    "Inhibitory Signal Failure: Fear of being marked as a 'Bad Node' (social exclusion)",
    "Action Anxiety: The 'Processing Overhead' of speaking up feels higher than the cost of a bad decision",
    "Negative Fantasy: Modeling catastrophic 'System Crashes' that wouldn't actually occur"
  ],
  "risk_factors": [
    "High-cohesion groups with low 'Conflict Tolerance'",
    "Hierarchical networks where the 'Root Node' is perceived as rigid",
    "Time-critical environments where 'Signal Validation' is skipped for speed"
  ],
  "diagnosis": [
    "The 'Private vs. Public' Audit: Comparing individual logs against the 'Group Output'",
    "Communication Latency Analysis: Checking if dissenting signals were 'Dropped' or 'Filtered'",
    "Post-Action Retrospectives: Identifying the point of 'Logic Divergence'",
    "Byzantine Fault Testing: Checking if a single node's false signal corrupted the whole cluster"
  ],
  "remedies": [
    "Anonymous Voting: Removing the 'Social Overhead' from the data transmission",
    "Devil’s Advocate Protocol: Forcing a 'Dissent Signal' to test network stability",
    "Psychological Safety Patches: Lowering the 'Cost' of reporting a Data Exception",
    "Check-and-Balance Verification: Asking 'Does anyone actually want to do this?'"
  ],
  "prevention": [
    "Encouraging 'Red-Teaming' and diverse signal inputs to prevent echo-chamber loops"
  ]
}
"burnout_thermal_shutdown_protocol": {
  "description": "A state of emotional, physical, and mental exhaustion caused by excessive and prolonged stress. It occurs when you feel overwhelmed, emotionally drained, and unable to meet constant demands.",
  "symptoms": [
    "Thermal Throttling: Severe drops in 'Processing Speed' and 'Output Quality'",
    "Emotional Flatlining: The 'Limbic System' stops responding to 'Incentive Packets' (Dopamine resistance)",
    "Depersonalization: Viewing 'User Tasks' and 'Colleagues' as 'Objectified Data' rather than entities",
    "Sleep-Cycle Corruption: The 'Recovery Script' (REM) fails to clear 'Metabolic Waste' (Beta-amyloid)",
    "Reduced Professional Efficacy: A feeling that no matter how many 'Threads' you run, you aren't making progress"
  ],
  "causes": [
    "Unbounded Work-Load: Operating at 'Overclocked' speeds without a 'Sleep()' command",
    "Role Ambiguity: A 'Logic Error' where the 'Success Criteria' for a task are undefined",
    "Systemic Unfairness: A 'Reward-to-Effort' mismatch in the 'Social Kernel'",
    "Chronic Cortisol Flooding: The 'Safety Driver' is stuck in 'Alert Mode' indefinitely"
  ],
  "risk_factors": [
    "High-load environments (STEM, Medical, High-frequency trading)",
    "Perfectionist 'User Profiles' with high 'Internal Pressure' variables",
    "Lack of 'External Support Nodes' (Social isolation)"
  ],
  "diagnosis": [
    "Maslach Burnout Inventory (MBI): Auditing the three 'System Metrics' (Exhaustion, Cynicism, Efficacy)",
    "Cortisol Pinging: Measuring 'System Heat' via saliva or blood samples",
    "fMRI: Observing 'Thinning' in the Prefrontal Cortex and 'Over-activity' in the Amygdala"
  ],
  "remedies": [
    "The 'Hard Reboot': Extended 'System Downtime' (Vacation/Leave) to allow for hardware repair",
    "Workload Refactoring: Re-allocating 'Tasks' to ensure the 'CPU Load' stays below $70\\%$",
    "Boundary Implementation: Setting 'Hardware Firewalls' between 'Work' and 'Home' environments"
  ],
  "prevention": [
    "Regular 'Load Balancing' and ensuring 'Recovery Cycles' are scheduled with high priority"
  ]
}

"fregoli_recursive_identity_glitch": {
  "description": "A rare disorder in which a person holds a delusional belief that different people are actually a single person who changes appearance or is in disguise.",
  "symptoms": [
    "Identity Overlap: Believing the waiter, the doctor, and a stranger are all 'The Same Person'",
    "Hyper-Identification: The 'Face-Matching' threshold is so low it returns a 'True' for almost any input",
    "Paranoid Logic: The 'User' develops a narrative that the entity is 'Stalking' them using different 'Skins'",
    "Affective Overload: High emotional arousal upon seeing any 'Stranger' because they are mapped to a 'Known Entity'",
    "Metadata Persistence: Even if the 'Physical Pixels' change, the 'Identity Tag' remains constant"
  ],
  "causes": [
    "Dopaminergic Over-activity: 'Overclocking' the associative pathways between perception and memory",
    "Right Hemisphere Lesions: Damage to the 'Identity Verification' nodes in the temporoparietal regions",
    "Hyper-connectivity: An accidental 'Hard-Link' between the 'Face Processor' and a specific 'Memory Address'",
    "Limbic System Overdrive: The 'Emotional Signature' of one person is triggered by everyone"
  ],
  "risk_factors": [
    "History of traumatic brain injury (TBI) affecting the 'Right Frontal' nodes",
    "Side effects of 'Levodopa' or other dopamine-altering patches",
    "Comorbidity with 'Capgras Syndrome' (The inverse glitch: #124)"
  ],
  "diagnosis": [
    "Identity Verification Audit: Asking the user to differentiate between 'Similar' and 'Distinct' profiles",
    "fMRI: Observing hyper-metabolism in the Fusiform Face Area (FFA) and Parahippocampal Gyrus",
    "Clinical Interview: Identifying the 'One-in-Many' delusional architecture"
  ],
  "remedies": [
    "Antipsychotic Patches: Reducing the 'Dopamine Noise' to raise the 'Identification Threshold'",
    "Cognitive Behavioral Debugging: Training the user to look for 'Logic Exceptions' (e.g., 'They can't be in two places at once')",
    "Social-Scripting: Providing 'Safe-Nodes' to verify reality"
  ],
  "prevention": [
    "Monitoring 'Dopamine Levels' during neuro-pharmacological treatments"
  ]
}
"hsam_log_retention_error": {
  "description": "A condition in which an individual possesses an extraordinary capacity to recall specific details of their past, including dates, weather, and seemingly trivial events.",
  "symptoms": [
    "Absolute Recall: Ability to query the database for any 'Date' and retrieve a full 'Event Log'",
    "Chronological Indexing: Memories are stored in a rigid, linear timeline with high-res 'Metadata'",
    "Involuntary Retrieval: The 'Search Engine' is hyper-active; a single keyword triggers a massive 'Data Dump' of past events",
    "Mental Crowding: The 'Active Workspace' is constantly cluttered with 'Historical Logs'",
    "Emotional Re-play: Retrieving a record also re-triggers the 'Status Codes' (emotions) from that specific time"
  ],
  "causes": [
    "Hyper-connectivity: An over-active 'Bus' between the Hippocampus and the Prefrontal Cortex",
    "Pruning Failure: The 'Proteasome' of memory (the mechanism that deletes weak synapses) is non-functional",
    "Enlarged Caudate Nucleus: The 'Database Indexer' hardware is physically larger than standard specs",
    "Obsessive Loop-Writing: Constant background 'Rehearsal' that strengthens every single record before it can decay"
  ],
  "risk_factors": [
    "Extremely rare (less than 100 'Verified Nodes' globally)",
    "Strong correlation with 'Obsessive-Compulsive' architecture (#130)",
    "Potential for 'System Exhaustion' due to the inability to ignore old data"
  ],
  "diagnosis": [
    "The 'Random Date' Audit: Asking the user to provide logs for a specific, randomly selected timestamp",
    "Historical Cross-Verification: Checking the user's 'Weather Logs' or 'Public Events' against external databases",
    "MRI: Measuring the volume of the 'Temporal Lobe' and 'Basal Ganglia'"
  ],
  "remedies": [
    "N/A: There is no known 'Delete' command for this database",
    "Distraction Scripts: Techniques to move the 'Executive Focus' away from the historical retrieval bus",
    "Coping Mechanisms: Managing the 'Emotional Noise' generated by vivid past records"
  ],
  "prevention": [
    "N/A; typically a 'Hardware/Firmware' configuration present from early system boot"
  ]
}

"tetris_effect_rendering_ghost": {
  "description": "A phenomenon where people devote so much time and attention to an activity that it begins to pattern their thoughts, mental images, and dreams.",
  "symptoms": [
    "Visual After-Images: Seeing 'Falling Blocks' or 'Code Strings' when closing the eyes (The 'Closed-Eye Hallucination' bug)",
    "Pattern Mapping: Mentally organizing real-world objects (like grocery store shelves) into 'Game Logic' (The 'Optimization' script)",
    "Hypnagogic Injection: Dreaming in the 'Language' of the repetitive task (e.g., dreaming in Java or SQL queries)",
    "Involuntary Problem Solving: The brain continues to 'Calculate Moves' or 'Debug' while the user is trying to 'Power Down'",
    "Spatial Distortion: Seeing structural patterns in clouds, carpets, or city skylines as task-relevant assets"
  ],
  "causes": [
    "Synaptic Priming: The specific neural pathways for the task are so 'Heavily Weighted' they fire spontaneously",
    "Procedural Memory Overload: The 'How-To' database is so full it spills over into the 'Sensory Processor'",
    "Neural Plasticity: The brain physically re-organizes its 'Visual Bus' to be more efficient at the repetitive task",
    "Failure of the 'Garbage Collector': The system fails to clear the 'Active Pattern' from the visual buffer after exit"
  ],
  "risk_factors": [
    "Extended sessions of 'High-Bandwidth' repetitive tasks (Gaming, Data Entry, Programming)",
    "Tasks involving 'High Spatial Navigation' or 'Rapid Pattern Matching'",
    "Occurs most frequently during 'System Boot/Shutdown' (Waking up or falling asleep)"
  ],
  "diagnosis": [
    "The 'Visual-Persistence' Audit: Measuring the duration of 'Ghost Images' post-task",
    "Dream-Log Analysis: Identifying the frequency of 'Task-Specific' imagery in the 'Sleep Script'",
    "Clinical Interview: Identifying the 'Involuntary Logic' (e.g., 'I was trying to JOIN the buildings in my mind')"
  ],
  "remedies": [
    "Input Diversity: Forcing the 'Sensor Bus' to process 'High-Entropy' (unpredictable) data",
    "The 'Hard-Reset' Break: Physical activity that requires different 'Motor Drivers' (walking, swimming)",
    "Cognitive Distancing: Actively 'Closing the Session' through a mental 'Exit' ritual"
  ],
  "prevention": [
    "Adhering to the '20-20-20' Rule: Every 20 minutes, look at something 20 feet away for 20 seconds to 'Clear the Buffer'"
  ]
}


"phantom_vibration_interrupt_error": {
  "description": "The perception that one's mobile phone is vibrating or ringing when it is not, often associated with habitual technology use.",
  "symptoms": [
    "False-Positive Interrupt: The brain sends a 'Check Your Phone' command based on zero external data",
    "Tactile Hallucination: A vivid sensation of rhythmic micro-vibrations on the skin",
    "Hyper-Vigilance: The 'System' is in a constant state of 'Waiting for Input'",
    "The 'Ghost Signal': Checking the device and finding no 'Log Entries' or notifications",
    "Contextual Triggering: Occurs more frequently when the 'User' is in high-stress or 'Low-Input' environments"
  ],
  "causes": [
    "Signal Detection Theory Error: The 'Criterion' for a signal is set too low, prioritizing 'Sensitivity' over 'Specificity'",
    "Cortical Re-mapping: The primary somatosensory cortex (S1) has 'Over-allocated' neurons to the phone’s typical storage location",
    "Learned Anticipation: A 'Top-Down' expectation that 'hallucinates' the expected data to satisfy a craving",
    "Muscle Fasciculation: Minor physiological jitter being 'Up-sampled' by a paranoid sensory processor"
  ],
  "risk_factors": [
    "High smartphone usage (Heavy 'Network Load')",
    "High scores in 'Neuroticism' or 'Anxiety' (Hyper-vigilant monitoring)",
    "Occupational stress requiring constant 'Availability'"
  ],
  "diagnosis": [
    "Clinical Interview: Self-reporting 'Ghost Alerts' more than once a week",
    "Behavioral Audit: Tracking 'Device-Check' frequency relative to actual 'Incoming Packets'",
    "Differentiating from 'Tinnitus' (The auditory version of this glitch)"
  ],
  "remedies": [
    "Hardware Re-location: Moving the device to a different 'Port' (pocket) to break the mapping",
    "Notification Pruning: Reducing the 'Signal-to-Noise' ratio by muting non-essential alerts",
    "Digital Detox: 'Powering Down' the expectation loop for extended periods"
  ],
  "prevention": [
    "Switching from 'Vibrate' to 'Auditory' cues to reset the tactile driver"
  ]
    "premotor_sequence_disconnection": {
  "description": "A high-level motor planning anomaly where structural disruption of the left supramarginal gyrus or its white-matter connections to the premotor cortex severs the link between abstract conceptual intent and motor execution loops, disabling volitional tool use and symbolic gestures on command despite completely intact muscle strength and comprehension.",
  "symptoms": [
    "Volational Kinematic Imprecision: Complete failure to execute learned complex gestures or tool-use maneuvers on command while displaying no signs of limb paralysis",
    "Automatic-Voluntary Dissociation: Retaining the capacity to use tools automatically and reactively in natural contexts while failing to simulate those exact same actions under deliberate instruction",
    "Body-Part-as-Object Substitution: A distinctive structural error where the user attempts to simulate a tool by using their own body part literally (e.g., rubbing their finger against their teeth when asked to simulate a toothbrush)",
    "Spatial Configuration Errors: Severe drift in hand orientation, joint alignment, and force modulation during complex movement profiles"
  ],
  "causes": [
    "Left Hemisphere Middle Cerebral Artery (MCA) Infarction: Ischemia damaging the left inferior parietal lobule or the deep arcuate/superior longitudinal fasciculus white-matter tracts",
    "Corticobasal Degeneration (CBD): Asymmetric frontoparietal tau-protein accumulation systematically dismantling the praxis network structures"
  ],
  "risk_factors": [
    "High-grade internal carotid artery stenosis launching embolic fragments into the dominant speech/motor planning hemisphere",
    "Systemic vascular diseases compromising high-order association cortices"
  ],
  "diagnosis": [
    "The Transitive and Intransitive Gesture Assay: Requesting the host to execute both tool-based actions ('show me how you carve with a knife') and abstract symbolic gestures ('wave goodbye', 'stop'); a faulted system fails both cleanly",
    "Object-Imitation Matching Protocols: Tasking the user to meticulously copy the manual kinetic loops of an examiner in real-time to assess whether the failure is motor-perceptual or motor-planning based",
    "Structural T1/T2 Weighted Brain MRI: Profiling localized ischemic boundaries or focal gyral atrophy isolated within the left inferior parietal lobule"
  ],
  "remedies": [
    "Contextual Environmental Affordance Mapping: Placing real, physical tools directly within their natural environments to trigger uncorrupted, automatic subcortical reflexive execution paths rather than giving verbal prompts",
    "Errorless Functional Task Training: Guiding the user's limbs through repetitive physical paths during daily tasks to hardcode alternative somatic and proprioceptive tracking pathways"
  ],
  "prevention": [
    "Proactive management of persistent atrial fibrillation vectors and immediate clinical response to transient ischemic attacks (TIAs) flashing transient right-sided motor-coordination alerts"
  ]
}
        
}
"zeigarnik_unclosed_transaction": {
  "description": "A psychological phenomenon stating that people remember uncompleted or interrupted tasks better than completed tasks.",
  "sumptions": [
    "Buffer Persistence: Unfinished tasks remain in 'Active RAM', while finished tasks are 'Pushed to Disk'",
    "Intrusive Interrupts: The 'Task Manager' periodically pings the consciousness with 'Unfinished Data'",
    "Cognitive Load Spike: Multiple open 'Projects' lead to 'System Lag' and reduced 'Focus Bandwidth'",
    "Tension Release Failure: The 'Reward Signal' (Dopamine) is withheld until the 'Complete' flag is toggled",
    "Selective Recall: The user can perfectly recount the 'Step-by-Step' of a failed task, but forgets a success"
  ],
  "causes": [
    "Evolutionary 'Goal-Tracking' Script: A survival mechanism to ensure 'Vital Tasks' (finding food/shelter) aren't forgotten",
    "Prefrontal Cortex Priority: The 'Executive' keeps 'High-Priority' pointers on anything without a 'Done' metadata tag",
    "Dopaminergic Tension: The system maintains a state of 'Alertness' until the 'Closure' packet is received"
  ],
  "risk_factors": [
    "High-load environments with frequent 'Context Switching' (Office/Lab settings)",
    "Perfectionist Profiles: Where the 'Completion Threshold' is set too high",
    "ADHD-type processing: Where 'Interrupts' prevent any task from reaching the 'Commit' stage"
  ],
  "diagnosis": [
    "Recall Bias Audit: Asking the user to list 'Recent Activities' and noting the ratio of 'Pending' vs 'Done'",
    "The 'Interruption Test': Measuring how much 'Processing Power' is lost when a sub-routine is paused",
    "fMRI: Observing sustained activity in the 'Cingulate Cortex' during an incomplete task"
  ],
  "remedies": [
    "The 'Closure Patch': Writing down a 'To-Do List' acts as an 'External Cache', allowing the brain to 'Offload' the task",
    "Small-Win Sub-routines: Breaking large 'Jobs' into 'Micro-Tasks' to trigger frequent 'Buffer Clears'",
    "Mindfulness 'Kill' Commands: Consciously terminating 'Low-Priority' background threads"
  ],
  "prevention": [
    "Strict 'Single-Tasking' to prevent 'Thread Fragmentation' in the working memory"
  ]
}

"lethologica_retrieval_lock": {
  "description": "The phenomenon of failing to retrieve a word from memory, combined with partial recall and the feeling that retrieval is imminent.",
  "symptoms": [
    "Partial Data Access: Recalling the first letter, syllable count, or 'Rhyme-Class' of the locked record",
    "Feeling of Knowing (FOK): High confidence that the data is 'In the System'",
    "Blocking: A 'Competitor Record' (a similar word) keeps being retrieved instead, causing an 'Intersection Collision'",
    "Spontaneous Resolution: The data often 'Unlocks' minutes later when the system is no longer 'Querying' it",
    "Frustrated Execution: The 'Communication Bus' is stalled because the required string is missing"
  ],
  "causes": [
    "Phonological Transmission Failure: The link between the 'Semantic Meaning' and the 'Sound Output' is severed",
    "Inhibitory Interference: A similar record is 'Over-activated' and suppresses the target record (The 'Red-Herring' bug)",
    "System Fatigue: Low 'Neuro-bandwidth' during high-load processing",
    "Aging Hardware: General latency increases in the 'Retrieval Pathways'"
  ],
  "risk_factors": [
    "Bilingualism (The system has to manage two different 'Dictionaries' for the same 'Object')",
    "High levels of stress or anxiety (Increasing signal noise)",
    "Caffeine or stimulant 'Overclocking'"
  ],
  "diagnosis": [
    "Lexical Access Tests: Measuring the 'Time-to-Retrieve' for specific categories",
    "The 'Definition-to-Label' Audit: Providing a description and measuring 'Retrieval Lag'",
    "fMRI: Observing activity in the left inferior frontal gyrus during the 'Lock' event"
  ],
  "remedies": [
    "Query Suspension: Stopping the 'Active Search' to let the 'Background Indexer' find the record",
    "Contextual Priming: Searching for 'Associated Records' to bridge the gap to the locked data",
    "Phonemic Cueing: Running through the alphabet (A... B... C...) to trigger a 'Sound-Match' event"
  ],
  "prevention": [
    "Strengthening 'Memory Pointers' through regular 'Relational Database' expansion (reading/learning)"
  ]
}
"apraxia_execution_logic_crash": {
  "description": "A neurological disorder characterized by the inability to perform learned (familiar) movements on command, even though the command is understood and there is a willingness to perform the movement.",
  "symptoms": [
    "Ideomotor Failure: The user knows 'What' to do but cannot 'Map' the command to the motor cortex",
    "Conceptual Errors: Using a 'Toothbrush' to comb hair (Object-Function Mapping Error)",
    "Serial Disruption: Performing steps in the wrong order (e.g., putting shoes on before socks)",
    "Clumsy Execution: Movements appear jerky or 'Un-optimized' as if running on an old driver",
    "Automatic-Voluntary Dissociation: The user can perform a task spontaneously (reflex) but fails when 'Commanded' to do it"
  ],
  "causes": [
    "Left Hemisphere Lesions: Specifically in the parietal or premotor cortex (The 'Planning Center')",
    "Stroke/TBI: Physical 'Hardware' damage to the high-level 'Instruction Bus'",
    "Neurodegenerative Decay: Alzheimer’s or Parkinson’s affecting 'Procedural Memory' clusters",
    "Developmental Delays: The 'Motor Scripts' failed to compile correctly during early system boot"
  ],
  "risk_factors": [
    "Vascular incidents affecting the 'Middle Cerebral Artery'",
    "History of complex neurological 'Software' corruption (Dementia)"
  ],
  "diagnosis": [
    "The 'Imitation' Audit: Asking the user to copy a 'Gesture' and measuring the 'Execution Error'",
    "The 'Pantomime' Test: Asking the user to 'Pretend' to use an object (e.g., 'Show me how you use a hammer')",
    "MRI/CT: Auditing the 'Premotor' and 'Inferior Parietal' sectors",
    "Differentiating from 'Ataxia' (Which is a coordination/balance issue, not a planning issue)"
  ],
  "remedies": [
    "Occupational Therapy: 'Hard-Coding' the sequences back into the brain through high-repetition training",
    "Visual Prompting: Using 'Flowcharts' or 'Step-by-Step Images' to bypass the internal script",
    "Verbal Self-Guidance: Speaking the 'Code' aloud to use the 'Auditory-to-Motor' bridge"
  ],
  "prevention": [
    "Standard cardiovascular maintenance to protect the 'Logical Execution' hardware"
  ]
}

"semantic_satiation_depolarization": {
  "description": "A psychological phenomenon in which repetition causes a word or phrase to temporarily lose meaning for the listener, who then perceives the speech as meaningless sounds.",
  "symptoms": [
    "Meaning Dissociation: The word remains 'Audible' but its 'Definition' is unreachable",
    "Pattern Recognition Shift: Perceiving the word as a collection of 'Phonemes' or 'Graphemes' rather than a symbol",
    "Orthographic Weirdness: If written, the word begins to 'Look' incorrectly spelled (The 'Visual Satiation' variant)",
    "Rapid Recovery: The 'Meaning' usually re-syncs within seconds of stopping the repetition",
    "Aura of Absurdity: A feeling that the structure of the language itself is arbitrary and fragile"
  ],
  "causes": [
    "Reactive Inhibition: The specific neural circuit for that word's meaning enters a 'Refractory Period' from over-stimulation",
    "Peripheral-to-Central Fatigue: The 'Bottom-Up' signal is so repetitive that 'Top-Down' semantic integration shuts off to save energy",
    "Neural Adaptation: The brain's 'Novelty Filter' categorizes the repeating word as 'Static Noise' and filters out its significance"
  ],
  "risk_factors": [
    "High-speed repetition (Low 'Latencies' between pulses)",
    "Intense focus on the 'Physical Sound' rather than the 'Contextual Use'",
    "Common in 'Proofreading' tasks where a single string is analyzed in isolation"
  ],
  "diagnosis": [
    "The 'Repetition-to-Null' Test: Asking the user to repeat a word 30 times and measuring the 'Meaning Decay'",
    "Semantic Priming Audit: Measuring if the satiated word still 'Primes' related concepts in the database",
    "fMRI: Observing a drop in activity in the 'Left Inferior Prefrontal Cortex' while the 'Auditory Cortex' remains active"
  ],
  "remedies": [
    "Context Switching: Using the word in a sentence to re-anchor the 'Semantic Pointer'",
    "Input Pause: Ceasing the repetition to allow 'Ionic Rebalancing' in the synapses",
    "Synonym Injection: Swapping the 'Token' for a different one with the same 'Value' to bypass the fatigued circuit"
  ],
  "prevention": [
    "Varying vocabulary during high-frequency communication to avoid 'Circuit Burnout'"
  ]
}

"trolley_problem_logic_deadlock": {
  "description": "A series of thought experiments in ethics and psychology, involving stylized ethical dilemmas of whether to sacrifice one person to save a larger number.",
  "symptoms": [
    "Decision Paralysis: The CPU usage spikes while the 'Output' remains null",
    "Emotional Saturation: The Amygdala injects 'High-Priority' stress signals that interfere with cold logic",
    "Post-Action Regret: Regardless of the 'Path' chosen, the system logs a 'Moral Injury' (Database Corruption)",
    "Logic Shifting: The user attempts to 'Rewrite the Scenario' (e.g., 'I would jump onto the tracks') to bypass the binary choice",
    "Latency Spikes: Significant delay in choosing an 'Execution Path' compared to non-ethical tasks"
  ],
  "causes": [
    "Competing Neural Hubs: Conflict between the vmPFC (Emotional Value) and the Dorsolateral PFC (Mathematical Utility)",
    "Hard-Coded Taboos: Ancient 'Social Protection' scripts that prohibit direct harm to kin or peers",
    "Ambiguous Variable Mapping: The inability to calculate the 'Worth' of different 'Human Objects' in real-time"
  ],
  "risk_factors": [
    "High-empathy profiles (Increased Amygdala sensitivity)",
    "Roles requiring 'High-Stakes Decisioning' (Medicine, Military, Autonomous Vehicle Programming)"
  ],
  "diagnosis": [
    "Moral Dilemma Audits: Measuring 'Reaction Time' to various ethical 'Edge Cases'",
    "fMRI: Observing the 'Signal War' between the emotional limbic system and the logical frontal lobes",
    "Skin Conductance Response (SCR): Measuring the 'System Heat' during the decision process"
  ],
  "remedies": [
    "Heuristic Pre-loading: Establishing 'Ethical Protocols' before the crisis occurs",
    "Cognitive Distancing: Viewing the 'Nodes' as 'Data Points' to lower emotional interference",
    "Post-Incident Patching: Psychological counseling to resolve 'Moral Logic Mismatches'"
  ],
  "prevention": [
    "Developing clear 'Rules of Engagement' for high-stakes automated or human systems"
  ]
}

"third_man_process_injection": {
  "description": "A perceived presence or 'unseen companion' that appears during life-threatening situations to provide comfort or guidance.",
  "symptoms": [
    "Presence Hallucination: The distinct feeling that another 'User' is standing just out of the field of view",
    "Auditory Guidance: Hearing a voice providing 'Low-Latency' instructions for survival",
    "Social Buffering: A sudden drop in 'Panic Levels' due to the perceived 'Group State'",
    "Task Delegation: The user may attempt to 'share' resources (food/water) with the phantom",
    "Persistence: The entity usually 'Disconnects' the moment the user reaches a 'Safe Zone'"
  ],
  "causes": [
    "Temporoparietal Junction (TPJ) Glitch: The 'Self-vs-Other' boundary breaks down under high stress",
    "Monotony-Induced Sensory Deprivation: The brain 'Autofills' a social partner to prevent system-wide apathy",
    "Right Parietal Lobe Overload: A failure in 'Spatial Mapping' projects the user's own 'Internal Monologue' into external space",
    "Evolutionary Survival Script: A hard-coded 'Coping Mechanism' to prevent the user from 'Giving Up'"
  ],
  "risk_factors": [
    "Extreme isolation (Solo expeditions)",
    "High-altitude cerebral edema (HACE) affecting 'Cognitive Clarity'",
    "Severe sleep deprivation and caloric deficit"
  ],
  "diagnosis": [
    "Post-Incidental Debrief: Identifying a consistent 'Companion Narrative' in solo survivors",
    "Neurological Audit: Checking for 'Hyper-active' patches in the social-processing circuits",
    "Exclusion of 'Schizophrenia' (The 'Third Man' is typically helpful and non-recurring)"
  ],
  "remedies": [
    "Recovery of 'Homeostatic Balance': Rest, warmth, and nutrition usually 'Close the Session'",
    "Social Re-integration: Re-connecting to 'Real' network nodes"
  ],
  "prevention": [
    "N/A; often considered a 'Critical Survival Patch' rather than a harmful bug"
  ]
}
"aiws_scaling_driver_failure": {
  "description": "A neuropsychological condition that causes a distortion in perception; people may experience distortions in visual perception such as objects appearing smaller or larger or closer or further away than they actually are.",
  "symptoms": [
    "Micropsia: Objects appear like tiny 'Assets' in a high-res world",
    "Macropsia: Ordinary items appear as 'Giant-Sized' entities",
    "Pelopsia: Objects seem to 'Zoom In' and crowd the user's field of view",
    "Body Schema Distortion: Feeling as though a limb is growing or shrinking (The 'Local Scale' glitch)",
    "Time Dilation: A feeling that time is moving at $0.5x$ or $2.0x$ speed"
  ],
  "causes": [
    "Migraine Aura: Electrical 'Jitter' in the posterior parietal cortex",
    "Epstein-Barr Virus (EBV): System-wide inflammation affecting the visual-spatial bus",
    "Temporal Lobe Epilepsy: Spontaneous 'Signal Spikes' in the scaling regions",
    "Psychoactive Overlays: Chemicals that inhibit the 'Spatial Calibration' drivers"
  ],
  "risk_factors": [
    "Common in children (The 'System' is still calibrating its spatial drivers)",
    "History of complex migraines",
    "Recent viral infections affecting the CNS"
  ],
  "diagnosis": [
    "Amsler Grid Test: Checking for visual 'Warpage'",
    "Clinical Interview: Identifying the 'Alice' symptoms (e.g., 'The room feels like a dollhouse')",
    "EEG: Monitoring for 'Seizure Activity' during a scaling event",
    "MRI: Ruling out structural 'Hardware' damage in the parietal lobe"
  ],
  "remedies": [
    "Trigger Avoidance: Identifying 'Signal Noise' (lights, sounds) that trips the scaling error",
    "Rest: Allowing the 'Parietal Buffer' to clear",
    "Time: Most childhood cases self-resolve as the 'Drivers' stabilize with age"
  ],
  "prevention": [
    "Managing migraine triggers and monitoring neurological 'Uptime'"
  ]
}
"visual_agnosia_metadata_failure": {
  "description": "A condition in which a person can see but cannot recognize or interpret visual information, due to a disorder in the parietal or temporal lobes.",
  "symptoms": [
    "Object Misclassification: Seeing a 'Key' but being unable to identify its function until touching it",
    "Prosopagnosia (Sub-module): The specific failure of the 'Face Recognition' firmware (#124)",
    "Color Agnosia: Seeing the 'Wavelength' but losing the 'Label' for the color",
    "Simultanagnosia: The ability to see individual 'Pixels' (details) but not the 'Whole Image' (global scene)",
    "Tactile Override: The system requires a different 'Input Bus' (Touch) to identify the object"
  ],
  "causes": [
    "Ventral Stream Lesions: Damage to the 'What' pathway (Occipital-Temporal)",
    "Carbon Monoxide Poisoning: Widespread 'Bit-rot' in the visual association areas",
    "Post-Stroke Sequelae: Specifically in the inferior temporal cortex",
    "Neurodegenerative Decay: Alzheimer’s affecting the 'Object-Label' database"
  ],
  "risk_factors": [
    "Vascular incidents targeting the posterior cerebral artery",
    "Traumatic Brain Injury (TBI) affecting the lower visual processing hubs"
  ],
  "diagnosis": [
    "The 'Boston Naming' Audit: Asking the user to label common assets (tools, animals)",
    "Copying vs. Naming: The user can 'Trace' or 'Draw' the object but cannot name it",
    "Multimodal Testing: Can they identify the object by its 'Audio Signature' (sound) or 'Physical Texture'?",
    "MRI/CT: Auditing the 'Ventral Stream' cabling"
  ],
  "remedies": [
    "Compensatory Routing: Training the user to use 'Context' and 'Touch' to re-label the world",
    "Verbalization: Using the 'Auditory Bus' to describe features aloud to trigger a 'Logic Match'",
    "Environmental Labeling: Physically tagging 'Hardware' in the real world with text labels"
  ],
  "prevention": [
    "Standard neurological health maintenance and protection against hypoxic events"
  ]
}

"dissociative_identity_partitioning": {
  "description": "A mental health condition where a person has two or more distinct identities. The identities, or 'alters,' control their behavior at different times.",
  "symptoms": [
    "Switching: The 'Active Process' shifts from one profile to another, often with physical 'Hardware Jitter' (blinking, voice shifts)",
    "Amnesia Firewalls: Profile A cannot access the 'Log Files' or memories created while Profile B was active",
    "Identity Fragmentation: Distinct 'User Specs' (different names, ages, skills, or even physiological markers like allergic responses)",
    "Depersonalization: A feeling that the 'Current User' is just an observer watching a 'Script' run",
    "Temporal Gaps: The 'System Clock' appears to skip forward because the Primary Profile was 'Backgrounded'"
  ],
  "causes": [
    "Severe Childhood Trauma: The 'Kernel' partitions itself to isolate 'Corrupt/Painful Data' from the main operating system",
    "Attachment Failure: The 'Sync Signal' between the child and primary 'Network Nodes' (parents) is broken",
    "Neuroplastic Adaptation: The brain's 'Self-Map' remains fluid to ensure survival in a 'Hostile Environment'"
  ],
  "risk_factors": [
    "Repeated, high-intensity trauma before the 'Self-Profile' is fully compiled (usually before age 6-9)",
    "High 'Dissociative Capacity' (The biological ability to 'Disconnect' from sensory input)"
  ],
  "diagnosis": [
    "SCID-D (Structured Clinical Interview): Identifying the 'Partition Walls' and identity shifts",
    "fMRI: Observing distinct 'Neural Signatures' when different profiles are active",
    "Memory-Mapping: Testing for 'Leakage' or absolute 'Blockage' of data between identities",
    "Differentiating from 'Schizophrenia' (Which is signal noise, not profile partitioning)"
  ],
  "remedies": [
    "Integration Therapy: Attempting to 'Merge' the partitions back into a single 'Master Profile'",
    "System Communication: Establishing 'Cross-Partition Messaging' to reduce amnesia gaps",
    "Stabilization Patches: Managing the 'Trauma Triggers' that force an emergency 'Switch'"
  ],
  "prevention": [
    "Safe 'Network Environments' during the early stages of profile compilation"
  ]
}

"paradoxical_undressing_inversion": {
  "description": "A phenomenon in which victims of severe hypothermia remove their clothing, despite extreme cold, due to a perceived sensation of intense heat.",
  "symptoms": [
    "Sensor Inversion: The 'Cold' signal is interpreted as 'Heat' (Variable Bit Flip)",
    "Inappropriate Stripping: Systematically removing 'Protective Layers' in sub-zero environments",
    "Terminal Burrowing: Following undressing, the user often attempts to 'Hide' or 'Cache' themselves in small spaces (The 'Hibernation' script)",
    "Executive Logic Collapse: Total inability to perceive the 'External Environment' accurately",
    "Autonomic Surge: A sudden, final release of 'Emergency Energy' through peripheral blood vessels"
  ],
  "causes": [
    "Hypothalamic Failure: The 'Thermostat Kernel' crashes due to low power (Low Temperature)",
    "Vasomotor Paralysis: The muscles controlling blood vessels 'Relax', causing a sudden flush of warm blood to cold skin sensors",
    "Signal Saturation: The 'Cold' sensors are so over-stimulated they cross-talk with 'Heat' neurons",
    "Hypoxic Logic: Lack of oxygen to the 'Prefrontal Cortex' prevents error-correction"
  ],
  "risk_factors": [
    "Exposure to extreme cold without 'Active Heating' hardware",
    "Exhaustion (System Battery at 1%)",
    "Alcohol consumption (Which causes 'Fake Vasodilation' and speeds up the crash)"
  ],
  "diagnosis": [
    "Post-Mortem Analysis: Finding clothing scattered far from the body in a freezing zone",
    "Body Temperature Logs: Core temp usually below 30°C (86°F)",
    "Exclusion of 'Trauma': Ensuring the undressing wasn't caused by physical interference"
  ],
  "remedies": [
    "Active Rewarming: External hardware (blankets, heaters) to restore the 'Hypothalamic Kernel'",
    "IV Fluid Injection: Restoring 'Liquid Cooling' and electrolyte balance",
    "Emergency Shelter: Bypassing the 'Terminal Burrowing' script to provide proper insulation"
  ],
  "prevention": [
    "Layered Redundancy: Using clothing that requires high 'Manual Dexterity' to remove"
  ]
}

"prosopagnosia_biometric_crash": {
  "description": "A cognitive disorder of face perception where the ability to recognize familiar faces, including one's own, is impaired, while other aspects of visual processing and intellectual functioning remain intact.",
  "symptoms": [
    "Identity Nullification: Faces appear as a collection of features without a 'Sum Identity'",
    "Metadata Dependency: Identifying targets via hair color, height, glasses, or voice (Heuristic-based ID)",
    "Social Navigation Errors: Failing to recognize significant nodes (partners, children, bosses) in public",
    "Internal Mirror Glitch: Inability to recognize the 'Self-Profile' in mirrors or photos",
    "Context Sensitivity: Recognizing a person at the 'Office' but failing to ID them at the 'Grocery Store'"
  ],
  "causes": [
    "Fusiform Gyrus Damage: Lesions or stroke in the occipitotemporal lobe",
    "Congenital Encoding Error: Hard-coded failure to develop the FFA 'Driver' from birth",
    "Neurodegenerative Decay: Progression of Alzheimer's or PCA affecting the ID-bus",
    "Temporal Lobe Trauma: Disrupting the link between visual data and emotional memory"
  ],
  "risk_factors": [
    "Genetic predisposition (Autosomal dominant traits in some families)",
    "Early childhood developmental delays in social-visual integration",
    "Vascular events in the posterior cerebral artery"
  ],
  "diagnosis": [
    "The Benton Facial Recognition Test (BFRT)",
    "The Cambridge Face Memory Test (CFMT): Assessing the ability to learn 'New Profiles'",
    "fMRI: Measuring 'Zero-Activation' in the FFA when presented with facial stimuli",
    "Differentiating from 'Object Agnosia' (Can they recognize a chair but not a face?)"
  ],
  "remedies": [
    "Metadata Cataloging: Training the brain to focus on 'Fixed Assets' (scars, birthmarks, unique jewelry)",
    "Algorithm Training: Using mnemonic devices to link voices to names",
    "System Transparency: Encouraging peers to 'Self-Identify' upon entering the user's proximity"
  ],
  "prevention": [
    "N/A for congenital cases; standard vascular health for acquired cases"
  ]
}
"aboulia_execution_latency": {
  "description": "A pathological inability to make decisions or initiate voluntary actions, ranging from subtle hesitation to a total lack of willpower.",
  "symptoms": [
    "Initiation Lag: Significant delay between a stimulus/intent and the resulting action",
    "Speech Latency: Long pauses before responding to simple queries",
    "Decision Paralysis: Inability to choose between two equally viable 'execution paths'",
    "Reduced Spontaneity: The system only runs 'Reactive' tasks, never 'Background' or self-generated ones",
    "Emotional Flatness: The 'Reward Driver' (Dopamine) fails to provide the necessary kickstart"
  ],
  "causes": [
    "Dopaminergic Path Collapse: Failure in the Mesocorticolimbic 'Incentive' bus",
    "Basal Ganglia Lesions: Damage to the 'Gatekeeper' that allows motor signals to pass",
    "Prefrontal Cortex Damage: Impairing the 'Executive Manager' responsible for goal-setting",
    "Post-Stroke Sequelae: Specifically in the Anterior Cingulate Cortex (ACC)"
  ],
  "risk_factors": [
    "Traumatic Brain Injury (TBI) targeting the frontal lobes",
    "Neurodegenerative diseases (Parkinson's, Huntington's)",
    "Severe chronic depression affecting the 'Motivation Kernel'"
  ],
  "diagnosis": [
    "The 'Reaction Time' Audit: Measuring the gap between command and execution",
    "Neuropsychological Scans: Checking for hypometabolism in the ACC and Striatum",
    "Motivation-Response Testing: Does the latency decrease if the 'Reward Value' increases?",
    "Differentiating from 'Apathy' (Which is a lack of caring) and 'Akinesia' (Which is a lack of movement)"
  ],
  "remedies": [
    "Dopamine Agonists: Chemically 'Overclocking' the initiation signal",
    "External Prompting: Using external 'Interrupts' (timers, alarms) to bypass the internal stall",
    "Cognitive-Motor Pacing: Breaking tasks into micro-instructions to lower the 'Initiation Cost'",
    "Environmental Enrichment: Increasing 'Input Signal' to force a response"
  ],
  "prevention": [
    "Standard neurological health maintenance and vascular protection"
  ]
}
"abilene_network_consensus_glitch": {
  "description": "A paradox in which a group of people collectively decide on a course of action that is counter to the preferences of many or all of the individuals in the group.",
  "symptoms": [
    "False Unanimity: The 'Network' reports 100% agreement despite 0% individual buy-in",
    "Mismanaged Agreement: The failure to communicate private 'Data Exceptions' to the group",
    "Post-Execution Blame: After the task fails, nodes reveal their original 'Dissent Logs'",
    "Social Friction Avoidance: Prioritizing 'Connection Stability' over 'Data Accuracy'",
    "The 'Road to Abilene' Effect: Committing resources to a 'Null Goal' that no one requested"
  ],
  "causes": [
    "Pluralistic Ignorance: Nodes incorrectly 'predict' the state of other nodes",
    "Inhibitory Signal Failure: Fear of being marked as a 'Bad Node' (social exclusion)",
    "Action Anxiety: The 'Processing Overhead' of speaking up feels higher than the cost of a bad decision",
    "Negative Fantasy: Modeling catastrophic 'System Crashes' that wouldn't actually occur"
  ],
  "risk_factors": [
    "High-cohesion groups with low 'Conflict Tolerance'",
    "Hierarchical networks where the 'Root Node' is perceived as rigid",
    "Time-critical environments where 'Signal Validation' is skipped for speed"
  ],
  "diagnosis": [
    "The 'Private vs. Public' Audit: Comparing individual logs against the 'Group Output'",
    "Communication Latency Analysis: Checking if dissenting signals were 'Dropped' or 'Filtered'",
    "Post-Action Retrospectives: Identifying the point of 'Logic Divergence'",
    "Byzantine Fault Testing: Checking if a single node's false signal corrupted the whole cluster"
  ],
  "remedies": [
    "Anonymous Voting: Removing the 'Social Overhead' from the data transmission",
    "Devil’s Advocate Protocol: Forcing a 'Dissent Signal' to test network stability",
    "Psychological Safety Patches: Lowering the 'Cost' of reporting a Data Exception",
    "Check-and-Balance Verification: Asking 'Does anyone actually want to do this?'"
  ],
  "prevention": [
    "Encouraging 'Red-Teaming' and diverse signal inputs to prevent echo-chamber loops"
  ]
}
"palinopsia_buffer_persistence": {
  "description": "The persistence or recurrence of a visual image after the stimulus has been removed.",
  "symptoms": [
    "Trailing: Moving objects leave a 'Motion Blur' or discrete 'Ghosting' path behind them",
    "Illusory Palinopsia: Images remain in the field of view for minutes or hours (The 'Burn-in' glitch)",
    "Light Streaking: Light sources leave long 'Smears' across the visual UI",
    "Categorical Recall: Seeing a pattern (like a grid) on one object and having it 'Leaking' onto every other object",
    "Decreased Contrast: The 'Ghost Images' can wash out real-time data"
  ],
  "causes": [
    "Toxicity: Specifically from SSRIs, Trazodone, or Topiramate (Software-induced lag)",
    "Migraine Aura: Temporary 'Circuit Jitter' in the occipital-parietal pathway",
    "Parietal Lobe Lesions: Damage to the 'Temporal Smoothing' hardware",
    "Tumors or Metabolic Shifts: Altering the 'Refresh Rate' of visual neurons"
  ],
  "risk_factors": [
    "Long-term use of specific psychiatric medications",
    "History of complex migraines",
    "Head trauma affecting the dorsal visual stream"
  ],
  "diagnosis": [
    "Visual Field Testing: Identifying if the persistence is localized or global",
    "Neuroimaging: Checking for 'Hot Spots' of activity in the visual cortex after the stimulus is gone",
    "Drug Screen: Auditing for 'Chemical Interference' in the neurotransmitter bus",
    "Differentiating from 'Hallucinations' (The user knows the image isn't really there)"
  ],
  "remedies": [
    "Medication Titration: Removing the 'Overtaxing' chemical patches",
    "Calcium Channel Blockers: To stabilize the 'Firing Threshold' of visual neurons",
    "Tinted Lenses: Reducing the 'Input Intensity' to lower the load on the buffer",
    "Time: Many cases are transient 'System Glitches' that self-resolve"
  ],
  "prevention": [
    "Monitoring 'System Load' when introducing new neurological medications"
  ]
}

"alien_hand_command_override": {
  "description": "A rare neurological disorder in which one hand functions involuntarily, with the victim feeling as though the hand is not part of their body and has a mind of its own.",
  "symptoms": [
    "Autonomous Motor Execution: The hand performs complex tasks (e.g., reaching for a cookie while the user is on a diet)",
    "Inter-manual Conflict: The 'Alien' hand actively works against the 'Primary' hand (e.g., one hand zips up a jacket while the other unzips it)",
    "Loss of Agency: The user perceives the hand as an external entity or 'stranger'",
    "Reflexive Grasping: The hand 'captures' objects and refuses to let go (Grasp Reflex)",
    "Intact Sensation: The user can feel the hand moving but cannot issue a 'Stop' command"
  ],
  "causes": [
    "Corpus Callosotomy: Disconnection of the 'Communication Bridge' between hemispheres",
    "Lesions in the Supplementary Motor Area (SMA): The hub for planning 'Internal' actions",
    "Anterior Cerebral Artery (ACA) Stroke: Starving the medial frontal lobes of power",
    "Neurodegenerative conditions (e.g., Creutzfeldt-Jakob or Corticobasal Degeneration)"
  ],
  "risk_factors": [
    "Brain surgery (specifically 'Split-brain' procedures)",
    "Vascular damage to the medial frontal cortex",
    "Tumors or trauma affecting the 'Inhibitory' motor loops"
  ],
  "diagnosis": [
    "Clinical Observation: Documenting 'Goal-Directed' vs. 'Random' movement",
    "MRI/CT: Identifying lesions in the Corpus Callosum or SMA",
    "Neuropsychological testing for 'Sense of Agency' thresholds",
    "EEG: Monitoring motor-readiness potentials (Bereitschaftspotential)"
  ],
  "remedies": [
    "Occupational Therapy: 'Task-specific' training to re-integrate the hand",
    "Sensory Distraction: Giving the 'Alien' hand an object to hold (The 'Fidget' patch)",
    "Visual Feedback: Using mirrors to 're-map' the hand to the self",
    "Physical Restraint: Using oven mitts or sleeves to limit the hand's 'Attack Surface'"
  ],
  "prevention": [
    "Minimizing surgical trauma to the corpus callosum and medial frontal lobes"
  ]
}
"cmmd_broadcast_override": {
  "description": "A condition in which intentional movements of one side of the body are accompanied by involuntary mirror movements of the other side.",
  "symptoms": [
    "Symmetric Mimicry: Wiggling left toes causes the right toes to wiggle identically",
    "Bilateral Deadlock: Difficulty with tasks requiring manual coordination (e.g., playing piano or typing)",
    "Muscle Fatigue: Double the 'Energy Consumption' for simple unilateral tasks",
    "Preserved Sensation: The 'Input' is fine, but the 'Output' is duplicated",
    "Logic Consistency: Mirroring is most prominent in distal muscles (fingers and toes)"
  ],
  "causes": [
    "DCC & RAD51 Gene Mutations: Errors in the 'Wiring Instructions' for the nervous system",
    "Failure of Decussation: Motor fibers fail to cross correctly in the Medulla (The 'Router' error)",
    "Incomplete Corpus Callosum Inhibition: The 'Inter-Hemispheric Bridge' fails to suppress the mirror signal",
    "Ipsilateral Tract Persistence: The brain maintains 'Wrong-Way' connections to the same side"
  ],
  "risk_factors": [
    "Genetic inheritance (Autosomal Dominant patterns)",
    "Early developmental 'Routing' failures in the corticospinal tract"
  ],
  "diagnosis": [
    "Electromyography (EMG): Detecting simultaneous 'Firing' in homologous muscles",
    "Transcranial Magnetic Stimulation (TMS): Observing bilateral 'Motor Evoked Potentials' from a single-side stimulus",
    "Genetic Sequencing: Looking for the 'RAD51' or 'DCC' patch errors",
    "Physical Coordination Audit"
  ],
  "remedies": [
    "Task Adaptation: Using tools that don't require independent hand movements",
    "Occupational Therapy: Developing 'Workarounds' for bilateral execution",
    "No 'Software Patch' currently exists for the hardware re-routing"
  ],
  "prevention": [
    "N/A; this is a 'Hard-Coded' architectural variation"
  ]
}
"confabulation_database_autofill": {
  "description": "The production of fabricated, distorted, or misinterpreted memories about oneself or the world, without the conscious intention to deceive.",
  "symptoms": [
    "Hallucinated Records: Creating entire events that never occurred to fill a gap in the logs",
    "Temporal Misplacement: Taking a real data point from 10 years ago and 'pasting' it into today’s record",
    "Lack of Error Detection: The user is $100\%$ certain the fabricated data is valid",
    "Provoked vs. Spontaneous: Can be triggered by a query (search) or occur as a background process",
    "Narrative Smoothing: The fabricated data is logically consistent with the user’s 'Current State'"
  ],
  "causes": [
    "Prefrontal Cortex (PFC) Failure: The 'Editor' or 'Validation Script' is offline",
    "Korsakoff’s Syndrome: Thiamine deficiency leading to severe database 'bit-rot'",
    "Anterior Communicating Artery (ACoA) Aneurysm: Damaging the 'Memory Indexing' hardware",
    "Dementia/Alzheimer's: General degradation of the 'Storage Clusters'"
  ],
  "risk_factors": [
    "Severe chronic alcohol consumption (Vitamin B1 depletion)",
    "Traumatic Brain Injury affecting the orbital-frontal circuits",
    "Advanced age-related memory degradation"
  ],
  "diagnosis": [
    "Source Monitoring Tests: Checking if the user can identify 'Where' a data point came from",
    "The 'D-E-S' Task: Identifying false recognition of 'lure' words in a list",
    "Neuroimaging: Observing low activity in the ventromedial prefrontal cortex (vmPFC)",
    "Collateral History: Checking the user's 'Output' against a 'Known Good' witness"
  ],
  "remedies": [
    "External Logging: Using 'Journaling' and 'Checklists' as a secondary hard drive",
    "Reality Orientation: Providing constant 'Sync Signals' (Clocks, Calendars, GPS)",
    "Memory Training: Strengthening the 'Source-Monitoring' filter through practice",
    "Nutritional Patching: Thiamine (B1) replacement to stop the hardware rot"
  ],
  "prevention": [
    "Adequate nutrition and protection against high-impact 'Hardware' damage"
  ]
}
"synesthesia_bus_crosstalk": {
  "description": "A neurological condition in which information meant to stimulate one of the senses stimulates several of them, creating a blended sensory experience.",
  "symptoms": [
    "Chromesthesia: Sound-to-color mapping (e.g., a C-sharp looks like neon violet)",
    "Grapheme-Color: Alphanumeric characters are perceived as inherently colored",
    "Lexical-Gustatory: Specific words trigger physical taste sensations (e.g., the word 'Logic' tastes like copper)",
    "Spatial Sequence: Numerical sequences or months appear as physical points in 3D space",
    "Mirror-Touch: Feeling the same physical sensation as another person (The 'Proxy-Input' glitch)"
  ],
  "causes": [
    "Hyper-connectivity: Failure of the 'Pruning Script' during early development, leaving too many neural bridges",
    "Cross-Activation: The 'Signal Firewall' between adjacent brain regions (like the V4 color area and the grapheme area) is porous",
    "Disinhibited Feedback: Higher-level cortical regions sending 'top-down' signals back to the wrong sensory entry point",
    "Transient Induction: Can be temporarily triggered by hallucinogenic 'Software Overwrites' or high-intensity meditation"
  ],
  "risk_factors": [
    "Genetic inheritance (Common in creative or 'High-Bandwidth' lineages)",
    "Neurodevelopmental variations where 'Signal Isolation' wasn't prioritized"
  ],
  "diagnosis": [
    "Consistency Testing: Checking if the mapping (e.g., 'A' = Red) remains identical over years",
    "Stroop-Style Interference Tests: Measuring 'Processing Lag' when the 'Real' color conflicts with the 'Synesthetic' color",
    "DTI (Diffusion Tensor Imaging): Identifying 'High-Density Cabling' between sensory hubs",
    "fMRI: Observing simultaneous activation of multiple sensory cortices from a single input"
  ],
  "remedies": [
    "N/A; usually categorized as a 'Feature' rather than a 'Bug'",
    "Sensory Management: Reducing 'Input Noise' to prevent cognitive fatigue",
    "Focus Training: Learning to ignore the 'Phantom Channels' during high-load tasks"
  ],
  "prevention": [
    "N/A; this is a 'Hard-Coded' architectural deviation"
  ]
}
"stendhal_aesthetic_overflow": {
  "description": "A psychosomatic disorder that causes rapid heartbeat, dizziness, fainting, confusion and even hallucinations when an individual is exposed to objects or phenomena of great personal significance or beauty.",
  "symptoms": [
    "Tachycardia: Sudden heart rate spike (System Overclocking)",
    "Syncope: Fainting or 'Power Cycling' due to autonomic overload",
    "Dissociative States: Feeling 'detached' from the hardware as the data stream peaks",
    "Euphoria/Panic Paradox: Simultaneous high-pleasure and high-threat signals",
    "Short-term Amnesia: Gaps in the 'Event Log' during the peak intensity of the experience"
  ],
  "causes": [
    "Limbic Hyper-activation: The 'Emotional Processor' cannot handle the packet density",
    "Thalamic Filtering Failure: The 'Signal Firewall' fails to suppress high-intensity beauty",
    "Vagus Nerve Over-stimulation: Leading to a sudden drop in blood pressure",
    "Cultural Priming: A 'Pre-loaded' expectation that increases the vulnerability of the node"
  ],
  "risk_factors": [
    "Sensitive 'Artistic' temperaments (High openness to experience)",
    "Travelers visiting high-density historical/artistic hubs (e.g., Florence, Paris)",
    "Underlying exhaustion or low 'System Battery' during the encounter"
  ],
  "diagnosis": [
    "Heart Rate Variability (HRV) Monitoring: Detecting sudden autonomic instability",
    "Clinical Interview: Identifying the 'Triggering Object' (e.g., a specific fresco or statue)",
    "Exclusion of 'Panic Disorder' (Which lacks the specific aesthetic trigger)",
    "Observation of recovery once the 'Visual Feed' is terminated"
  ],
  "remedies": [
    "Signal Isolation: Removing the user from the high-density environment",
    "Anxiolytics: Using chemical 'Dampeners' to lower the gain on the limbic system",
    "Grounding Exercises: Forcing the brain to process 'Low-Density' data (e.g., counting floor tiles)",
    "Hydration and Glucose: Restoring 'Hardware Stability'"
  ],
  "prevention": [
    "Pacing: Limiting 'Museum Cycles' to prevent data-stream saturation"
  ]
}
"cotards_profile_nullification": {
  "description": "A rare neuropsychiatric delusion in which the affected person holds the delusional belief that they are already dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Existential Negation: The core belief that the self has been 'Deleted' from reality",
    "Hypochondriacal Delusions: Claims that the stomach is missing or the heart has stopped",
    "Analgesia: A high threshold for physical pain (The system ignores 'Hardware Damage' alerts)",
    "Social Withdrawal: Disconnection from the 'Network' (Why interact if I don't exist?)",
    "Immortal Delusions: Paradoxically believing they cannot die because they are already dead"
  ],
  "causes": [
    "Amygdala-Sensory Disconnect: The emotional 'Validation Script' fails to fire for any internal stimuli",
    "Right Parietal Lobe Lesions: Disrupting the 'Spatial Self-Map'",
    "Severe Depression/Psychosis: A complete 'Logic-Level' shutdown of the reward and existence circuits",
    "Adverse Drug Reactions: Specifically linked to Acyclovir in patients with renal failure"
  ],
  "risk_factors": [
    "Schizophrenia or Bipolar Disorder",
    "Neurological trauma affecting the 'Identity-Emotion' pathway",
    "Severe metabolic imbalances affecting cortical 'Awareness' thresholds"
  ],
  "diagnosis": [
    "Clinical Interview: Identifying the 'Null-State' logic",
    "fMRI: Observing zero activity in the 'Self-Reference' nodes during introspection",
    "Metabolic Panel: Checking for 'System Toxins' that might be corrupting the logic",
    "Differentiating from 'Capgras Delusion' (Where others are fakes, here the *Self* is the fake)"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT): A 'Hard Reset' of the brain's electrical state",
    "Antipsychotic/Antidepressant Patches: Stabilizing the 'Neurotransmitter Bus'",
    "Reality Validation Therapy: Attempting to 'Re-sync' sensory input with emotional value"
  ],
  "prevention": [
    "Early intervention in severe mood disorders to prevent 'Existential Logic Collapse'"
  ]
}

"semantic_satiation_pointer_break": {
  "description": "A psychological phenomenon in which repetition causes a word or phrase to temporarily lose meaning for the listener, who then perceives the speech as meaningless sounds.",
  "symptoms": [
    "Meaning Decay: The rapid 'Erosion' of the link between a word and its definition",
    "Phonetic Alienation: The word begins to sound like an 'unrecognized' sound sequence",
    "Visual Fragmentation: If reading, the letters stop forming a 'concept' and become just 'shapes'",
    "The 'Jamais Vu' Effect: Feeling that a common word is suddenly 'New' or 'Incorrect'",
    "Rapid Recovery: The 'Pointer' re-establishes as soon as the repetition stops (Cache Refresh)"
  ],
  "causes": [
    "Reactive Inhibition: Specific neurons in the temporal lobe 'fire and tire' from rapid repetition",
    "Neural Adaptation: The brain's 'Delta-Detection' system stops reporting the word as 'Information' because it's too static",
    "Linguistic Saturation: Overloading the 'Signifier-Signified' bus"
  ],
  "risk_factors": [
    "High-speed proofreading or data entry",
    "Intense vocal rehearsal",
    "Neurodivergent focus patterns (Hyper-focus on specific strings)"
  ],
  "diagnosis": [
    "The 'Repetition Threshold' Test: Measuring how many cycles it takes for meaning to drop to zero",
    "Interference Tasks: Seeing if the 'Satiated' word still triggers related concepts",
    "Functional MRI: Showing decreased activity in the Left Inferior Prefrontal Cortex during satiation"
  ],
  "remedies": [
    "System Pause: Ceasing the repetition for 10-30 seconds",
    "Context Switching: Using the word in a completely different sentence/context",
    "Synonym Injection: Swapping the 'String' for an alternative to bypass the fatigued circuit"
  ],
  "prevention": [
    "Varied linguistic input to keep the 'Semantic Mapping' hardware fresh"
  ]
}

"aiws_viewport_scaling_error": {
  "description": "A disorienting neurological condition that affects human perception, causing objects or body parts to appear larger, smaller, closer, or further away than they actually are.",
  "symptoms": [
    "Micropsia: Objects appear unnaturally small (The 'Zoom Out' glitch)",
    "Macropsia: Objects appear unnaturally large (The 'Zoom In' glitch)",
    "Pelopsia: Objects appear closer than they are (The 'Depth Buffer' error)",
    "Teleopsia: Objects appear much further away (The 'Field of View' error)",
    "Metamorphopsia: Linear lines appear wavy or distorted",
    "Time Distortion: The 'Clock Speed' feels altered (Time seems to move too fast or too slow)"
  ],
  "causes": [
    "Migraine Aura: The most common trigger; an electrical wave 'resetting' the visual cortex",
    "Epstein-Barr Virus (EBV): Systemic infection affecting the central nervous system",
    "Temporal Lobe Epilepsy: Electrical 'Jitter' in the spatial-processing circuits",
    "Parietal Lobe Lesions: Damage to the 'Spatial Mapping' hardware"
  ],
  "risk_factors": [
    "Family history of migraines",
    "Childhood development (often resolves as the 'Hardware' matures)",
    "High-stress environments affecting sensory integration"
  ],
  "diagnosis": [
    "The Amsler Grid Test: Identifying 'Coordinate Distortion'",
    "EEG: Checking for 'Signal Noise' (epileptic activity)",
    "MRI: Ruling out structural damage to the Parietal-Occipital junction",
    "Clinical History: Tracking the 'Scaling Episodes' relative to migraines"
  ],
  "remedies": [
    "Trigger Management: Identifying and patching migraine or seizure triggers",
    "Rest and Sensory Deprivation: Turning off the 'Video Feed' to allow the system to recalibrate",
    "Pharmacological Stability: Anti-convulsants or migraine-preventative patches"
  ],
  "prevention": [
    "Maintaining stable sleep cycles and hydration to prevent 'Aura' events"
  ]
}
"tinnitus_gain_feedback_loop": {
  "description": "The perception of noise or ringing in the ears when no external sound is present, caused by maladaptive neural plasticity in the auditory pathway.",
  "symptoms": [
    "Phantom Tones: Persistent ringing, buzzing, roaring, or clicking in the 'Audio Feed'",
    "Hyperacusis: Sensitivity to normal sounds (The 'Gain' is set too high for everyone)",
    "Frequency Selective: Often matches the specific frequency 'Bin' where hearing loss occurred",
    "Psychological Load: Increased 'CPU' usage leads to anxiety, fatigue, and loss of focus",
    "Reactive Tinnitus: The 'Phantom Signal' gets louder in response to external noise"
  ],
  "causes": [
    "Cochlear Hardware Damage: Loss of hair cells (The 'Sensors') due to noise or age",
    "Central Gain Increase: The Auditory Cortex 'cranking the volume' to find a missing signal",
    "Somatosensory Crosstalk: Nerve signals from the jaw (TMJ) or neck 'leaking' into the audio bus",
    "Limbic Integration: The 'Emotional Processor' tagging the phantom noise as a 'Threat'"
  ],
  "risk_factors": [
    "Exposure to high-decibel 'Data Spikes' (Loud music, machinery)",
    "Ototoxic medications that 'Corrupt' the inner ear sensors",
    "High systemic stress levels that lower the 'Noise Floor' of the brain"
  ],
  "diagnosis": [
    "Audiometry: Identifying the 'Frequency Gap' where the sensor is broken",
    "Tinnitus Pitch Matching: Identifying the exact 'Tone' of the glitch",
    "Tympanometry: Checking the physical 'Hardware' of the middle ear",
    "fMRI: Observing hyper-activity in the Auditory Cortex and Thalamus"
  ],
  "remedies": [
    "Sound Masking: Providing 'External White Noise' to satisfy the Gain Control",
    "Tinnitus Retraining Therapy (TRT): Teaching the 'Logical Auditor' to ignore the signal",
    "Notched Music Therapy: Listening to audio with the 'Glitch Frequency' filtered out",
    "Cognitive Behavioral Therapy (CBT): Desensitizing the Limbic System to the 'Alarm' signal"
  ],
  "prevention": [
    "Using 'Hardware Firewalls' (Earplugs) in high-noise environments",
    "Avoiding 'System Overclocking' (Extreme stress and lack of sleep)"
  ]
}


"akinetopsia_frame_rate_crash": {
  "description": "A neuropsychological disorder in which a patient cannot perceive motion in their visual field, despite being able to see stationary objects without issue.",
  "symptoms": [
    "Stroboscopic Vision: Moving objects appear as a series of frozen snapshots",
    "Motion Trails: Seeing multiple 'Residual Frames' of an object as it moves",
    "Disappearing Objects: A car may be far away in one frame and suddenly right in front of the user in the next",
    "Inability to Track Flow: Extreme difficulty pouring liquids (the 'Water' looks like a frozen glacier)",
    "Social Lag: Difficulty reading facial expressions because the subtle motion of muscles is 'skipped'"
  ],
  "causes": [
    "Bilateral lesions in the V5/MT (Middle Temporal) complex",
    "Stroke in the Posterior Cerebral Artery (PCA) or Middle Cerebral Artery (MCA) territories",
    "Traumatic Brain Injury (TBI) to the lateral-posterior cortex",
    "Transient induction via high-dose antidepressant toxicity or certain seizures"
  ],
  "risk_factors": [
    "Neurodegenerative diseases affecting the dorsal stream",
    "Vascular instability in the visual processing hubs",
    "Severe poisoning (e.g., carbon monoxide) targeting high-metabolic motion neurons"
  ],
  "diagnosis": [
    "The 'Moving Dot' Test: Identifying thresholds for direction and speed",
    "fMRI: Measuring 'Zero Activation' in the V5 area during motion stimuli",
    "Visual Evoked Potentials (VEP) to check signal timing",
    "Perimetric testing to rule out simple 'Blind Spots' (Scotomas)"
  ],
  "remedies": [
    "Rhythm-Based Navigation: Using sound or 'Ticks' to estimate speed",
    "Visual Pacing: Moving the head slowly to 'Force-Refresh' the static frames",
    "Safety Protocols: Avoiding high-velocity environments (crossing busy streets)",
    "Pharmacological Adjustment: If the glitch is induced by chemical toxicity"
  ],
  "prevention": [
    "Standard cardiovascular maintenance and head protection"
  ]
}

"mpi_network_entropy": {
  "description": "The rapid spread of illness signs and symptoms affecting members of a cohesive group, originating from a nervous system disturbance involving no corresponding organic etiology.",
  "symptoms": [
    "Rapid Onset: Symptoms spread through a group in minutes or hours",
    "Mimicry: Twitching, fainting, dizziness, or respiratory 'Jitter' that looks like a virus",
    "Node Clustering: Spread usually occurs in closed environments (schools, offices, factories)",
    "Phantom Triggers: Often attributed to a 'Smell' or 'Toxin' that sensors cannot detect",
    "Recovery: Symptoms usually vanish once the 'Nodes' are isolated from the network"
  ],
  "causes": [
    "Mirror Neuron Hyper-activation: The 'Mirror Driver' executing observed code",
    "High Network Latency/Stress: Excessive background 'System Load' in the group",
    "Shared Belief Systems: A common 'Security Protocol' that makes nodes vulnerable to the same rumor",
    "Prefrontal 'Filter' Failure: The inability to distinguish between 'External Observation' and 'Internal State'"
  ],
  "risk_factors": [
    "Cohesive social groups with high levels of mutual observation",
    "Recent shared trauma or high-stress 'Compute cycles'",
    "Digital Hyper-connectivity (Social-media induced 'Virtual MPI')"
  ],
  "diagnosis": [
    "Cluster Analysis: Identifying that the symptoms don't follow biological 'Infection' paths",
    "Environmental Audit: Ruling out actual hardware toxins (CO2, gas leaks)",
    "Observation of 'Spread Dynamics': Does it spread faster when people are watching?"
  ],
  "remedies": [
    "Network Segmentation: Separating the 'Nodes' to stop the propagation",
    "System Reassurance: Providing a 'Clear' status report to lower anxiety gain",
    "Filter Training: Strengthening the 'Logical Auditor' to ignore false peer-signals"
  ],
  "prevention": [
    "Maintaining low-stress 'Network Environments' and transparent communication"
  ]
}

"dissociative_fugue_profile_migration": {
  "description": "A rare dissociative disorder characterized by reversible amnesia for personal identity, including the memories, personality, and other identifying characteristics of individuality.",
  "symptoms": [
    "Identity Nullification: Sudden loss of the 'Primary Key' (Name, Family, History)",
    "Unauthorized Travel: Unexpected journey away from the 'Home Directory' (Home/Work)",
    "Profile Substitution: Adoption of a new identity (often more outgoing or simple)",
    "Preserved Procedural Memory: Retaining 'System Skills' like driving, speaking, or coding",
    "Post-Episode Recovery: Sudden 'Re-authentication' of the old profile, often followed by amnesia of the 'Fugue Partition'"
  ],
  "causes": [
    "Severe Stress-Induced Disconnection: A 'Safety Shutdown' of the Hippocampal-Prefrontal bus",
    "Extreme Emotional Trauma: Overloading the 'Identity Controller' until it crashes",
    "Inhibited Retrieval: The frontal lobe actively 'Write-Protects' the old memory sectors",
    "Neurological Instability: Related to temporal lobe activity or limbic system spikes"
  ],
  "risk_factors": [
    "Exposure to severe trauma (natural disasters, war, personal loss)",
    "Pre-existing dissociative tendencies",
    "Extreme internal conflict regarding the current 'User Role'"
  ],
  "diagnosis": [
    "The 'Missing Person' Audit: Identifying the gap between physical location and identity",
    "Psychiatric Evaluation: Differentiating from 'Malingering' or 'Dementia'",
    "Brain Imaging: Often showing decreased metabolic activity in the prefrontal and temporal regions",
    "Hypnosis or Amobarbital Interviews: Attempting to 'Mount' the hidden identity partition"
  ],
  "remedies": [
    "Psychotherapy: Safely 'Re-mounting' the old identity data",
    "Environment Stabilization: Providing a 'Safe Boot' environment to lower stress",
    "Clinical Integration: Merging the 'Fugue' memories with the 'Primary' profile",
    "Stress-management 'Patching' to prevent future crashes"
  ],
  "prevention": [
    "Trauma-informed care and early intervention for 'Identity Overload'"
  ]
}

"fregoli_identity_aliasing": {
  "description": "A rare disorder in which a person holds a delusional belief that different people are in fact a single person who changes appearance or is in disguise.",
  "symptoms": [
    "Global Identity Mapping: Assigning the 'Identity' of a known person to multiple strangers",
    "Hyper-Familiarity: A misplaced sense of 'knowing' someone they have never met",
    "Paranoia: Often believing the 'duplicated' person is following or spying on them",
    "Visual-Semantic Overload: The 'Face Recognition' system is constantly triggering the 'Identity Record'",
    "Intact Logic: The user can see the physical differences (hair color, height) but dismisses them as 'disguise tech'"
  ],
  "causes": [
    "Lesions in the Right Temporoparietal Junction (Identity Verification Hub)",
    "Hyper-connectivity between the Fusiform Face Area (FFA) and the Amygdala",
    "Dopamine Overdrive: Excessive signaling in the 'Meaning-Making' circuits",
    "Traumatic Brain Injury (TBI) affecting the right hemisphere's 'Global Context' centers"
  ],
  "risk_factors": [
    "Schizophrenia or Bipolar Disorder (affecting 'Reality Filtering')",
    "Neurodegeneration in the right frontal or temporal lobes",
    "Post-seizure 'Electrical Storms' in the limbic system"
  ],
  "diagnosis": [
    "The 'Familiarity Rating' Test (Measuring emotional response to strangers)",
    "fMRI during face-viewing to detect 'Spurious Hits' in the Amygdala",
    "Neuropsychological evaluation for 'Source Monitoring' failures",
    "MRI to check for lesions in the Right Fusiform Gyrus"
  ],
  "remedies": [
    "Antipsychotics (Dopamine antagonists) to lower the 'Meaning-Signal' gain",
    "Cognitive Behavioral Therapy (CBT): Teaching the 'Auditor' to challenge the 'Mapping Error'",
    "Visual Verification: Using non-facial markers (gait, voice) to break the 'Face Loop'",
    "Environment Control: Minimizing exposure to large crowds (Reducing 'Input Noise')"
  ],
  "prevention": [
    "Maintaining neural stability and monitoring neurochemical balance"
  ]
}
"cotard_null_identity": {
  "description": "A rare neuropsychiatric delusion in which the affected person holds the delusional belief that they are already dead, do not exist, are putrefying, or have lost their blood or internal organs.",
  "symptoms": [
    "Nihilistic Delusion: Absolute conviction that the 'Self' is a null set",
    "Biological Denial: Insisting that they don't need to eat because they have no stomach",
    "Analgesia: A high threshold for pain because 'dead things don't feel'",
    "Chronic Depression: A total collapse of the 'Reward/Motivation' circuits",
    "Immortality Paradox: Ironically, some believe they cannot die because they are already dead"
  ],
  "causes": [
    "Disconnection between the Fusiform Gyrus (Recognition) and the Amygdala (Emotion)",
    "Right Parietal Lobe atrophy (Failure of the 'Body Schema' map)",
    "Severe hypermetabolism in the 'Default Mode Network'",
    "Adverse reactions to Acyclovir (in rare cases of renal failure)"
  ],
  "risk_factors": [
    "Severe clinical depression with psychotic features",
    "Schizophrenia (affecting reality-testing filters)",
    "Neurological trauma to the right hemisphere"
  ],
  "diagnosis": [
    "Clinical Interview for Nihilistic Themes",
    "PET Scans: Often showing 'Cold Spots' (hypometabolism) in the frontal and parietal regions",
    "Exclusion of 'Depersonalization Disorder' (Feeling unreal vs. Believing one is dead)",
    "Assessment of the 'Body Ownership' circuits"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT): Often the most effective 'Hard Reboot' for this glitch",
    "Antipsychotics and Antidepressants to re-balance the 'Limbic Gain'",
    "Reality-Anchoring Therapy",
    "Treating underlying medical triggers (e.g., kidney function/viral load)"
  ],
  "prevention": [
    "Aggressive management of severe mood disorders"
  ]
}

"synesthesia_signal_crosstalk": {
  "description": "A perceptual phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway.",
  "symptoms": [
    "Chromesthesia: Hearing sounds (music, voices) and seeing specific 'Color Shaders' in the visual field",
    "Grapheme-Color: Associating specific letters or numbers with fixed, consistent colors",
    "Lexical-Gustatory: Experiencing specific 'Flavors' on the tongue when hearing or reading certain words",
    "Spatial Sequence: Seeing numerical sequences (months, years) as physical shapes in 3D space",
    "Consistency: The 'Mapping' is immutable; if 'A' is red today, it will be red in 40 years"
  ],
  "causes": [
    "Reduced Synaptic Pruning: Failure to 'Trim' the neural connections between adjacent cortical areas during development",
    "Cross-Activation: Direct 'Signal Bleed' between the V4 color area and the Visual Word Form Area (VWFA)",
    "Disinhibited Feedback: Failure of the 'Top-Down' filters to suppress sensory crosstalk",
    "Hyper-connectivity in the 'Feature Integration' zones of the Parietal Lobe"
  ],
  "risk_factors": [
    "Genetic predisposition (often runs in 'Creative' or 'Systemizing' families)",
    "Neurodivergence (high correlation with the Autism Spectrum)",
    "Temporary induction via hallucinogens (serotonin 2A receptor agonists)"
  ],
  "diagnosis": [
    "Consistency-over-Time Test: Verifying that the mapping hasn't changed over months/years",
    "fMRI: Observing simultaneous activation in two 'Unrelated' sensory modules (e.g., Auditory Cortex and V4 Color Area)",
    "Stroop Task Variance: Slower response times when a grapheme is presented in a 'Conflicting' color"
  ],
  "remedies": [
    "None required: Usually viewed as an 'Enhanced Feature' rather than a 'Critical Bug'",
    "Sensory Management: Reducing 'Input Noise' to prevent 'Visual/Flavor Overload'",
    "Mnemonic Utilization: Using the 'Crosstalk' as a high-speed indexing system for memory"
  ],
  "prevention": [
    "N/A; it is a fundamental 'Hard-Wiring' variation"
  ]
}
"catatonia_state_deadlock": {
  "description": "A complex behavioral syndrome characterized by abnormal movements, immobility, abnormal behaviors, and withdrawal.",
  "symptoms": [
    "Waxy Flexibility: The body stays in whatever position it is placed in (Mannequin Mode)",
    "Stupor: No psychomotor activity; no interaction with the environment",
    "Mutism: Little to no verbal output despite intact vocal hardware",
    "Negativism: Opposition or no response to instructions or external stimuli",
    "Catalepsy: Passive induction of a posture held against gravity",
    "Excited Catatonia: Paradoxical 'State Jitter'—purposeless, excessive motor activity"
  ],
  "causes": [
    "GABA-A Receptor Down-regulation: A failure in the 'Inhibitory Bus'",
    "Dopamine D2 Blockade: Sudden 'Driver Crash' in the basal ganglia",
    "Glutamate Storms: Over-excitation leading to a 'Safety Shutdown' of the motor cortex",
    "Underlying psychiatric 'Kernel Panics' (Schizophrenia, Bipolar, or MDD)"
  ],
  "risk_factors": [
    "Severe mood disorder instability",
    "Sudden withdrawal from GABA-ergic medications (e.g., Benzodiazepines)",
    "Neuroleptic Malignant Syndrome (High-toxicity hardware failure)"
  ],
  "diagnosis": [
    "The Bush-Francis Catatonia Rating Scale (BFCRS)",
    "The 'Lorazepam Challenge': Injecting a GABA agonist to see if the 'State Machine' resets",
    "EEG to rule out 'Non-Convulsive Status Epilepticus'",
    "Metabolic screening to check for 'Systemic Power' issues"
  ],
  "remedies": [
    "GABA Modulation: Using Lorazepam to 'unstick' the motor-inhibitory loops",
    "Electroconvulsive Therapy (ECT): A high-voltage 'System Reboot' of the thalamocortical loops",
    "NMDA Antagonists: Modulating the glutamate 'Noise' in the system"
  ],
  "prevention": [
    "Careful management of neuroleptic titration and GABA-ergic stability"
  ]
}


"bppv_imu_contamination": {
  "description": "A common vestibular disorder caused by displaced calcium carbonate crystals in the inner ear, resulting in brief episodes of intense vertigo.",
  "symptoms": [
    "Rotational Vertigo: Feeling like the room is 'spinning' at high RPM",
    "Positional Trigger: Symptoms only occur when changing head orientation (e.g., rolling over in bed)",
    "Nystagmus: The 'Eye Flicker'—the brain tries to track the 'phantom' motion by jerking the eyes",
    "Nausea/Emesis: The 'Motion Sickness' script triggers because the sensor data is internally inconsistent",
    "Postural Instability: A temporary loss of the 'Gravity Vector'"
  ],
  "causes": [
    "Otoconia Displacement: Calcium crystals (the 'Hardware Weights') falling into the semicircular canals",
    "Head Trauma: A physical shock that 'shakes' the sensors loose",
    "Age-related Degradation: Weakening of the 'Glue' (gelatinous membrane) holding the crystals in place",
    "Inner ear infections or long-term bed rest"
  ],
  "risk_factors": [
    "High-impact sports or accidents",
    "Osteoporosis (affecting crystal density)",
    "Genetic predisposition to vestibular instability"
  ],
  "diagnosis": [
    "The Dix-Hallpike Maneuver: A 'Stress Test' designed to trigger the glitch and observe eye movement",
    "Videonystagmography (VNG): Recording the 'Eye-Flicker' logs to identify which 'Channel' is contaminated",
    "Exclusion of Central Vertigo (ensuring the 'Processor' isn't the problem, just the 'Sensor')"
  ],
  "remedies": [
    "The Epley Maneuver: A sequence of 'Hardware Tilts' designed to use gravity to wash the crystals back into place",
    "Vestibular Rehabilitation: 'Re-calibrating' the brain to ignore the noise from the broken sensor",
    "Hydration and electrolyte management"
  ],
  "prevention": [
    "Head protection during high-velocity activities",
    "Maintaining Vitamin D and Calcium levels to keep the 'Weights' stable"
  ]
}
"hyperlexia_parser_uncoupled": {
  "description": "A condition characterized by an advanced ability to read words, significantly above what is expected for the child's age, often accompanied by difficulties in understanding or using verbal language.",
  "symptoms": [
    "High-Speed Decoding: Reading complex text at a professional level by age 3-4",
    "Compulsive Parsing: An intense, obsessive preoccupation with letters, numbers, and symbols",
    "Semantic Null: The ability to read a paragraph aloud with perfect phonetics but zero comprehension",
    "Echolalia: Repeating 'Parsed Packets' of speech (scripts) without understanding context",
    "Asynchronous Development: Exceptional 'Visual-Textual' skills paired with 'Social-Linguistic' deficits"
  ],
  "causes": [
    "Hyper-connectivity in the Left Angular Gyrus (The 'Symbolic Mapper')",
    "Early specialization of the Visual Word Form Area (VWFA)",
    "Neurodivergent architectural shift (often associated with the Autism Spectrum)",
    "Accelerated 'Pattern Recognition' at the expense of 'Abstract Integration'"
  ],
  "risk_factors": [
    "Genetic predisposition to 'Systemizing' vs. 'Empathizing' brain types",
    "Premature activation of the reading sub-circuits before the 'Limbic-Social' circuits are online"
  ],
  "diagnosis": [
    "Reading Level vs. Comprehension Level gap (The 'Delta Test')",
    "Social-Communication Screening",
    "Eye-tracking during reading (Observing the 'High-Speed Scanner' behavior)",
    "MRI to identify hyper-density in the posterior-temporal regions"
  ],
  "remedies": [
    "Semantic-First Training: Forcing the 'Parser' to pause and map words to visual images",
    "Social Scripting: Using the high-speed 'Text Database' to learn social rules via 'Algorithm'",
    "Visual-Aids: Linking the 'String' to a 'JPEG' (Picture) to bypass the missing auditory link"
  ],
  "prevention": [
    "N/A; it is a 'Factory-Set' architectural variation"
  ]
}

"tga_buffer_flush": {
  "description": "A sudden, temporary episode of memory loss that can't be attributed to a more common neurological condition, such as epilepsy or a stroke.",
  "symptoms": [
    "Anterograde Amnesia: Total inability to form new memories during the attack",
    "Repetitive Querying: Asking 'Where am I?' or 'What happened?' every 60 seconds",
    "Preserved Identity: The user knows their name, profession, and family members",
    "Preserved Complex Skills: Ability to drive, cook, or code during the episode",
    "Retrograde Window: Brief loss of memories from the few hours preceding the glitch",
    "Duration: Typically resolves within 6 to 24 hours (The 'System Reboot')"
  ],
  "causes": [
    "Temporary Ischemia (Low power) in the CA1 region of the Hippocampus",
    "Venous Congestion: A 'Backflow' of blood causing a temporary pressure spike",
    "Triggers: Sudden immersion in cold/hot water, extreme physical exertion, or high-stress 'Emotional Spikes'",
    "Glutamate Storm: Over-excitation of the memory-encoding circuits"
  ],
  "risk_factors": [
    "History of Migraines (The 'Vascular Stability' bug)",
    "Age > 50 (System hardware wear and tear)",
    "Recent Valsalva maneuvers (Sudden internal pressure changes)"
  ],
  "diagnosis": [
    "The 'Persistent Loop' observation (The hallmark behavioral log)",
    "High-resolution MRI (DWI) showing 'Punctate Spots' in the Hippocampus",
    "EEG to rule out 'Seizure-based' data corruption",
    "Exclusion of 'Alcohol-induced' buffer wipes (Blackouts)"
  ],
  "remedies": [
    "Time: The system usually performs a self-healing 'Reboot' within 24 hours",
    "Monitoring: Ensuring no concurrent 'Hardware' failure (Stroke)",
    "Reassurance: Providing a 'Status Report' to the user to lower anxiety levels"
  ],
  "prevention": [
    "Avoiding sudden, extreme physiological shocks if the 'Vascular Bus' is unstable"
  ]
}
"visual_agnosia_inference_error": {
  "description": "An impairment in recognition of visually presented objects, not due to a deficit in vision, language, or memory.",
  "symptoms": [
    "Apperceptive Agnosia: Failure in 'Preprocessing' (Inability to perceive the structure or shape of an object)",
    "Associative Agnosia: Failure in 'Database Query' (Perceiving the shape but failing to link it to its meaning)",
    "Object-to-Label Mismatch: Correctly tracing the outline of a 'spoon' but guessing it's a 'paddle'",
    "Sensory Substitution: Instant recognition if the user touches the object (using the Haptic Driver)",
    "Prosopagnosia (#1): A specialized sub-class targeting the 'Face' recognition library"
  ],
  "causes": [
    "Lesions in the Occipito-Temporal Border (The 'Lateral Occipital Complex')",
    "Carbon Monoxide Poisoning (targeting the high-metabolic recognition neurons)",
    "Stroke in the Posterior Cerebral Artery (PCA)",
    "Hypoxic-Ischemic Encephalopathy (System-wide power dip)"
  ],
  "risk_factors": [
    "Bilateral damage to the ventral visual stream",
    "Post-surgical complications in the temporal-occipital junction",
    "Severe head trauma affecting the 'Feature Integration' hubs"
  ],
  "diagnosis": [
    "The 'Object Drawing' Test (Can they copy a picture of an anchor without knowing what it is?)",
    "Overlapping Figures Test (Can they separate multiple objects in one image?)",
    "fMRI to monitor the 'Inference Engine' during image categorization",
    "Visual-to-Semantic matching tasks"
  ],
  "remedies": [
    "Multi-Modal Tagging: Using touch or sound to 're-identify' the world",
    "Environmental Simplification: Using high-contrast, 'Unique-Key' labels on household items",
    "Contextual Inference training: Using surrounding data (e.g., 'If it's on the stove, it's a pot')"
  ],
  "prevention": [
    "Neurological protection and standard vascular health"
  ]
}

"apraxia_motor_program_error": {
  "description": "A neurological disorder characterized by the inability to perform learned, purposeful movements despite having the physical ability and desire to do so.",
  "symptoms": [
    "Ideomotor Failure: Inability to mimic gestures (e.g., 'Wave goodbye') on command",
    "Ideational Error: Losing the 'Object Logic' (e.g., trying to use a toothbrush as a spoon)",
    "Sequence Corruption: Performing steps of a task in the wrong order (e.g., putting shoes on before socks)",
    "Clumsy Tool Handling: Holding a hammer by the wrong end despite knowing what it is",
    "Verbal Apraxia: The 'Speech Hardware' is fine, but the 'Articulatory Script' is lost"
  ],
  "causes": [
    "Lesions in the Left Posterior Parietal Cortex (The 'Procedural Database')",
    "Damage to the Premotor Cortex (The 'Command Assembler')",
    "Stroke in the Middle Cerebral Artery (MCA) territory",
    "Neurodegenerative diseases like Corticobasal Degeneration (CBD)",
    "Corpus Callosum disconnection (preventing the 'Admin' from sending scripts to the right hand)"
  ],
  "risk_factors": [
    "History of left-hemisphere stroke",
    "Head trauma involving the parietal or frontal lobes",
    "Progressive cognitive decline affecting 'Action Knowledge'"
  ],
  "diagnosis": [
    "Pantomime tasks (e.g., 'Show me how you would use a saw')",
    "Imitation of meaningless gestures (testing 'Real-Time Encoding')",
    "Multi-step assembly tests (e.g., folding a letter and placing it in an envelope)",
    "MRI/CT to identify 'Null Zones' in the motor planning network"
  ],
  "remedies": [
    "Occupational Therapy (OT) using 'Errorless Learning' to rebuild scripts",
    "Sensory Cueing: Using rhythmic beats or visual prompts to bypass the missing library",
    "Gestural Training: Re-associating physical movements with semantic meaning",
    "Augmentative and Alternative Communication (AAC) for verbal variants"
  ],
  "prevention": [
    "Standard neurological maintenance and vascular health"
  ]
}
"cerebral_achromatopsia_v4_crash": {
  "description": "An acquired form of color blindness caused by damage to the cerebral cortex, rather than abnormalities in the cells of the retina.",
  "symptoms": [
    "Total Grayscale Vision: The world is perceived in shades of gray, black, and white",
    "Dirty/Muddy Perception: Some users report colors looking 'washed out' or like 'lead'",
    "Loss of Color Memory: Inability to remember what colors used to look like",
    "Hemiachromatopsia: If the lesion is unilateral, only half the visual field is grayscale",
    "Preserved Acuity: Sharpness, depth, and motion detection remain at 100% functionality"
  ],
  "causes": [
    "Bilateral lesions in the Ventral Occipito-Temporal Cortex (Area V4)",
    "Stroke in the Posterior Cerebral Artery (PCA) territory",
    "Traumatic Brain Injury (TBI) to the base of the Occipital Lobe",
    "Transient ischemia during severe migraine 'Aura' events"
  ],
  "risk_factors": [
    "Vascular disease affecting the posterior circulation",
    "Carbon monoxide poisoning (specifically targeting the sensitive V4 neurons)",
    "Tumors in the ventral visual stream"
  ],
  "diagnosis": [
    "Ishihara Plate Test (Testing for basic color detection)",
    "The Farnsworth-Munsell 100 Hue Test (Testing for color discrimination/sorting)",
    "fMRI showing 'Null Activation' in the V4 complex during color-rich stimuli",
    "MRI to identify localized 'Infarct Zones' in the Lingual and Fusiform gyri"
  ],
  "remedies": [
    "Chromostereopsis training: Using depth and texture to identify objects",
    "External Metadata: Using 'Color-to-Sound' sensors to identify objects",
    "High-Contrast environments to maximize edge-detection utility",
    "Lifestyle Adaptation: Labeling clothing and food by 'Metadata' (text) rather than hue"
  ],
  "prevention": [
    "Standard stroke prevention and cardiovascular maintenance"
  ]
}


"astereognosis_haptic_fail": {
  "description": "The inability to identify an object by active touch of the hands without visual or auditory input, despite intact primary sensation.",
  "symptoms": [
    "Object Identity Null: Feeling all physical properties but failing to 'name' the object",
    "Manual Search Failure: Inability to find a specific item in a bag or pocket by touch alone",
    "Texture-Shape Dissociation: Being able to describe a 'smooth sphere' but not recognizing a 'marble'",
    "Bilateral or Unilateral: Depending on the lesion, it may affect only one hand (the 'Port' is down)",
    "Preserved Sensation: $100\%$ accuracy in detecting pain, heat, and vibration"
  ],
  "causes": [
    "Lesions in the Superior Parietal Lobule (The 'Haptic Integration Hub')",
    "Damage to the Secondary Somatosensory Cortex (S2)",
    "Posterior Cerebral Artery (PCA) strokes affecting the parietal association areas",
    "Neurodegeneration (Corticobasal Degeneration) causing 'Alien Hand' variants (#86)"
  ],
  "risk_factors": [
    "Parietal lobe tumors or trauma",
    "Vascular incidents in the non-dominant hemisphere",
    "Chronic demyelinating diseases affecting high-order integration"
  ],
  "diagnosis": [
    "The 'Hidden Object' Test: Asking the user to identify common items (coin, key, paperclip) with eyes closed",
    "Two-Point Discrimination: Testing if the 'Primary Sensors' are still high-resolution",
    "MRI/fMRI to locate the 'Broken Link' in the parietal association pathways",
    "Graphesthesia Test: Testing if the user can recognize a number 'written' on their palm"
  ],
  "remedies": [
    "Visual Compensation: 'Looking' at the object to provide the missing metadata",
    "Haptic Re-training: Repetitive 'Touch-and-See' exercises to rebuild the mapping",
    "Sensory Substitution: Using other senses to build a 'Tactile Proxy'",
    "Occupational Therapy for functional safety"
  ],
  "prevention": [
    "Standard stroke prevention and protection against head trauma"
  ]
}

"anton_babinski_syndrome": {
  "description": "A rare symptom of brain damage occurring in the occipital lobe where those who are blind deny their blindness.",
  "symptoms": [
    "Anosognosia: Total lack of awareness of a deficit (denying blindness)",
    "Confabulation: Inventing detailed visual descriptions of the environment to 'prove' sight",
    "Collision Denial: Blaming furniture or low lighting for walking into walls",
    "Persistent Visual Hallucinations (Charles Bonnet-style) that the user accepts as reality",
    "Aggressive defense of the 'Vision' status when challenged"
  ],
  "causes": [
    "Bilateral Occipital Lobe damage (often via stroke or TBI)",
    "Disconnection between the Visual Cortex and the 'Reality-Monitoring' circuits in the Frontal Lobe",
    "Damage to the Association Cortex that integrates sensory 'Health Reports'",
    "Failure of the 'Error-Detection' loop in the Parietal Lobe"
  ],
  "risk_factors": [
    "Ischemic stroke in the Posterior Cerebral Artery (PCA)",
    "Severe head trauma affecting the back of the skull",
    "Advanced neurodegeneration affecting global cognitive monitoring"
  ],
  "diagnosis": [
    "The 'Flashlight Test' (Asking the user to count fingers while blind)",
    "MRI/CT scans showing bilateral occipital infarction",
    "Neurological testing for 'Source Monitoring' failures",
    "Observation of 'Visual Confabulation' under stress"
  ],
  "remedies": [
    "None to restore sight if the hardware is destroyed",
    "Occupational Therapy for 'Compensatory Safety'",
    "Antipsychotics (rarely) to reduce the intensity of confabulations",
    "Gentle Reality-Testing (helping the brain 'Accept' the NULL signal)"
  ],
  "prevention": [
    "Management of vascular health to prevent bilateral strokes"
  ]
}
"akinetopsia_frame_skip": {
  "description": "A rare neuropsychological disorder in which a patient cannot perceive motion in their visual field, despite being able to see stationary objects.",
  "symptoms": [
    "Strobe-Vision: The world appears as a sequence of still images",
    "Motion Trails: Seeing multiple 'Ghost' frames of a moving object (similar to long-exposure photography)",
    "Spatial Teleportation: Objects appearing to 'jump' from one point to another without traveling the distance",
    "Pouring Difficulty: Inability to stop pouring liquid because the 'Rising Level' isn't perceived as motion",
    "Social Disorientation: Faces appearing to 'jump' from one expression to another, making social cues impossible to read"
  ],
  "causes": [
    "Bilateral lesions in Area V5 (MT) of the Extrastriate Cortex",
    "Stroke in the Middle Cerebral Artery (MCA) territory",
    "Hyper-toxicity of certain medications (e.g., high-dose antidepressants) affecting MT signaling",
    "Transient 'Software Lag' during severe migraines"
  ],
  "risk_factors": [
    "Traumatic brain injury to the posterior-lateral regions",
    "Vascular incidents affecting the 'Motion Processor' sub-circuits",
    "Neurodegenerative conditions affecting the visual-parietal pathways"
  ],
  "diagnosis": [
    "The 'Moving Dot' Test (Asking the user to identify the direction of a moving stimulus)",
    "fMRI to check for 'Null Response' in the V5/MT complex",
    "Transcranial Magnetic Stimulation (TMS) to temporarily 'Mute' the V5 area (experimental benchmark)",
    "Exclusion of Optic Atrophy (ensuring the 'Cameras' are working)"
  ],
  "remedies": [
    "None to restore the 'Interpolation Engine' if the hardware is destroyed",
    "Compensatory Strategies: Relying on 'Sound Depth' to estimate motion",
    "Yellow-tinted lenses (occasionally reduces the 'Visual Echo' effect)",
    "Safety Training: Learning to cross streets by checking 'Static Distance' only"
  ],
  "prevention": [
    "Standard neurological maintenance and vascular health"
  ]
}

"topographical_disorientation": {
  "description": "An inability to orient oneself in the environment, navigate through space, or recognize landmarks, despite intact vision and memory.",
  "symptoms": [
    "Egocentric Disorientation: Inability to represent the location of objects with respect to the self",
    "Heading Disorientation: Losing the 'Sense of Direction' (The internal compass is spinning)",
    "Landmark Agnosia: Seeing a familiar building but failing to recognize it as a 'Node' in the map",
    "Pathfinding Loop: Walking in circles because the 'Exit' logic is corrupted",
    "Mental Map Erasure: Inability to visualize the layout of one's own house"
  ],
  "causes": [
    "Lesions in the Right Posterior Cingulate Cortex or the Parahippocampal Gyrus",
    "Damage to the 'Grid Cells' and 'Place Cells' in the Hippocampal formation",
    "Stroke in the Posterior Cerebral Artery (PCA) territory",
    "Neurodegeneration (Alzheimer’s or Posterior Cortical Atrophy)",
    "Developmental Topographical Disorientation (A 'Factory Setting' glitch)"
  ],
  "risk_factors": [
    "Traumatic Brain Injury (TBI) to the parietal-occipital junction",
    "Vascular dementia affecting the spatial-memory bus",
    "Chronic high-stress cortisol levels damaging the hippocampus"
  ],
  "diagnosis": [
    "The 'Map Drawing' Task (Asking the user to sketch a familiar route)",
    "Virtual Reality Navigation tests (Observing 'Lost' behavior in a digital maze)",
    "MRI to check for atrophy in the Parahippocampal Place Area (PPA)",
    "The 'Orientation-by-Landmark' test"
  ],
  "remedies": [
    "Cognitive Mapping training: Building 'If-Then' logic for navigation (e.g., 'If I see the red door, turn left')",
    "External GPS reliance: Outsourcing the 'Pathfinding Engine' to a smartphone",
    "Visual Cues: High-contrast stickers or 'Breadcrumbs' in the physical environment",
    "Vestibular-Visual Integration therapy"
  ],
  "prevention": [
    "Lifelong spatial puzzles and navigation without GPS to maintain 'Grid Cell' health"
  ]
}
"exploding_head_syndrome_ehs": {
  "description": "A benign parasomnia where the subject experiences loud imagined noises or a sense of explosion in the head when transitioning to or from sleep.",
  "symptoms": [
    "Auditory Shock: Perceiving a 'Bomb blast', 'Cymbal crash', or 'Loud Shout'",
    "Visual Flash: A simultaneous 'White-out' or strobe effect behind the eyelids",
    "Tachycardia: A massive spike in heart rate following the 'Impact'",
    "Adrenaline Surge: A 'Fight-or-Flight' response triggered by a non-existent threat",
    "Myoclonic Jerk: Often accompanied by a sudden muscle twitch (#77)"
  ],
  "causes": [
    "Reticular Activating System (RAS) Lag: Failure to inhibit sensory neurons during the sleep-state handover",
    "Temporal Lobe Seizure (Minor/Transient): A localized electrical storm",
    "Middle Ear Component: Sudden movement of the Eustachian tube or Tensor Tympani muscle",
    "Calcium Channel Dysfunction: Excessive neurotransmitter release during the 'Sleep Gate' phase"
  ],
  "risk_factors": [
    "High Stress & Anxiety (Increasing 'Baseline Voltage')",
    "Chronic Sleep Deprivation (Forcing the brain into 'Glitchy' transitions)",
    "Abrupt withdrawal from benzodiazepines or SSRIs",
    "History of sleep paralysis or night terrors"
  ],
  "diagnosis": [
    "Polysomnography (PSG) to rule out sleep apnea or seizures",
    "EEG during sleep-onset to capture the 'Spike' profile",
    "Clinical interview to differentiate from psychiatric hallucinations"
  ],
  "remedies": [
    "Sleep Hygiene Optimization (Stabilizing the 'Handover Protocol')",
    "Clomipramine or Calcium Channel Blockers (to dampen the 'Discharge')",
    "Stress Reduction (Lowering the system's 'Idle Noise')",
    "Education: The 'No-Harm' Patch (Knowing it isn't a stroke reduces the panic loop)"
  ],
  "prevention": [
    "Maintaining a consistent 'Sleep/Wake' schedule to train the RAS"
  ]
}
"chronostasis_temporal_overstretch": {
  "description": "A temporal illusion where the first impression following a voluntary eye movement (saccade) appears to be extended in time.",
  "symptoms": [
    "The 'Frozen Second': Feeling like a clock hand has stopped moving for >1 second",
    "Auditory Chronostasis: The first 'Beep' in a sequence sounding longer than the rest",
    "Visual Persistence: High-fidelity 'freezing' of the first frame after a rapid head/eye turn",
    "Temporal Lag: A brief feeling of 'Catching up' to real-time once the clock starts moving",
    "Consistent Reproducibility: This happens to almost everyone with a functional visual system"
  ],
  "causes": [
    "Saccadic Masking: The brain 'turning off' the visual feed during rapid eye movement",
    "Post-Saccadic Chronostasis: The brain 'backdating' the arrival of a new image to fill the blur gap",
    "Superior Colliculus Activity: Coordinating the eye-move and the 'Temporal Patch'",
    "Hyper-active 'Predictive Coding' in the Prefrontal Cortex"
  ],
  "risk_factors": [
    "Fatigue (Increasing the duration of the saccade and the subsequent 'Patch')",
    "Low-light environments (Increasing the brain's 'Estimation' error)",
    "Intentional Focus: The more you 'look' for the freeze, the more the brain tries to edit it"
  ],
  "diagnosis": [
    "The 'Ticking Clock' Test (The standard behavioral benchmark)",
    "Eye-tracking latency measurement",
    "fMRI showing activity spikes in the Parietal Cortex during the 'Backdating' phase"
  ],
  "remedies": [
    "None required (It is a 'Feature' of the Human OS to ensure visual stability)",
    "Consistent sensory input (Steady-state environments minimize the need for 'Editing')"
  ],
  "prevention": [
    "N/A; built-in video-processing architecture"
  ]
}
"reduplicative_paramnesia": {
  "description": "A delusional belief that a place or location has been duplicated, exists in two locations simultaneously, or has been relocated.",
  "symptoms": [
    "Location Doubling: Believing there are two identical versions of the same city or house",
    "Chimeric Locations: Believing a hospital is actually a 'disguised' version of their office",
    "Spatial Displacement: Insisting that a building has 'moved' hundreds of miles overnight",
    "Intact Logic (mostly): The user can navigate the room perfectly but misidentifies the 'Global Coordinates'",
    "Resistance to Evidence: Dismissing maps or GPS data as 'fakes' or 'corrupted logs'"
  ],
  "causes": [
    "Bilateral Frontal Lobe damage (The 'Reality Monitor' is offline)",
    "Right Hemisphere lesions affecting spatial 'Global Context'",
    "Disconnection between the Hippocampus (Memory) and the Frontal Cortex (Audit)",
    "Traumatic Brain Injury (TBI) affecting the 'Orientation Registry'"
  ],
  "risk_factors": [
    "Severe stroke in the right frontal-parietal region",
    "Advanced Alzheimer’s (where the 'Current Location' buffer is unstable)",
    "Encephalitis affecting the limbic system"
  ],
  "diagnosis": [
    "The 'Coordinate Verification' test (Asking the user to explain how they traveled to the current 'displaced' location)",
    "Neuropsychological testing for 'Source Monitoring' failures",
    "MRI to identify lesions in the Right Executive Center",
    "Clock-drawing and spatial layout tasks"
  ],
  "remedies": [
    "Reality Orientation Therapy (ROT): Constant, gentle re-syncing with current data",
    "Environment Stabilization: Minimizing changes to the 'Physical UI' to prevent confusion",
    "Antipsychotics (rarely) if the delusion causes severe distress",
    "Cognitive 'Check-Sum' routines: Helping the brain manually verify location markers"
  ],
  "prevention": [
    "Vascular health maintenance to protect the 'Reality-Monitoring' hardware"
  ]
}

"autotopagnosia_addressing_error": {
  "description": "A form of agnosia characterized by an inability to localize and orient different parts of the body, either on oneself or on others.",
  "symptoms": [
    "Localization Failure: Pointing to the wrong body part when prompted (e.g., pointing to the knee when asked for the elbow)",
    "Spatial Contiguity Error: Touching a part *near* the target because the 'Coordinate' is fuzzy",
    "Functional preserved, Spatial lost: Knowing what a hand *does* but not exactly where it *is* in the schema",
    "Body-Part Name Confusion: A 'Symbolic Link' error between the word and the limb",
    "Mirror Disorientation: Inability to map the 'Reflected' body onto the 'Actual' body"
  ],
  "causes": [
    "Lesions in the Left Posterior Parietal Lobe (The 'Body-Map' Server)",
    "Damage to the Somatosensory Association Cortex",
    "Tumors or strokes affecting the 'Egocentric Coordinate' generators",
    "Generalized neurodegeneration (e.g., Pick's Disease)"
  ],
  "risk_factors": [
    "Ischemic stroke in the left hemisphere",
    "Severe traumatic brain injury to the parietal region",
    "Neurosurgical complications involving the spatial-processing centers"
  ],
  "diagnosis": [
    "The 'Point-to-Command' Test (Asking the user to identify 20 body parts)",
    "The 'Contingency Test' (Can the user point to parts on a doll but not themselves?)",
    "MRI to identify 'Dead Sectors' in the Left Parietal Lobe",
    "Exclusion of Aphasia (ensuring they actually understand the word 'nose')"
  ],
  "remedies": [
    "Tactile Reinforcement: Using vibration or pressure to 'Re-ping' the body part",
    "Visual Anchoring: Looking in a mirror to 'Manually' map the coordinates",
    "Occupational Therapy: Re-building the 'Body-Address Table' through repetitive touch",
    "Compensatory verbal cues (e.g., 'The part you use for smelling')"
  ],
  "prevention": [
    "Standard stroke prevention and neurological health maintenance"
  ]
}

"apraxia_motor_program_error": {
  "description": "A neurological disorder characterized by the inability to perform learned, purposeful movements despite having the physical ability and desire to do so.",
  "symptoms": [
    "Ideomotor Failure: Inability to mimic gestures (e.g., 'Wave goodbye') on command",
    "Ideational Error: Losing the 'Object Logic' (e.g., trying to use a toothbrush as a spoon)",
    "Sequence Corruption: Performing steps of a task in the wrong order (e.g., putting shoes on before socks)",
    "Clumsy Tool Handling: Holding a hammer by the wrong end despite knowing what it is",
    "Verbal Apraxia: The 'Speech Hardware' is fine, but the 'Articulatory Script' is lost"
  ],
  "causes": [
    "Lesions in the Left Posterior Parietal Cortex (The 'Procedural Database')",
    "Damage to the Premotor Cortex (The 'Command Assembler')",
    "Stroke in the Middle Cerebral Artery (MCA) territory",
    "Neurodegenerative diseases like Corticobasal Degeneration (CBD)",
    "Corpus Callosum disconnection (preventing the 'Admin' from sending scripts to the right hand)"
  ],
  "risk_factors": [
    "History of left-hemisphere stroke",
    "Head trauma involving the parietal or frontal lobes",
    "Progressive cognitive decline affecting 'Action Knowledge'"
  ],
  "diagnosis": [
    "Pantomime tasks (e.g., 'Show me how you would use a saw')",
    "Imitation of meaningless gestures (testing 'Real-Time Encoding')",
    "Multi-step assembly tests (e.g., folding a letter and placing it in an envelope)",
    "MRI/CT to identify 'Null Zones' in the motor planning network"
  ],
  "remedies": [
    "Occupational Therapy (OT) using 'Errorless Learning' to rebuild scripts",
    "Sensory Cueing: Using rhythmic beats or visual prompts to bypass the missing library",
    "Gestural Training: Re-associating physical movements with semantic meaning",
    "Augmentative and Alternative Communication (AAC) for verbal variants"
  ],
  "prevention": [
    "Standard neurological maintenance and vascular health"
  ]
}
"acalculia_alu_failure": {
  "description": "An acquired impairment in which patients have difficulty performing mathematical tasks, often following brain injury to the parietal lobe.",
  "symptoms": [
    "Anarithmetia: Loss of the basic 'Addition/Subtraction' logic (The ALU is offline)",
    "Asemantic Acalculia: Inability to understand the 'Magnitude' of numbers (Is 10 bigger than 2?)",
    "Spatial Acalculia: Misaligning numbers in columns (A 'Formatting' or 'Buffer' error)",
    "Operator Confusion: Mistaking a '+' for a 'x'",
    "Number-Reading/Writing Errors: Transposing 12 into 21 or failing to recognize symbols"
  ],
  "causes": [
    "Lesions in the Left Angular Gyrus or the Intraparietal Sulcus (IPS)",
    "Gerstmann's Syndrome: A specific quartet of glitches (Acalculia, Agraphia, Finger Agnosia, Left-Right Disorientation)",
    "Stroke in the Left Posterior Parietal Artery",
    "Tumors or TBI affecting the 'Symbolic Mapping' centers"
  ],
  "risk_factors": [
    "Vascular incidents in the dominant hemisphere",
    "Advanced neurodegeneration (often an early signal in Alzheimer's)",
    "Intracranial pressure affecting the parietal 'Calculation Hub'"
  ],
  "diagnosis": [
    "Simple Arithmetic Screening (Single-digit addition/subtraction)",
    "Magnitude Comparison Tests (e.g., 'Which is larger, a dog or a cat?')",
    "MRI/CT to identify 'Infarct Zones' in the IPS",
    "Testing for 'Gerstmann's Quartet' to see if the error is localized or global"
  ],
  "remedies": [
    "Compensatory Technology: Outsourcing calculation to external 'Processors' (Calculators)",
    "Drill-based Re-mapping: Attempting to build new 'Look-up Tables' in the brain",
    "Visual/Tactile Math: Using physical beads or fingers to ground abstract symbols in 'Hardware'",
    "Speech-Language Therapy if the math error is linked to a 'Language' glitch"
  ],
  "prevention": [
    "Standard neurological maintenance and hypertension control"
  ]
}

"synesthesia_cross_talk": {
  "description": "A neurological trait where stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway.",
  "symptoms": [
    "Grapheme-Color: Letters or numbers are inherently 'colored' (e.g., 'A' is always red)",
    "Chromesthesia: Sound-to-color mapping (Music triggers visual light shows)",
    "Lexical-Gustatory: Words have specific tastes (e.g., the name 'Derek' tastes like earwax)",
    "Spatial Sequence: Numbers or months occupy physical 3D coordinates in space",
    "Mirror-Touch: Feeling a physical sensation when watching someone else being touched",
    "Consistency: The 'Mappings' are fixed and do not change over the user's lifetime"
  ],
  "causes": [
    "Cross-Activation: Physical 'Wiring' exists between adjacent sensory areas (e.g., V4 and the Grapheme area)",
    "Disinhibited Feedback: Failure of the 'Top-Down' filters to suppress sensory cross-talk",
    "Incomplete Pruning: Failure to delete 'Extra' neural connections during infancy",
    "Genetic 'Patch' mutation affecting axonal guidance"
  ],
  "risk_factors": [
    "Strong hereditary component (often runs in families)",
    "Neurodivergence (High correlation with Autism Spectrum and ADHD)",
    "High 'Openness to Experience' personality scores"
  ],
  "diagnosis": [
    "The 'Consistency Test' (Testing the user's color-mapping months apart with 100% accuracy)",
    "Stroop-style interference tasks (e.g., showing the letter 'A' in blue when the user 'sees' it as red)",
    "fMRI showing simultaneous activation of two isolated sensory 'Cores'",
    "Diffusion Tensor Imaging (DTI) to map 'Extra' white-matter cabling"
  ],
  "remedies": [
    "Usually not treated (often viewed as a 'Feature' rather than a 'Bug')",
    "Sensory Management: Reducing 'Noisy' environments if over-stimulation occurs",
    "Focus Training: Learning to prioritize the 'Primary' data stream"
  ],
  "prevention": [
    "N/A; purely structural/developmental architecture"
  ]
}

"deja_vecu_loop": {
  "description": "A pathological form of déjà vu where the sensation of 'having lived through' the present is persistent, intense, and often involves 'recollecting' the future.",
  "symptoms": [
    "Recollective Confabulation: Claiming to 'remember' current events as they happen",
    "Anosognosia: The user may stop watching news or reading because they 'already know the plot'",
    "Temporal Displacement: A feeling that the present is actually a playback of a 10-year-old log",
    "Loss of Spontaneity: Life feels like a scripted movie where the user has already seen the ending",
    "Secondary Delusions: Developing 'Time Travel' or 'Reincarnation' theories to explain the glitch"
  ],
  "causes": [
    "Hyper-active 'Familiarity' signaling in the Parahippocampal Gyrus",
    "Partial Seizures in the Temporal Lobe (Temporal Lobe Epilepsy)",
    "Frontal-Temporal Disconnection: The 'Logic Auditor' cannot verify the 'Memory' tag",
    "Neurodegeneration (Dementia with Lewy Bodies or Alzheimer's variant)",
    "Dopaminergic surges affecting the 'Salience' of the present moment"
  ],
  "risk_factors": [
    "Chronic Temporal Lobe Epilepsy",
    "Advanced age with memory-circuit atrophy",
    "Severe sleep deprivation causing 'Sync Lag' in the hippocampus"
  ],
  "diagnosis": [
    "EEG to detect sub-clinical 'Temporal Spikes'",
    "Memory-Source monitoring tasks (Asking 'Where exactly did you learn this?')",
    "MRI to check for volume loss in the parahippocampal regions",
    "The 'News Forecast' test: Asking the user to predict a random headline"
  ],
  "remedies": [
    "Anticonvulsants (e.g., Carbamazepine) to stabilize the temporal 'Read/Write' heads",
    "Dopamine antagonists to reduce the 'Sense of Significance'",
    "Cognitive 'Discrepancy' training: Forcing the brain to notice small differences in the 'script'",
    "Environmental 'Novelty' saturation"
  ],
  "prevention": [
    "Management of seizure activity and neurological maintenance"
  ]
}
"wernickes_aphasia": {
  "description": "A type of aphasia in which an individual is unable to understand language in its written or spoken form, while producing fluent but meaningless speech.",
  "symptoms": [
    "Fluent Nonsense: Speaking at a normal rate with correct syntax but zero meaning",
    "Logorrhea: A 'Press of Speech' (excessive talking that is hard to interrupt)",
    "Neologisms: Inventing entirely new, non-existent words (e.g., 'The flurben is garking')",
    "Anosognosia: Lack of awareness that their own speech is unintelligible",
    "Reading/Writing Failure: Severe impairment in decoding or encoding written symbols"
  ],
  "causes": [
    "Lesion in the Posterior Superior Temporal Gyrus (Wernicke’s Area)",
    "Ischemic stroke in the Inferior Division of the Left Middle Cerebral Artery",
    "Traumatic Brain Injury (TBI) to the left temporal-parietal junction",
    "Neurodegeneration (Primary Progressive Aphasia)"
  ],
  "risk_factors": [
    "Atrial fibrillation (increasing stroke risk)",
    "Hypertension leading to vascular compromise in the language centers",
    "Advanced age affecting cortical plasticity"
  ],
  "diagnosis": [
    "The 'Cookie Theft' description task (Testing for semantic relevance)",
    "Naming tasks and word-matching comprehension tests",
    "MRI/CT to localize the infarct in the Left Temporal Lobe",
    "Western Aphasia Battery (WAB) for standardized scoring"
  ],
  "remedies": [
    "Speech-Language Pathology (SLP) focusing on 'Contextual Grounding'",
    "Visual Action Therapy (using gestures as a backup 'Protocol')",
    "Social-Pragmatic therapy to help the user recognize 'Listener Confusion' cues",
    "Pharmacotherapy (e.g., Piracetam) to support cortical recovery (experimental)"
  ],
  "prevention": [
    "Vascular health maintenance and early stroke intervention"
  ]
}

"prosopometamorphopsia_pmo": {
  "description": "A visual perception disorder characterized by distorted perceptions of faces, where features appear altered in shape, size, or position.",
  "symptoms": [
    "Hemi-PMO: Distortions appearing only on one side of a face",
    "Feature Migration: Eyes drifting toward ears, or mouths moving to the forehead",
    "Texture Warping: Skin appearing to 'melt', 'scaly', or 'metallic'",
    "Hyper-Vividness: Facial features appearing unnaturally sharp or 'demonic'",
    "Persistence: The distortion remains as long as the user looks at the face"
  ],
  "causes": [
    "Lesions in the Splenium of the Corpus Callosum",
    "Hyper-excitability in the Fusiform Face Area (FFA)",
    "Damage to the Lingual or Fusiform gyri (Visual Processing Units)",
    "Temporal Lobe Migraines (transient 'Software Spikes')",
    "Asymmetry in the 'Face-Patch' communication bus"
  ],
  "risk_factors": [
    "Posterior cerebral artery stroke",
    "Traumatic brain injury to the occipital-temporal junction",
    "Specific pharmacological reactions affecting visual integration"
  ],
  "diagnosis": [
    "The 'Face-Morphing' test (asking the user to adjust a digital face to match their distortion)",
    "fMRI to identify 'hot spots' of hyper-activity in the FFA",
    "Neurological mapping of the Splenium",
    "Exclusion of purely psychiatric hallucinations"
  ],
  "remedies": [
    "Prism Lenses to shift the visual field away from the 'Distortion Zone'",
    "Color Filters (e.g., green or red tints can sometimes 'Mute' the shader error)",
    "Treating the underlying migraine or seizure activity",
    "Neuroplastic Adaptation (the 'Logic Auditor' eventually learns to ignore the warp)"
  ],
  "prevention": [
    "Protecting visual processing centers from vascular incidents"
  ]
}

"musical_hallucinosis": {
  "description": "A form of auditory hallucination where individuals hear music in the absence of an external source, typically associated with hearing loss.",
  "symptoms": [
    "High-Fidelity Loops: Hearing full orchestrations or clear vocals (often 'Radio-like')",
    "Involuntary Playback: The music starts and stops without conscious intent",
    "External Localization: Feeling certain the sound is coming from a neighbor's radio or a speaker",
    "Repetitive Playlists: Often limited to music the user knew well in the past",
    "Intact Insight: Knowing the music isn't 'real' despite how real it sounds"
  ],
  "causes": [
    "Sensory Deprivation (The 'Deafferentation' theory)",
    "Hyper-excitability in the Superior Temporal Gyrus (Auditory Cortex)",
    "Abnormal connectivity in the 'Phonological Loop' of working memory",
    "Release Phenomenon: The brain 'releases' stored patterns when external signals fade",
    "Lesions in the Pons or Thalamus (Signal-Routing hardware)"
  ],
  "risk_factors": [
    "Acquired deafness or severe hearing loss (Presbycusis)",
    "Advanced age (The 'Legacy Hardware' phase)",
    "Social isolation reducing environmental audio 'Gain'",
    "Chronic stress increasing 'Cortical Noise'"
  ],
  "diagnosis": [
    "Audiometric testing to quantify hearing loss",
    "fMRI/EEG showing activity in the Primary Auditory Cortex during 'Silence'",
    "Psychiatric screening to rule out Schizophrenia (where voices are more common than music)",
    "Elimination of 'Earworm' (INMI) via duration and intensity metrics"
  ],
  "remedies": [
    "Hearing Aids: Re-introducing real 'Signal' to drown out the 'Noise'",
    "Low-level background noise (White Noise generators) to saturate the sensors",
    "Acetylcholinesterase inhibitors (often used in dementia) to stabilize signals",
    "Cognitive 'Source Monitoring' training"
  ],
  "prevention": [
    "Early treatment of hearing loss to keep the 'Auditory API' active"
  ]
}

"akinetopsia_motion_blindness": {
  "description": "A neuropsychological disorder in which a patient cannot perceive motion in their visual field, despite being able to see stationary objects clearly.",
  "symptoms": [
    "Strobe-Light Effect: The world appears as a succession of freeze-frames",
    "Trailing/After-images (Palinopsia) following moving objects",
    "Difficulty with 'Fluid Dynamics': Inability to see liquid being poured (it looks like a frozen glacier)",
    "Social Lag: Missing facial micro-expressions, making conversations feel 'jumpy'",
    "Navigational Hazard: Cars 'jump' from the distance to right in front of the user"
  ],
  "causes": [
    "Bilateral damage to the Middle Temporal (MT/V5) area of the visual cortex",
    "High-dose exposure to certain antidepressants or antiepileptics",
    "Persistent Aura without Infarction (in severe migraineurs)",
    "Neurodegeneration (Alzheimer's variant: Posterior Cortical Atrophy)",
    "Traumatic Brain Injury (TBI) localized to the posterior-lateral regions"
  ],
  "risk_factors": [
    "Ischemic stroke in the temporal-occipital junction",
    "Specific drug toxicities affecting visual temporal integration",
    "Rare genetic predispositions to cortical 'Motion-Blindness'"
  ],
  "diagnosis": [
    "The 'Random Dot Kinematogram' (RDK) test (Detecting signal in noise)",
    "fMRI while viewing moving vs. static stimuli",
    "Visual Evoked Potentials (VEP) to measure latency in the V5 pathway",
    "Perimetry testing to map the 'Static' vs 'Dynamic' visual fields"
  ],
  "remedies": [
    "Compensatory Strategies: Using sound cues (echolocation-lite) to track movement",
    "Pharmacological Adjustment (if drug-induced)",
    "Yellow-tinted lenses (to increase contrast and reduce 'Trail' noise)",
    "Vestibular training to use 'Balance' sensors to guess motion"
  ],
  "prevention": [
    "Protection against repetitive TBI",
    "Monitoring neurotoxicity in complex medication stacks"
  ]
}
"fregoli_delusion_aliasing": {
  "description": "A rare disorder in which a person holds a delusional belief that different people are actually a single person who changes appearance or is in disguise.",
  "symptoms": [
    "Identity Aliasing: Seeing the same 'Target Person' in every crowd",
    "Hyper-familiarity: Feeling an intense sense of 'knowing' a complete stranger",
    "Paranoia: Belief that the 'Target' is stalking them via various 'Skins'",
    "Recall of false interactions with strangers based on the 'Target's' history",
    "High autonomic arousal (anxiety) during social navigation"
  ],
  "causes": [
    "Hyper-connectivity between the Fusiform Face Area (FFA) and the Perirhinal Cortex",
    "Dopaminergic over-activity in the Right Temporoparietal Junction (rTPJ)",
    "Failure of the 'Novelty Filter': The brain tags new faces as 'Already Known'",
    "Lesions in the Right Frontal or Left Temporo-parietal regions"
  ],
  "risk_factors": [
    "Treatment with Levodopa (dopamine agonists)",
    "Traumatic Brain Injury (TBI) affecting the right hemisphere",
    "Schizophrenia or other psychotic-spectrum conditions"
  ],
  "diagnosis": [
    "Facial Recognition tasks (testing for 'False Positives')",
    "Skin Conductance Response (SCR) to monitor 'Recognition Spikes' for strangers",
    "MRI to check for right-hemisphere atrophy",
    "Psychiatric evaluation for 'Monothematic' delusions"
  ],
  "remedies": [
    "Antipsychotic medication (Dopamine antagonists) to lower the 'Recognition Gain'",
    "Cognitive Behavioral Therapy (CBT) to challenge the 'Logic of Disguise'",
    "Anticonvulsants to stabilize temporal lobe activity",
    "Environmental management (reducing exposure to high-density crowds)"
  ],
  "prevention": [
    "Monitoring dopamine levels in patients treated for Parkinson's disease"
  ]
}

"stendhal_syndrome": {
  "description": "A psychosomatic condition involving rapid heartbeat, dizziness, fainting, confusion and even hallucinations when an individual is exposed to objects or phenomena of great beauty.",
  "symptoms": [
    "Acute Tachycardia (racing heart) upon entering museums or historic sites",
    "Dissociative episodes (feeling 'unplugged' from reality)",
    "Temporary Vision Loss or 'Grey-out' due to sensory overload",
    "Paranoia or Euphoria (system-wide emotional instability)",
    "Physical collapse (Fainting/Syncope)"
  ],
  "causes": [
    "Hyper-activation of the Ventral Striatum (the 'Reward Engine')",
    "Dysfunction in the Autonomic Nervous System's 'Gain Control'",
    "Over-stimulation of the Medial Prefrontal Cortex (mPFC) during aesthetic judgment",
    "Cross-talk between the Limbic System and the Vestibular (Balance) system"
  ],
  "risk_factors": [
    "Highly sensitive or 'Imaginative' personality types",
    "Travel to high-density aesthetic zones (e.g., Florence, Italy)",
    "Pre-existing travel fatigue or 'System Exhaustion'"
  ],
  "diagnosis": [
    "Observation of physiological spikes in specific environments",
    "Clinical history of aesthetic sensitivity",
    "Exclusion of standard panic attacks or heatstroke",
    "The 'Florence Test' (measuring heart rate variability near masterpieces)"
  ],
  "remedies": [
    "Sensory Deprivation: Closing eyes and leaving the environment",
    "Hydration and 'Grounding' (Physical contact with non-aesthetic surfaces)",
    "Benzodiazepines (in extreme cases) to lower the 'Emotional Gain'",
    "Aesthetic Pacing: Limiting museum time to 'Standard Bandwidth' levels"
  ],
  "prevention": [
    "Gradual exposure to high-stimulus environments"
  ]
}

"hyper_empathy_syndrome": {
  "description": "A condition characterized by an intense, uncontrollable, and physically overwhelming emotional response to the perceived emotions of others.",
  "symptoms": [
    "Involuntary 'emotional mirroring' (feeling sad/angry/anxious because someone nearby is)",
    "Physical symptoms triggered by others' distress (nausea, tremors, or rapid heart rate)",
    "Inability to 'turn off' the social input feed",
    "Extreme social fatigue and 'compassion burnout'",
    "Difficulty making objective decisions when others are present",
    "Feeling 'haunted' by the emotions of fictional characters or strangers"
  ],
  "causes": [
    "Hyper-excitability of the Mirror Neuron System (MNS)",
    "Increased gray matter volume in the Anterior Insular Cortex",
    "Loss of inhibitory control in the Right Inferior Frontal Gyrus",
    "Post-surgical complications (e.g., following a temporal lobectomy)",
    "Genetic conditions such as Williams Syndrome"
  ],
  "risk_factors": [
    "Neuroplasticity-related changes after right-hemisphere trauma",
    "Pre-existing high-sensitivity traits",
    "Specific neurotransmitter imbalances (Oxytocin/Vasopressin receptor density)"
  ],
  "diagnosis": [
    "Interpersonal Reactivity Index (IRI) assessment",
    "fMRI showing hyper-activation in the Insula and Cingulate Cortex during empathy tasks",
    "Physiological monitoring (GSR/Heart Rate) while observing others in distress",
    "Exclusion of Borderline Personality Disorder (BPD) and typical anxiety"
  ],
  "remedies": [
    "Cognitive-Behavioral Therapy (CBT) to build 'Affective Boundaries'",
    "Oxytocin modulators (experimental)",
    "Mindfulness training to 'tag' emotions as 'External Data'",
    "Social isolation/controlled exposure to prevent system overload"
  ],
  "prevention": [
    "Early cognitive training in emotional regulation"
  ]
}
"alice_in_wonderland_syndrome": {
  "description": "A neuropsychological condition that distorts perception, causing objects and body parts to appear altered in size or distance.",
  "symptoms": [
    "Micropsia/Macropsia: Objects appearing tiny or giant",
    "Teleopsia/Pelopsia: Objects appearing much further or closer than they are",
    "Zoom-and-Dolly effects: The visual field expanding or shrinking rapidly",
    "Distortion of time: Feeling like events are moving in slow-motion or fast-forward",
    "Body Schema Distortions: Feeling like one's head or hands are growing to the size of a room"
  ],
  "causes": [
    "Hyper-excitability in the Posterior Parietal Cortex (Spatial Integration)",
    "Temporal Lobe Migraines (the most common 'Trigger Script')",
    "Epstein-Barr Virus (EBV) infection affecting the central nervous system",
    "Temporal Lobe Epilepsy (localized 'Electrical Spikes')",
    "Psychoactive substance interference (LSD, Psilocybin)"
  ],
  "risk_factors": [
    "History of complex migraines",
    "Childhood (symptoms often 'Patch Out' as the brain matures)",
    "High-stress environments triggering 'Visual Lag'"
  ],
  "diagnosis": [
    "MRI to rule out structural lesions or tumors in the visual path",
    "EEG to monitor for sub-clinical seizure activity",
    "Amsler Grid testing to map the specific 'Scaling Distortion'",
    "Clinical history focusing on migraine prodromes"
  ],
  "remedies": [
    "Treating the underlying migraine or infection",
    "Rest in a low-stimulus environment (Dark Room 'Sleep Mode')",
    "Beta-blockers or Anticonvulsants to stabilize cortical excitability",
    "Reassurance: Mentally 'Tagging' the distortion as a harmless rendering error"
  ],
  "prevention": [
    "Identifying and avoiding migraine triggers (diet, light, stress)"
  ]
}
"urbach_wiethe_fear_glitch": {
  "description": "A rare genetic disorder where bilateral calcification of the amygdala leads to a total loss of the ability to experience or recognize fear.",
  "symptoms": [
    "Absolute Fearlessness: No response to snakes, spiders, or physical threats",
    "Social Boundary Blindness: Standing uncomfortably close to strangers (No 'Personal Space' alarm)",
    "Emotional Flatness: Inability to recognize 'Fear' on faces (while still recognizing joy or anger)",
    "Hoarding/Collecting behavior (Obsessive-Compulsive traits)",
    "Dermatological changes (warty skin lesions around the eyes)",
    "Hoarse voice (calcification of the vocal cords)"
  ],
  "causes": [
    "Mutation in the ECM1 (Extracellular Matrix Protein 1) gene",
    "Bilateral calcification of the Temporal Lobes (specifically the Amygdalae)",
    "Disconnection of the 'Threat API' from the Prefrontal Cortex"
  ],
  "risk_factors": [
    "Autosomal recessive inheritance (very rare, found in specific genetic clusters)",
    "Progressive neural calcification starting in childhood"
  ],
  "diagnosis": [
    "CT/MRI showing symmetrical 'Stone-Like' calcifications in the Amygdalae",
    "Standardized fear-response testing (Carbon Dioxide inhalation or horror stimuli)",
    "Genetic testing for the ECM1 mutation",
    "Laryngoscopy to check for vocal cord thickening"
  ],
  "remedies": [
    "No current 'Hardware Patch' to reverse calcification",
    "Safety Training: Learning 'Logical Fear' (e.g., 'If I see a snake, it is dangerous' as a rule-based fact)",
    "Dermatological treatments for skin symptoms"
  ],
  "prevention": [
    "Genetic counseling for known carriers"
  ]
}

"cotards_delusion": {
  "description": "A rare neuropsychiatric condition in which the patient holds the delusional belief that they are dead, non-existent, or putrefying.",
  "symptoms": [
    "Denial of self-existence ('I don't exist', 'I have no heart')",
    "Sensations of rotting or foul odors (olfactory hallucinations of decay)",
    "Analgesia (insensitivity to pain, as 'dead things can't feel')",
    "Chronic suicidal ideation or self-harm to 'prove' the lack of life",
    "Social withdrawal and cessation of eating (starvation due to 'no stomach')"
  ],
  "causes": [
    "Total disconnection between the Fusiform Face Area and the Amygdala",
    "Severe atrophy in the Temporoparietal and Frontal lobes",
    "Right-hemisphere lesions leading to 'Alienation' of the entire body",
    "Extreme metabolic depression in the Prefrontal Cortex",
    "Post-ictal states in severe epilepsy"
  ],
  "risk_factors": [
    "Severe clinical depression with psychotic features",
    "Schizophrenia or Bipolar Disorder",
    "Traumatic brain injury or advanced neurodegeneration"
  ],
  "diagnosis": [
    "Clinical interview and mental status exam (MSE)",
    "PET/SPECT scans showing 'Silent Zones' in the parietal/frontal cortex",
    "Exclusion of Capgras or other misidentification syndromes",
    "Neurological screening for underlying stroke or tumor"
  ],
  "remedies": [
    "Electroconvulsive Therapy (ECT) - often considered the 'System Hard Reset'",
    "Antipsychotic and Antidepressant pharmaceutical stack",
    "Intensive nutrition and hydration support",
    "Psychotherapy focusing on 'Embodied Presence' and sensory grounding"
  ],
  "prevention": [
    "Aggressive treatment of severe mood disorders and psychotic symptoms"
  ]
}

"hyper_reflexivity_loop": {
  "description": "A state where tacit, automatic mental and physical processes become the object of explicit, conscious awareness, leading to a sense of alienation from the self.",
  "symptoms": [
    "Loss of 'Spontaneity': Simple actions like walking or smiling require manual calculation",
    "Infinite Regress: Thinking about 'the fact that I am thinking about thinking'",
    "Self-Alienation: The body feels like a 'machine' or an 'object' being operated by a stranger",
    "Spatial/Temporal Distention: Seconds feel like hours as every micro-process is audited",
    "Semantic Satiation: Words and concepts lose meaning because they are analyzed too deeply"
  ],
  "causes": [
    "Dysfunction in the Prefrontal-Thalamic-Cerebellar circuit",
    "Over-activation of the Medial Prefrontal Cortex (mPFC)",
    "Failure of the 'Gating' mechanism that keeps background tasks out of conscious RAM",
    "Neuroplastic shift where 'Tacit' knowledge is forced into 'Explicit' memory banks"
  ],
  "risk_factors": [
    "Schizotypal personality traits",
    "Intense philosophical or existential preoccupation",
    "Severe sleep deprivation or chronic 'System Stress'"
  ],
  "diagnosis": [
    "Self-Experience Lifespan Assessment (EASE)",
    "fMRI showing hyper-metabolism in the 'Self-Referential' default mode network",
    "Clinical observation of 'Manual' social behaviors",
    "Exclusion of standard anxiety or depersonalization"
  ],
  "remedies": [
    "Absorption Therapy: Engaging in high-bandwidth 'External' tasks (sports, music)",
    "Cognitive 'De-Focusing' techniques",
    "Dopamine modulators to reset the 'Saliency' filter",
    "Grounding exercises to 'Re-Mount' the self into the physical environment"
  ],
  "prevention": [
    "Maintaining a healthy balance between introspection and outward-facing activity"
  ]
}

"mirror_pain_synesthesia": {
  "description": "A rare condition where an individual experiences the same sensation of pain that they see another person experiencing.",
  "symptoms": [
    "Localized pain: Seeing someone stub a toe causes a sharp pain in the user's own toe",
    "Physical flinching or autonomic responses (sweating, increased heart rate) to others' injuries",
    "High-fidelity mapping: The sensation matches the location and intensity of the observed pain",
    "Sensory 'Overload' in crowded or high-action environments",
    "Preserved 'Insight': The user knows they aren't actually injured, yet the 'Pain Driver' fires anyway"
  ],
  "causes": [
    "Hyper-activation of the Anterior Cingulate Cortex (ACC) and Anterior Insula",
    "Excessive connectivity between the Visual Cortex and the Somatosensory Homunculus",
    "Inadequate 'Self-Other' inhibition in the Right Temporoparietal Junction (rTPJ)",
    "Neuroplastic changes following limb loss (common in amputees observing others)"
  ],
  "risk_factors": [
    "High scores in 'Trait Empathy' metrics",
    "Pre-existing synesthetic traits (e.g., Grapheme-Color synesthesia)",
    "History of vicarious trauma"
  ],
  "diagnosis": [
    "fMRI observation: Measuring ACC activation while viewing 'Pain Stimuli' videos",
    "Sensory mapping: Correlating observed touch/pain with subjective reporting",
    "Psychological screening for 'Sensory Processing Sensitivity' (SPS)",
    "Exclusion of conversion disorders or psychosomatic illness"
  ],
  "remedies": [
    "Visual 'Gating' (looking away from injury triggers)",
    "Cognitive 'Decoupling': Consciously tagging the data as 'External'",
    "Mindfulness to strengthen the 'Self' boundary in the rTPJ",
    "Safe-environment design (avoiding violent media/crowds during flares)"
  ],
  "prevention": [
    "Early boundary-training for highly sensitive individuals"
  ]
}
"mirror_touch_synesthesia": {
  "description": "A condition where individuals experience the same sensation of touch that they see another person experiencing.",
  "symptoms": [
    "Tactile mirroring: Seeing a touch on someone’s left cheek causes a sensation on the user’s right (mirror) or left (anatomical) cheek",
    "Physical 'Echoes': Feeling the texture of objects someone else is holding",
    "Hyper-sensitivity to social touch (feeling 'smothered' in crowds)",
    "Strong emotional resonance with the person being touched",
    "Inability to 'ignore' the physical presence of others in the visual field"
  ],
  "causes": [
    "Over-activation of the Primary Somatosensory Cortex (S1 and S2)",
    "Reduced gray matter volume in the Right Temporoparietal Junction (rTPJ)",
    "Hyper-connectivity between the Visual (MT/V5) and Tactile systems",
    "Failure of the 'Inhibitory Gate' that usually suppresses vicarious touch"
  ],
  "risk_factors": [
    "Congenital (born with the cross-wiring)",
    "Acquired (secondary to limb loss or right-hemisphere stroke)",
    "High scores in emotional contagion tests"
  ],
  "diagnosis": [
    "The 'Visual-Tactile Interference' task (testing if observed touch slows down reaction to real touch)",
    "fMRI showing S1/S2 firing during passive observation of touch",
    "Self-report mapping of 'Mirror' vs 'Anatomical' orientation",
    "Exclusion of tactile hallucinations or purely psychological empathy"
  ],
  "remedies": [
    "Visual avoidance (looking away from intense tactile interactions)",
    "Focusing on 'Self-Touch' (pinching one's own arm to 're-anchor' the sensor)",
    "Cognitive 'Boundary Strengthening' exercises",
    "Wearing heavy or textured clothing to provide a 'Constant Baseline' of real touch"
  ],
  "prevention": [
    "No known prevention for congenital cases; sensory management is key"
  ]
}
"ekbom_syndrome": {
  "description": "A form of psychosis where individuals hold a firm, false belief that they are infested with parasites, insects, or bugs.",
  "symptoms": [
    "Formication: The sensation of 'crawling' or 'biting' on the skin",
    "The 'Matchbox Sign': Bringing small containers of lint, skin flakes, or debris as 'proof' of the bugs",
    "Self-mutilation: Scratching or cutting the skin to 'extract' the parasites",
    "Hyper-vigilance: Constantly cleaning the environment or using pesticides",
    "Intact Logic: The user is often rational in every other domain except the infestation"
  ],
  "causes": [
    "Dopamine dysregulation in the Striatum (the 'Filtering' hub)",
    "Micro-lesions in the Basal Ganglia or Parietal Lobe",
    "Systemic toxicity (e.g., Cocaine or Methamphetamine 'coke bugs')",
    "Vitamin B12 deficiency or chronic kidney failure (Metabolic 'Noise')",
    "Reduced activity in the Prefrontal 'Reality-Checking' cortex"
  ],
  "risk_factors": [
    "Advanced age (more common in post-menopausal women)",
    "Chronic stimulant abuse",
    "History of social isolation or tactile hypersensitivity"
  ],
  "diagnosis": [
    "Dermatological exam to rule out actual scabies or mites",
    "Blood panels for metabolic imbalances (liver/kidney function)",
    "Psychiatric evaluation for 'Monothematic' delusional disorder",
    "Observation of the 'Matchbox Sign'"
  ],
  "remedies": [
    "Low-dose Antipsychotics (e.g., Risperidone) to 'mute' the dopamine noise",
    "Antihistamines to reduce the physical 'itch' signal",
    "Empathy-based therapy (acknowledging the distress without validating the bugs)",
    "Treating the underlying metabolic or toxic cause"
  ],
  "prevention": [
    "Management of neurotransmitter health and avoiding neurotoxic substances"
  ]
}

"amnestic_misidentification": {
  "description": "A rare syndrome where a patient, due to memory loss, misidentifies their current chronological age and environment, believing they are living in a previous period of their life.",
  "symptoms": [
    "Chronological Displacement (believing it is 10, 20, or 40 years ago)",
    "Misidentifying family members (e.g., mistaking a son for a brother or a spouse for a parent)",
    "Looking in the mirror and not recognizing the 'older' reflection (Reflection Disconnect)",
    "Attempting to perform 'outdated' routines (e.g., trying to go to a job they retired from decades ago)",
    "Confabulation to explain 'modern' technology (e.g., 'This smartphone is a fancy calculator')"
  ],
  "causes": [
    "Severe Retrograde and Anterograde Amnesia",
    "Bilateral Hippocampal damage (the Indexing service)",
    "Frontal Lobe atrophy (the 'Reality Monitor')",
    "Wernicke-Korsakoff Syndrome (often Thiamine deficiency related)",
    "Advanced Alzheimer’s or Post-Traumatic Brain Injury"
  ],
  "risk_factors": [
    "Chronic alcoholism (B1 deficiency)",
    "Severe head trauma affecting the temporal lobes",
    "Neurodegenerative diseases affecting memory retrieval"
  ],
  "diagnosis": [
    "The 'Orientation to Time' test (Standard MMSE)",
    "MRI showing significant hippocampal or thalamic volume loss",
    "Family interviews to establish the 'Target Era' of the delusion",
    "PET scans to detect 'Cold Zones' in the prefrontal cortex"
  ],
  "remedies": [
    "Validation Therapy (entering the patient's 'Time Zone' to reduce distress)",
    "Environmental 'Cueing' (photos, music, and items from the current era)",
    "High-dose Thiamine (if Korsakoff-related)",
    "Structured routine to 'anchor' the user to the present"
  ],
  "prevention": [
    "Managing nutritional health (B vitamins)",
    "Preventing repetitive TBI"
  ]
}
"apotemnophilia_biid": {
  "description": "A rare condition where an individual possesses an overwhelming desire to amputate one or more healthy limbs or to become disabled.",
  "symptoms": [
    "Feeling of 'incompleteness' while the limb is attached",
    "Intense envy of people who are actual amputees",
    "Pretending behavior (using crutches or wheelchairs to simulate the desired state)",
    "Specific 'Mapping': The user can point to the exact line where they feel the limb should end",
    "Relief/Euphoria: The 'glitch' often resolves instantly once the limb is removed"
  ],
  "causes": [
    "Failure of the Right Parietal Lobe to integrate the limb into the Body Schema",
    "Structural anomalies in the Superior Parietal Lobule",
    "Reduced cortical thickness in the Primary Somatosensory Cortex (S1) for that limb",
    "Developmental 'Hard-Coding' error in the neural representation of the self"
  ],
  "risk_factors": [
    "Early childhood exposure to amputees (acting as a 'Template' for the error)",
    "Co-occurring Obsessive-Compulsive traits",
    "Right-hemisphere developmental variations"
  ],
  "diagnosis": [
    "Skin Conductance Response (SCR) mapping (the 'unwanted' limb shows high arousal/stress)",
    "fMRI showing a 'Silent Zone' in the parietal lobe when the limb is touched",
    "Psychiatric evaluation to distinguish from Body Dysmorphic Disorder (BDD)",
    "Exclusion of psychosis or secondary gain"
  ],
  "remedies": [
    "Cognitive Behavioral Therapy (focusing on distress management)",
    "Antidepressants (SSRIs) to reduce the obsessive 'Uninstall' loop",
    "Mirror therapy (experimental, attempting to 're-mount' the limb)",
    "Ethical debate regarding 'Elective Amputation' as a functional cure"
  ],
  "prevention": [
    "Currently unknown (likely a deep-seated developmental neuro-architecture error)"
  ]
}

"phantom_limb_syndrome": {
  "description": "The sensation that an amputated or missing limb is still attached to the body and is moving appropriately with other body parts.",
  "symptoms": [
    "Vivid sensation of the limb's presence (length, weight, and volume)",
    "Phantom pain (cramping, burning, or shooting sensations)",
    "Telescoping (feeling that the phantom limb is shrinking over time)",
    "Kinesthetic sensations (feeling the 'ghost' hand grasp an object)",
    "Triggering of the phantom by touching other body parts (e.g., the face)"
  ],
  "causes": [
    "Cortical Remapping in the Somatosensory Cortex",
    "Persistence of the 'Neuromatrix' (the hardcoded body map)",
    "Spontaneous firing from the dorsal horn of the spinal cord",
    "Peripheral nerve irritation at the site of amputation (neuromas)",
    "Mismatch between motor commands and sensory feedback"
  ],
  "risk_factors": [
    "Pre-amputation pain (the brain 'saves' the pain state)",
    "Upper limb amputations (more common than lower limb)",
    "Sudden traumatic loss of a limb"
  ],
  "diagnosis": [
    "Clinical history and subjective reporting",
    "fMRI showing activity in the 'vacant' cortical regions",
    "Physical mapping of 'Referred Sensation' zones",
    "Exclusion of localized stump pain"
  ],
  "remedies": [
    "Mirror Box Therapy (Visual feedback to 'reset' the brain)",
    "TENS (Transcutaneous Electrical Nerve Stimulation)",
    "Targeted Muscle Reinnervation (TMR)",
    "Graded Motor Imagery (GMI)",
    "Neuromodulation (Spinal cord stimulators)"
  ],
  "prevention": [
    "Aggressive pain management before elective surgeries",
    "Immediate post-operative sensory feedback training"
  ]
}

"reduplicative_paramnesia": {
  "description": "A delusional belief that a place or location has been duplicated, exists in two places at once, or has been relocated to another site.",
  "symptoms": [
    "Insisting the current room is an 'identical copy' of the original",
    "Believing the hospital has been 'shipped' or moved to their hometown",
    "Identifying familiar landmarks but claiming they belong to a 'second version' of the city",
    "Confabulation to explain the discrepancy (e.g., 'They built a replica of my house here')",
    "Intact recognition of people and objects (only the 'Location Tag' is corrupted)"
  ],
  "causes": [
    "Damage to the Right Cerebral Hemisphere (Spatial Processing)",
    "Bilateral Frontal Lobe lesions (Executive Monitoring failure)",
    "Disconnection between the Hippocampus (Spatial Memory) and the Frontal Cortex",
    "Post-stroke ischemia or Traumatic Brain Injury (TBI)",
    "Severe encephalopathy or neurodegeneration"
  ],
  "risk_factors": [
    "Right-hemisphere stroke affecting the parietal or temporal lobes",
    "Dementia or Alzheimer's-related atrophy",
    "Acute brain swelling or inflammation"
  ],
  "diagnosis": [
    "The 'Location Mapping' test (asking the patient to explain their current coordinates)",
    "MRI/CT to identify right-hemisphere and frontal lesions",
    "Neuropsychological assessment of spatial orientation",
    "Exclusion of generalized delirium"
  ],
  "remedies": [
    "Orientation therapy (using external GPS/Maps to challenge the delusion)",
    "Managing the underlying neurological injury (stroke recovery, anti-inflammatories)",
    "Environmental 'Anchoring' (fixed, unmoving markers of reality)",
    "Antipsychotic medication to reduce delusional rigidity"
  ],
  "prevention": [
    "Standard neuro-protective health and stroke prevention"
  ]
}

"foreign_accent_syndrome": {
  "description": "A speech disorder where changes in the timing, intonation, and tongue placement cause a speaker to sound as though they have a foreign accent.",
  "symptoms": [
    "Vowel elongation or distortion (e.g., 'cup' sounding like 'koop')",
    "Inappropriate voicing of consonants ('p' sounding like 'b')",
    "Insertion of extra vowels between consonant clusters",
    "Altered pitch and rhythm (Staccato speech)",
    "The patient sounds like a 'non-native' speaker of their own language"
  ],
  "causes": [
    "Damage to the Left Premotor Cortex (Broca’s Area)",
    "Lesions in the Basal Ganglia or Cerebellum (the timing hardware)",
    "Stroke or TBI affecting the 'Speech Motor' planning",
    "Psychogenic triggers (rare, associated with severe trauma)",
    "Multiple Sclerosis (MS) lesions"
  ],
  "risk_factors": [
    "Vascular disease in the left hemisphere",
    "History of complex migraines affecting speech",
    "High-impact head trauma"
  ],
  "diagnosis": [
    "Acoustic analysis of speech patterns (Pitch/Duration mapping)",
    "MRI to identify lesions in the motor speech planning centers",
    "Evaluation by a Speech-Language Pathologist (SLP)",
    "Exclusion of Aphasia (the ability to find words is usually intact)"
  ],
  "remedies": [
    "Speech therapy to 're-map' native phonetic targets",
    "Cognitive-behavioral therapy to manage the 'Identity Crisis'",
    "Imitation therapy (mimicking native speakers)",
    "Treating the underlying vascular or neurological cause"
  ],
  "prevention": [
    "Standard cardiovascular health to prevent stroke",
    "Head protection to avoid TBI"
  ]
}

"object_capgras_syndrome": {
  "description": "A delusional misidentification where a patient believes that familiar inanimate objects have been replaced by identical replicas or 'fake' versions.",
  "symptoms": [
    "Emotional detachment from high-value personal assets (home, wedding ring)",
    "Insisting a replacement is 'too perfect' or 'missing the soul' of the original",
    "Hoarding the 'fakes' while searching for the 'originals'",
    "Treating the object with suspicion or hostility",
    "Intact visual recognition (the 'checksum' of the object's appearance is correct)"
  ],
  "causes": [
    "Disconnection between the Ventral Visual Stream and the Autonomic Nervous System",
    "Damage to the Perirhinal Cortex (responsible for object-familiarity)",
    "Right-hemisphere lesions affecting 'Global Integration'",
    "Post-stroke ischemia in the posterior cerebral arteries",
    "Severe neurodegeneration (Dementia with Lewy Bodies)"
  ],
  "risk_factors": [
    "Traumatic Brain Injury (TBI) to the right parietal/temporal regions",
    "History of complex psychiatric disorders",
    "Advanced age with vascular complications"
  ],
  "diagnosis": [
    "Neuropsychological testing for 'Object-Affect' (how does the object feel?)",
    "MRI to check for lesions in the right-sided visual-emotional pathways",
    "Skin Conductance Response (SCR) testing to see if familiar objects trigger a 'warmth' signal",
    "Clinical interview focusing on 'Object-Identity' logic"
  ],
  "remedies": [
    "Treating the underlying neurological injury",
    "Validation therapy (avoiding direct confrontation of the 'replica' theory)",
    "Environmental 'tagging' (adding unique, non-visual markers to items)",
    "Antipsychotic medication to stabilize the belief-monitoring system"
  ],
  "prevention": [
    "Standard cardiovascular and neuroprotective health protocols"
  ]
}

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
"anton_babinski_syndrome": {
  "description": "A rare condition in which patients who are cortically blind (due to brain damage) deny their blindness and attempt to behave as if they can see.",
  "symptoms": [
    "Total blindness (lack of light perception)",
    "Anosognosia (complete lack of insight into the deficit)",
    "Confabulation (inventing detailed descriptions of the surroundings)",
    "Bumping into objects while insisting they 'just didn't see them'",
    "Aggressive defense of their 'vision' when challenged"
  ],
  "causes": [
    "Bilateral lesions in the Occipital Lobe (the primary visual cortex)",
    "Disconnection between the visual processing area and the 'Self-Monitoring' center",
    "Ischemic stroke in the posterior cerebral arteries",
    "Traumatic Brain Injury (TBI) to the back of the head"
  ],
  "risk_factors": [
    "High blood pressure and vascular disease",
    "Advanced age (increased stroke risk)",
    "Severe head trauma"
  ],
  "diagnosis": [
    "Visual field testing (patient fails all light/motion tests)",
    "MRI/CT showing bilateral damage to the primary visual cortex (V1)",
    "The 'Fingers Test' (patient guesses wildly while claiming to see them)",
    "Neurological assessment of the frontal lobe (monitoring function)"
  ],
  "remedies": [
    "Treating the underlying stroke or inflammation",
    "Occupational therapy for safety and navigation",
    "Neuropsychological counseling to address the anosognosia",
    "Time (the 'denial' flag occasionally resets as the brain heals)"
  ],
  "prevention": [
    "Aggressive management of cardiovascular health",
    "Use of protective headgear in high-risk environments"
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
"mirrored_self_misidentification": {
  "description": "A delusional misidentification syndrome where an individual is unable to recognize their own reflection in a mirror, treating it as a separate person.",
  "symptoms": [
    "Talking to the reflection as if it were another person",
    "Feeling 'followed' or watched by the person in the mirror",
    "Intact recognition of other people in the mirror (e.g., recognizing a spouse standing behind them)",
    "Attempts to cover or remove mirrors to 'hide' from the stranger",
    "Logic loops: 'He looks like me and moves like me, but he isn't me'"
  ],
  "causes": [
    "Right Hemisphere damage (specifically the Right Frontal and Parietal lobes)",
    "Disconnection between the visual 'Face' processing and 'Self-Referential' logic",
    "Impaired 'Mirror Neuron' integration",
    "Advanced Alzheimer’s or dementia (system-level resource depletion)"
  ],
  "risk_factors": [
    "History of right-sided stroke",
    "Neurodegenerative diseases",
    "Severe atrophy in the prefrontal cortex"
  ],
  "diagnosis": [
    "The 'Mirror Test' (observing interactions with a reflection)",
    "CT/MRI to locate right-hemisphere lesions",
    "Neuropsychological testing for 'Self-Monitoring' and 'Belief Evaluation'",
    "Assessment of mirror-concept (can they explain how a mirror works?)"
  ],
  "remedies": [
    "Covering mirrors to reduce 'Visual Interrupts'",
    "Antipsychotic medication to dampen the delusional logic",
    "Consistent environmental cues (labels, photos of the 'Self' at different ages)",
    "Validation therapy (reducing the distress of the 'Stranger')"
  ],
  "prevention": [
    "Management of vascular health to prevent right-hemisphere ischemia"
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
"semantic_dementia_schema_failure": {
  "description": "A progressive, irreversible corruption of the central relational database schemas where the core dictionary definitions of objects are permanently deleted, leaving the hardware fully operational but rendering the system unable to decode conceptual meanings.",
  "symptoms": [
    "Granular Class Truncation: Loss of specialized, low-level object classifications while temporarily retaining broad, abstract root categories (e.g., calling an eagle a 'bird', then later a 'thing')",
    "Structural Definition Dropout: Absolute loss of functional object comprehension; everyday tools, animals, and items lose their associated utility maps",
    "Preserved Lexical Mechanics: Flawless ability to execute surface-level language tasks, such as syntax checking, grammatical formatting, and reading aloud complex words without understanding their context",
    "Associative Matching Collapse: Inability to pair conceptually related assets (e.g., failing to match a picture of a hammer with a picture of a nail, despite seeing both perfectly)",
    "Preserved Non-Semantic Pipelines: Intact retention of short-term episodic memory logs, spatial orientation grids, and procedural motor macros (the user can drive a car but cannot define what a car is)"
  ],
  "causes": [
    "Asymmetric Anterior Temporal Lobe Atrophy: Ubiquitin-positive and TDP-43 protein inclusions aggregating within the cortical layers, causing structural cell death across the semantic hub",
    "Ventral Stream Disconnection: Degradation of the white-matter tract cables (uncinate fasciculus) that link visual processing arrays to the conceptual routing engines"
  ],
  "risk_factors": [
    "Primary progressive aphasia spectrum anomalies affecting mid-to-late career execution lifecycles",
    "Genetic mutations within the GRN (Granulin) or MAPT (Microtubule-Associated Protein Tau) system operational genes"
  ],
  "diagnosis": [
    "The 'Pyramids and Palm Trees' Schema Audit: Presenting an asset token (e.g., a Pyramid) and forcing the system to link it to one of two conceptual choices (a Palm Tree or a Pine Tree); tracking the absolute failure of semantic association rules",
    "Granular Lexical Naming Evaluation: Confronting the system with direct visual assets of low-frequency items (e.g., a stethoscope, an anvil) and observing immediate asset-lookup timeouts",
    "High-Resolution Volumetric MRI: Detecting profound, localized, knife-edge tissue volume drops isolated strictly within the bilateral or left-dominant anterior temporal lobes"
  ],
  "remedies": [
    "Procedural Macro Hard-Coding: Relying heavily on intact procedural and motor memory systems to execute daily routines implicitly, bypassing the broken semantic lookup servers",
    "Visual Symbol Replacement Dashboards: Using basic, simplified iconographies anchored directly to physical actions to slow down the functional isolation of the user interface",
    "Environmental Optimization Shunting: Simplifying the external operational space to reduce the volume of unknown object tokens hitting the damaged parsing hubs"
  ],
  "prevention": [
    "No current low-level hardware or software patch exists to halt the progressive degradation of the physical temporal storage disks once protein aggregation scripts initiate"
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

