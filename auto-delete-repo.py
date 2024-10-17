from github import Github
import tkinter as tk
from tkinter import messagebox

# Your GitHub auth token
token = "your_github_token_here"

def fetch_repositories():
    g = Github(token)
    user = g.get_user()
    return user.get_repos()

def delete_selected_repositories(selected_repos):
    g = Github(token)
    for repo_name in selected_repos:
        try:
            user = g.get_user()
            repo = user.get_repo(repo_name.split('/')[1])
            repo.delete()
            messagebox.showinfo("Success", f"Repository '{repo_name}' has been deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete '{repo_name}': {str(e)}")
    root.quit()

def submit():
    selected_repos = [repo.full_name for repo, var in zip(repositories, checkboxes_vars) if var.get()]
    if not selected_repos:
        messagebox.showwarning("Warning", "No repositories selected for deletion.")
        return
    delete_selected_repositories(selected_repos)

# Create Tkinter window
root = tk.Tk()
root.title("Delete GitHub Repositories")

# Fetch repositories
repositories = fetch_repositories()


checkboxes_vars = []

label = tk.Label(root, text="Select repositories to delete:")
label.pack(pady=10)


for repo in repositories:
    var = tk.IntVar()
    checkboxes_vars.append(var)
    checkbox = tk.Checkbutton(root, text=repo.full_name, variable=var)
    checkbox.pack(anchor='w')

submit_button = tk.Button(root, text="Delete Selected Repositories", command=submit)
submit_button.pack(pady=20)

root.mainloop()
