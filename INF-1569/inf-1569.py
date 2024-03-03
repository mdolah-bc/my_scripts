import requests
import json

# from repos import repositories

token = "REDACTED"

# repositories = ["https://github.com/TriggerMail/mdolah-test-repo"]
# repositories = ["TriggerMail/mdolah-test-repo", "TriggerMail/k8s-ops-manifests"]
repositories = ["TriggerMail/tf-bluecore-foundation"]

for repo_url in repositories:
    url = f"https://api.github.com/repos/{repo_url}/branches/master/protection/required_pull_request_reviews"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        # "branch": "master",
        # "required_status_checks": {"enabled": True},
        "dismiss_stale_reviews": True,
    }

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Successfully updated for {repo_url}")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error updating for {repo_url}: {response.text}")
        json_obj = response.json()
        print(json.dumps(json_obj, indent=2))
        # print(type(response.json()))

# data = {
#     "dismissal_restrictions": {
#         "users": ["octocat"],
#         "teams": ["justice-league"],
#         "apps": ["octoapp"],
#     },
#     "bypass_pull_request_allowances": {
#         "users": ["octocat"],
#         "teams": ["justice-league"],
#         "apps": ["octoapp"],
#     },
#     "dismiss_stale_reviews": True,
#     "require_code_owner_reviews": True,
#     "required_approving_review_count": 2,
#     "require_last_push_approval": True,
# }
