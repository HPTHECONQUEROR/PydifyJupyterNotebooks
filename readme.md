# How to upload your weekly tasks?

Follow these steps carefully to clone the repository and submit your work.

---

## Step 1: Configure Git (one-time setup)

Run these commands in your terminal or PowerShell:

```bash
git config --global user.name "your-github-username"
git config --global user.email "your-github-email"
```

> This identifies your commits on GitHub.
> You only need to do this once per computer.

---

## Step 2: Clone the Repository

```bash
git clone https://github.com/HPTHECONQUEROR/PydifyJupyterNotebooks.git
cd PydifyJupyterNotebooks
```

---

## Step 3: Create Your Folder

Inside the repository, go to the `Assignments` folder and make a folder with your name.

Example:

```
Assignments/
 ├── name_1/
 ├── name_2/
 └── name_3/
```

Put all your assignment files inside your folder only.

---

## Step 4: Commit and Push Your Work

After adding or updating your files:

```bash
git add .
git commit -m "Added answers for week 1"
git push origin main
```

> The first time you push, GitHub might ask you to log in via browser or token — just follow the prompt.

---

## Step 5: Important Rules

* Do **not** edit or delete other students’ folders.
* Always commit inside your own folder.
* Keep commit messages short and meaningful.
* If you face a push error, run `git pull origin main` first, then push again.

---

### That’s it!

You’re now ready to submit assignments and track your progress directly in GitHub.
