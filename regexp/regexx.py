import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')
# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))    # ['e', 'a', 'd', 'b', 'e', 'a']


'''
\d  class[0-9]
\D  non-digit character
\s  whitespace character
\S  non-whitespace character
\w  class [a-zA-Z0-9_]  alphanumeric character
\W  non-alphanumeric character
'''

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))   # ['1', '1', '4', '1', '8', '8', '6']
# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))   # ['11', '4', '1886']


p = re.compile("\w")
print(p.findall("Raghav Gupta went to him at 11 A.M., he said *** in some_language."))
# ['R', 'a', 'g', 'h', 'a', 'v', 'G', 'u', 'p', 't', 'a', 'w', 'e', 'n', 't', 't', 'o', 'h', 'i', 'm', 'a', 't', '1', '1', 'A', 'M', 'h', 'e', 's', 'a', 'i', 'd', 'i', 'n', 's', 'o', 'm', 'e', '_', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
p = re.compile("\w*")
print(p.findall("Raghav Gupta went to him at 11 A.M., he said *** in some_language."))
# ['Raghav', '', 'Gupta', '', 'went', '', 'to', '', 'him', '', 'at', '', '11', '', 'A', '', 'M', '', '', '', 'he', '', 'said', '', '', '', '', '', 'in', '', 'some_language', '', '']
p = re.compile("\w+")
print(p.findall("Raghav Gupta went to him at 11 A.M., he said *** in some_language."))
# ['Raghav', 'Gupta', 'went', 'to', 'him', 'at', '11', 'A', 'M', 'he', 'said', 'in', 'some_language']


p = re.compile("ab*")
print(p.findall("abab bab abasa basbb abbab abba"))
# ['ab', 'ab', 'ab', 'ab', 'a', 'a', 'a', 'abb', 'ab', 'abb', 'a']




from re import split     # re.split(pattern, string, maxsplit=0, flags=0)
# maxsplit: if any nonzero value is provided, then at most that many splits occurs.
# flags = re.IGNORECASE (example)

print(split(r'\W+', 'Words, words , Words'))
# ['Words', 'words', 'Words']
print(split(r'\W+', "Word's     words Words"))
# ['Word', 's', 'words', 'Words']
print(split(r'\W+', 'On 12th Jan 2016, at 11:02 AM'))
# ['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']
print(split(r'\d+', 'On 12th Jan 2016, at 11:02 AM'))
# ['On ', 'th Jan ', ', at ', ':', ' AM']


from re import sub
# re.sub(pattern, repl, string, count=0, flags=0)
# sub searches substring 'pattern' in string and replace with 'repl'. count checks and maintains the number of times this occurs1
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))
# S~*ject has ~*er booked already
# S~*ject has Uber booked already

from re import subn
# subn() is similar to sub() in all ways, except in its way to providing output. It returns a tuple with count of total of replacement and the new string rather than just the string.
print(re.subn('ub', '~*', 'Subject has Uber booked already'))
print(re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
# ('S~*ject has Uber booked already', 1)
# ('S~*ject has ~*er booked already', 2)

from re import search
obj = search("([a-zA-Z]+) (\d+)", "I was born on June 24")
if obj is not None:
    print (obj)  # <_sre.SRE_Match object; span=(14, 21), match='June 24'>
    print (obj.group())  # June 24
    print (obj.group(1), obj.group(2))   # June 24

# email address regex
mail = r"[a-z0-9\.\-+_\\]+@[a-z0-9\.\-+_]+\.[a-z]+"
text = '''
Real, you say. I'll list a few fictional ones as an introduction to my post - all taken from animated TV shows:
1 Chun+-kyLover53@aol.com (Homer Simpson - The Simpsons)
2 smartgirl63_\@Yahoo.com (Lisa Simpson - The Simpsons)
3 awo_ng@marslink.web (Amy Wong - Futurama)
4 Zoidberg@freemail.web (Zoidberg - Futurama)
5 Bender@Ilovebender.com (Bender - Futurama)
6 loismustdie@yahoo.com (Stewie - Family Guy)
(wow, Lisa has a backslash in her email address!)
sorce: https://www.quora.com/What-are-the-most-famous-real-email-addresses
'''
print(re.findall(mail, text, re.I))
# ['Chun+-kyLover53@aol.com', 'smartgirl63_\\@Yahoo.com', 'awo_ng@marslink.web', 'Zoidberg@freemail.web', 'Bender@Ilovebender.com', 'loismustdie@yahoo.com']

'''
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One ore more occurrences
{}  Indicate number of occurrences of a preceding RE
    to match.
()  Enclose a group of REs
'''
