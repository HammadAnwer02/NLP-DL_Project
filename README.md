## NLP-DL Library Chatbot 🚀

Welcome to the NLP-DL Library Chatbot project! This repository contains the implementation of an AI-powered chatbot designed to assist students in navigating and retrieving contextual information from a university’s online library. Using state-of-the-art NLP and deep learning techniques, we provide an intuitive and effective way to access knowledge from a vast collection of books.

## Table of Contents 📚
	1.	Overview
	2.	Features
	3.	Technologies Used
	4.	Setup Instructions
	5.	Usage
	6.	File Structure
	7.	Screenshots
	8.	Contributing
	9.	License

## Overview 📝

The NLP-DL Library Chatbot combines Retrieval-Augmented Generation (RAG) with a Large Language Model (LLM) to provide contextually accurate responses to user prompts. By leveraging the Groq API and advanced NLP techniques, the chatbot accesses and retrieves information specific to the university library’s vast digital collection, ensuring students receive precise and relevant answers.

## Features ✨
	•	Contextual Question Answering: Responds to library-related queries with relevant and accurate information.
	•	Book Retrieval: Scans the library database to provide detailed information about books, authors, and topics.
	•	Dynamic RAG Integration: Combines retrieval and generation capabilities for enhanced performance.
	•	Scalable Design: Built for seamless integration and scalability.

## Technologies Used 🛠️
	•	Python 3.9+: Used for running the RAG Model and connecting to the LLM.
	•	Selenium: For web scraping and library data extraction.
	•	Hugging Face Transformers: Pre-trained models for RAG and NLP tasks.
	•	Groq API: Provides LLM capabilities.
	•	Streamlit: Front-end UI for chatbot communication.
	

## Setup Instructions 🔧

## Prerequisites:
	•	Python 3.9 or higher with requirement libraries installed
	•	ChromeDriver (for Selenium)
	•	Streamlit
    •	Groq API Key
    


## Steps:
	1.	Clone the repository:

git clone https://github.com/HammadAnwer02/NLP-DL_Project.git
cd NLP-DL_Project


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Set up environment variables:
Create a .env file and include your GROQ API keys:

GROQ_API_KEY=your_groq_api_key


	4.	Run the application:

streamlit run frontend.py


	5.	Open your browser and navigate to:

http://localhost:8501/ # Or whatever URL is provided from Streamlit

## Usage 💻
	1.	Enter your query into the chatbot interface.
	2.	The bot retrieves relevant information using the library’s database and responds.
	3.	Review the results and refine your query if necessary.

## File Descriptions

- **`frontend.py`**:  
  Handles the core logic of the application, including:
  - Preprocessing user queries
  - Connecting with the LLM through the Groq API
  - Building the user interface for interaction  

- **`requirements.txt`**:  
  Contains all the dependencies and libraries required to run the project.

- **`libextract.py`**:  
  Implements a Selenium-based web scraper to extract relevant data.

- **`README.md`**:  
  Comprehensive documentation for understanding and setting up the project.

## Contributing 🤝

Contributions are welcome! If you’d like to contribute to the project:
	1.	Fork this repository.
	2.	Create a new branch:

git checkout -b feature/your-feature-name

	3.	Commit your changes:

git commit -m "Add your message here"

	4.	Push the branch:

git push origin feature/your-feature-name

	5.	Create a pull request.

## License 📜

This project is licensed under the MIT License.

## Acknowledgments 🙏

Special thanks to:
	•	Hugging Face for their state-of-the-art transformers.
	•	Groq for providing LLM capabilities.
	•	GIK Institute for their support in facilitating this project.
