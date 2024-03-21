def are_characters_valid(input_string: str, allowed_characters: set[str]) -> bool:
        for character in input_string:
            if character not in allowed_characters:
                return False
        return True

def is_length_valid(input_string: str, min_length: int, max_length: int) -> bool:
    return max_length >= len(input_string) >= min_length