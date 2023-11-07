from urllib.request import urlopen
import re

BAD_WORDS = ("bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism")

url = input("Give me a valid URL to download: ")
response = None

# Open url and get data
try:
    response = urlopen(url)

except ValueError as e:
    print(f"Invalid URL. {e}")

except Exception as e:
    print(f"Something went wrong opening the URL. {e}")

if (not response): exit()

data = response.read()
content_type = response.info().get_content_type()

# Parse bad words
if (content_type == "text/html"):
    data_string = data.decode("utf-8", "ignore")
    text_content = data_string

    bad_words_string = "|".join(BAD_WORDS)
    regex = f"\\b({bad_words_string})\\b"
    matches = re.findall(regex, text_content, re.IGNORECASE)

    print(f"Number of dangerous words: {len(matches)}")
else:
    text_content = data
    print(f"Content doesn't seem to be an HTML file. Found {content_type}")

# Save data to file
out_path = input("Give me a valid path to save the contents: ")

try:
    if (content_type == "text/html"):
        encoding = "utf-8"
        open_mode = 'w'
    else:
        encoding = None
        open_mode = 'wb'

    with open(out_path, open_mode, encoding=encoding) as out_file:
        out_file.write(text_content)
    
    print(f"Saving succeeded to: {out_path}")

except OSError as e:
    print(f"Couldn't open file. {e}")

except Exception as e:
    print(f"Something went wrong saving the content. {e}")