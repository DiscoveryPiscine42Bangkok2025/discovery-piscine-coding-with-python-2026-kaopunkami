#!/usr/bin/env python3
def array_of_names(persons: dict) -> list:
    full_names = []
    for first, last in persons.items():
        full_names.append(f"{first.capitalize()} {last.capitalize()}")
    return full_names


if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))