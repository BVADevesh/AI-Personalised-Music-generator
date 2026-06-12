import streamlit as st
import pretty_midi
import numpy as np
import tempfile
import os
import json
from datetime import datetime

# ----------------------------------------
# Page Config
# ----------------------------------------

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

# ----------------------------------------
# Helpers
# ----------------------------------------

MOODS = {
    "Happy": {
        "scale": [60, 62, 64, 65, 67, 69, 71],
        "tempo": 140
    },
    "Sad": {
        "scale": [60, 62, 63, 65, 67, 68, 70],
        "tempo": 70
    },
    "Calm": {
        "scale": [60, 62, 64, 67, 69],
        "tempo": 80
    },
    "Energetic": {
        "scale": [60, 64, 67, 72, 76],
        "tempo": 170
    },
    "Romantic": {
        "scale": [60, 63, 67, 70, 72],
        "tempo": 90
    }
}

INSTRUMENTS = {
    "Piano": 0,
    "Guitar": 24,
    "Violin": 40,
    "Flute": 73,
    "Trumpet": 56,
    "Strings": 48
}

# ----------------------------------------
# Music Generator
# ----------------------------------------

def generate_music(
        mood,
        instrument,
        duration):

    midi = pretty_midi.PrettyMIDI()

    program = INSTRUMENTS[instrument]

    inst = pretty_midi.Instrument(
        program=program
    )

    scale = MOODS[mood]["scale"]

    notes_count = duration * 4

    current = 0

    for _ in range(notes_count):

        pitch = np.random.choice(scale)

        note = pretty_midi.Note(
            velocity=np.random.randint(70, 120),
            pitch=int(pitch),
            start=current,
            end=current + 0.5
        )

        inst.notes.append(note)

        current += 0.5

    midi.instruments.append(inst)

    return midi


# ----------------------------------------
# Feedback
# ----------------------------------------

def save_feedback(
        mood,
        genre,
        feedback):

    filename = "feedback.json"

    if os.path.exists(filename):

        with open(filename, "r") as f:
            data = json.load(f)

    else:
        data = []

    data.append({

        "time":
            str(datetime.now()),

        "mood":
            mood,

        "genre":
            genre,

        "feedback":
            feedback

    })

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ----------------------------------------
# UI
# ----------------------------------------

st.title("🎵 Personalized AI Music Generator")

st.markdown(
"""
Generate AI-composed music
based on mood and preferences.
"""
)

col1, col2 = st.columns(2)

with col1:

    mood = st.selectbox(
        "Mood",
        list(MOODS.keys())
    )

    genre = st.selectbox(
        "Genre",
        [
            "LoFi",
            "Classical",
            "Jazz",
            "Ambient",
            "Pop"
        ]
    )

with col2:

    instrument = st.selectbox(
        "Instrument",
        list(INSTRUMENTS.keys())
    )

    duration = st.slider(
        "Duration (seconds)",
        10,
        120,
        30
    )

# ----------------------------------------
# Generate
# ----------------------------------------

if st.button("🎶 Generate Music"):

    with st.spinner(
            "Composing your music..."):

        midi = generate_music(
            mood,
            instrument,
            duration
        )

        temp_dir = tempfile.mkdtemp()

        midi_path = os.path.join(
            temp_dir,
            "generated.mid"
        )

        midi.write(midi_path)

    st.success(
        "Music generated!"
    )

    with open(
            midi_path,
            "rb"
    ) as file:

        st.download_button(
            label="⬇ Download MIDI",
            data=file,
            file_name=f"{mood}.mid",
            mime="audio/midi"
        )

# ----------------------------------------
# Feedback
# ----------------------------------------

st.divider()

st.subheader(
    "Did you like the music?"
)

c1, c2 = st.columns(2)

with c1:

    if st.button("👍 Like"):

        save_feedback(
            mood,
            genre,
            "Like"
        )

        st.success(
            "Feedback Saved!"
        )

with c2:

    if st.button("👎 Dislike"):

        save_feedback(
            mood,
            genre,
            "Dislike"
        )

        st.warning(
            "Feedback Recorded."
        )

# ----------------------------------------
# Footer
# ----------------------------------------

st.divider()

st.caption(
"""
Built with Python,
Streamlit,
PrettyMIDI,
and AI-inspired music generation.
"""
)
