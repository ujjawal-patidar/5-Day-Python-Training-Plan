# Write a program using regular expressions to extract email addresses, phone numbers, and URLs from text.

import re

text = "ujjawal-patidar@gmail.com and 9191919191, 2323322323 and https://www.google.com some random text"

extracted_data = re.findall(r"[\w\.-]+@[\w\.]+ | \d+ | https?://[\w.-]+", text)

print(extracted_data)