import openai
from dotenv import dotenv_values

config = dotenv_values('.env')

openai.api_key = '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'

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )
  retrieve_blog = response.choices[0].text
  return retrieve_blog

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False

