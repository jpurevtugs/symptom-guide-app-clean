import streamlit as st

# title + captions 
st.title("symptom-to-care guide ✱⚕️")
st.caption("this app does NOT provide medical diagnosis - it only gives general guidance")
st.write("urgent care vs ER vs wait it out")

# symptoms by body system 
symptoms_by_system = {
    "cardiovascular": [
        "chest pain", "heart palpitations", "shortness of breath", "sudden weakness", "loss of consciousness"
    ],
    "respiratory": [
        "persistent cough", "mild cough", "difficulty breathing", "mild shortness of breath"
    ],
    "gastrointestinal": [
        "severe abdominal pain","moderate abdominal pain","mild stomachache","vomiting","persistent diarrhea","nausea",
        "mild nausea","mild indigestion","mild bloating","mild cramps"
    ],
    "neurological": [
        "severe headache","moderate headache","mild headache","seizure","slurred speech","sudden confusion",
        "loss of coordination","severe dizziness","mild dizziness","sudden numbness","sudden paralysis"
    ],
    "musculoskeletal": [
        "severe trauma","moderate cough","mild muscle soreness","mild joint pain","back pain",
        "mild back pain","minor backache","sprains","minor joint stiffness"
    ],
    "dermatological": [
        "mild rash","moderate rash","mild bruising","minor scratch","minor bruise","mild itchy eyes","mild seasonal allergy"
    ],
    "ENT / eye / ear": [
        "ear pain","sinus pain","pink eye","runny nose","mild congestion","mild sore throat","sore throat with fever","mild sneezing"
    ],
    "other": [
        "fever","high fever with stiff neck","fainting","severe vomiting","severe dehydration",
        "mild fever","occasional fatigue","persistent fatigue","minor cramp","minor stomachache",
        "mild heartburn","mild chest discomfort","cut that needs stitches","uncontrolled bleeding","poisoning",
        "minor muscle pain","minor headache","traumatic injury","severe burns","mild burns","mild allergic reaction",
        "moderate headache","tooth pain","urinary discomfort","swollen lymph nodes","difficulty speaking",
        "severe eye pain","severe allergic reaction"
    ]
}

# multiselect filtering 
all_symptoms = sorted(set([s for system in symptoms_by_system.values() for s in system]))

# dropdown by body system 
selected_symptoms = []

for system, symptoms in symptoms_by_system.items():
    with st.expander(system):
        # use multiselect inside each expander with typeahead
        selected = st.multiselect(
            f"select symptom(s) in {system}:", 
            sorted(symptoms),
            key=system  # key needed because we have multiple multiselects
        )
        selected_symptoms.extend(selected)

# display guidance 
er_symptoms = [
    "chest pain","shortness of breath","severe abdominal pain","severe headache","loss of consciousness",
    "seizure","sudden weakness","slurred speech","severe trauma","difficulty breathing",
    "severe allergic reaction","fainting","severe burns","uncontrolled bleeding","sudden vision loss",
    "sudden confusion","severe vomiting","severe dehydration","high fever with stiff neck","poisoning",
    "heart palpitations","difficulty speaking","severe dizziness","severe back pain","traumatic injury",
    "sudden numbness","sudden paralysis","loss of coordination","severe eye pain"
]

urgent_symptoms = [
    "fever","vomiting","persistent diarrhea","moderate abdominal pain","mild allergic reaction",
    "ear pain","mild dehydration","mild chest discomfort","persistent cough","sore throat with fever",
    "mild rash","cut that needs stitches","sprains","mild burns","moderate headache",
    "tooth pain","sinus pain","pink eye","urinary discomfort","swollen lymph nodes",
    "mild dizziness","persistent fatigue","nausea","mild swelling","back pain",
    "mild shortness of breath","moderate rash","mild palpitations","mild fever","mild joint pain",
    "mild congestion","mild muscle soreness","moderate cough","moderate headache","moderate nausea"
]

monitor_symptoms = [
    "mild headache","mild sore throat","mild stomachache","mild cough","mild fatigue",
    "mild nausea","mild rash","mild dizziness","mild back pain","mild joint pain",
    "mild swelling","mild bruising","mild cut","mild congestion","mild muscle soreness",
    "mild heartburn","mild bloating","mild cramps","mild seasonal allergy","mild itchy eyes",
    "runny nose","minor scratch","minor bruise","minor cramp","minor joint stiffness",
    "occasional fatigue","mild indigestion","mild headache with cold","mild sneezing","minor stomachache",
    "minor muscle pain","minor headache","minor backache","minor cough"
]

def show_guidance(symptom_list):
    for s in symptom_list:
        st.markdown(f"**{s}**")
        if s in er_symptoms:
            st.error("go to the ER immediately")
            st.caption("[CDC Emergency Symptoms Guidelines](https://www.cdc.gov/)")
        elif s in urgent_symptoms:
            st.warning("consider urgent care")
            st.caption("[CDC Urgent Care Guidelines](https://www.cdc.gov/)")
        elif s in monitor_symptoms:
            st.info("you can likely monitor at home")
            st.caption("[CDC Self-Care Guidelines](https://www.cdc.gov/)")
        st.write("---")

if selected_symptoms:
    show_guidance(selected_symptoms)