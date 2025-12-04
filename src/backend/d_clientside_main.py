import requests
from b_db_utils import user_likes
from f_class_hashtag_recs import HashtagRecs

# this function will enable the user to see all public posts via the Flask interface
def get_public_feed():
    url = 'http://127.0.0.1:5000/feed'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will provide a json of all public and private entries that user has input
def get_username_entries(username):
    url = f'http://127.0.0.1:5000/{username}'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will provide user with a list of support resources
def get_support_hub():
    url = 'http://127.0.0.1:5000/support_hub'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will enable the user to add a like a public entry in their feed
# and their username will also be added to the userlikes column on SQL and to the list of
# userlikes, as produced by the user_likes function in DB_utils.
def like_entry(username, post_id):
    url = f'http://127.0.0.1:5000/feed/{post_id}'
    result = requests.post(
        url, json={"userlike": username},
        headers={'content-type': 'application/json'})
    return result.json()

# this function produces hashtag recommendations by calling from f_class_hashtag_recs 
def hashtag_generation(post):
    hashtag_recs = HashtagRecs()

    # using the methods in the HashtagRecs class, we are now extract keywords from the user's post and
    # converting those into a list of hashtags to reocmmend to the user
    keywords = hashtag_recs.extract_keywords(post)
    hashtags = hashtag_recs.generate_hashtags(keywords)

    hashtags_q = input(f"Thank you so much for sharing!"
                       f"\nWould you like to include some hashtags (Y/N)? ").lower()

    if hashtags_q == "y":
        print(f"Here are some hashtags I can recommend: {hashtags}")
        user_hashtags = input("Your hashtags: ")
    else:
        user_hashtags = ""

    return user_hashtags

# # This function collects a user's journal entry from the terminal,
# # asks whether the entry should be public or private, and then sends
# # the data as JSON to the Flask API route POST /feed. The API then
# # stores the entry in the SQL database. If the request is successful,
# # the user is shown a confirmation message and the ID of their new post.
def create_post(username):
    print("\nCreate a New Post")

    title = input("Title of your entry: ")
    post_content = input("Write your entry:\n> ")
    private_public = input("Make this public or private? ").lower()
    user_hashtags = hashtag_generation(post_content) # calling the hashtags function above

    entry_data = {"name": username, "title": title, "post": post_content,"private_public": private_public,
                  "hashtags": user_hashtags}

    url = "http://127.0.0.1:5000/feed"
    result = requests.post(url, json=entry_data, headers={"content-type": "application/json"})
    response_data = result.json()

    if result.status_code == 201:
        print("\nYour post has been created successfully!")
        print("Post ID:", response_data["post_id"])
    else:
        print("\nSomething went wrong, please try again.")
        print("STATUS CODE:", result.status_code)
        print("RESPONSE:", response_data)

def run():
    pass

# PRACTICE: run() function code for like/userlike functionality
username = input("What is your username? ")

# we can use this helper function in the run function
def like_helper_func():
    like_y_n = input("Would you like to like a post? Y or N: ").lower()
    if like_y_n == "y":
        post_id_like_post = input("Please provide the post_id of the post you want to like: ")
        list_of_userlikes = user_likes(post_id_like_post)
        if username in list_of_userlikes:
            print("You have already liked this post.")
        else:
            response = like_entry(username, post_id_like_post)
            print(f"Thank you, {username}, for liking this post:", response)

# to test the create post function, since it now contain hashtag recommendation functionality
create_post(username)

# Display the Support Hub category
hub = get_support_hub()
categories = hub["categories"]

print("Choose a Support Category:")
for key, value in categories.items():
    print(f"{key}. {value["category"]}")

chosen_category = input("Enter the category number: ")
if chosen_category not in categories:
    print("Invalid. Please select the category number from the list.")

print(f"\n{categories[chosen_category]["category"]}:\n")

for idx, item in enumerate(categories[chosen_category]["support"], start = 1):
    print(f"{idx:>2}. {item["name"]}")

    if "phone" in item:
        print(f"    Phone: {item["phone"]}")
    if "Text" in item:
        print(f"    Text: {item["Text"]}")
    if "website" in item:
        print(f"    Website: {item["website"]}")
    print()
