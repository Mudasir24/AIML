# AIML — Coursework & Labs

Notebooks, lab exercises, and one standalone bonus project from an AI/ML course.
This is coursework, not a portfolio showcase repo — kept public as a record of
what was covered, with one small app (Task-6) that grew into something more
polished than the rest.

## 📓 Contents

| File | Topic |
|---|---|
| [`Task1.py`](./Task1.py) | Python OOP basics — `Pet`/`Dog` class hierarchy |
| [`Task2/Task-2.ipynb`](./Task2/Task-2.ipynb) | Linear Regression (diabetes dataset) and KMeans clustering (sneaker image dataset) |
| [`Task-3.ipynb`](./Task-3.ipynb) | Neural network basics on MNIST with Keras |
| [`Task4.ipynb`](./Task4.ipynb) | Real-time bicep curl counter using OpenCV + MediaPipe pose estimation |
| [`Task-5.ipynb`](./Task-5.ipynb) | Teaching an AI to play NIM via Q-learning (reinforcement learning) |
| [`Task-6/`](./Task-6) | **Analogizer Bot** — a small Flask web app that generates funny analogies with voice input/output. See its own [README](./Task-6/README.md). |
| [`AIML_Module_01_Lab_03_Data_Augmentation.ipynb`](./AIML_Module_01_Lab_03_Data_Augmentation.ipynb) | Course-provided lab notebook on data augmentation techniques |
| [`AIML_Tutorial_Training_a_Neural_Network.ipynb`](./AIML_Tutorial_Training_a_Neural_Network.ipynb) | Course-provided tutorial notebook on how neural networks work |

> **Note on the two "Module"/"Tutorial" notebooks:** these read as instructor-provided
> teaching material worked through during the course, rather than originally
> authored assignments like the numbered Tasks. Keeping that distinction clear
> here so the repo doesn't imply more original authorship than is accurate —
> nothing wrong with keeping them for reference, just worth being upfront about
> what's original work versus course material you completed.

## 🎯 Highlight: Analogizer Bot (Task-6)

The most complete piece here — a Flask app combining an LLM (via Groq), speech
transcription (Whisper), text-to-speech (ElevenLabs), and reaction GIFs (Giphy)
into a lighthearted "generate a funny comparison about yourself" tool. See
[`Task-6/README.md`](./Task-6/README.md) for setup and details.
