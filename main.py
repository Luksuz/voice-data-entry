from AudioTranscriber import AudioTranscriber
from ColumnValidator import ColumnValidator
from LLM import LLM

        
if __name__ == "__main__":
    transcriber = AudioTranscriber()
    column_validator = ColumnValidator()
    transcriber.start_recording()
    while True:
        input("\nPress Enter to stop recording and save... ")
        transcriber.save_audio()
        transcription = transcriber.transcribe_audio()
        value_dict = LLM.stream_data(transcription)
        print(value_dict)
