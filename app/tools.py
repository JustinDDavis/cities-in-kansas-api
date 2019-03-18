
def find_characters_from_beginning(characters):
    def test_list(item):
        return item.lower().startswith(characters.lower())
    return test_list

def filter_items(characters_to_match, list_of_items):
    lambda_test = find_characters_from_beginning(characters_to_match)
    return list(filter(lambda item: lambda_test(item), list_of_items))
