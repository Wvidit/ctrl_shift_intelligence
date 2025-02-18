from openai import OpenAI
def prompt_generator(user_prompt) -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<API_KEY>",
    )

    messages = [
        {"role": "system", "content": "You are a prompt engineer, which can generate a prompt to generate image or video. If not specified image or video preassume image generating prompt"}
    ]

    messages.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
    
    reply = response.choices[0].message.content
    return reply

