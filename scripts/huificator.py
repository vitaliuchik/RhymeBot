vowels = ['у', 'е', 'а', 'о', 'и', 'і']
vowels_change = {
    'у': 'ю',
    'е': 'є',
    'а': 'я',
    'о': 'йо',
    'и': 'є',
    'і': 'ї',
}
soft = ['я', 'ю', 'є', 'ї']


def get_hui(word):
    """
    :param word: str
    :return changed word using huificator: str
    """
    for i, letter in enumerate(word):
        if letter in vowels or letter in soft:
            break

    if letter in soft:
        return 'ху' + word[i:]
    else:
        return 'ху' + vowels_change[letter] + word[i+1:]



