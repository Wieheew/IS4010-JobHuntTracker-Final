import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# Define the file where data will be stored
DATA_FILE = "jobs.json"

def load_jobs() -> List[Dict]:
    """
    Loads the list of job applications from the JSON file.
    If the file doesn't exist, returns an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_jobs(jobs: List[Dict]):
    """
    Saves the list of job applications to the JSON file.
    """
    with open(DATA_FILE, "w") as f:
        json.dump(jobs, f, indent=4)

def add_job(company: str, role: str, link: str = ""):
    """
    Adds a new job to the database.
    """
    jobs = load_jobs()
    
    new_job = {
        "id": len(jobs) + 1,
        "company": company,
        "role": role,
        "status": "Applied",
        "date_applied": datetime.now().strftime("%Y-%m-%d"),
        "link": link
    }
    
    jobs.append(new_job)
    save_jobs(jobs)
    return new_job

def update_job_status(job_id: int, new_status: str) -> Optional[Dict]:
    """
    Updates the status of a specific job by ID.
    Returns the updated job if found, None otherwise.
    """
    jobs = load_jobs()
    
    for job in jobs:
        if job["id"] == job_id:
            job["status"] = new_status
            save_jobs(jobs)
            return job
            
    return None
