import praw
from secrets import client_id, secret_id, username, password
from datetime import datetime

def post_comment(post_id, comment_text):
    # Initialize the Reddit client with PRAW using your credentials
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret_id,
        username=username,
        password=password,
        user_agent='MyAPI/0.0.1'
    )
    
    # Fetch the submission (post) by ID
    submission = reddit.submission(id=post_id)
    
    # Post a comment on the submission
    comment = submission.reply(comment_text)
    
    # Optional: Print or return some information about the comment
    print(f"Comment posted: {comment.id}")
    print(f"Comment body: {comment.body}")
    print(f"Comment created at: {datetime.fromtimestamp(comment.created_utc).isoformat()}")
    
    return comment

# Example usage
post_id = 'eberem'  # Replace with the actual post ID
comment_text = 'Me commenting on this post at this moment of time has already been priced in.'
comment = post_comment(post_id, comment_text)
