import logging
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS  # Updated import
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)

class GeminiQABot:
    def __init__(self, file_path, google_api_key):
        self.file_path = file_path
        self.qa = None
        os.environ["GOOGLE_API_KEY"] = google_api_key
        self.initialize_bot()

    def initialize_bot(self):
        logging.debug("Initializing bot...")
        
        # Read and process the text file
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            logging.debug("Text file loaded successfully.")
        except Exception as e:
            logging.error(f"Error reading the text file: {e}")
            return

        # Split text into chunks
        try:
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
            )
            texts = text_splitter.split_text(text)
            logging.debug(f"Text split into {len(texts)} chunks.")
        except Exception as e:
            logging.error(f"Error during text splitting: {e}")
            return
        
        # Create Gemini embeddings and vector store
        try:
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            docsearch = FAISS.from_texts(texts, embeddings)
            logging.debug("Vector store created successfully.")
        except Exception as e:
            logging.error(f"Error during vector store creation: {e}")
            return
        
        # Create QA chain with Gemini Free model (if available)
        try:
            self.qa = RetrievalQA.from_chain_type(
                llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro"),  # Use the free model
                chain_type="stuff",
                retriever=docsearch.as_retriever(),
                return_source_documents=True
            )
            logging.debug("QA chain initialized successfully.")
        except Exception as e:
            logging.error(f"Error during QA chain initialization: {e}")
            return

    def ask(self, question):
        if not self.qa:
            return "Bot not initialized properly"

        logging.debug(f"Asking question: {question}")
        try:
            result = self.qa({"query": question})
            return f"Answer: {result['result']}\nSource: {result['source_documents'][0].page_content}"
        except Exception as e:
            logging.error(f"Error during QA execution: {e}")
            return "There was an error processing your question."

# Usage example
if __name__ == "__main__":
    # Initialize bot with your text file and Google API key
    bot = GeminiQABot(
        file_path="scraped_docs.txt",
        google_api_key="AIzaSyBLJljSU18ph_MbVOjzdENY2fVo1BZo4Zw"  # Use your actual Google API key
    )
    
    while True:
        question = input("\nAsk a question (type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        response = bot.ask(question)
        print(response)