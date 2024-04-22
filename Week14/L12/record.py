import sounddevice as sd 
from scipy.io import wavfile as wf

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

print("Recording...")

# Start recorder with the given values 
# of duration and sample frequency 
recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1) 

# Record audio for the given number of seconds 
sd.wait() 

print("Done")

# This will convert the NumPy array to an audio 
# file with the given sampling frequency 
wf.write("recording0.wav", SAMPLE_RATE, recording) 

