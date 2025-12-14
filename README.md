# OurVoice

## Description

OurVoice is a terminal-based journaling and wellbeing application designed to provide users with a calm, low-pressure digital space for reflection and support.

The app allows users to write journal entries that can be kept private or shared publicly, view reflections from others, and access trusted support resources when needed. Through keyword detection and sentiment analysis, users can also receive personalised affirmations tailored to their emotional tone.

OurVoice intentionally avoids features such as comments or direct messaging. This design choice prioritises user safety, autonomy, and emotional comfort, ensuring the platform remains reflective rather than performative.

This project was developed as part of the Code First Girls Software Engineering Degree.

## Features
Main Features:
- Create journal entries (public or private)
- View a public feed of shared reflections
- View a personal profile with all your posts
- Like public posts 
- Support Hub with trusted wellbeing organisations
- Wellness & Career Hub for development resources
- Receive personalised affirmations 

Other Supporting Features:
- Hashtag recommendations using NLP
- Keyword detection to trigger support hub suggestions
- Sentiment analysis to determines pesonalised affirmation

## Project File Description
Backend
- [config.py]() - keep database credentials
- [db_utils.py]() - sql operations
- [api_server.py]() - api endpoints
- [clientside_main.py]() - main app that handles the menu, API calls and user input. 
- [class_keyword_detection.py]() - triggers the support suggestion.
- [class_hashtag_recs.py]() - NLTK keyword extraction for hashtag recommendation
- [class_afirmations.py]() - sentiment analysis and external api for affirmations
- [support_hub_data.py]() - wellbeing resources 
- [wellness_resources.py]() - learning, productivity and wellness resources

Other files:
- SQL_DB.sql - database storage
- [requirements.txt]() - Python required packages

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

### Installation & Setup
1. Clone the repository
```
git clone https://github.com/yousely15/cfg-group-project.git
cd src/backend
```

2. Create and activate a virtual environment
```
python -m venv .venv
. .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate      # Windows
```

3. Install packages
```
pip install -r requirements.txt
```

4. Set up the MYSQL database
- Open MYSQL or MYSQL Workbench
- Run the SQL schema included in the SQL_DB file

5. Configure database credentials
- In my config.py, set your MYSQL credentials

6. Download required NLTK data
Run the following once in a Python shell:
```
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
```
### Environment Variables

This project uses an external affirmations API via RapidAPI. 
1. Sign up or login to [RapidAPI](https://rapidapi.com)
2. Subscribe to the [Affirmations API by API Robots](https://rapidapi.com/apirobots/api/affirmations-api-by-apirobots)
3. Create a `.env` file and add:
```
RAPIDAPI_KEY = 'your_api_key_here'
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
[Alisha](), [Mia](), [Yousr](), [Sara](), [Chimna](), [Siham](), [Priscilla]()

## Acknowledgements
We would like to thank Code First Girls and our instructors for their guidance and support throughout the course and the project. 
