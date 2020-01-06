"""
Converts text to Pig Latin

>>> import piglatin
>>> 
>>> piglatin.translate('this is a test string')
'is-thay is-ay a-ay est-tay ing-stray'

"""
import re
import string
from string import ascii_letters
from ._version import __version__


def translate(txt):
    """Translates text into pig latin."""

    vowels = "aeiou"

    # Separates text into words and whitespace
    words = re.findall(r"(?:\S+)|(?:\s+)", txt)
    output = []
    ascii_set = set(ascii_letters)

    for word in words:
        # Whitespace does not require translation
        if not word.strip():
            output.append(word)
            continue

        # Punctuation-only "words" do not require translation
        if not ascii_set.intersection(word):
            output.append(word)
            continue

        # Gather pre and post punctuation (ie; quotes, etc.). They should
        # still remain at the beginning and end of the translated word.
        m = re.match(r"^(?P<pre>[\W]*)(?P<word>.+?)(?P<post>[\W]*)$", word)
        d = m.groupdict()

        # pig latin removes any leading consonants to a word and places them
        # at the end of the word, followed by -ay.  If the word starts with a
        # vowel, just append -ay.  Treat y as a vowel only if it is not at
        # the beginning of a word and preceded by a consonant (this isn't
        # foolproof, but it works in most cases).
        i = 0
        word = d["word"]
        while len(word) > i:
            if word[i].lower() in vowels:
                break
            if i > 0 and word[i].lower() == "y":
                break
            i += 1
        d["fore"] = word[i:]
        d["aft"] = word[:i]
        new_word = "{pre}{fore}-{aft}ay{post}".format(**d)
        output.append(new_word)

    return "".join(output)
			
	
