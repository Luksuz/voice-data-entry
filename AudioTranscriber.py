from transformers import WhisperProcessor, WhisperForConditionalGeneration
import threading
import pyaudio
import queue
import wave


class AudioTranscriber:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

        self.processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
        self.model.config.forced_decoder_ids = None

        self.stop_event = None
        self.audio_queue = None
        self.audio_thread = None

        self.p = pyaudio.PyAudio()

    def start_recording(self):
        self.stop_event = threading.Event()
        self.audio_queue = queue.Queue()
        self.audio_thread = threading.Thread(target=self._record_audio)
        self.audio_thread.start()

    def _record_audio(self):
        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK)

        while not self.stop_event.is_set():
            data = stream.read(self.CHUNK)
            self.audio_queue.put(data)

        stream.stop_stream()
        stream.close()

    def save_audio(self):
        self.stop_event.set()
        self.audio_thread.join()

        audio_frames = []
        while not self.audio_queue.empty():
            audio_frames.append(self.audio_queue.get())
        audio_data = b''.join(audio_frames)

        with wave.open(self.WAVE_OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(audio_data)

        print(f"Audio saved to {self.WAVE_OUTPUT_FILENAME}")
        
        self.start_recording()