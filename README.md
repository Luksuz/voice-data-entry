<!-- Project Title -->
# Voice Data Entry Assistant 🎙️📝

<!-- Badges (Optional) -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- Project Description -->
This repository hosts a Voice Data Entry Assistant that utilizes the Whisper model for voice-to-text conversion and the Phi3 model for categorizing transcribed data into predefined columns.

## Overview

The Voice Data Entry Assistant enables users to speak into a microphone. The Whisper model translates voice inputs into text, while the Phi3 model categorizes this text into predefined categories, such as Time, Temperature, Wind, and others defined in the modelfile.

## Features

- **Voice-to-Text Conversion**: Utilizes the Whisper model to convert spoken input into text.
- **Data Categorization**: Leverages the Phi3 model to categorize textual data into predefined columns.
- **Local Execution**: Ensures data privacy and fast processing by running models locally.

## Installation

### Prerequisites

- Install [Ollama Official App](https://example.com/ollama-app) on your device.
- Train a Phi3 model using the provided modelfile.

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/voice-data-entry-assistant.git
   cd voice-data-entry-assistant
   ```

2. **Install the dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

3. **Configure models:**
  •	Download and set up the Whisper model using the Ollama Official App.
	•	Train the Phi3 model locally using the modelfile provided.



**USAGE**
1.	Run the application
  ```bash
  python main.py
  ```

2.	Provide Voice Input:
Follow the prompts to speak clearly into the microphone.
3.	View Categorized Output:
The application will display categorized data formatted as a dictionary.


**Example input**
*voice input*
```bash
  "The temperature is 20 degrees, wind speed is 10 knots, and barometer reading is 1013 hPa."
```

**Example output**
The assistant categorizes it into:
```bash
{
  "Temperature": "20 degrees",
  "Wind": "10 knots",
  "Barometer": "1013 hPa"
}
```



**Contributing**

Contributions are welcome! Fork the repository and submit a pull request.



