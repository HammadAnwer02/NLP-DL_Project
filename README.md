# NLP-DL Library Chatbot 🚀  

Welcome to the **NLP-DL Library Chatbot**! This project features an AI-powered chatbot designed to help university students navigate and retrieve contextual information from their online library. With cutting-edge NLP and deep learning techniques, the chatbot provides an intuitive and efficient way to explore a vast collection of books.  

## Table of Contents 📚  
1. [Overview](#overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Setup Instructions](#setup-instructions)  
5. [Usage](#usage)  
6. [File Structure](#file-structure)  
7. [Screenshots](#screenshots)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Acknowledgments](#acknowledgments)  

## Overview 

The **NLP-DL Library Chatbot** leverages a **Retrieval-Augmented Generation (RAG)** model paired with a **Large Language Model (LLM)** to deliver precise, contextually relevant responses to user queries. By integrating the **Groq API** and advanced retrieval techniques, this chatbot allows students to interact effortlessly with the university library's digital collection.  

Key highlights include:  
- Seamless access to detailed book information and academic references.  
- Contextual answers tailored to user queries.  
- Scalable and intuitive design for both developers and users.  

---

## Features  
- **Contextual Question Answering**: Retrieve accurate information about books, authors, and academic topics.  
- **Dynamic Retrieval System**: Combines retrieval with generation for optimal performance.  
- **Streamlined UI**: User-friendly interface powered by Streamlit.  
- **Scalability**: Designed for future expansion and integration with other systems.  

---

## Technologies Used 🛠️  
- **Python 3.9+**: Core programming language for RAG and LLM integration.  
- **Selenium**: Web scraping to extract relevant library data.  
- **Hugging Face Transformers**: Pre-trained RAG models for retrieval and generation.  
- **Groq API**: Provides advanced LLM capabilities for natural language understanding.  
- **Streamlit**: Framework for building an interactive chatbot interface.  

---

## Setup Instructions  

### Prerequisites:  
- Python 3.9 or higher installed on your system.  
- **ChromeDriver** (required for Selenium-based scraping).  
- A valid **Groq API key** for LLM functionality.  
- Streamlit installed (via `requirements.txt`).  

## Steps:  

1.	Clone the repository:

> git clone https://github.com/HammadAnwer02/NLP-DL_Project.git && cd NLP-DL_Project  

2.	Install dependencies:

> pip install -r requirements.txt  

3.	Create a .env file and include your GROQ API keys:
	
> GROQ_API_KEY=your_groq_api_key

4. Scrap data from GIKI's Library:

> python3 libextract.py

5.	Run the application:

> streamlit run frontend.py

6.	Open your browser and navigate to (or the URL provided by streamlit):

> http://localhost:8501/ 



## Usage 
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

## Contributing 

# Contributions are welcome! If you’d like to contribute to the project:

1.	Fork this repository.
2.	Create a new branch:

> git checkout -b feature/your-feature-name

3.	Commit your changes:

> git commit -m "Add your message here"

4.	Push the branch:

> git push origin feature/your-feature-name

5.	Create a pull request.

## License 

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to:
	•	Hugging Face for their state-of-the-art transformers.
	•	Groq for providing LLM capabilities.
	•	GIK Institute for their support in facilitating this project.
