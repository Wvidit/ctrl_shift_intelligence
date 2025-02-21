from openai import OpenAI

# Constants
API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1"

# MODEL = "deepseek/deepseek-r1-distill-llama-70b:free"
MODEL = "deepseek/deepseek-chat:free"

def get_response(user_message:str, messages:list=[]):
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    messages.append({
        'role':'user',
        'content':user_message
    })
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        extra_body={}
    )
    # print(response)
    response = response.choices[0].message.content
    print(response)
    return response

def initial_topic_explainer_response(subject:str, topic:str, messages:list=[]):
    message=(
        f"Subject: {subject}\n"
        f"Topic: {topic if topic else subject}"
    )
    return get_response(user_message=message, messages=messages)

def initial_question_maker_response(subject:str, topic:str, messages:list=[], question_count:int=3, difficulty:str='Medium'):

    prompt = (
            f"Subject: {subject}\n"
            f"Topic: {topic}\n"
            f"Number of questions: {question_count}\n"
            f"Difficulty: {difficulty}"
        )
    return get_response(user_message=prompt, messages=messages)


# def shakespear_says(author:str, messages:list=[]) -> str:
#     get_response(user_message=f"{author}", messages=messages)

    

