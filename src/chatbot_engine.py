from typing import List

import langchain
from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import VectorStoreInfo, VectorStoreToolkit
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, PythonLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.tools import BaseTool

langchain.verbose = True


def create_index() -> VectorStoreIndexWrapper:
    loader = DirectoryLoader("./src/", glob="**/*.py", loader_cls=PythonLoader)
    return VectorstoreIndexCreator().from_loaders([loader])


def create_tools(index: VectorStoreIndexWrapper, llm) -> List[BaseTool]:
    vectorstore_info = VectorStoreInfo(
        vectorstore=index.vectorstore,
        name="python_source_code",
        description="Python source code from the project directory. Use this to search and analyze Python code files.",
    )
    toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info, llm=llm)
    return toolkit.get_tools()


def chat(
    message: str, history: ChatMessageHistory, index: VectorStoreIndexWrapper
) -> str:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    tools = create_tools(index, llm)

    memory = ConversationBufferMemory(
        chat_memory=history, memory_key="chat_history", return_messages=True
    )

    agent_chain = initialize_agent(
        tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, memory=memory
    )

    return agent_chain.run(input=message)
