from prompt_generator import prompt_generator
from shakespear import shakespear_says
from openai import OpenAI

user_input = str(input("What do you want to do?:"))

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<API-KEY>",
        )
messages1 = [
        {"role": "system", "content": "You are a helpful assistant"}
]
messages1.append({"role": "user", "content": "Summarize the following sentence(as it could be used a prompt for an ai assistant):" + user_input})

response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages1
        )

input_better = response.choices[0].message.content

messages2 = [
        {"role": "system", "content": "You have to figure out what is the prompt asking, output 1 if it is asking something related to image or video generation and 2 if it is asking to generate something in the domain of writing."}
]
messages2.append({"role": "user", "content": input_better})
value = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = messages2
        )
value = value.choices[0].message.content

match value:
        case '1':
            prompt = prompt_generator(input_better)
        case '2':
            target = shakespear_says(input_better)

print(target)
