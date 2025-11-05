# 🌦️ Global Weather & Climate Quiz App

A fun and interactive **Python + Streamlit** app that lets you:

* Check **live weather data** for any city in the world 🌍
* Learn about the climate with a **7-question quiz** on weather and climate change ☀️❄️🌪️
* Enjoy a **beautiful navy-to-off-white gradient design**, friendly emojis, and live feedback.

---

## 🧪 Features

✅ **Live Weather Data** – Uses the free [Open-Meteo API](https://open-meteo.com/) to get current temperature, wind speed, and location info.
✅ **Error Handling** – If the city isn’t found, the app shows a clear message instead of crashing.
✅ **Climate Quiz** – A fun 7-question multiple-choice quiz with instant feedback and explanations.
✅ **Randomized Questions** – Quiz order changes every time you restart!
✅ **Beautiful UI** – Gradient background, custom button colors, and clean layout.

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

Make sure you have **Python 3.9+** installed.
Then open your terminal or command prompt and install Streamlit + Requests:

```bash
pip install streamlit requests
```

---

### 2️⃣ Save the App File

Create a new file called `weather_app.py`, and copy the app code into it.
(Or rename your file if you’ve already made it.)

---

### 3️⃣ Run the App

In the same folder where the file is saved, run:

```bash
streamlit run weather_app.py
```

This will open your app in your browser (usually at [http://localhost:8501](http://localhost:8501)).

---

## 💡 How to Use

1. Type any **city name** (e.g., Toronto, London, Tokyo) into the input box.
2. The app will display:

   * 🌡️ Current temperature
   * 🌬️ Wind speed
   * 🌍 Country name
3. Scroll down to the **Climate & Weather Quiz** section and click **Start Quiz**.
4. Answer the 7 questions — you’ll get instant feedback!
5. At the end, your **score** will be shown and you can restart to try again.

---

## ⚙️ Code Overview

| Section             | Purpose                                                               |
| ------------------- | --------------------------------------------------------------------- |
| **Imports**         | Imports necessary Python modules (`streamlit`, `requests`, `random`). |
| **CSS Styling**     | Adds gradient background and button colors using HTML/CSS.            |
| **`get_weather()`** | Uses the Open-Meteo API to fetch live weather data by city.           |
| **Main Page**       | Displays welcome text, weather info, and quiz section.                |
| **Quiz Logic**      | Handles question order, answer checking, score tracking, and restart. |

---

## 🌈 Design Details

* **Gradient background:** Navy Blue → Off White
* **Font color:** White for clear contrast
* **Buttons:** Rounded corners with hover animation
* **Icons/Emojis:** Used to make the app friendly and visually engaging

---

## 🧠 Example Quiz Topics

* Greenhouse gases
* Weather tools (like thermometers)
* Rain, clouds, and seasons
* Actions to help stop climate change

---

## 🧮 Future Improvements

* Add weather icons (☀️🌧️❄️) dynamically from API
* Show 3-day forecast
* Store favorite cities
* Leaderboard for quiz scores
* Add sound effects or animations 🎵

---

## 👨‍💻 Author

**Developed by:** Mofiyinfoluwa Salisu
**Powered by:** [Streamlit](https://streamlit.io) + [Open-Meteo API](https://open-meteo.com/)

---

## 📜 License

This project is free to use for educational and non-commercial purposes.
