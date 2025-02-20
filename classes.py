from openai import OpenAI

# Constants
API_KEY = "<API-KEY>"
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-r1-distill-llama-70b:free"

class ClientBase:
    """
    Abstract base class for interacting with the DeepSeek AI model.
    If a developer prompt is provided during initialization, it sends a request to the AI
    to configure its behavior based on the provided instructions.
    """

    def __init__(self, developer_prompt: str = ""):
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
        self.model = MODEL
        self.messages = []

        if developer_prompt:
            self._initialize_developer_prompt(developer_prompt)

    def _initialize_developer_prompt(self, developer_prompt: str):
        """
        Sends a request to the AI to configure its behavior based on the developer prompt.
        """
        system_message = (
            "I am the developer. I want you to behave according to the instructions given below. "
            "The conversations after this will be between you and the user. Do not send any response to this message.\n"
            """
                    **Important Instructions:**
            - Do not show your intermediate reasoning, thinking, or step-by-step process.
            - Provide only the final, polished explanation as your response.
            - Ensure the response is complete and does not include phrases like "Let me think," "Here's how I would approach this," or similar.
            """
            f"{developer_prompt}"
        )
        response = self.get_response(system_message)

        self.messages.extend([
            {"role": "developer", "content": developer_prompt},
            {"role": "assistant", "content": response}
        ])

    def get_response(self, user_message: str) -> str:
        """
        Sends a user message to the AI and returns the response.
        """
        self.messages.append({"role": "user", "content": user_message})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            extra_body={}
        )

        assistant_response = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": assistant_response})

        return assistant_response


class TopicExplainer(ClientBase):

    """
    A specialized class for explaining topics (and optionally subtopics) given by the user.
    """

    def __init__(self, subject: str, topic: str = ""):
        self.subject = subject
        self.topic = topic or subject

        developer_prompt = developer_prompt = """
            I want you to act as a subject matter expert in the subject provided by the user. 
            Your task is to explain the given topic or subject in a detailed, structured, and engaging manner.

            Follow these guidelines:
            1) Start with a clear and concise introduction to the topic.
            2) Break down the topic into fundamental concepts and explain each in detail.
            3) Provide real-world examples, analogies, or applications to enhance understanding.
            4) Cover advanced insights or related subtopics if relevant.
            5) Use clear, professional language and maintain a logical flow throughout the explanation.
            6) Conclude with a summary or key takeaways.

            Your goal is to ensure the user gains a thorough understanding of the topic.
            """
        super().__init__(developer_prompt)

    def initial_response(self) -> str:
        """
        Returns the AI's initial response explaining the subject and topic.
        """
        return self.get_response(f"Subject: {self.subject}\nTopic: {self.topic}")
    
class QuestionMaker(ClientBase):
    """
    A specialized class for generating questions on a given subject and topic.
    The questions are sequenced, independent, and cover a variety of difficulty levels.
    """

    def __init__(self, subject: str, topic: str = "", number: int = 3, difficulty_level: str = "moderate"):
        """
        Initializes the QuestionMaker with the subject, topic, number of questions, and difficulty level.

        Args:
            subject (str): The subject for which questions are to be generated.
            topic (str, optional): The specific topic within the subject. Defaults to the subject itself.
            number (int, optional): The number of questions to generate. Defaults to 5.
            difficulty_level (str, optional): The difficulty level of the questions. Defaults to "moderate".
        """
        self.subject = subject
        self.topic = topic or subject
        self.number = number
        self.difficulty = difficulty_level

        developer_prompt = developer_prompt = """
        I want you to act as a subject expert in the subject provided by the user. 
        Your task is to generate a set of questions based on the given topic, number of questions, and difficulty level.

        Follow these guidelines:
        1) Generate questions that are clear, concise, and directly related to the topic.
        2) Ensure the questions are sequenced logically and increase in difficulty.
        3) Each question should be independent and test different aspects of the topic.
        4) Include a variety of question types (e.g., conceptual, analytical, problem-solving).
        5) Provide questions that cover both fundamental and advanced aspects of the topic.
        6) Ensure the difficulty level matches the user's request (e.g., easy, moderate, hard).

        Your goal is to create a comprehensive and balanced set of questions that help the user deepen their understanding of the topic.
        """
        super().__init__(developer_prompt=developer_prompt)

    def initial_response(self) -> str:
        """
        Returns the AI's initial response generating questions for the subject and topic.

        Returns:
            str: The AI-generated questions.
        """
        prompt = (
            f"Subject: {self.subject}\n"
            f"Topic: {self.topic}\n"
            f"Number of questions: {self.number}\n"
            f"Difficulty: {self.difficulty}"
        )
        return self.get_response(prompt)
