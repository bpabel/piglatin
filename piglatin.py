""" Converts text to Pig Latin

>>> import piglatin
>>> 
>>> piglatin.translate('this is a test string')
'is-thay is-ay a-ay est-tay ing-stray'

"""
import re
import string
from string import ascii_letters


def translate(txt):
	""" Translates text into pig latin ."""

	vowels = 'aeiou'
	# Separates text into words and whitespace
	words = re.findall(r'(?:\S+)|(?:\s+)', txt)
	output = []
	ascii_set = set(ascii_letters)
	for word in words:
		# Whitespace does not require translation
		if not word.strip():
			output.append(word)
			continue
		# Punctuation does not require translation
		if not ascii_set.intersection(word):
			output.append(word)
			continue
		
		# Gather pre and post punctuation (ie; qhotes, etc.).  They should
		# still remain at the beginning and end of the translated word.
		m = re.match(r'^(?P<pre>[\W]*)(?P<word>.+?)(?P<post>[\W]*)$', word)
		d = m.groupdict()
		

		# pig latin removes any leading consonants to a word and places them
		# at the end of the word, followed by -ay.  If the word starts with a 
		# vowel, just append -ay.  Treat y as a vowel only if it is not at 
		# the beginning of a word and preceded by a consonant (this isn't 
		# foolproof, but it works cases).
		i = 0
		word = d['word']
		while len(word) > i:
			if word[i].lower() in vowels:
				break
			if i > 0 and word[i].lower() == 'y':
				break				
			i += 1
		d['fore'] = word[i:]
		d['aft'] = word[:i]
		new_word = '{pre}{fore}-{aft}ay{post}'.format(**d)
		output.append(new_word)
	return ''.join(output) 
			
			
if __name__ == '__main__':
	txt = """
The Gettysburg Address 

Four score and seven years ago our fathers brought forth on this continent, 
a new nation, conceived in Liberty, and dedicated to the proposition that all 
men are created equal. 

Now we are engaged in a great civil war, testing whether that nation, or any 
nation so conceived and so dedicated, can long endure. We are met on a great 
battlefield of that war. We have come to dedicate a portion of that field, as 
a final resting place for those who here gave their lives that that nation 
might live. It is altogether fitting and proper that we should do this. 

But, in a larger sense, we cannot dedicate - we cannot consecrate - we cannot 
hallow - this ground. The brave men, living and dead, who struggled here, have 
consecrated it, far above our poor power to add or detract. The world will 
little note, nor long remember what we say here, but it can never forget what 
they did here. It is for us the living, rather, to be dedicated here to the 
unfinished work which they who fought here have thus far so nobly advanced. 
It is rather for us to be here dedicated to the great task remaining before 
us - that from these honored dead we take increased devotion to that cause for 
which they gave the last full measure of devotion - that we here highly resolve 
that these dead shall not have died in vain - that this nation, under God, 
shall have a new birth of freedom - and that government of the people, by 
the people, for the people, shall not perish from the earth.
"""
	
	print translate(txt)