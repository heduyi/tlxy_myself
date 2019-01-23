#! Python3
# mailRegex.py - find email address on the clipboard

import re, pyperclip

mailRegex01 = re.compile(r'''(
    '
    (@
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    (\.[a-zA-Z]{2,4})?
    ))''',re.DOTALL|re.VERBOSE)

matches01 = []
text = str(pyperclip.paste())
for groups in mailRegex01.findall(text):
    matches01.append(groups[1])
    matches01 = set(matches01)
    matches01 = list(matches01)



mailRegex02 = re.compile(r'''(
    ([a-zA-Z0-9._%+-]+)
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    (\.[a-zA-Z]{2,4})?
    )''',re.DOTALL|re.VERBOSE)

matches02 = []
text = str(pyperclip.paste())
for groups in mailRegex02.findall(text):
    matches02.append(groups[0])
    matches02 = set(matches02)
    matches02 = list(matches02)

pyperclip.copy('\n'.join(matches01) + '\n' + '\n'.join(matches02))
# print('\n'.join(matches01))
# print('\n'.join(matches02))


