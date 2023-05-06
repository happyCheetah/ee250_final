import requests
import pprint
import pyaudio
import wave
import json 
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import time

URL = "http://172.20.10.3:5000"

stateNum = 0


def main():
    # res = requests.get(f'{URL}/success')
    # pprint.pprint(res.json())
    #print(requests.get(f'{URL}/success').json())

    #reference: https://realpython.com/playing-and-recording-sound-python/
    # record audio
    input("<< PRESS ENTER TO RECORD AUDIO >>")
    chunk = 1024  # Record in chunks of 1024 samples

    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    seconds = 1
    filename = "output.mp3"
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('-> Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('-> Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("-> Performing FFT")

    # perform fft

    time.sleep(0.5)
    # Load audio file
    sampling_frequency, audio_signal = wavfile.read("output.mp3")

    # Compute FFT
    fft = np.fft.fft(audio_signal)

    # Compute frequency axis
    freq_axis = np.linspace(0, sampling_frequency/2, len(fft)//2)

    # Plot FFT magnitude spectrum
    # plt.plot(freq_axis, np.abs(fft[:len(fft)//2]))
    # plt.xlabel("Frequency (Hz)")
    # plt.ylabel("Magnitude")
    # plt.show()


    max_index = np.argmax(np.abs(fft[:len(fft)//2]))
    most_common_freq = freq_axis[max_index]
    # print("The most common frequency is:", most_common_freq, "Hz")

    if most_common_freq > 210 and most_common_freq < 220:
        str = input("FREQUENCY CORRECT, enter your message: ")
        message = {'message': str}
        response = requests.post(f'{URL}/post', json=message)
    else: 
        print("Frequency Incorrect. Please rerun file.")

if __name__ == "__main__":
    main()
