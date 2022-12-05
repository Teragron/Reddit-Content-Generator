import sys
# Import the os library
import os
# Import the praw library
import praw
# Import the MoreComments class from the praw.models module
from praw.models import MoreComments
# Import the random module
import random
# Import the os.path module
import os.path
# Import the gTTS class from the gtts module
from gtts import gTTS
# Import the webdriver class from the selenium module
from selenium import webdriver
# Import the Image class from the PIL module
from PIL import Image
# Import the cv2 module
import cv2
# Import the randrange function from the random module
from random import randrange
# Import the ffmpeg_extract_subclip function from the moviepy.video.io.ffmpeg_tools module
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# Import multiple classes and functions from the moviepy.editor module
from moviepy.editor import VideoFileClip, concatenate_videoclips, concatenate_audioclips ,CompositeAudioClip, AudioFileClip, ImageClip, CompositeVideoClip






# Names of the folders
filenames_list = ["subfiles/cropped_screenshots", "subfiles/cropped_submission_screenshots", "subfiles/finished", "subfiles/screenshots", "subfiles/sounds", "subfiles/submission_screenshots", "subfiles/submission_sounds", "subfiles/submission_texts", "subfiles/texts", "subfiles/concatenated_sounds"]##########
# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()
# Add the specified Chrome extension
chrome_options.add_extension(r"C:\Users\ahmet\tt\subfiles\extension_4_1_46_0.crx")
# Initialize the Chrome webdriver with the options
driver = webdriver.Chrome(options=chrome_options)

# Set the name of the subreddit
name_of_subreddit = "askreddit"
# Initialize an empty list for comments
comment_list = []
# Initialize an empty list for submission IDs
submission_ids = []
# Initialize an empty list for comment IDs
comment_ids = []

# Initialize the reddit object using the praw library with the specified client id, client secret, and user agent
reddit = praw.Reddit(client_id ='xxxxxxxxxxxxxxxxxxxxxx',
                     client_secret ='xxxxxxxxxxxxxxxxxx', user_agent ='xxxxxxxxxxxx')

# Iterate through the top 10 hot posts in the subreddit and append the submission id of each post to the submission_ids list
for submission in reddit.subreddit(name_of_subreddit).hot(limit=15):
    submission_ids.append(submission.id)

# Select a random submission from the submission_ids list


# Keep choosing a random element until the condition is met
while True:
  # Choose a random element
    secilen = random.choice(submission_ids)
    submission = reddit.submission(secilen)
    # Check if the condition is met
    if not submission.over_18 and not os.path.exists(f"subfiles/submission_texts/{submission.id}.txt"):
        print(submission.title)
        # Print the id of the selected submission
        print(submission.id)
        # If the condition is met, exit the loop
        break
    else:
        print("Trying to choose an appropriate submission")

# This function checks whether a folder exists, if not it then creates the folders
def check_create_folders(folder_names):
    for folder_name in folder_names:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
           
# Calling the function to add the missing folders
check_create_folders(filenames_list)

