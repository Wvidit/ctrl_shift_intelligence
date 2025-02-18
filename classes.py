from openai import OpenAI
API_KEY="<API-KEY>"


class ClientBase:
    """
    This acts as the abstract base class to be used for chatting with deepseek.
    while initializing, if developer prompt is provided, it sends a request to AI
    during object creation as a developer and inform it to behave as instructed    
    """
    def __init__(self, developer_prompt=""):
        self.client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
        )
        self.model = "deepseek/deepseek-r1-distill-llama-70b:free"
        self.messages=[]

        if developer_prompt:
            response =  self.get_response("I am the developer. I want you to behave the instructions given below. The conversations after that will be with you and user. Do no send any reponse to this message\n"+developer_prompt)

            self.messages.append({
                "role":"developer",
                "content": developer_prompt
            })
            self.messages.append({
                "role":"assistant",
                "content":response
            })
        
    def get_response(self, user_message:str):
        self.messages.append({
            "role":"user",
            "content":user_message
        })
        response = self.client.chat.completions.create(
          extra_body={},
          model=self.model,
          messages=self.messages
        )
        # pprint(response)
        
        self.messages.append({
            "role":"assistant",
            "content":response.choices[0].message.content
        })
        
        return response.choices[0].message.content
        

class TopicExplainer(ClientBase):
    
    """
    This is made for explaining topics (and optionally subtopics) given by the user. 
    """

    def __init__(self, subject:str, topic:str=""):
        if not topic:
            topic = subject
        self.subject=subject
        self.topic=topic

        developer_prompt= f"""
        I want you to act as a subject matter expert in the subject given by the user.
        Explain the topic/subject given in depth. Provide a thorough, structured explanation, covering fundamental concepts, key details, and advanced insights as needed. Use clear, concise language and include examples or analogies where helpful.
"""
        super().__init__(developer_prompt)
    
    def initial_response(self):
        return super().get_response(f"Subject: {self.subject}\nTopic: {self.topic}")
