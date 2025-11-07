# initialize git repo (if you haven't)
git init
git add skillswap_full_streamlit.py

# create a minimal initial data file so the app starts clean
cat > data.json <<'EOF'
{
  "users": [],
  "requests": [],
  "messages": [],
  "endorsements": [],
  "achievements": []
}
EOF
git add data.json

# create requirements
cat > requirements.txt <<'EOF'
streamlit>=1.20.0
pandas
numpy
# add any other libraries your app uses, e.g. matplotlib, python-dateutil
EOF
git add requirements.txt

# optional .gitignore
cat > .gitignore <<'EOF'
__pycache__/
.env
.vscode/
EOF
git add .gitignore

# commit & push (replace <YOUR-REPO-URL> with your GitHub repo)
git commit -m "Initial SkillSwap app"
git branch -M main
git remote add origin <YOUR-REPO-URL>
git push -u origin main
