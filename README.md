# Reddit-Content-Generator
A Python script that generates a video from a specified subreddit on Reddit 

This is a Python script that uses the praw, selenium, OpenCV, and moviepy libraries to scrape comments and submissions from a specified subreddit on Reddit, choose a random submission, and generate a video using the submission's text and comments.

## Requirements

- Python 3.7 or later
- The praw, selenium, OpenCV, and moviepy libraries
- A Reddit account and API keys for accessing the Reddit API

## Installation

1. Clone this repository or download the files as a zip.
2. Install the required libraries by running the following command:

```python
pip install -r requirements.txt
```
3. Create a Reddit app and get the API keys by following the instructions [here](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps).
4. Replace the `client_id`, `client_secret`, and `user_agent` values in the `reddit = praw.Reddit(...)` line with your own API keys.
5. Place the Adblocker extension to the corresponding folder.
6. The first time it openes up the browser, you need to close the cookie agreement pop-up of reddit by clicking accept or reject non-essential
7. Place the parkour videos to the corresponding folder.

## Usage
1. Open a terminal and navigate to the directory where the script is located.
2. Run the script by typing the following command:

```python
python subreddit_video_generator.py
```

3. The script will scrape comments and submissions from the specified subreddit, choose a random submission, create the necessary folders, and generate a video using the submission's text and comments. The video will be saved in the `subfiles/finished` folder.

## Customization
You can customize the script by changing the following variables:

- `name_of_subreddit`: The name of the subreddit from which to scrape comments and submissions. By default, it is set to "askreddit".
- `limit`: The number of hot posts to scrape from the subreddit. By default, it is set to 15.

You need to have five videos for the background:

- `parkur1.mp4`
- `parkur2.mp4`
- `parkur3.mp4`
- `parkur4.mp4`
- `parkur5.mp4`

The script will randomly choose one of these five videos to use as the background for the generated video.

## Showcase


https://user-images.githubusercontent.com/54573938/205771009-0ec0c873-9a89-4d8d-aa5e-d7db9399f7d3.mp4



## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This script is for educational and research purposes only. The author does not endorse or condone any illegal or unethical use of the script. The user is solely responsible for any consequences of using the script.
