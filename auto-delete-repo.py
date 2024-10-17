from github import Github
import tkinter as tk
from tkinter import messagebox

# your github auth token
token = "github-auth-token"

def delete_repository(repo_name):
    g = Github(token)
    try:
        user = g.get_user()
        repo = user.get_repo(repo_name)
        repo.delete()
        messagebox.showinfo("Success", f"Repository '{repo_name}' has been deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def submit():
    repo_name = entry.get()
    delete_repository(repo_name)

#Tkinter window
root = tk.Tk()
root.title("Delete GitHub Repository")

label = tk.Label(root, text="Enter the name or full name (username/repo) of the repository to delete:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Delete Repository", command=submit)
submit_button.pack(pady=20)

root.mainloop()
