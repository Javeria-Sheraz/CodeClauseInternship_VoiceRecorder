# CodeClauseInternship VoiceRecorder


# 🎙️ Python Voice Recorder (`soundRecorder.py`)

A clean, beginner‑friendly GUI voice recorder built in Python. Features GUI creation with Tkinter, basic OOP, and handling audio with `sounddevice`.

## 🚀 Features

* Record audio from your mic with **Start / Stop** controls
* **Real‑time timer** display (HH\:MM\:SS)
* Save recordings automatically as `.wav` files
* Minimal and modern Tkinter GUI
* Encapsulated logic using Python classes


---

## 📥 Requirements

Install required Python packages:

```
sounddevice==0.4.6
numpy==1.26.4
```

Tkinter, `wave`, and `datetime` come built‑in with standard Python. No install needed.

---

## 💡 How to Run

### 1. Download or Clone

```bash
git clone https://github.com/Javeria-Sheraz/CodeClauseInternship_VoiceRecorder.git
cd CodeClauseInternship_VoiceRecorder
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies (Or install sounddevice and numpy libraries separately)

```bash
pip install -r requirements.txt
```

### 4. Launch the App

```bash
python soundRecorder.py
```

Make sure your microphone is connected and working fine.

---

## 🖥️ What Happens

* GUI window opens with **Start**, **Stop**, and **Exit** buttons.
* Clicking **Start** begins recording and shows a live timer.
* Clicking **Stop** ends recording and saves a `.wav` file with a timestamped filename (e.g. `recording_20250728_153025.wav`).
* Clicking **Exit** closes the app (and stops recording if in progress).

---

## 🧠 Logic of the code

* Uses `sounddevice.InputStream` to process live mic input.
* Audio chunks are collected via a **callback** function and stored in memory.
* `numpy.concatenate` joins chunks and scales values properly to 16-bit PCM.
* Tkinter's `.after()` method updates the timer label every second without freezing the GUI.

---

## 🛠️ Troubleshooting Tips

| Problem                             | Fix                                                                         |
| ----------------------------------- | --------------------------------------------------------------------------- |
| GUI doesn't appear                  | Ensure you're using `window.mainloop()` and launching the correct script    |
| Microphone not recording            | Check system permissions and default audio device settings                  |
| Python errors about missing modules | Verify that `sounddevice` and `numpy` are properly installed                |
| No `.wav` file output               | Make sure you clicked **Stop** and script saved data into working directory |

---

## 📝 Credits

Created by **Javeria Sheraz**


