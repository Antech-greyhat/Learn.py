# Order jobs so every dependency comes before the job that needs it.
# Practice: directed graphs, topological sorting, heaps, and cycle detection.
import heapq
import json


def schedule_jobs(dependencies):
    if not isinstance(dependencies, dict) or not 1 <= len(dependencies) <= 50:
        raise ValueError("Enter a JSON object with from 1 to 50 jobs.")
    for job, prerequisites in dependencies.items():
        if not isinstance(job, str) or not job or job != job.strip():
            raise ValueError("Job names must be nonempty strings without surrounding spaces.")
        if not isinstance(prerequisites, list) or len(prerequisites) > 50:
            raise ValueError("Each dependency value must be a list of at most 50 job names.")
        if any(not isinstance(name, str) or name not in dependencies for name in prerequisites):
            raise ValueError(f"Job {job!r} refers to an unknown dependency.")
    remaining = {job: len(set(prerequisites)) for job, prerequisites in dependencies.items()}
    followers = {job: [] for job in dependencies}
    for job, prerequisites in dependencies.items():
        for prerequisite in set(prerequisites):
            followers[prerequisite].append(job)
    ready = [job for job, count in remaining.items() if count == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        job = heapq.heappop(ready)
        order.append(job)
        for follower in followers[job]:
            remaining[follower] -= 1
            if remaining[follower] == 0:
                heapq.heappush(ready, follower)
    if len(order) != len(dependencies):
        blocked = sorted(job for job, count in remaining.items() if count)
        raise ValueError(f"Dependency cycle blocks: {', '.join(blocked)}")
    return order


def main():
    print('Dependency Scheduler - example: {"test": ["build"], "build": []}.')
    print("Alphabetical order breaks ties; repeated dependencies count once.")
    while True:
        text = input("Jobs JSON (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            print(f"Order: {' -> '.join(schedule_jobs(json.loads(text)))}")
        except (ValueError, RecursionError) as error:
            print(f"Cannot schedule jobs: {error}")


if __name__ == "__main__":
    main()
