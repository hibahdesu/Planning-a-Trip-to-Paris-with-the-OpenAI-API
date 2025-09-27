# Paris Tourist Chatbot

A simple chatbot built with the OpenAI API that helps answer common tourist questions about Paris.  
It demonstrates how to use the `chat.completions` endpoint with a predefined conversation flow.

## ✨ Features
- Uses the OpenAI Chat API (`gpt-4o-mini`).
- Provides tourist information about:
  - Distance between the Eiffel Tower and the Louvre.
  - Location of the Arc de Triomphe.
  - Must-see artworks at the Louvre Museum.
- Demonstrates conversation handling with roles (`system`, `user`, `assistant`).


## 📦 Requirements
- Python 3.9+
- [OpenAI Python library](https://pypi.org/project/openai/)

Install dependencies with:
```bash
pip install openai



---

### 4. Setup & Running
```markdown
## 🚀 Setup & Running

1. Clone the repository:
```bash
git clone https://github.com/your-username/paris-tourist-chatbot.git
cd paris-tourist-chatbot


export OPENAI_API_KEY="your_api_key_here"   # Mac/Linux
setx OPENAI_API_KEY "your_api_key_here"     # Windows


python chatbot.py


---

### 5. Example Output
```markdown
## 💬 Example Conversation

**User:** How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?  
**Assistant:** The driving distance between the Eiffel Tower and the Louvre is about 3 miles (around 4.8 kilometers).  

**User:** Where is the Arc de Triomphe?  
**Assistant:** The Arc de Triomphe is located at the western end of the Champs-Élysées, on Place Charles de Gaulle in Paris.  

**User:** What are the must-see artworks at the Louvre Museum?  
**Assistant:** Some must-see artworks at the Louvre include the Mona Lisa, the Venus de Milo, the Winged Victory of Samothrace, Liberty Leading the People, and The Coronation of Napoleon.


## 📁 Project Structure

.
├── chatbot.py       # Main script with the conversation logic
├── README.md        # Project documentation


