from __future__ import print_function, division
import numpy as np
import pyaudio
import wave
import samplerate as sr

target_rate = 16000

sample_format = pyaudio.paInt16  # 16 bits resolution per sample
channels = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 5 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output = 'test1.wav' # name of .wav file
converter = 'sinc_best'  # or 'sinc_fastest', ...
audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format = sample_format,
                    channels = channels,
                    rate = samp_rate,
                    frames_per_buffer=chunk,
                    input_device_index = dev_index,
                    input = True
                    )
print("recording")

resampler = sr.Resampler(converter,channels)
ratio = target_rate / samp_rate

raw_frames = []
frames = []
# loop through stream and append audio chunks to frame array
for i in range(0,int(samp_rate/chunk*record_secs)):
    raw_data = stream.read(chunk,exception_on_overflow = False)
    #raw_frames.append(raw_data)
    frames.append(raw_data)
print("finished recording")
# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()
#print("start encoding")
#for ii in range(0,int(samp_rate/chunk*record_secs)):
#    data = np.frombuffer(raw_frames[ii],dtype=np.int16)
#    resampled_data = resampler.process(data,ratio)
#    print('{} -> {}'.format(len(data),len(resampled_data)))
    # Do something with resampled_data
#    frames.append(resampled_data)
    #frames.append(raw_data)

#print("finish encoding")



# save the audio frames as .wav file
wf = wave.open(wav_output,'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(sample_format))
#wf.setframerate(target_rate)
wf.setframerate(samp_rate)
wf.writeframes(b''.join(frames))
wf.close()
