.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/emotion_engine.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/emotion_engine
    .. image:: https://readthedocs.org/projects/emotion_engine/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://emotion_engine.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/emotion_engine/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/emotion_engine
    .. image:: https://img.shields.io/pypi/v/emotion_engine.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/emotion_engine/
    .. image:: https://img.shields.io/conda/vn/conda-forge/emotion_engine.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/emotion_engine
    .. image:: https://pepy.tech/badge/emotion_engine/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/emotion_engine
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/emotion_engine

.. .. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
..     :alt: Project generated with PyScaffold
..     :target: https://pyscaffold.org/

.. |

.. ==============
.. emotion_engine
.. ==============


..     Add a short description here!


.. A longer description of your project goes here...


.. .. _pyscaffold-notes:

.. Note
.. ====

.. This project has been set up using PyScaffold 4.6. For details and usage
.. information on PyScaffold see https://pyscaffold.org/.


emotion_engine
==============

Multimodal Emotion Recognition Engine combining **audio**, **speech-to-text (ASR)**,
and **text-based emotion classification**, with a simple CLI and Python API.

This project is designed as a modular engine that can:
- 🎙️ Listen from microphone
- 📂 Analyze audio files
- 🧠 Fuse audio + text emotion signals
- ⚡ Run locally with pretrained models

---

Features
--------

- **Audio emotion recognition**
  - MFCC + pitch based model
- **Speech-to-text (ASR)**
  - Powered by `faster-whisper`
- **Text emotion classification**
  - DistilRoBERTa emotion model
- **CLI interface**
  - `emotion-engine listen`
  - `emotion-engine analyze <file>`
- **Python API**
- **PyScaffold-based project structure**
- **Tested with pytest**

---

Project Structure
-----------------

::

    emotion_engine/
    ├── src/emotion_engine/
    │   ├── audio/
    │   │   ├── emotion_model.py
    │   │   ├── features.py
    │   │   └── mic.py
    │   ├── text/
    │   │   └── asr.py
    │   ├── engine.py
    │   ├── cli.py
    │   └── config.py
    ├── models/
    │   └── emotion_model.pt
    ├── tests/
    ├── pyproject.toml
    └── setup.cfg

---

Installation
------------

### 1. Clone the repository

.. code-block:: bash

    git clone https://github.com/satsin06/emotion_engine.git
    cd emotion_engine

---

### 2. Create and activate a virtual environment (recommended)

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate   # macOS / Linux
    venv\Scripts\activate      # Windows

---

### 3. Install the package

#### Minimal install

.. code-block:: bash

    pip install -e .

#### With audio support

.. code-block:: bash

    pip install -e ".[audio]"

#### With ASR support

.. code-block:: bash

    pip install -e ".[asr]"

#### Full installation (recommended)

.. code-block:: bash

    pip install -e ".[full]"

---

CLI Usage
---------

After installation, the CLI command is available as:

.. code-block:: bash

    emotion-engine --help

### 🎙️ Listen from microphone

.. code-block:: bash

    emotion-engine listen

This will:
- Record audio from your microphone
- Run emotion recognition
- Print emotion probabilities

Press **Ctrl+C** to stop recording (microphone is safely closed).

---

### 📂 Analyze an audio file

.. code-block:: bash

    emotion-engine analyze path/to/audio.wav

---

Python API Usage
----------------

You can also use the engine programmatically:

.. code-block:: python

    from emotion_engine.engine import EmotionEngine

    engine = EmotionEngine()
    result = engine.analyze_file("sample.wav")

    print(result)

Example output:

.. code-block:: python

    {
        "neutral": 0.38,
        "happy": 0.10,
        "sad": 0.11,
        "angry": 0.05
    }

---

Models
------

- **Audio emotion model**
  - Stored in: ``models/emotion_model.pt``
- **Text emotion model**
  - ``j-hartmann/emotion-english-distilroberta-base`` (downloaded automatically)
- **ASR model**
  - Faster-Whisper (downloaded on first use)

Models are cached under:

::

    ~/.cache/emotion-engine/

---

Running Tests
-------------

Install test dependencies:

.. code-block:: bash

    pip install -e ".[dev]"

Run tests:

.. code-block:: bash

    pytest

---

Development Notes
-----------------

- Python ≥ 3.9
- PyScaffold 4.6
- Type hints enabled (Pylance / MyPy friendly)
- Modular design for future multimodal fusion

---

Roadmap
-------

- [ ] Real-time streaming emotion detection
- [ ] Multilingual ASR
- [ ] Emotion fusion weighting
- [ ] REST API
- [ ] Model retraining pipeline

---

License
-------

MIT License. See ``LICENSE.txt`` for details.

---

Author
------

**Satyam Sinha**

- GitHub: https://github.com/satsin06
- Email: satyamsinha9404@gmail.com
