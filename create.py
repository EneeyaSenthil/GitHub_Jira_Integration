import requests
from requests.auth import HTTPBasicAuth
import json

url_issue_types = "https://eneeyasenthil.atlassian.net/rest/api/3/issuetype"
url_create_issue = "https://domain_name.atlassian.net/rest/api/3/issue"

API_TOKEN = ""

auth = HTTPBasicAuth("email@mail.com", API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Fetch available issue types
response = requests.get(url_issue_types, auth=auth, headers=headers)
issue_types = json.loads(response.text)

# Find the desired issue type by name
desired_issue_type = next((issue_type for issue_type in issue_types if issue_type["name"] == "Task"), None)

if desired_issue_type:
    issue_type_id = desired_issue_type["id"]

    # Create Jira issue using the desired issue type
    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "My first Jira ticket",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "project": {
                "key": "EFP"
            },
            "issuetype": {
                "id": issue_type_id
            },
            "summary": "First JIRA Ticket"
        },
        "update": {}
    })

    # Send request to create the Jira issue
    response = requests.post(url_create_issue, data=payload, headers=headers, auth=auth)

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
else:
    print("Desired issue type not found.")
