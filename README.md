# OurVoice

## Table of Contents
- Description
- Features
- Project Folder
- Getting Started
- Running the App
- Testing
- Authors
- Acknowledgements

## Description

OurVoice is a terminal-based journaling and wellbeing application designed to provide users with a calm, low-pressure digital space for reflection and support.

The app allows users to write journal entries that can be kept private or shared publicly, view reflections from others, and access trusted support resources when needed. Through keyword detection and sentiment analysis, users can also receive personalised affirmations tailored to their emotional tone.

OurVoice intentionally avoids features such as comments or direct messaging. This design choice prioritises user safety, autonomy, and emotional comfort, ensuring the platform remains reflective rather than performative.

This project was developed as part of the Code First Girls Software Engineering Degree

## Features

- Create journal entries (public or private)

- View a public feed of shared reflections

- View a personal profile with all your posts

- Like public posts (duplicate likes prevented)

- Keyword detection to suggest relevant support resources

- Support Hub with trusted wellbeing organisations

- Wellness & Career Hub for development resources

- Sentiment analysis using vaderSentiment

- Personalised affirmations via an external API

- Persistent data storage using MySQL

## Project Structure

backend/
├── SQL DB/
├── __init__.py
├── a_config.py
├── b_db_utils.py
├── c_api_server.py
├── d_clientside_main.py
├── e_class_keyword_detection.py
├── f_class_hashtag_recs.py
├── g_class_affirmations.py
├── support_hub_data.py
├── welcome_message.py
└── wellness_resources.py



## Getting Started

### Requirements
- Python 3.x.x
- MySQL
- Flask
- mysql-connector-python
- requests
- nltk
- vaderSentiment

### Installation
1. Clone the repository
```
git clone https://github.com/yousely15/cfg-group-project.git
cd src/backend
```

2. Create a virtual environment
```
python -m venv .venv
```

3. Activate the virtual environment
- For Mac/Linux:
```
. .venv/bin/activate
```

- For Windows:
```
.venv\Scripts\activate
```

4. Install packages
```
pip install -r requirements.txt
```

## Running the App
1. Start the Flask API Server
```
python c_api_server.py
```
2. Run the Client
```
python d_clientside_main.py
```

3. Follow the interactive prompts

## Testing

## Authors

## Acknowledgements



