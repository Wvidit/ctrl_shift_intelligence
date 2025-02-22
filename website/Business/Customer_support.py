from openai import OpenAI
import json
#This models presumes there exists a unique product and bill ids
#For testing purposes we are using product name(assuming they are distinct)
API_KEY ="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"
with open('Data.json', 'r') as file:
    bills_data = json.load(file)

def customer_support(product_name:str, issue:str) -> str:
    model = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY
    )
    response = model.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are an expert for a product."},
            {"role": "user", "content": f"Provide assistance to the user for {product_name} facing {issue}"}
        ]
    )
    return response['choices'][0]['message']['content']

#def process_requests(product_name:str, bill_id:str) -> str:

user_prompt = str(input("How may I assist you?"))
message = [
                    {"role": "system", "content": '''Check if prompt have the following information or the following information can be deduced from it: 
                                        1)Product id or Product name
                                        2)Bill id
                                        if yes then return them in format
                                                    Product_name or Product_id,Bill_id
                                                    Eg:[[microwave],[HUJ998]]'''}
        ]
message.append({"role":"user", "content":user_prompt})

model = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key = API_KEY,
    )
response = model.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message
    )

useful_data =[]
useful_data.append(response.choices[0].message.content)
for i in useful_data:
    if i[0] and i[1] in
    customer_support(i[0], i[1])

#API KEY HAS EXPIRED
