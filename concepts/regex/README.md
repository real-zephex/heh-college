# Regular Expressions in Python
A pattern matching system used to search, match, and manipulate text using pattern rules.

## Basic Concepts
The fundamental building blocks and syntax rules that make up regular expressions.

### Special Sequences
Predefined patterns that match specific types of characters, marked with a backslash.

- `\d` - Matches any digit (0-9)
- `\D` - Matches any non-digit
- `\w` - Matches word characters (a-z, A-Z, 0-9, _)
- `\W` - Matches non-word characters
- `\s` - Matches whitespace (space, tab, newline)
- `\S` - Matches non-whitespace
- `\b` - Matches word boundary
- `\B` - Matches non-word boundary

### Character Classes
Groups of characters enclosed in square brackets that match any single character from the set.

- `[abc]` - Matches any character in the set
- `[^abc]` - Matches any character not in the set
- `[a-z]` - Matches any lowercase letter
- `[A-Z]` - Matches any uppercase letter
- `[0-9]` - Matches any digit

### Quantifiers
Symbols that specify how many times a pattern should match.

- `*` - 0 or more occurrences
- `+` - 1 or more occurrences
- `?` - 0 or 1 occurrence
- `{n}` - Exactly n occurrences
- `{n,}` - n or more occurrences
- `{n,m}` - Between n and m occurrences

### Common Methods
Built-in functions in Python's re module for working with regular expressions.

- `re.search()` - Search for pattern anywhere in string
- `re.match()` - Match pattern at start of string
- `re.findall()` - Find all occurrences of pattern
- `re.sub()` - Replace pattern matches with replacement text
- `re.split()` - Split string by pattern

### Flags
Optional parameters that modify how the regex pattern matching behaves.

- `re.I` or `re.IGNORECASE` - Case-insensitive matching
- `re.M` or `re.MULTILINE` - Multi-line matching
- `re.S` or `re.DOTALL` - Dot matches any character including newline
- `re.X` or `re.VERBOSE` - Allow verbose regex patterns
