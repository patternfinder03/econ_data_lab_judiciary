import praw
from secrets import client_id, secret_id, username, password
from datetime import datetime
import json  # Add this import

def read_post(post_id):
    # Initialize the Reddit client with praw using your credentials
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret_id,
        username=username,
        password=password,
        user_agent='MyAPI/0.0.1'
    )
    
    # Fetch the submission (post) by ID
    submission = reddit.submission(id=post_id)
    
    # Populate the initial post details
    post_details = {
        'Social_Media_Site': 'Reddit',
        'Post_Topic': submission.title,
        'Post_Content': submission.selftext,
        'Post_Hashtags': ' '.join([f"#{tag}" for tag in submission.link_flair_text.split()]) if submission.link_flair_text else '',
        'Post_Date': datetime.fromtimestamp(submission.created_utc).isoformat(),
        'Post_Likes_Pre_Comment': submission.ups,
        'Post_Reply_Num_Pre_Comment': submission.num_comments,
        'Comments': []
    }
    
    # Replace "more" objects to get all comments, including nested ones
    submission.comments.replace_more(limit=None)
    
    # Process each comment
    for comment in submission.comments.list():
        if comment.author and comment.author.name == 'Dspa1r':
            # Get all nested replies count
            num_replies = len(comment.replies.list())
            
            comment_details = {
                'Comment': comment.body,
                'Comment_Date': datetime.fromtimestamp(comment.created_utc).isoformat(),
                'Comment_Likes': comment.ups,
                'Comment_Replies': num_replies,
                'Replies': []
            }
            
            # Process each reply to the comment
            for reply in comment.replies.list():
                reply_details = {
                    'Reply': reply.body,
                    'Reply_Date': datetime.fromtimestamp(reply.created_utc).isoformat(),
                    'Reply_Likes': reply.ups
                }
                comment_details['Replies'].append(reply_details)
            
            post_details['Comments'].append(comment_details)
    
    return post_details

# Example usage
post_data = read_post('eberem')  # Replace 'eberem' with the actual post ID
print(post_data)

# Save 'post_data' to a JSON file
with open('post_data.json', 'w') as outfile:
    json.dump(post_data, outfile, indent=4)
