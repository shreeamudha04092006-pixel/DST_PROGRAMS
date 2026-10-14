permissions = {
    'admin': {'read', 'write', 'delete'},
    'operator': {'read', 'write'},
    'auditor': {'read', 'export'}
}

users = list(permissions.values())

common = users[0]

for user_permissions in users[1:]:
    common = common & user_permissions

all_permissions = set()

for user_permissions in users:
    all_permissions = all_permissions | user_permissions

print("Common permissions:", sorted(common))
print("All permissions:", sorted(all_permissions))