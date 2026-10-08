entry = "22:45"
exit = "01:20"

# Convert entry time
entry_parts = entry.split(":")
entry_hour = int(entry_parts[0])
entry_minute = int(entry_parts[1])

# Convert exit time
exit_parts = exit.split(":")
exit_hour = int(exit_parts[0])
exit_minute = int(exit_parts[1])

entry_total = entry_hour * 60 + entry_minute
exit_total = exit_hour * 60 + exit_minute

# Handle midnight
if exit_total < entry_total:
    exit_total = exit_total + 24 * 60

duration = exit_total - entry_total

hours = duration // 60
minutes = duration % 60

# Billable hours
billable_hours = (duration + 59) // 60

if billable_hours <= 1:
    fee = 30
else:
    fee = 30 + (billable_hours - 1) * 20

print("Parking Duration :", hours, "hours", minutes, "minutes")
print("Billable Hours   :", billable_hours)
print("Parking Fee      :", "₹" + str(fee))