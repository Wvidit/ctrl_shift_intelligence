from openai import OpenAI

#This models presumes there exists a unique product and bill ids
#For testing purposes we are using product name(assuming they are distinct)
def customer_support(context):
    model = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    messages = [
        {"role": "system", "content": '''Check if prompt have the following information or the following information can be deduced from it: 
                                        1)Product id or Product name
                                        2)Bill id
                                        if both of them are there return 1 else return 0
                                        '''},
    ]
    response = model.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    if response.choices[0].message.content == '1':

        message2 = [
            {"role": "system", "content": '''You are a customer support executive, provide customer support for Product name given if bill id is mentioned.'''}
        ]

        response = model.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = message2
        )