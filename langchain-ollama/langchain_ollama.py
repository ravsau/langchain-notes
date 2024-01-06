from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama




llm = Ollama(model="mistral")



print(llm("Tell me about the history of AI. And tell me names of some influencial figures in the AI Space"))




