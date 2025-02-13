import streamlit as st
import requests

# Flask API URL
FLASK_API_URL = "http://127.0.0.1:5000/get_recipe"

st.title("🍽️ RecipeBot - AI Chef Assistant")

# Ingredients input
ingredients = st.text_area("Enter ingredients (comma-separated)", "")

# Right-aligned Hover Tooltip using HTML & CSS
st.markdown(
    """
    <style>
        .tooltip-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
            color: blue;
            font-weight: bold;
        }
        .tooltip .tooltip-text {
            visibility: hidden;
            width: 250px;
            background-color: #f1f1f1;
            color: black;
            text-align: left;
            padding: 8px;
            border-radius: 5px;
            position: absolute;
            z-index: 1;
            top: 100%;
            right: 0;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip:hover .tooltip-text {
            visibility: visible;
            opacity: 1;
        }
    </style>
    
    <div class="tooltip-container">
        <label style="font-weight: bold;">Enter your dietary preference/restriction:</label>
        <span class="tooltip">❓
            <span class="tooltip-text">
                <b>Dietary Options:</b><br>
                🥦 Vegetarian<br>
                🍖 Non-Vegetarian<br>
                🍞 Gluten-Free<br>
                🥛 Dairy-Free<br>
                🥩 Low-Carb<br>
                🍳 Low-Fat<br>
                🥑 Keto<br>
                🍗 Paleo<br>
                🥜 Nut-Free<br>
                🕌 Halal<br>
                ✡️ Kosher<br>
                ➕ Others (Specify Below)
            </span>
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# Dietary preference input
preference = st.text_input("")

if st.button("Get Recipe"):
    if not ingredients:
        st.warning("⚠️ Please enter ingredients.")
    else:
        st.write("⏳ Fetching recipe...")

        response = requests.post(
            FLASK_API_URL,
            json={
                "ingredients": ingredients,
                "preference": preference
            }
        )

        try:
            data = response.json()
            if "recipe" in data:
                st.success("✅ Recipe Generated!")
                st.write(data["recipe"])
            else:
                st.error(f"❌ Error: {data.get('error', 'Unknown error')}")
        except requests.exceptions.JSONDecodeError:
            st.error("❌ Failed to parse response. Check API logs.")
