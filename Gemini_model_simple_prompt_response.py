import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key.
### Disabled as jupyter is not installed on the local machine.
# from google.colab import userdata

### disabling as printing raw text instead.
# from IPython.display import display
# from IPython.display import Markdown


#def to_markdown(text):
#  text = text.replace('•', '  *')
#  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# Generate API key from https://ai.google.dev/tutorials/python_quickstart
GOOGLE_API_KEY="AIzaSyDVFJ3Aog_LVJoVvwDJbwPdvM7YW39oc0A"

genai.configure(api_key=GOOGLE_API_KEY)

# Listing the models.
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# This is text model. Other one in the list is for vision inputs.
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)

