# 1) Sort the `people` list of dictionaries alphabetically based on the
# 'name' key from each dictionary using the `sorted` function and store
# the new list as `sorted_by_name`

people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 40},
    {"name": "Victor Wong", "age": 74},
]

sorted_by_name = sorted(people, key=lambda d: d['name'].lower())

print(sorted_by_name)

assert sorted_by_name == [
    {"name": "Ariana Richards", "age": 40},
    {"name": "finn Carter", "age": 59},
    {"name": "Fred Ward", "age": 77},
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Victor Wong", "age": 74},
], f"Expected sorted_by_name to equal '{sorted_by_name}' to equal '{[{'name': 'Ariana Richards', 'age': 40}, {'name': 'finn Carter', 'age': 59}, {'name': 'Fred Ward', 'age': 77}, {'name': 'Kevin Bacon', 'age': 61}, {'name': 'Victor Wong', 'age': 74}]}''"


# Another example of sorting

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda student: student[2])) # sort by age