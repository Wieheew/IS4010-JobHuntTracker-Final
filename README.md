# Job Hunt Tracker

[![CI/CD Pipeline](https://github.com/Wieheew/IS4010-JobHuntTracker-Final/actions/workflows/ci.yml/badge.svg)](https://github.com/Wieheew/IS4010-JobHuntTracker-Final/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

**IS4010 Final Project** - A professional CLI tool to track job applications using Python, Typer, and Rich.

## 📋 Overview

Job Hunt Tracker is a command-line application that helps you organize and manage your job search. Track applications, update statuses, and view your progress in a beautiful terminal interface. All data is stored locally in a JSON file (`jobs.json`).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher installed on your system
- Basic knowledge of using the command line/terminal

### Step 1: Download the Project

Clone or download this repository to your local machine.

### Step 2: Install Dependencies

Open PowerShell and navigate to the project directory:

```powershell
cd "path\to\IS4010-JobHuntTracker-Final"
```

Install the required Python packages:

```powershell
python -m pip install -r requirements.txt
```

This will install:
- **Typer** - For building the CLI interface
- **Rich** - For beautiful terminal formatting
- **Pytest** - For running tests

---

## 📖 How to Use the Application

### Command 1: Adding a Job Application

To add a new job to your tracker, use the `add` command:

```powershell
python -m src.main add "Company Name" "Job Title"
```

**Example:**
```powershell
python -m src.main add "Google" "Software Engineer"
```

**With optional link:**
```powershell
python -m src.main add "Microsoft" "Backend Developer" --link "https://careers.microsoft.com/job123"
```

**What happens:**
- A new job entry is created with an auto-generated ID
- Status is automatically set to "Applied"
- Current date is recorded as the application date
- Data is saved to `jobs.json`

---

### Command 2: Viewing All Job Applications

To see all your tracked jobs in a formatted table:

```powershell
python -m src.main list
```

**Example output:**
```
                      My Job Applications                      
┏━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ ID ┃ Company   ┃ Role              ┃ Status       ┃ Date Applied ┃
┡━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│  1 │ Google    │ Software Engineer │ Interviewing │ 2025-12-05   │
│  2 │ Microsoft │ Backend Developer │ Applied      │ 2025-12-05   │
└────┴───────────┴───────────────────┴──────────────┴──────────────┘
```

**Filter by status:**
```powershell
python -m src.main list --status "Interviewing"
```

---

### Command 3: Updating Job Status

To update the status of a job application, use the job ID from the list:

```powershell
python -m src.main update <JOB_ID> "New Status"
```

**Example:**
```powershell
python -m src.main update 1 "Interviewing"
```

**Common status values:**
- `Applied` - Initial application submitted
- `Interviewing` - In the interview process (shown in yellow)
- `Rejected` - Application rejected (shown in red)
- `Offer` - Received an offer
- `Accepted` - Accepted the position

---

## 🧪 Running Tests

To verify the application works correctly, run the test suite:

```powershell
python -m pytest tests/test_tracker.py -v
```

**Expected output:**
```
tests/test_tracker.py::test_add_job PASSED        [ 50%]
tests/test_tracker.py::test_update_job PASSED     [100%]

2 passed in 0.03s
```

---

## 📁 Project Structure

```
IS4010-JobHuntTracker-Final/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # CLI commands (add, list, update)
│   └── storage.py           # JSON storage functions
├── tests/
│   └── test_tracker.py      # Pytest test cases
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── AGENTS.md               # AI usage documentation
└── jobs.json               # Your job data (created after first add)
```

---

## 💡 Tips and Best Practices

1. **Backup your data**: The `jobs.json` file contains all your job applications. Consider backing it up regularly.

2. **Stay organized**: Update job statuses as soon as you hear back from companies.

3. **Use consistent status names**: Stick to a set of standard status values for easier filtering.

4. **Add links**: Include application links when adding jobs for easy reference.

---

## 🔧 Troubleshooting

**Problem:** `ModuleNotFoundError: No module named 'typer'`
- **Solution:** Run `python -m pip install -r requirements.txt`

**Problem:** Tests fail or commands don't work
- **Solution:** Make sure you're in the project root directory and Python 3.7+ is installed

**Problem:** Can't find `jobs.json`
- **Solution:** The file is created automatically in your current directory after adding your first job

---

## 📝 Data Storage

All job data is stored in `jobs.json` in the following format:

```json
[
  {
    "id": 1,
    "company": "Google",
    "role": "Software Engineer",
    "status": "Interviewing",
    "date_applied": "2025-12-05",
    "link": "https://careers.google.com"
  }
]
```

---

## 👨‍💻 Author

Ethan Wiehe, student University of Cincinnati, IS4010

## 📄 License

See LICENSE file for details.
