import requests
import itertools
from b_db_utils import user_likes
from e_class_keyword_detection import KeywordDetection
from f_class_hashtag_recs import HashtagRecs
from g_class_affirmations import Affirmations
from welcome_message import welcome_message

# this function will enable the user to see all public posts via the Flask interface
def get_public_feed():
    url = 'http://127.0.0.1:5001/feed'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will provide a json of all public and private entries that user has input
def get_username_entries(username):
    url = f'http://127.0.0.1:5001/{username}'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will provide user with a list of support resources
def get_support_hub():
    url = 'http://127.0.0.1:5001/support_hub'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will provide user with a list of wellness and career resources
def get_wellness_and_career_hub():
    url = 'http://127.0.0.1:5001/wellness_career'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will enable the user to add a like a public entry in their feed
# and their username will also be added to the userlikes column on SQL and to the list of
# userlikes, as produced by the user_likes function in DB_utils.
def like_entry(username, post_id):
    url = f'http://127.0.0.1:5001/feed/{post_id}'
    result = requests.post(
        url, json={"userlike": username},
        headers={'content-type': 'application/json'})
    return result.json()

#--------------------------------------------------------------------------------------------

                                    # HELPER FUNCTIONS

#--------------------------------------------------------------------------------------------                                   

# this helper function assists in condensing the run function by printing out posts when the user
# wants to 1) see our public feed and 2) see their profile, which deatures their own private and public 
# posts.

def print_helper_func(array, username=None, post_id = None):
    labs = ["\nPost ID: ", "Username: ", "Title: ", "Post: ", "Status: ", "Likes: ",
            "Userlikes: ", "Hashtags: "]

    # this if statement triggers when username and post_id are not set, i.e. when the user has opted to
    # see our public feed.
    if username is None and post_id is None:
        labels = labs * len(array)
        iter_array = list(itertools.chain.from_iterable(array))
        for i, j in list(zip(labels, iter_array)):
            print(i, j)

    # this if statement triggers when username is set but post_id is now, i.e. when the user has opted to
    # see their own public and private posts.
    if username is not None and post_id is None:
        username_array = []
        for i in array:
            if i[1] == username:
                username_array.append(i)
        labels = labs * len(username_array)
        iter_array = list(itertools.chain.from_iterable(username_array))
        for i, j in list(zip(labels, iter_array)):
            print(i, j)

# this helper function allows a user to decide if they want to like a post in their public feed. The 
# like is stored on SQL, as well as a list of users that have liked that post already. If you have 
# already like a post, you will not be able to like it again.

def like_helper_func(username):
    like_y_n = input("\nWould you like to like a post? Y or N: ").lower()
    
    while like_y_n not in ["y", "n"]:
        like_y_n = input("Invalid input. Please enter Y or N: ").lower()
    
    if like_y_n == "y":
        post_id = input("Please provide the post_id of the post you want to like: ")
        if not post_id.isdigit():
            print("Invalid Post ID, please try again.")
        else:  
            list_of_userlikes = user_likes(post_id)
            if username in list_of_userlikes:
                print("You have already liked this post.")
            else:
                response = like_entry(username, post_id)
                print(f"\nThank you, {username}, for liking this post:\n") 
                labs = ["Post ID: ", "Username: ", "Title: ", "Post: ", "Status: ", "Likes: ",
                "Userlikes: ", "Hashtags: "]
                for i, j in list(zip(labs, response)):
                    print(i, j)

# this helper function produces hashtag recommendations by calling from f_class_hashtag_recs, it is 
# incorporated into the create_post function below.

def hashtag_generation(post):
    hashtag_recs = HashtagRecs()

    # using the methods in the HashtagRecs class, we are extracting keywords from the user's post and
    # converting those into a list of hashtags to recommend to the user
    keywords = hashtag_recs.extract_keywords(post)
    hashtags = hashtag_recs.generate_hashtags(keywords)

    hashtags_q = input(f"\nThank you so much for sharing!"
                       f"\nWould you like to include some hashtags (Y/N)? ").lower()
    
    while hashtags_q not in ["y", "n"]:
        hashtags_q = input("Invalid input. Please enter Y or N: ").lower()

    if hashtags_q == "y":
        print(f"\nHere are some hashtags I can recommend: {hashtags}")
        user_hashtags = input("\nYour hashtags: ")
    else:
        user_hashtags = ""

    return user_hashtags  

# This function collects a user's journal entry from the terminal,
# asks whether the entry should be public or private, and then sends
# the data as JSON to the Flask API route POST /feed. The API then
# stores the entry in the SQL database. If the request is successful,
# the user is shown a confirmation message and the ID of their new post.

def create_post(username):
    print("\nCreate a New Post")

    title = input("\nTitle of your entry: ")
    post_content = input("\nWrite your entry:\n> ")
    private_public = input("\nMake this public or private? ").lower()
    user_hashtags = hashtag_generation(post_content) # calling the hashtags function above

    entry_data = {"name": username, "title": title, "post": post_content,"private_public": private_public,
                  "hashtags": user_hashtags}

    url = "http://127.0.0.1:5001/feed"
    result = requests.post(url, json=entry_data, headers={"content-type": "application/json"})
    response_data = result.json()

    if result.status_code == 201:
        print("\nYour post has been created successfully!")
        
    else:
        print("\nSomething went wrong, please try again.")
        print("STATUS CODE:", result.status_code)
        print("RESPONSE:", response_data)
    
    return post_content

