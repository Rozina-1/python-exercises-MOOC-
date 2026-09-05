def oldest_person(people: list):
    oldest_record = people[0]
    for item in people:
        if item[1]<oldest_record[1]:
            oldest_record = item
    return oldest_record[0]
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))