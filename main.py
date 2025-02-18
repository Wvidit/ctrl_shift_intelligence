from pprint import pprint
API_KEY="<API-KEY>"

from classes import TopicExplainer

new = TopicExplainer("Linear Algebra", "System of linear equations")

print("Thinking")
pprint(new.initial_response())

print("\n\nThinking\n\n")
pprint(new.get_response("can you go in a bit in depth about consistent and inconsitent system of solutions"))









# completion = client.chat.completions.create(
  
#   extra_body={},
#   model="deepseek/deepseek-r1-distill-llama-70b:free",
#   messages=[
#     {
#       "role": "user",
#       "content": "What is the meaning of life?"
#     }
#   ]
# )
# print(completion.choices[0].message.content)