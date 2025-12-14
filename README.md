# OurVoice

## Description

OurVoice is a terminal-based journaling and wellbeing application designed to provide users with a calm, low-pressure digital space for reflection and support.

The app allows users to write journal entries that can be kept private or shared publicly, view reflections from others, and access trusted support resources when needed. Through keyword detection and sentiment analysis, users can also receive personalised affirmations tailored to their emotional tone.

OurVoice intentionally avoids features such as comments or direct messaging. This design choice prioritises user safety, autonomy, and emotional comfort, ensuring the platform remains reflective rather than performative.

This project was developed as part of the Code First Girls Software Engineering Degree.

## Features
- Create journal entries (public or private)
- View a public feed of shared reflections
- View a personal profile with all your posts
- Like public posts 
- Support Hub with trusted wellbeing organisations
- Wellness & Career Hub for development resources
- Receive personalised affirmations based on sentiment analysis

## Project File Description
### Backend
- [config.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/a_config.py) - database connection information 
- [db_utils.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/b_db_utils.py) - database utilities functions for sql operations
- [api_server.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/c_api_server.py) - api endpoints
- [clientside_main.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/d_clientside_main.py) - main app file that handles the menu, user input and api calls. 
- [class_keyword_detection.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/e_class_keyword_detection.py) - triggers the support suggestion.
- [class_hashtag_recs.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/f_class_hashtag_recs.py) - NLTK keyword extraction for hashtag recommendation
- [class_affirmations.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/g_class_affirmations.py) - sentiment analysis and external api for affirmations
- [support_hub_data.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/support_hub_data.py) - wellbeing resources for the support hub
- [wellness_resources.py](https://github.com/yousely15/cfg-group-project/blob/main/src/backend/wellness_resources.py) - learning, productivity and wellness resources

### Other files:
- SQL_DB.sql - sql schema for database setup
- [requirements.txt]() - required Python packages

## Getting Started

### Requirements
- Python 3.x.x
- MySQL

### Installation & Setup
1. Clone the repository
```
git clone https://github.com/yousely15/cfg-group-project.git
cd cfg-group-project
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
- Run the SQL schema in the SQL_DB file

5. Configure database credentials
- Open config.py, set your MYSQL host, username and password

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
cd src/backend
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

3. Follow the interactive prompts in the terminal. 

## Testing
All test files are located in `src/tests/`.
Each test file can be run individually using the Run button in your IDE or by running the file from the terminal.

1. Unit tests 

From the `src/` folder:
```
python tests/test_keyworddetection.py
python tests/test_public_feed.py
python tests/test_user_posts.py
```

2. Manual testing

These were used to verify helper functions that print to the terminal or involve user input.

From the `src/` folder:
```
python tests/test_affirmations.py
python tests/test_printer_function.py
python tests/test_support_helper_function.py
python tests/test_wellness_hub.py
python tests/test_hashtag_recs.py
```

## Authors
[Alisha](https://github.com/Alisha71), [Mia](https://github.com/miamccl), [Yousr](https://github.com/yousely15), [Sara](https://github.com/sara-hyder), [Chimna](https://github.com/CLIONN3), [Siham](https://github.com/sihamnimale), Priscilla

## Acknowledgements
Thanks to Code First Girls and the wider community for your continued guidance and support throughout the CFG course. 
