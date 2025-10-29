def sort_list_of_dictionaries(data, key):
    """Sorts a list of dictionaries by a specified key."""
    try:
        return sorted(data, key=lambda x: x[key])
    except KeyError:
        print(f"Error: Key '{key}' not found in one of the dictionaries.")
        return data
    except TypeError:
        print("Error: Values under the key are not comparable.")
        return data
# Test cases for the sort_list_of_dictionaries function
def test_sort_list_of_dictionaries():
    data = [
        {'name': 'Alice', 'score': 85, 'age': 30},
        {'name': 'Bob', 'score': 92, 'age': 25},
        {'name': 'Charlie', 'score': 78, 'age': 35}
    ]

    # Test sorting by score
    sorted_by_score = sort_list_of_dictionaries(data, 'score')
    assert sorted_by_score == [
        {'name': 'Charlie', 'score': 78, 'age': 35},
        {'name': 'Alice', 'score': 85, 'age': 30},
        {'name': 'Bob', 'score': 92, 'age': 25}
    ], "Test failed: Sorting by score did not produce expected result."

    # Test sorting by age
    sorted_by_age = sort_list_of_dictionaries(data, 'age')
    assert sorted_by_age == [
        {'name': 'Bob', 'score': 92, 'age': 25},
        {'name': 'Alice', 'score': 85, 'age': 30},
        {'name': 'Charlie', 'score': 78, 'age': 35}
    ], "Test failed: Sorting by age did not produce expected result."

    # Test with a missing key
    result_with_missing_key = sort_list_of_dictionaries(data, 'height')
    assert result_with_missing_key == data, "Test failed: Function should return original data on missing key."

    # Test with incomparable types
    data_with_incomparable_types = [
        {'name': 'Alice', 'value': 10},
        {'name': 'Bob', 'value': 'twenty'},
        {'name': 'Charlie', 'value': 15}
    ]
    result_with_incomparable_types = sort_list_of_dictionaries(data_with_incomparable_types, 'value')
    assert result_with_incomparable_types == data_with_incomparable_types, "Test failed: Function should return original data on incomparable types."

    print("All tests passed!")
    # Execute the test function
if __name__ == "__main__":
    test_sort_list_of_dictionaries() 
 