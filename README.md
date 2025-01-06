# Easy-RepoDe

A simple Python script to delete your GitHub repositories with ease.
Useful when contributing to open source project and easy to remove forked projects.

- Prompt-based interface to enter the name or URL of the repository you want to delete.
- Safely deletes the specified repository from your GitHub account.

Setup Instructions:-

Clone the repository to your local machine:-

Install the required dependencies:-

```bash
pip install -r requirements.txt
```

Add your GitHub authentication token:

Open the auto-delete-repo.py file.
Replace "your_github_token_here" with your personal GitHub authentication token.
python
```
token = "your_github_token_here"
````
Note: You can generate a GitHub personal access token from your GitHub account's settings under "Developer Settings" → "Personal Access Tokens." Make sure to give it appropriate scopes, like repo, for accessing and deleting repositories.

Run the code
