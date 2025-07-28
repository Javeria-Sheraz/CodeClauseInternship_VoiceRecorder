import tkinter as tk
import wave
from datetime import datetime
import numpy as np
import sounddevice as sd
from tkinter import messagebox
import time

class voiceRecorder:
    def __init__(self, timer_label):
        self.fs = 44100
        self.recording = False
        self.audio_data = []
        # A list for storing recorded audio data
        # we take 44100 samples per second which is the standard CD quality
        self.timer_label = timer_label
        self.start_time = None

    def startRecording(self):
        if self.recording:
            return
        # Exit of out this method if the recording is already in progress
        self.recording = True
        self.audio_data = []
        self.start_time = time.time()
        self.update_timer()
        # messagebox.showinfo("Recording", "Recording started...")
        self._record() 
        # Show popup using tkinter.messagebox
        # Actual recording starts using a private method

    def update_timer(self):
        if self.recording:
            elapsed = int(time.time() - self.start_time)
            # subtracting current time in secs with time since recording started to calculate duration
            mins, secs = divmod(elapsed, 60)
            # Elaspsed duration is split into minutes and seconds
            hours, mins = divmod(mins, 60)
            # Minutes are split into hours
            self.timer_label.config(text = f"Recording: {hours: 02d}:{mins:02d}:{secs:02d}")
            self.timer_label.after(1000, self.update_timer)
            # Update the timer after every second
        else:
            self.timer_label.config(text = "Not Recording")

    #record is a private method because it should be called inside the class only to keep things organized
    def _record(self):
        def callback(indata, frames, time, status):
            if self.recording:
                self.audio_data.append(indata.copy())
        # Callback is called repeatedly and inputs data from mic
        self.stream = sd.InputStream(samplerate=self.fs, channels =1, callback=callback)
        self.stream.start()
        #InputStream starts the mic input, 1 channel means we are using 1 mic
        # Stream sets the mic so everytime audio is detected it captures the sound

    def stopRecording(self):
        if not self.recording:
            return
        self.recording = False
        self.stream.stop()
        self.stream.close()
        messagebox.showinfo("Recording", "Recording stopped...")
        self.save_recording()

    def save_recording(self):
        filename = f"Audio_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.wav"
        audio = np.concatenate(self.audio_data)
        # This generates a filename using current date and time. "audio" joins list of arrays to one big array
        audio = np.int16(audio * 32767)
        # Audio is in float format (between -1 and 1). We scale it to 16-bit integer by multiplying with 32767.
        # np.int16() converts it to a format WAV can store.

        # This opens .wav file to write
        with wave.open(filename, 'w') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(self.fs)
            wf.writeframes(audio.tobytes())
        # Channel is set as mono. Set amplitude width as 2 bytes (16 bits)
        # Set frame rate as our recording rate. Write frames to save audio data as bytes
        messagebox.showinfo("Saved", f"Recording saved as {filename}")

def create_gui():
    # Creates a small window with a title
    window = tk.Tk()
    window.title("Simple Python Voice Recorder")
    window.geometry("480x400")
    window.configure(bg="#3f055f") #Dark background

    title = tk.Label(window, text = "Voice Recorder", font=("Arial", 26, "bold"), fg="white", bg="#3f055f")
    title.pack(pady=21)

    timer_label = tk.Label(window, text = "Not Recording", font = ("Consolas", 17, "bold"), fg = "red", bg = "#3f055f")
    timer_label.pack(pady=12)

    recorder = voiceRecorder(timer_label)
    btn_style = {"font": ("Helvetica", 14), "width":19, "bg":"#6e4eff", "fg":"white", "bd":2}
    # This is a dictionary holding common styling for buttons

    tk.Button(window, text="Start Recording", command=recorder.startRecording, **btn_style).pack(pady=8)
    tk.Button(window, text="Stop Recording", command=recorder.stopRecording, **btn_style).pack(pady=8)
    tk.Button(window, text="Exit", command=window.destroy, **btn_style).pack(pady=8)
    
    window.mainloop()
    # It starts the main event loop, which keeps the window open and responsive to clicks.

if __name__ == "__main__":
    create_gui()







        




        






