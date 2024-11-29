GitHub User Activity
This Python script fetches and displays the public GitHub activities of a specified user.

Features
Fetches public events for a specified GitHub user.
Displays various types of events, such as push events, issue events, watch events, fork events, and create events.
Prerequisites
Python 3.x installed on your system.
The requests library installed. You can install it using the following command:
pip install requests
How to Use
Clone the Repository

Clone this repository to your local machine using:

git clone https://github.com/moimoi05/GitHub-User-Activity.git
Navigate to the Directory

Change to the directory of the cloned repository:

cd GitHub-User-Activity
Edit the Script (Optional)

By default, the script fetches events for the user moimoi05. If you want to fetch events for a different user, edit the base_url variable in the github_api.py file:

base_url = "https://api.github.com/users/<username>/events/public"
Replace <username> with the GitHub username of the user whose events you want to fetch.

Run the Script

Execute the script using Python:

python github_api.py
View the Output

The script will fetch and display the public events of the specified GitHub user. The output will include information about various event types such as:

PushEvent: Number of commits pushed to a repository.
IssuesEvent: Actions on issues in a repository.
WatchEvent: Repositories starred by the user.
ForkEvent: Repositories forked by the user.
CreateEvent: Repositories or branches created by the user.
Example Output
Pushed 3 commits to moimoi05/Task-Tracker
Opened a new issue in moimoi05/Task-Tracker
Starred moimoi05/Task-Tracker
Forked moimoi05/Task-Tracker
Created repository in moimoi05/Task-Tracker
Error Handling
If the script encounters an error while fetching the data, it will display an error message with the HTTP status code and the corresponding error details.

License
This project is released under the MIT License. Feel free to use and modify it as needed.

Save this content as README.md in your project directory.
project url:  https://roadmap.sh/projects/github-user-activity
