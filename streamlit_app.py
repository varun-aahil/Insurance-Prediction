import json
from urllib import error, request

import streamlit as st


DEFAULT_API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(page_title="Insurance Predictor")
st.title("Insurance Prediction")
st.write("Enter the user details below and submit to get a prediction.")


with st.form("prediction_form"):
    age = st.number_input("Age", min_value=1, max_value=119, value=30, step=1)
    sex = st.selectbox("Sex", ["female", "male"])
    bmi = st.number_input("BMI", min_value=0.1, max_value=49.9, value=25.0, step=0.1)
    children = st.number_input("Children", min_value=0, max_value=9, value=0, step=1)
    smoker = st.selectbox("Smoker", ["no", "yes"])
    region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])
    api_url = st.text_input("API URL", value=DEFAULT_API_URL)
    submitted = st.form_submit_button("Predict")


if submitted:
    payload = {
        "age": int(age),
        "sex": sex,
        "bmi": float(bmi),
        "children": int(children),
        "smoker": smoker,
        "region": region,
    }

    req = request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))
        st.success(f"Predicted insurance cost: {result['prediction']:.2f}")
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        st.error(f"Request failed with status {exc.code}")
        st.code(details)
    except error.URLError as exc:
        st.error(f"Could not reach the API: {exc.reason}")
    except Exception as exc:
        st.error(f"Something went wrong: {exc}")
