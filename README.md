# GitHub_Repo_Analyzer

Goal: Automate scanning of repos in an org to collect data like last commit, open issues, and contributors.

	What You'll Learn:
	GitHub REST API with requests
	Authentication with personal tokens
	JSON handling and reporting

	Extra: Output report as .csv or upload to a dashboard

github-repo-analyzer/
│
├── .env                 # 🔐 Secret token (not pushed)
├── .gitignore           # 📦 Ignore unnecessary files
├── config.yaml          # ⚙️ App config (org name, output file)
├── config.py            # 🧠 Loads config and token
├── github_analyzer.py   # 🧾 Main script logic
├── requirements.txt     # 📚 Python dependencies
└── .github/
    └── workflows/
        └── analyze.yml  # ⚙️ GitHub Actions workflow
