📌 Overview

This project is an AI-powered chatbot that uses Google Gemini AI and FAISS to provide intelligent responses based on scraped documentation data. The chatbot loads text from a file, indexes it using embeddings, and allows users to query it for answers.

🌟 Features

✔️ Conversational AI powered by Google Gemini AI.✔️ Efficient document retrieval with FAISS vector search.✔️ Real-time Q&A based on extracted documentation.✔️ Simple command-line interaction for easy usage.✔️ Logs errors and processes for debugging.

🔧 Requirements

Ensure you have the following dependencies installed:

pip install selenium beautifulsoup4 webdriver-manager langchain langchain-google-genai faiss-cpu

🚀 Quick Start

1️⃣ Clone the repository:

git clone https://github.com/Kunal-bot235/Chatbot.git
cd Chatbot

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run the chatbot:

python chatbot.py

⚙️ Configuration

The chatbot reads from a text file (scraped_docs.txt) and initializes a FAISS vector store with Google Gemini AI embeddings. Ensure the file path is correctly set in GeminiQABot initialization:

bot = GeminiQABot(
    file_path="scraped_docs.txt",
    google_api_key="YOUR_GOOGLE_API_KEY"
)

Replace YOUR_GOOGLE_API_KEY with a valid API key from Google.

🎯 How It Works

1️⃣ Loads text from scraped_docs.txt and splits it into chunks.2️⃣ Generates embeddings using Google Generative AI.3️⃣ Stores embeddings in a FAISS vector database.4️⃣ Uses retrieval-based question answering to respond to user queries.

📝 Example Usage

Ask a question (type 'exit' to quit): What is Lytics?
Answer: Lytics is a customer data platform that...
Source: Lytics Documentation

❗ Troubleshooting

If you encounter Google API key errors, ensure your API key is valid and set correctly in the environment variables.

If you get large file errors, consider using Git Large File Storage (LFS):

git lfs track "*.txt"
git add .gitattributes scraped_docs.txt
git commit -m "Enable LFS for large files"


🤖 Enjoy chatting with Gemini AI! 🚀





