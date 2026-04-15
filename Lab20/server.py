"""Lab 20: Build the Other Side — Server

Your FastAPI grading server. Build each section as you work
through the tasks. The TODOs tell you what to add and where.
"""

from fastapi import FastAPI

app = FastAPI()


# ---------------------------------------------------------------------------
# Task 1: The Naive Server
# ---------------------------------------------------------------------------
# Import the grade function from grading.py, then create a POST /grade
import grading
from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse
import uuid
grading_log = []
completed = {}
jobs = {}
job_submission_map = {}
@app.post("/grade")
def grade(data: dict):
    score = grading.grade(data["student"],data["lab"])
    slow = data.get("slow",False)
    if "submission_id" in data:
        sub_id =data.get("submission_id")
        if sub_id in completed:
            return completed[sub_id]
        if sub_id not in completed:
            completed[sub_id] = {"student":data["student"],"lab": data["lab"], "score": score,"slow":slow,"submission_id":sub_id}
        grading_log.append({"student":data["student"],"lab": data["lab"], "score": score,"slow":slow,"submission_id":sub_id})
        return {"student":data["student"],"lab": data["lab"], "score": score,"slow":slow,"submission_id":sub_id}
    grading_log.append({"student":data["student"],"lab": data["lab"], "score": score,"slow":slow})
    return {"student":data["student"],"lab": data["lab"], "score": score,"slow":slow}
# endpoint that accepts {"student": ..., "lab": ...} and returns the score.


# ---------------------------------------------------------------------------
# Task 2: Retries Reveal a Problem
# ---------------------------------------------------------------------------
# Add a grading_log list that records every grading event.
# Update POST /grade to (1) accept an optional "slow" field and pass it
# to grade(), and (2) append each grading event to the log.
# Add GET /log and POST /reset-log endpoints.



# TODO: update POST /grade to log events and support "slow
# TODO: GET /log endpoint
@app.get("/log")
def log():
    return {"entries":grading_log}
# TODO: POST /reset-log endpoint
@app.post("/reset-log")
def reset_log():
    grading_log.clear()
    return{"status":"cleared"}


# ---------------------------------------------------------------------------
# Task 3: Idempotency Makes Retries Safe
# ---------------------------------------------------------------------------
# Add a completed dict that maps submission IDs to results.
# Update POST /grade to check for an optional "submission_id" field —
# if the ID is already in completed, return the cached result without
# grading again or logging.
# Add POST /reset-completed endpoint.

# TODO: completed = {}

# TODO: update POST /grade to check submission_id

# TODO: POST /reset-completed endpoint
@app.post("/reset-completed")
def reset_completed():
    completed.clear()
    return{"status":"cleared"}

# ---------------------------------------------------------------------------
# Task 4: Honest About Time
# ---------------------------------------------------------------------------
# You'll need: from fastapi import BackgroundTasks
#              from fastapi.responses import JSONResponse
#
# Add jobs dict, job_submission_map dict, and a job ID generator.
# Create POST /grade-async (returns 202, runs grading in background).
# Create a run_grade_job helper that does the actual grading.
# Create GET /grade-jobs/{job_id} to check job status.

# TODO: jobs = {}
# TODO: job_submission_map = {}

# TODO: POST /grade-async endpoint
@app.post("/grade-async")
def grade_async(data:dict,background_tasks:BackgroundTasks):
    sub_id = data.get("submission_id")
    if sub_id and sub_id in job_submission_map:
        job_id = job_submission_map[sub_id]
        return {"job_id":job_id}
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "pending"}
    background_tasks.add_task(run_grade_job, job_id, data.get("student"), data.get("lab"))
    if sub_id:
        job_submission_map[sub_id] = job_id
    return JSONResponse({"job_id": job_id, "status": "accepted"},status_code=202)
# TODO: run_grade_job helper function
def run_grade_job(job_id,student,lab):
    score = grading.grade(student,lab,slow=True)
    dictionary = {"student":student,"lab":lab,"score":score}
    grading_log.append(dictionary)
    jobs[job_id] = {"status":completed}
# TODO: GET /grade-jobs/{job_id} endpoint
@app.get("/grade-jobs/{job_id}")
def grade_jobs(job_id):
    if job_id not in job_submission_map:
        return JSONResponse({"error": "job not found"}, status_code=404)
    job = jobs[job_id]
    if job["status"] == 'pending':
        return {"job_id": job_id,"status":"pending"}
    if job["status"] == "complete":
        return {"job_id":job_id,"status":"complete","result":job}