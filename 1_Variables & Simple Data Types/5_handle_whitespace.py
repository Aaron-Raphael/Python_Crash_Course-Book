# \t adds tab to text
# \n adds newline to text

language = 'Languages:\n\tPython\n\tJavascript' # \t and \n can be combined in a string
print(language)

# lstrip() removes whitespace at left of string 
# rstrip() removes whitespace at right of string 
# strip() removes whitespace at both ends of string

fav_language = '    Python    '
print("'" + fav_language + "'")

print("'" + fav_language.lstrip() + "'")
print("'" + fav_language.rstrip() + "'")
print("'" + fav_language.strip() + "'")

print(fav_language)

fav_language = fav_language.strip()
print("'" + fav_language + "'")