# OurVoice

## Description

OurVoice is a terminal-based journaling and wellbeing application designed to provide users with a calm, low-pressure digital space for reflection and support.

The app allows users to write journal entries that can be kept private or shared publicly, view reflections from others, and access trusted support resources when needed. Through keyword detection and sentiment analysis, users can also receive personalised affirmations tailored to their emotional tone.

OurVoice intentionally avoids features such as comments or direct messaging. This design choice prioritises user safety, autonomy, and emotional comfort, ensuring the platform remains reflective rather than performative.

This project was developed as part of the Code First Girls Software Engineering Degree

## Features
- Create journal entries (public or private)
- View a public feed of shared reflections
- View a personal profile with all your posts
- Like public posts 
- Support Hub with trusted wellbeing organisations
- Wellness & Career Hub for development resources
- Receive personalised affirmations 

## Project File Description
- config.py - Stores MySQL credentials and configuration values
- db_utils.py - Contains all SQL operations 
- api_server.py - Call our Flask API providing all routes
- clientside_main.py - The main file that handles menus, API calls and all user interactions.
- class_keyword_detection.py - Contains logic that scans user posts for keywords and triggers the support suggestion.
- class_hashtag_recs.py - NLP-based hashtag recommendation using NLTK keyword extraction
- class_afirmations.py - This file processes sentiment analysis and external API calls to generate personalised affirmations
- support_hub_data.py - Data file to store wellbeing resources for the support hub
- wellness_resources.py - Data file to to store learning, productivity and wellness resources
- welcome_message.py - File containing the application's introduction message. 
- SQL_DB - SQL schema and setup script (users, journal entries)

## Getting Started

### Requirements
- Python 3.x.x
- MySQL
- Flask
- mysql-connector-python
- requests
- python-dotenv
- vaderSentiment
- nltk

### Installation
1. Clone the repository
```
git clone https://github.com/yousely15/cfg-group-project.git
cd src/backend
```

2. MYSQL database setup
- Open MYSQL or MYSQL Workbench
- Run the SQL schema included in the file

3. Configure database credential
- In my config.py, set your MYSQL credentials

4. Environment variable for API key
- Create a .env file and add:
```
RAPIDAPI_KEY = 'your_api_key_here'
```

5. Create and activate a virtual environment
```
python -m venv .venv
. .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate      # Windows
```

6. Install packages
```
pip install -r requirements.txt
```

7. Download required NLTK data
```
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
```

## Running the App
1. Start the Flask API Server
```
python c_api_server.py
```

The API will run on:
```
http://127.0.0.1:5001
```

2. Run the Client
```
python d_clientside_main.py
```

3. Follow the interactive prompts

## Testing
1. Navigate to the src directory
```
python -m unittest
```

## Authors
Alisha, Mia, Yousr, Sara, Chimna, Siham, Priscilla

## Acknowledgements
We would like to thank Code First Girls and our instructors for their guidance and support throughout the course and the project. 