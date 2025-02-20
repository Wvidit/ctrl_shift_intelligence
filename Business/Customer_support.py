from openai import OpenAI

#This models presumes there exists a unique product and bill ids
#For testing purposes we are using product name(assuming they are distinct)
def customer_support(context):
    model = OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key = "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",
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
            {"role": "system", "content": "You are an expert for the product provided by the user."},
        ]
        message2.append({"role": "user", "content": context })
        response1 = model.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = message2
        )
        return response1.choices[0].message.content
    else:
        return "Please provide Product id or Product name and Bill id"
