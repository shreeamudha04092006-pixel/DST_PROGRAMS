def parse_numeric_log(log_records):
    valid = []
    corrupted_count = 0

    for record in log_records:
        try:
            parts = record.split(",")
            transaction_id = parts[0].strip()
            value = float(parts[1].strip())

            valid.append({
                "id": transaction_id,
                "value": value
            })

        except:
            corrupted_count += 1

    return {
        "valid": valid,
        "corrupted_count": corrupted_count
    }


log_records = [
    "TXN101, 145.50",
    "TXN102, invalid_num",
    "TXN103, 300.00",
    "CORRUPTED_LINE",
    "TXN104, 82.25"
]

print(parse_numeric_log(log_records))