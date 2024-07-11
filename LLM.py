import ollama

class LLM:
    @staticmethod
    def stream_data(transcription):
        output = ollama.chat(
            model='phi3',
            messages=[{'role': 'user', 'content': transcription}],
        )
        text = output['message']["content"] + "}"
        return text