# affirmations helper function

def affirmations_helper(post_content):
    affirmation = Affirmations()    
    print(f"\nHere is your personalised affirmation: {affirmation.personalised_affirmation(post_content)}")

# this helper function detects keywords that could indicate that support is needed by the user by calling from the 
# e_class_keyword_detection

def keyword_trigger(post):
    detector = KeywordDetection()
    support_triggered = detector.detect_keywords(post)
    # checks if keyword is detected then a message pops up to redirect them to the support hub
    if support_triggered:
        print("\nSome topics in your post are commonly linked to wellbeing and support.")
        print("If you feel it could be helpful, please consider visiting our Support Hub.\n")
        return True
    
    return False     

# support hub helper
def support_hub_helper(categories):
    if not categories:
        print("\nSupport hub is currently unavailable.")
    else:
        print("\nChoose a Support Category:")
        for key, value in categories.items():
            print(f"{key}. {value['category']}")

        chosen_category = input("Enter the category number: ")
        while chosen_category not in categories:
            chosen_category = input("Invalid. Please select the category number from the list: ")   
        
        if chosen_category in categories:
            print(f"\n{categories[chosen_category]['category']}:\n")

            for idx, item in enumerate(categories[chosen_category]["support"], start=1):
                print(f"{idx:>2}. {item['name']}")

                if "phone" in item:
                    print(f"    Phone: {item['phone']}")
                if "Text" in item:
                    print(f"    Text: {item['Text']}")
                if "website" in item:
                    print(f"    Website: {item['website']}")
                print()

def support_hub_helper_call():
    hub = get_support_hub()
    categories = hub['categories']
    return support_hub_helper(categories)

# wellness and career hub helper
def wellness_career_helper(categories):
    if not categories:
        print("\nWellness / Career Hub is currently unavailable.")
    else:
        print("\nChoose a Wellness / Career Category:")
        for key, value in categories.items():
            print(f"{key}. {value['category']}")

        chosen_category = input("Enter the category number: ")
        while chosen_category not in categories:
            chosen_category = input("Invalid. Please select the category number from the list: ")   
        
        if chosen_category in categories:
            print(f"\n{categories[chosen_category]['category']}:\n")

            for idx, item in enumerate(categories[chosen_category]["support"], start=1):
                print(f"{idx:>2}. {item['name']}")

                if "author" in item:
                    print(f"    Author: {item['author']}")
                if "description" in item:
                    print(f"    Description: {item['description']}")
                if "good_for" in item:
                    print(f"    Good for: {', '.join(item['good_for'])}")

                if "Description" in item:
                    print(f"    Description: {item['Description']}")
                if "website" in item:
                    print(f"    Website: {item['website']}")
                print()

def run():
    """
    Main clientside function:
    - asks for a username
    - shows a menu (see feed / write post / support hub / review entries / wellness/career hub / exit)
    - calls helper functions to talk to the Flask API
    """
    print(welcome_message)
    username = input("Please enter your username: ").strip()
    # CALLING FUNCTION TO ADD USER TO SQL DATABASE, NOT INTEGRATED YET AS NEED TO
    # PREVENT DUPLICATION OF USERNAMES BEING INPUT INTO THE DB

    # entry_data = {"username": username}
    # username_entry(entry_data)

    while not username:
        username = input("Username cannot be empty. Please enter your username: ").strip()

    while True:
        print("\nHow do you want to move today?")
        print("\n1. See our feed")
        print("2. Write a post (public/private)")
        print("3. See our support hub")
        print("4. Review your profile")
        print("5. See our Wellness / Career Hub")
        print("6. Exit")

        choice = input("\nEnter 1–6: ").strip()

        while choice not in ["1", "2", "3", "4", "5", "6"]:
            choice = input("Invalid input. Please enter a number between 1 and 6: ").strip()

        # 1. See our feed + like a post
        if choice == "1":
            posts = get_public_feed()

            if not posts:
                print("\nThere are no public posts yet.")
            else:
                print("\n--- Public Feed ---")
                print_helper_func(posts)
                like_helper_func(username)

        # 2. Write a post (this uses your create_post function)
        elif choice == "2":
            post_content = create_post(username)
        
            # if keyword is detected for support then redirect to support hub
            if keyword_trigger(post_content):
                user_choice = input("Would you like to visit our support hub now? (y/n) ")
                
                while user_choice not in ["y", "n"]:
                    user_choice = input("Invalid input. Please enter Y or N: ").lower()
                
                if user_choice == "y":
                    support_hub_helper_call()
                else:
                    affirmations_helper(post_content)
            else:
                # affirmations
                affirmations_helper(post_content)
                
        # 3. See our support hub
        elif choice == "3":
            support_hub_helper_call()
            
        # 4. Review your previous posts
        elif choice == "4":
            posts = get_username_entries(username)

            if not posts:
                print("\nYou have no previous posts.")
            else:
                print("\n--- Your previous posts ---")                
                print_helper_func(posts, username=username)

        # 5. See our Wellness and Career hub
        elif choice == "5":
            hub = get_wellness_and_career_hub()
            categories = hub['categories']
            wellness_career_helper(categories)

        # 6. Exit
        elif choice == "6":
            print("\nSee you next time, and thank you for using OurVoice. ☺️✨")
            break

        else:
            print("Please enter a number between 1 and 6.")


if __name__ == "__main__":
    run()