# This function creates a video from a given submission ID
def editing(submissionid):
    # Load a random video file named "videos/parkur{randrange(1,6)}.mp4"
    parkur = VideoFileClip(f"subfiles/videos/parkur{randrange(1,6)}.mp4")
    #parkur = parkur.resize(height=720)
   
    # Load 4 audio files using the submission ID and the first 3 elements of the comment_ids list
    submission_audio = AudioFileClip(f"subfiles/submission_sounds/{submissionid}.mp3")
    first_comment_audio = AudioFileClip(f"subfiles/sounds/{comment_ids[0]}.mp3")
    second_comment_audio = AudioFileClip(f"subfiles/sounds/{comment_ids[1]}.mp3")
    third_comment_audio = AudioFileClip(f"subfiles/sounds/{comment_ids[2]}.mp3")
   
    # Calculate the total duration of the 4 audio files
    total_time = int(submission_audio.duration+first_comment_audio.duration+second_comment_audio.duration+third_comment_audio.duration)
   
    # Load 4 images using the submission ID and the first 3 elements of the comment_ids list
    submission_title = ImageClip(f"subfiles/cropped_submission_screenshots/{submissionid}.png").set_start(0).set_duration(submission_audio.duration).set_pos(("center", "center"))
    first_comment_text = ImageClip(f"subfiles/cropped_screenshots/{comment_ids[0]}.png").set_start(submission_audio.duration).set_duration(first_comment_audio.duration).set_pos(("center", "center"))
    second_comment_text = ImageClip(f"subfiles/cropped_screenshots/{comment_ids[1]}.png").set_start(submission_audio.duration+first_comment_audio.duration).set_duration(second_comment_audio.duration).set_pos(("center", "center"))
    third_comment_text = ImageClip(f"subfiles/cropped_screenshots/{comment_ids[2]}.png").set_start(submission_audio.duration+first_comment_audio.duration+second_comment_audio.duration).set_duration(third_comment_audio.duration).set_pos(("center", "center"))
   
    # Concatenate the 4 audio files into a single audio file
    final_clip = concatenate_audioclips([submission_audio, first_comment_audio, second_comment_audio, third_comment_audio])
   
    # Save the concatenated audio file to a file named "concatenated_{submissionid}.mp3"
    final_clip.write_audiofile(f"subfiles/concatenated_sounds/concatenated_{submissionid}.mp3")
   
    # Load the concatenated audio file as a new AudioFileClip
    zufugende = AudioFileClip(f"subfiles/concatenated_sounds/concatenated_{submissionid}.mp3")
   
    # Set the audio of the parkur video to be the zufugende audio file
    parkur.audio = zufugende
   
    # Create a composite video clip by adding the parkur video and the 4 images
    final = CompositeVideoClip([parkur, submission_title, first_comment_text, second_comment_text, third_comment_text])

    # Create a subclip of the final video with a duration of total_time + 1 seconds
    final = final.subclip(0, total_time+1)

    # Write the final video to a file named "finished/{submissionid}.mp4"
    final.write_videofile(f"subfiles/finished/{submissionid}.mp4", codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

# This function generates an audio file from a given text and ID
def soundbeat(mytext, myid):
    # Set the language of the text to be English
    language = 'en'
   
    # Create a gTTS object using the given text and language
    myobj = gTTS(text=mytext, lang=language, slow=False)
   
    # Save the gTTS object to a file named "sounds/{myid}.mp3"
    myobj.save(f"subfiles/sounds/{myid}.mp3")
   
# This function generates an audio file from a given text and ID for a submission
def soundbeat_submission(mytext, myid):
    # Set the language of the text to be English
    language = 'en'
   
    # Create a gTTS object using the given text and language
    myobj = gTTS(text=mytext, lang=language, slow=False)
   
    # Save the gTTS object to a file named "submission_sounds/{myid}.mp3"
    myobj.save(f"subfiles/submission_sounds/{myid}.mp3")
   

# This function takes a screenshot of a given comment and saves it to a file
def get_comment_screenshot():
    # Get the link of the comment
    link_of_comment = f"https://www.reddit.com/r/{name_of_subreddit}/comments/{submission.id}/comment/{comment.id}/"
   
    # Navigate to the link using the driver object
    driver.get(link_of_comment)
   
    # Take a screenshot and save it to a file named "screenshots/{comment.id}.png"
    driver.save_screenshot(f"subfiles/screenshots/{comment.id}.png")
   

# This function takes a screenshot of a given submission and saves it to a file
def get_submission_screenshot(submissionid):
    # Get the link of the submission
    link_of_submission = f"https://www.reddit.com/{submissionid}"
   
    # Navigate to the link using the driver object
    driver.get(link_of_submission)
   
    # Take a screenshot and save it to a file named "submission_screenshots/{submissionid}.png"
    driver.save_screenshot(f"subfiles/submission_screenshots/{submissionid}.png")

# This function crops a screenshot of a given comment and saves it to a file
def crop_screenshots():
    # Load the image from the file named "screenshots/{commentid}.png"
    img = cv2.imread(f"subfiles/screenshots/{comment.id}.png")
   
    # Crop the image using the coordinates (590:792, 36:800)
    cropped_img = img[590:810, 36:800]
   
    # Save the cropped image to a file named "cropped_screenshots/{commentid}.png"
    cv2.imwrite(f"subfiles/cropped_screenshots/{comment.id}.png", cropped_img)
   

# This function crops a screenshot of a given submission and saves it to a file
def crop_screenshots_submission(submissionid):
    # Load the image from the file named "submission_screenshots/{submissionid}.png"
    img = cv2.imread(f"subfiles/submission_screenshots/{submissionid}.png")
   
    # Crop the image using the coordinates (347:518, 29:822)
    cropped_img = img[347:550, 20:830]
   
    # Save the cropped image to a file named "cropped_submission_screenshots/{submissionid}.png"
    cv2.imwrite(f"subfiles/cropped_submission_screenshots/{submissionid}.png", cropped_img)
                           
def iter_top_level(comments):
    # Iterate through the comments in the input list
    for top_level_comment in comments:
        # Check if the current comment is a MoreComments instance
        if isinstance(top_level_comment, MoreComments):
            # If it is, yield each of its nested comments in turn
            yield from iter_top_level(top_level_comment.comments())
        else:
            # If it's not a MoreComments instance, yield the comment directly
            yield top_level_comment

# Open a file named 'submission.id.txt' in the 'submission_texts' directory with the mode 'w' (write) and the encoding "utf-8" and assign a reference to this file to the variable 'f'.
with open(f'subfiles/submission_texts/{submission.id}.txt', 'w', encoding="utf-8") as f:

# Write the value of 'submission.title' to the file.
    f.write(f'{submission.title}')

# Call the 'get_submission_screenshot()' function with 'submission.id' as an argument.
get_submission_screenshot(submission.id)

# Call the 'crop_screenshots_submission()' function with 'submission.id' as an argument.
crop_screenshots_submission(submission.id)

# Call the 'soundbeat_submission()' function with 'submission.title' and 'submission.id' as arguments.
soundbeat_submission(submission.title, submission.id)

# Iterate over the comments in 'submission.comments', filtering out any comments that are not between 100 and 300 characters long, and appending the remaining comments to a list named 'comment_list'.
for comment in iter_top_level(submission.comments):
    if 100<len(comment.body)<300:          
        comment_list.append(comment.body)

# For each filtered comment, open a file named 'comment.id.txt' in the 'texts' directory with the mode 'w' (write) and the encoding "utf-8" and assign a reference to this file to the variable 'f'.
        with open(f'subfiles/texts/{comment.id}.txt', 'w', encoding="utf-8") as f:

# Write the value of 'comment.body' to the file.
            f.write(f'{comment.body}')

# Call the 'soundbeat()' function with 'comment.body' and 'comment.id' as arguments.
        soundbeat(comment.body, comment.id)
        
# Call the 'get_comment_screenshot()' function with no arguments.
        get_comment_screenshot()

# Call the 'crop_screenshots()' function with no arguments.
        crop_screenshots()

# Append 'comment.id' to the 'comment_ids' list.
        comment_ids.append(comment.id)

# If the length of the 'comment_list' is greater than 2, terminate the loop.
        if len(comment_list)>2:
            break
driver.close()
driver.quit()
editing(submission.id)