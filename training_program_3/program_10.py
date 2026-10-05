def top_k_frequent_logs(logs, k):
    frequency = {}

    for log in logs:
        tag = log.split(":")[0]

        if tag in frequency:
            frequency[tag] += 1
        else:
            frequency[tag] = 1

    result = sorted(
        frequency,
        key=lambda x: (-frequency[x], x)
    )

    return result[:k]


logs = [
    "ERROR: db timeout",
    "INFO: user login",
    "ERROR: auth failed",
    "WARNING: disk low",
    "ERROR: lost connection",
    "INFO: user logout"
]

print(top_k_frequent_logs(logs, k=2))