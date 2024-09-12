from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.language_models.llms import BaseLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from python.helpers.dirty_json import DirtyJson
from python.helpers.defer import DeferredTask
from python.helpers.print_style import PrintStyle
from agent import AgentContext, AgentConfig
from langchain.schema import AIMessage
import python.helpers.log as Log
import models
import os

class Perplex:
    def __init__(self, agent) -> None:
        self.agent = agent
        self.config = agent.config
        self.history = []
        
        if os.getenv("API_KEY_GOOGLE"):
            self.client = models.get_google_chat(model_name="gemini-1.5-flash", temperature=0)
        else:
            self.client = self.config.chat_model

    async def execute(self, query: str):
        await self.append_message(query, human=True) 
        try:
            prompt = ChatPromptTemplate.from_messages([
                    MessagesPlaceholder(variable_name="messages") ])

            inputs = {"messages": self.history}
            chain = prompt | self.client

            # Replace streaming with a single call
            response = await chain.ainvoke(inputs)
            
            if isinstance(response, str): agent_response = response
            elif hasattr(response, "content"): agent_response = str(response.content)
            else: agent_response = str(response)

            await self.append_message(agent_response, human=False)
            return agent_response
        
        except Exception as e:
            PrintStyle(font_color="red", padding=True).print(e)
            return f"Error: {str(e)}"

    async def append_message(self, msg: str, human: bool = False):
        message_type = "human" if human else "ai"
        if self.history and self.history[-1].type == message_type:
            self.history[-1].content += "\n\n" + msg
        else:
            new_message = HumanMessage(content=msg) if human else AIMessage(content=msg)
            self.history.append(new_message)


    async def scraper(self, queries: str, content: str):
        template = self.agent.read_prompt("perplex.prompt.md", content=content)
        await self.append_message(msg=f'"system: "{template}"', human=True)
        results = ""
        messages = queries.split(", ")
        for query in messages:
            result = await self.execute(query)
            results += f"Result for '{query}':\n{result}\n\n"
        return results.strip()