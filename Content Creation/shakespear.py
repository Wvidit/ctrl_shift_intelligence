from openai import OpenAI
def shakespear_says(user_prompt) -> str:
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
        )

        messages = [
        {"role": "system", "content": "You are a author whose name maybe provided by the user. If any topic is not provided pick a topic yourself."}
        ]

        messages.append({"role": "user", "content": user_prompt})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
