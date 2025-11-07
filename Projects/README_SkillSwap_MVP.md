# 🧩 SkillSwap MVP — Peer-to-Peer Skill Exchange Platform

## 🚀 Quick Start Guide

Follow these steps to get the SkillSwap project up and running easily.

---

### ⚙️ 1. Clone or Open the Project
If you already have the project folder:
```bash
cd D:\Projects
```

If using Git:
```bash
git clone https://github.com/<your-repo-name>.git
cd SkillSwap
```

---

### 🐍 2. Create a Virtual Environment (Python 3.11 Recommended)
```powershell
py -3.11 -m venv .venv
```

Activate it (PowerShell):
```powershell
& '.\.venv\Scripts\Activate.ps1'
```

If activation is blocked by PowerShell policy:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
& '.\.venv\Scripts\Activate.ps1'
```

You should now see `(.venv)` in your terminal prompt.

---

### 📦 3. Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install streamlit
```

If you have a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### ▶️ 4. Run the Application
```bash
streamlit run app.py
```

After launching, open the **Local URL** displayed (usually http://localhost:8501) in your browser.

To stop the app, press **Ctrl + C** in the terminal.

---

### 💾 5. Data Storage
- All user data is stored in a file named `data.json` in the same directory.
- To reset, delete `data.json` or use the **All Data → Reset** button in the app.

---

### 💡 6. App Sections
| Section | Purpose |
|----------|----------|
| **Create Profile** | Add your name, bio, and list of offered/wanted skills. |
| **Discover** | View other users, see compatibility scores, and send swap requests. |
| **Swap Requests** | Track and manage your exchanges (Pending, Accepted, Completed). |
| **All Data (Debug)** | View or reset all stored data. |

---

### 🧠 7. Common Errors & Fixes
| Problem | Solution |
|----------|-----------|
| `streamlit : command not found` | Activate your venv using `& '.\.venv\Scripts\Activate.ps1'` first. |
| `pyarrow build failed` | Ensure you’re using **Python 3.11** (3.14 causes issues). |
| Browser didn’t open | Manually open http://localhost:8501 in your browser. |

---

### 👨‍💻 Developer Information
**Daksh Shinde**  
B.Tech (Computer Science) — SGGS Institute of Engineering and Technology  
📍 Bhopal, Madhya Pradesh  
📅 November 2025
