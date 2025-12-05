"""
Job Hunt Tracker Package
A CLI tool for tracking job applications.
"""

__version__ = "1.0.0"

# Import main functions from storage for easier access
from .storage import (
    load_jobs,
    save_jobs,
    add_job,
    update_job_status,
    DATA_FILE
)

__all__ = [
    "load_jobs",
    "save_jobs", 
    "add_job",
    "update_job_status",
    "DATA_FILE"
]
