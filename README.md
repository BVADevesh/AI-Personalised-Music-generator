<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>🎵 Personalized AI Music Generator</h1>
  <p>
    An intelligent music generation system that creates personalized audio tracks based on user moods, genres, and preferences using deep learning techniques and symbolic/audio modeling.
    Built for researchers, hobbyists, and AI music enthusiasts looking to explore generative creativity in music.
  </p>

  <h2>📌 Project Overview</h2>
  <p>
    This project aims to blend user-centered design with generative AI to produce music that's not just algorithmically generated — 
    but <strong>emotionally resonant</strong> and <strong>context-aware</strong>. Users can input their preferences or provide sample MIDI files, 
    and the AI will generate musically coherent tracks using pretrained or fine-tuned models.
  </p>

  <h2>🛠️ Features</h2>
  <ul>
    <li>🎶 Mood- and genre-based music generation</li>
    <li>🎹 Support for symbolic (MIDI) and audio output</li>
    <li>🧠 Fine-tuning on user-provided data for personalization</li>
    <li>⚙️ Modular design: easy to plug in custom models or utilities</li>
    <li>📊 Feedback-driven generation (likes/dislikes)</li>
    <li>📈 Notebook-based experimentation and model exploration</li>
  </ul>

  <h2>🧱 Project Structure</h2>
  <pre>
personalized_music_generator/
│
├── data/
│   ├── input_midi/
│   ├── generated_midi/
│   └── audio_output/
│
├── models/
│   └── music_vae/
│
├── src/
│   ├── config.py
│   ├── generator.py
│   ├── midi_utils.py
│   ├── audio_utils.py
│   └── personalization.py
│
├── feedback/
│   └── feedback_log.json
│
├── notebooks/
│   └── exploration.ipynb
│
├── app.py
├── requirements.txt
└── README.md
  </pre>

  <h2>🚀 Getting Started</h2>
  <h3>1. Clone the repository</h3>
  <pre><code>
git clone https://github.com/klu2200032499/AI-Personalised-Music-generator.git
cd AI-Personalised-Music-generator
  </code></pre>

  <h3>2. Install dependencies</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>3. Run the application</h3>
  <pre><code>python app.py</code></pre>

  <h2>🎧 Example Use Case</h2>
  <blockquote>
    “Generate lo-fi chill beats using piano and ambient textures, tailored for evening study sessions with a calm mood.”
  </blockquote>

  <h2>🧠 Models Used</h2>
  <ul>
    <li><a href="https://github.com/magenta/magenta/tree/main/magenta/models/music_vae" target="_blank">Magenta MusicVAE</a></li>
    <li>PyTorch-based Transformer / LSTM for symbolic generation</li>
    <li>FluidSynth / pretty_midi for MIDI-to-audio conversion</li>
  </ul>

  <h2>📦 Dependencies</h2>
  <pre><code>
pretty_midi
fluidsynth
torch
magenta
numpy
  </code></pre>

  <h2>🤝 Contributing</h2>
  <ol>
    <li>Fork the repo</li>
    <li>Create a new branch (<code>git checkout -b feature/your-feature</code>)</li>
    <li>Make your changes</li>
    <li>Push and create a PR</li>
  </ol>
<hr>
 <h2> LICENSE</h2>
 <p> MIT License

Copyright (c) 2026 Bellamkonda V A Devesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to some Conditons</p>
 <hr>
  <h2>🙋‍♂️ Author</h2>
  <p>
    Developed by <strong>Bellamkonda V A Devesh</strong><br>
    For research, collaboration, or freelance inquiries, connect on 
    <a href="https://www.linkedin.com/in/bellamkonda-v-81511a289/" target="_blank">LinkedIn</a>.
  </p>

  <hr>
  <blockquote><em>
    “Where words fail, music speaks — especially when it’s AI-generated and personalized.”
  </em></blockquote>

</body>
</html>
