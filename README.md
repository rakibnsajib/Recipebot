# 🍽️ RecipeBot - AI Chef Assistant
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq%20AI-FF6B35?style=flat-square)](https://groq.com/)
[![GitHub issues](https://img.shields.io/github/issues/rakibnsajib/Recipebot?style=flat-square)](https://github.com/rakibnsajib/Recipebot/issues)


RecipeBot is an intelligent recipe generator that helps you create delicious recipes based on your available ingredients and dietary preferences. Using the power of AI through Groq's Llama model, it provides personalized recipe suggestions with detailed instructions.

## ✨ Features

- **Ingredient-based Recipe Generation**: Input your available ingredients and get customized recipes
- **Dietary Preferences**: Specify dietary restrictions or preferences (vegetarian, vegan, gluten-free, etc.)
- **AI-Powered**: Uses Groq's Llama3-8b model for intelligent recipe generation
- **User-Friendly Interface**: Clean Streamlit frontend for easy interaction
- **RESTful API**: Flask backend with JSON API endpoints

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: Streamlit
- **AI Model**: Groq Llama3-8b-8192
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.7 or higher
- Groq API key (sign up at [Groq](https://groq.com/))

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/rakibnsajib/Recipebot.git
   cd Recipebot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your Groq API key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🏃‍♂️ Running the Application

### Start the Backend Server

```bash
python backend.py
```

The Flask API will start running on `http://127.0.0.1:5000`

### Start the Frontend (in a new terminal)

```bash
streamlit run fronted.py
```

The Streamlit app will open in your browser at `http://localhost:8501`

## 📡 API Endpoints

### POST /get_recipe

Generate a recipe based on ingredients and preferences.

**Request Body:**

```json
{
  "ingredients": "chicken, rice, vegetables",
  "preference": "spicy, Asian-style"
}
```

**Response:**

```json
{
  "recipe": "Generated recipe with detailed instructions..."
}
```

## 🎯 Usage

1. Open the Streamlit interface in your browser
2. Enter your available ingredients (comma-separated)
3. Optionally specify dietary preferences or restrictions
4. Click "Get Recipe" to generate your personalized recipe
5. Enjoy cooking your AI-generated meal!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing the AI inference API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Flask](https://flask.palletsprojects.com/) for the lightweight backend

## 🐛 Issues

If you encounter any issues or have suggestions for improvements, please feel free to [open an issue](https://github.com/rakibnsajib/Recipebot/issues).

---

Happy Cooking! 👨‍🍳👩‍🍳
