import streamlit as st
import requests

# ---------- Utilities for styling ----------

def set_gradient_background():
    """
    Adds a CSS block to create a gradient background from navy blue to off-white.
    """
    st.markdown(
        """
        <style>
        .stApp {
          background: linear-gradient(to bottom right, #001F3F, #F8F8F8);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def get_weather_by_city(city_name):
    """
    Use geocoding to find lat/lon, then call Open-Meteo forecast API.
    Returns dict or None on error.
    """
    # First, use a geocoding API to convert city name → latitude & longitude.
    # We can use e.g. Open-Meteo’s free geocoding endpoint.
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    geo_resp = requests.get(geo_url, params=params)
    if geo_resp.status_code != 200:
        return None
    geo_data = geo_resp.json()
    results = geo_data.get("results")
    if not results:
        return None
    lat = results[0]["latitude"]
    lon = results[0]["longitude"]
    # Now call Open-Meteo forecast / current weather endpoint
    weather_url = "https://api.open-meteo.com/v1/forecast"
    wparams = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "hourly": "relative_humidity_2m",
        # you can ask for more fields if you like
        "timezone": "auto",
    }
    wresp = requests.get(weather_url, params=wparams)
    if wresp.status_code != 200:
        return None
    wdata = wresp.json()
    return {
        "city": results[0]["name"],
        "latitude": lat,
        "longitude": lon,
        "current": wdata.get("current_weather"),
        "hourly": wdata.get("hourly"),
    }


# ---------- Quiz Data ----------

quiz_questions = [
    {
        "question": "What gas is the primary driver of recent climate change?",
        "choices": ["Nitrogen", "Carbon Dioxide", "Oxygen", "Helium"],
        "answer": "Carbon Dioxide",
        "explanation": "CO₂ emissions from burning fossil fuels have increased greenhouse effect.",
    },
    {
        "question": "Which layer of the atmosphere contains most of Earth’s weather?",
        "choices": ["Mesosphere", "Stratosphere", "Troposphere", "Thermosphere"],
        "answer": "Troposphere",
        "explanation": "The troposphere, the lowest layer, is where most weather happens.",
    },
    {
        "question": "Which phenomenon causes nights to be warmer in cities than rural areas?",
        "choices": ["Urban Heat Island", "Ozone Layer", "Volcanic Ash", "Green Flash"],
        "answer": "Urban Heat Island",
        "explanation": "Concrete and infrastructure absorb heat and slow cooling at night.",
    },
    {
        "question": "What is relative humidity a measure of?",
        "choices": ["Amount of water vapor in the air vs. maximum possible at that temp",
                    "Absolute humidity", "Rainfall amount", "Wind moisture"],
        "answer": "Amount of water vapor in the air vs. maximum possible at that temp",
        "explanation": "Relative humidity is the current vapor amount divided by max at that temperature.",
    },
    {
        "question": "Which of these is a feedback loop that **accelerates** warming?",
        "choices": ["Ice albedo feedback", "Cloud cover increasing", "More volcanic eruptions", "More aerosols"],
        "answer": "Ice albedo feedback",
        "explanation": "Melting ice reduces reflectivity, causing more absorption of sunlight, speeding warming.",
    },
    {
        "question": "Which region is warming faster than the global average?",
        "choices": ["Tropics", "Equator", "Polar regions", "Temperate zones"],
        "answer": "Polar regions",
        "explanation": "Arctic and Antarctic are warming disproportionately (polar amplification).",
    },
    {
        "question": "What human activity is the largest source of CO₂ emissions?",
        "choices": ["Deforestation", "Air travel", "Electricity & heat production", "Livestock farming"],
        "answer": "Electricity & heat production",
        "explanation": "Burning fossil fuels for electricity/heat is the top CO₂ emitter sector.",
    },
]

# ---------- Main App ----------

def main():
    st.set_page_config(page_title="Weather & Climate Quiz App", layout="centered")
    set_gradient_background()

    st.title("🌦️ Weather + Climate Quiz App")

    # Tabbed layout: Weather vs Quiz
    tab1, tab2 = st.tabs(["Weather", "Quiz"])

    with tab1:
        st.header("Check Live Weather")
        city_input = st.text_input("Enter a city:", placeholder="e.g. Toronto")
        if st.button("Get Weather"):
            if not city_input.strip():
                st.error("Please enter a city name.")
            else:
                info = get_weather_by_city(city_input.strip())
                if info is None or info.get("current") is None:
                    st.error("Could not find weather for that city. Try another one.")
                else:
                    cur = info["current"]
                    temp = cur.get("temperature")
                    wind = cur.get("windspeed")
                    # humidity is in hourly list; match time index
                    humidity = None
                    # note: hourly has many arrays; we try find humidity corresponding to current time
                    hourly = info.get("hourly")
                    if hourly:
                        hums = hourly.get("relative_humidity_2m")
                        times = hourly.get("time")
                        # find index where time matches current
                        if times and cur.get("time") in times:
                            idx = times.index(cur["time"])
                            humidity = hums[idx]
                    st.markdown(
                        f"""
                        <div style='padding: 20px; border-radius:10px; background: rgba(255,255,255,0.8);'>
                          <h3>{info['city']}</h3>
                          <p>🌡️ Temperature: <b>{temp}°C</b></p>
                          <p>💧 Humidity: <b>{humidity if humidity is not None else '?'}%</b></p>
                          <p>💨 Wind speed: <b>{wind} m/s</b></p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    with tab2:
        st.header("Weather & Climate Quiz")
        # We'll store in session_state: index, score, user_answers, show_results
        if "q_index" not in st.session_state:
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.user_answers = []
            st.session_state.show_results = False

        if not st.session_state.show_results:
            qidx = st.session_state.q_index
            q = quiz_questions[qidx]
            st.subheader(f"Question {qidx + 1} / {len(quiz_questions)}")
            st.write(q["question"])
            choice = st.radio("Choose one:", q["choices"], key=f"radio_{qidx}")

            if st.button("Submit"):
                st.session_state.user_answers.append(choice)
                if choice == q["answer"]:
                    st.session_state.score += 1
                st.session_state.q_index += 1

                if st.session_state.q_index >= len(quiz_questions):
                    st.session_state.show_results = True

                # To force re-render
                st.rerun()

        else:
            # Show results
            st.subheader("Your Results 🎉")
            total = len(quiz_questions)
            score = st.session_state.score
            st.write(f"You scored **{score} / {total}**")

            st.write("---")
            # Show each question, user answer, correct, explanation
            for i, q in enumerate(quiz_questions):
                user_ans = st.session_state.user_answers[i]
                correct = q["answer"]
                st.write(f"**Q{i+1}. {q['question']}**")
                st.write(f"Your answer: {user_ans}")
                if user_ans == correct:
                    st.success("✅ Correct")
                else:
                    st.error(f"❌ Wrong — correct answer: {correct}")
                    st.write(f"*Explanation:* {q['explanation']}")
                st.write("")

            if st.button("Restart Quiz"):
                # Reset
                st.session_state.q_index = 0
                st.session_state.score = 0
                st.session_state.user_answers = []
                st.session_state.show_results = False
                st.rerun()



if __name__ == "__main__":
    main()
