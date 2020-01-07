"""Converts text to Pig Latin"""

import re
import string

__version__ = "1.0.6"


def translate(txt):
    # type: (str) -> str
    """Translates text into pig latin.
    
    Args:
        txt (str): The text to translate.

    Returns:
        str: The text converted to pig latin.
    """

    vowels = "aeiou"

    # Separates text into words and whitespace
    words = re.findall(r"(?:\S+)|(?:\s+)", txt)
    output = []
    ascii_set = set(string.ascii_letters)

    for word in words:
        # Whitespace does not require translation
        if not word.strip():
            output.append(word)
            continue

        # Punctuation-only "words" do not require translation
        if not ascii_set.intersection(word):
            output.append(word)
            continue

        # Gather pre and post punctuation (i.e. quotes, etc.). They should
        # still remain at the beginning and end of the translated word.
        m = re.match(r"^(?P<pre>[\W]*)(?P<word>.+?)(?P<post>[\W]*)$", word)
        
        # If for some reason, this word can't be parsed, just include it as-is
        # in the output without translating it.
        if not m:
            output.append(word)
            continue

        d = m.groupdict()

        # pig latin removes any leading consonants to a word and places them
        # at the end of the word, followed by -ay.  If the word starts with a
        # vowel, just append -ay.  Treat y as a vowel only if it is not at
        # the beginning of a word and preceded by a consonant (this isn't
        # foolproof, but it works in most cases).
        word = d["word"]
        for i, letter in enumerate(word):
            if letter in vowels or i > 0 and letter == "y":
                break
        else:
            # If the word contains no vowels, don't strip any letters off the front.
            i = 0
        d["fore"] = word[i:]
        d["aft"] = word[:i]
        new_word = "{pre}{fore}-{aft}ay{post}".format(**d)
        output.append(new_word)

    return "".join(output)
