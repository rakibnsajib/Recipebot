from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

# Function to get a recipe from Groq LLM
def get_recipe_from_llm(query):
    client = Groq(api_key=GROQ_API_KEY)

    # Construct message format
    messages = [{"role": "user", "content": [{"type": "text", "text": query}]}]

    try:
        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/get_recipe", methods=["POST"])
def get_recipe():
    try:
        data = request.json
        ingredients = data.get("ingredients", "").strip()
        preference = data.get("preference", "").strip()

        if not ingredients:
            return jsonify({"error": "Ingredients are required"}), 400

        # Build query for LLM
        query = f"Give me a recipe using {ingredients}."
        if preference:
            query += f" The recipe should be {preference}."

        result = get_recipe_from_llm(query)
        return jsonify({"recipe": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error as JSON

if __name__ == "__main__":
    app.run(debug=True, port=5000)
