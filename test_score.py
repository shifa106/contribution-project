def calibrate_perfect():
    members = [
        {"name": "Aarav", "tasks": 12, "files": 8, "commits": 32, "cons": 1.0, "peer": 4.8, "claim": 40},
        {"name": "Riya", "tasks": 6, "files": 5, "commits": 7, "cons": 0.75, "peer": 4.2, "claim": 30},
        {"name": "Kabir", "tasks": 2, "files": 1, "commits": 1, "cons": 0.35, "peer": 3.0, "claim": 20},
        {"name": "Dev", "tasks": 0, "files": 0, "commits": 0, "cons": 0.10, "peer": 1.2, "claim": 10},
    ]

    total_tasks = sum(m["tasks"] for m in members) or 1
    total_files = sum(m["files"] for m in members) or 1
    total_commits = sum(m["commits"] for m in members) or 1
    total_cons = sum(m["cons"] for m in members) or 1
    total_peer = sum(m["peer"] for m in members) or 1

    raw_scores = []
    for m in members:
        t = (m["tasks"] / total_tasks)
        d = (m["files"] / total_files)
        a = (m["commits"] / total_commits)
        c = (m["cons"] / total_cons)
        p = (m["peer"] / total_peer)

        raw = (t * 0.30) + (d * 0.25) + (a * 0.20) + (c * 0.15) + (p * 0.10)
        # Base participation smoothing
        smoothed = raw * 0.94 + 0.015
        raw_scores.append(smoothed)

    total_raw = sum(raw_scores)
    estimates = [round((r / total_raw) * 100) for r in raw_scores]
    diff = 100 - sum(estimates)
    estimates[0] += diff

    print(f"Target calibrated scores:")
    for m, est in zip(members, estimates):
        print(f" - {m['name']}: {est}%")

calibrate_perfect()
