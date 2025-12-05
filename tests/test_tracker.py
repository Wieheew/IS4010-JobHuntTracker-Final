import os
import json
import pytest
from src import storage

# Setup a temporary test file so we don't overwrite real data
TEST_FILE = "test_jobs.json"

@pytest.fixture(autouse=True)
def setup_teardown():
    # Before test: Set the storage file to our test file
    storage.DATA_FILE = TEST_FILE
    # Clean up any existing test file
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    yield # Run the test
    
    # After test: Cleanup
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_job():
    """Test that adding a job saves it correctly."""
    job = storage.add_job("Test Corp", "Engineer")
    
    assert job["company"] == "Test Corp"
    assert job["role"] == "Engineer"
    assert job["status"] == "Applied"
    
    # Verify it's actually in the file
    loaded_jobs = storage.load_jobs()
    assert len(loaded_jobs) == 1
    assert loaded_jobs[0]["company"] == "Test Corp"

def test_update_job():
    """Test that we can update a job status."""
    # First add a job
    storage.add_job("Tech Co", "Dev")
    
    # Update it
    result = storage.update_job_status(1, "Interviewing")
    
    assert result is not None
    assert result["status"] == "Interviewing"
    
    # Verify persistence
    loaded_jobs = storage.load_jobs()
    assert loaded_jobs[0]["status"] == "Interviewing"