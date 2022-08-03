FILTER_PHRASES = [
    'Nintendo Switch',
    'Microsoft Windows and Powerpoint',
    'Microsoft Word',
    'SONY devices',
    'usb-C'
]

TEXTS = [
    'i am enjoying the nintendo    switch',
    'i prefer the microsoft wordishness',
    'i love playing on the microsoft xbox',
    'do you have a usb charger?',
    'no, but i have a microsoft word',
    'i have both the Nintendo Gameboy and the Nintendo Switch',
]


def filter_phrases(texts, filter_phrases):
    lookup_table = {}
    for phrase in filter_phrases:
        phrase = phrase.lower().split()
        lookup_table[phrase[0]] = (phrase, len(phrase))

    filter_phrases = []
    for text in texts:
        tokens = text.lower().split()
        should_filter = False
        for i, token in enumerate(tokens):
            if token in lookup_table:
                phrase, length = lookup_table[token]
                if tokens[i:i+length] == phrase:
                    should_filter = True
                    break
            else:
                continue

        if not should_filter:
            filter_phrases.append(text)
    return filter_phrases


if __name__ == '__main__':
    print(filter_phrases(TEXTS, FILTER_PHRASES))

