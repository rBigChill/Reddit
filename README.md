Reddit CLI Reader

Overview
This script fetches and displays the top 10 posts from a user's Reddit front page using the PRAW library. Users can view article titles in the terminal and open selected articles in their web browser.

Features
- Fetches the latest top 10 Reddit posts.
- Displays article titles in a formatted list.
- Allows users to open selected articles in their default web browser.
- Automatically installs missing dependencies.

Prerequisites
- Python 3.x
- A Reddit API account (client ID, client secret, user agent, username, and password)
- Internet connection

Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/rBigChill/Reddit-CLI.git
   cd Reddit-CLI
   ```
2. Install dependencies:
   ```bash
   pip install praw
   ```
3. Configure your Reddit API credentials in `redditCreds.py`:
   ```python
   CLIENT_ID = "your_client_id"
   CLIENT_SECRET = "your_client_secret"
   USER_AGENT = "your_user_agent"
   USERNAME = "your_username"
   PASSWORD = "your_password"
   ```

Usage
Run the script using:
```bash
python reddit_reader.py
```

#How It Works
- The script fetches the top Reddit posts from the user's front page.
- It prints a numbered list of article titles.
- Users can enter an article number to open it in their browser.
- Pressing Enter quits the program.

Future Improvements
- Support for fetching more than 10 articles.
- Additional filtering options (e.g., by subreddit, hot/new/top posts).
- Caching for offline access.

License
This project is open-source and available for modification and distribution.

