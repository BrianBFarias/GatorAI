# from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
# from langchain.embeddings import GooglePalmEmbeddings
# from langchain.llms import GooglePalm
# from langchain.llms import VertexAI


# #Keep personal api keys private


from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm

llm = GooglePalm(google_api_key = "AIzaSyD1mO8UehBXGRKVjpD_ztFZYVw3W5Apzxk")
llm.temperature = 0.1
print(llm.predict("Does verizon sell apple phones?"))
