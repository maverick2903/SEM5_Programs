
import re

file = open("pattern.txt")
text = file.read()

# for names
# pattern_names = r'M\w*.\s*\w*\s*\w*[\n]'
pattern_names = r'M.+\..*[\n]'
# pattern_email = r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+'

names1 = re.findall(pattern_names, text)
names = []
for i in names1:
    names.append(i[:-1])

print("Names are:")
for i in names:
    print(i)
print()

# for website addresses
# pattern_web = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

# websites = re.findall(pattern_web, text)

# print("Websites are:")
# for i in websites:
#     if 'https://' in i[0]:
#         print(i[0][8:])
#     elif 'http://' in i[0]:
#         print(i[0][7:])
#     else:
#         print(i[0])
# print()

# pattern_web = r"(https?://(.{4}|.{3})(.+)\.(com|in))"
# websites = re.findall(pattern_web,text)
# for match in websites:
#     print(match[2])
# print(websites)

pattern_web = r"(https?://)(.*)"
websites = re.findall(pattern_web,text)
for match in websites:
    print(match[1])


# for email addresses
# emails = re.findall(pattern_email, text)

# print("Email addresses are:")
# for i in emails:
#     print(i)
# print()

pattern_email = r"\w*\.?\w*\@.*"
emails = re.findall(pattern_email, text)

print("Email addresses are:")
for i in emails:
    print(i)
print()

pattern_username = r'\S+.@'
pattern_domain = r'@\S+.'

usernames = re.findall(pattern_username, ' '.join(emails))
domains = re.findall(pattern_domain, ' '.join(emails))

print("Usernames and domains of each of the email addresses are:")
for i, j in zip(usernames, domains):
    print("User Id.: ", i[:-1], "; Domain: ", j[1:], sep="")
print()

# for numbers
pattern_number = r'[0-9]+[#\-*]*[0-9]+[#\-*]*[0-9]+'
numbers = re.findall(pattern_number, text)

print("Phone numbers are:")
for i in numbers:
    print(i)
