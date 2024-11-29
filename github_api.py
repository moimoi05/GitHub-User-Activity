import requests

# api url
# use url below
# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events
base_url = "https://api.github.com/users/moimoi05/events/public"

response = requests.get(base_url)

if response.status_code == 200:
      events = response.json()
      if not events:
        print("No public activity found for this user.")
      else:
            for event in events:
                  event_type = event["type"]
                  repo_name = event["repo"]["name"]
                  # check action
                  if event_type == "PushEvent":
                        commits = len(event["payload"]["commits"])
                        print(f"Pushed {commits} commits to {repo_name}")
                  elif event_type == "IssuesEvent":
                        action = event["payload"]["action"]
                        print(f"{action.capitalize()} a new issue in {repo_name}")
                  elif event_type == "WatchEvent":
                        print(f"Starred {repo_name}")
                  elif event_type == "ForkEvent":
                        print(f"Forked {repo_name}")
                  elif event_type == "CreateEvent":
                        print(f"Created {event['payload']['ref_type']} in {repo_name}")

else:
      print(f"Error: {response.status_code}, {response.json()}")
