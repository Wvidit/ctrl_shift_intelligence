from openai import OpenAI
import streamlit as st

# Constants
API_KEY = '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'
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
    prompt=(
        f"Subject: {subject}\n"
        f"Topic: {topic if topic else subject}"
    )
    return get_response(user_message=prompt, messages=messages)

def initial_question_maker_response(subject:str, topic:str, messages:list=[], question_count:int=3, difficulty:str='Medium'):

    prompt = (
            f"Subject: {subject}\n"
            f"Topic: {topic}\n"
            f"Number of questions: {question_count}\n"
            f"Difficulty: {difficulty}"
        )
    return get_response(user_message=prompt, messages=messages)


def initial_customer_support_response(product_name:str, product_id:str, issue:str, messages:list, bill_id)->str:
    """
    Returns response of chatbot if appropriate data is passed
    
    return -1 if bill_id doesn't exist
    """
    import json
    with open("./data.json", "r") as f:
        data = json.load(f)
    
    if bill_id not in data:
        return -1 

    data = data[bill_id]
    
    prompt = f"Product Name: {data['product_name']}\nProduct ID: {data['product_id']}\n\nIssue:\n{issue}"

    return get_response(user_message=prompt, messages=messages)
    

