# Rules

```
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group


Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


Flags:
re.I    - Performs case-insensitive matching
re.L    - 
re.M    - Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
re.S    - 
re.U    - Interprets letters according to the Unicode character set.
re.X    -
```

# Functions:


### `re.compile` - to specify pattern

```python
pattern = re.compile(r'')
```

### `re.finditer`

returns match object `<_sre.SRE_MATCH object; span(start, stop), match='matched_string'>`
```python
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
```
we can access the matches from `finditer` using group:
```python
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)

for match in matches: 
     print(match.group(3))

```
here:

`group()` is whole string.

`group(0)` prints first group (here, whole string).

`group(1)` is `www.` or `None`.

`group(2)` is domain name i.e. `google`, `youtube`.

`group(3)` is top level domains i.e. `.com`, `.gov`.


### `re.sub` to perform subtituion

```python
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

```
Here, `sub` method replace the matches found in `urls` by `group(1)` and `group(2)`. i.e. `\1\2`

### `re.findall`

just returns match string as a list of strings, same as `finditer` but with less information.

### `re.match`

The `re.match` function returns a match object on success, `None` on failure. `re.match` matches only at beginning of the string. We `usegroup(num)` or `groups()` function of match object to get matched expression.

```python
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

```
output:
```
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```

### `re.search`

`re.search` is same as `re.match` except it searches the first match in whole string, while `re.match` searches first match at the begining of string. `re.search` returns a match object on success, `None` on failure.

```python
sentence = 'Start a sentence and then sentence bring it to an end'
```

if our pattern is `r'Start'`, `re.match` and `re.search` will return same `match object`.

if our pattern is `r'sentence'`, `re.match` will return `None`, while `re.search` will return first occurance of word 'sentence' i.e. `<_sre.SRE_MATCH object; span(8, 16), match='sentence'>`



