# Multi-Mode Chatbot


## Overview

The Multi-Mode Chatbot is a versatile conversational AI tool that can generate responses using multiple APIs. Built using Streamlit, this multi-page application offers a minimal and straightforward user interface. It leverages the OpenAI and Google GenerativeAI APIs to provide intelligent and context-aware responses. Whether you need a chatbot for customer support, knowledge base, or just casual conversation, this project has you covered.

## App Link:
To access the application click [here](https://basicchatbot-openai-palm.streamlit.app)

## Key Features

### Multi-Page Streamlit Application

- A **multi-page Streamlit application** with a clean and intuitive interface that's easy for users to navigate.

### OpenAI and Google GenerativeAI Integration

- Utilizes the **OpenAI API** and **Google GenerativeAI API** to generate responses, ensuring diverse and context-aware interactions.

### Minimal User Interface

- Provides a **minimal and simple user interface** for a seamless and hassle-free chatbot experience.

## Prerequisites

Before using the application, ensure you have the following prerequisites:

- **Python**: Make sure you have Python installed on your system.
- **Streamlit**: Install Streamlit using pip or your preferred package manager.
- **OpenAI API Key**: Obtain an API key for the OpenAI API.
- **Google GenerativeAI API Key**: Obtain an API key for the Google GenerativeAI API.
- **Other Dependencies**: Install other libraries specified in the `requirements.txt` file.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/AnkitBaliyan1/BasicChatBot.git
   cd BasicChatBot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   To run the base version - single mode
   ```bash
   streamlit run ver-2.0.py
   ```

   To run the upgraded version - multimodel
   ```bash
   streamlit run app-Google-API.py
   ```

4. Access the chatbot through your web browser (usually at http://localhost:8501).

## Usage

1. **Select API Mode**: Choose between OpenAI or Google GenerativeAI to power your chatbot responses.

2. **Chat**: Start a conversation with the chatbot by typing messages in the input field.

3. **Receive Responses**: The chatbot will generate responses based on your input and the selected API.

## Use Cases

- **Customer Support**: Provide automated customer support with context-aware responses.
- **Knowledge Base**: Build a knowledge base chatbot that answers questions and provides information.
- **Casual Conversation**: Create a chatbot for fun and engaging interactions with users.

## Contact

For inquiries, suggestions, or assistance, please feel free to contact Ankit Baliyan at [a.baliyan008@gmail.com](mailto:a.baliyan008@gmail.com).

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
