data = [
    " Asha, Chennai, 25 ",
    "Bala, chennai, 30",
    " asha, Chennai, 25",
    "Charan, Bangalore, 28",
    "Bala, Chennai, 30 "
]

cleaned = []
seen = set()

for record in data:
    name, city, age = record.strip().split(",")

    name = name.strip().title()
    city = city.strip().title()
    age = int(age.strip())

    key = (name, city, age)

    if key not in seen:
        seen.add(key)
        cleaned.append({
            "name": name,
            "city": city,
            "age": age
        })

print(cleaned)