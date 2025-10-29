# --- Python Function to Sort a List of Dictionaries by a Specific Key (Manual Implementation) ---

def sort_list_of_dicts_manual(list_of_dicts, key_to_sort_by):
    """
    Sorts a list of dictionaries based on the value of a specified key.

    Args:
        list_of_dicts (list): The list of dictionaries to be sorted.
        key_to_sort_by (str): The dictionary key to use for the sorting criteria.

    Returns:
        list: A new sorted list of dictionaries.
    """
    # We use the built-in sorted() function.
    # The 'key' argument takes a lambda function, which specifies that for 
    # every dictionary 'd' in the list, the value of 'd[key_to_sort_by]' 
    # should be used for comparison during the sort.
    try:
        sorted_list = sorted(list_of_dicts, key=lambda d: d[key_to_sort_by])
        return sorted_list
    except KeyError:
        # Handle the case where the key doesn't exist in one or more dictionaries
        print(f"Error: The key '{key_to_sort_by}' was not found in one of the dictionaries.")
        return list_of_dicts # Return the original list
    except TypeError:
        # Handle the case where values under the key are of incomparable types
        print("Error: Values under the key are not comparable (e.g., mixing strings and numbers).")
        return list_of_dicts


# --- Example Usage ---
data = [
    {'name': 'Alice', 'score': 85, 'age': 30},
    {'name': 'Bob', 'score': 92, 'age': 25},
    {'name': 'Charlie', 'score': 78, 'age': 35}
]

# Sort by 'score'
sorted_by_score = sort_list_of_dicts_manual(data, 'score')
print("Sorted by Score:")
for item in sorted_by_score:
    print(item)

print("\n" + "-"*30 + "\n")

# Sort by 'age'
sorted_by_age = sort_list_of_dicts_manual(data, 'age')
print("Sorted by Age:")
for item in sorted_by_age:
    print(item)