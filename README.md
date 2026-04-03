# Insurance Prediction

A simple end-to-end machine learning project that predicts medical insurance charges from user details such as age, sex, BMI, number of children, smoking status, and region.

This repository includes:

- A trained `scikit-learn` model saved as `model.pkl`
- A `FastAPI` backend for serving predictions
- A basic `Streamlit` frontend with a form for user input
- A training notebook showing how the model was built

## Project Overview

The goal of this project is to take common user information and estimate insurance charges using a machine learning pipeline.

The model uses:

- Feature engineering with a derived `lifestyle_risk` field
- One-hot encoding for categorical variables
- Standard scaling for numeric variables
- A `RandomForestRegressor` for prediction

## Features

- Predict insurance charges through an API
- Minimal frontend built with Streamlit
- Clean separation between model, backend, and frontend
- Notebook included for training and experimentation

## Tech Stack

- Python
- FastAPI
- Streamlit
- Pandas
- Scikit-learn
- Pydantic

## Project Structure

```text
Insurance-prediction/
|-- main.py                  # FastAPI backend
|-- streamlit_app.py         # Streamlit frontend
|-- model.pkl                # Trained ML model
|-- Insurance_Premium.ipynb  # Training and experimentation notebook
|-- requirements.txt         # Project dependencies
`-- README.md                # Project documentation
```

## How It Works

The backend accepts the following input fields:

- `age`
- `sex`
- `bmi`
- `children`
- `smoker`
- `region`

From these inputs, the app also computes a derived feature called `lifestyle_risk`, which is then passed into the trained model before making a prediction.

## API Endpoint

### `POST /predict`

Send JSON data like this:

```json
{
  "age": 30,
  "sex": "male",
  "bmi": 24.5,
  "children": 1,
  "smoker": "no",
  "region": "southwest"
}
```

Example response:

```json
{
  "prediction": 3317.72
}
```

## Running the Project Locally

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Start the FastAPI backend

```powershell
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### 4. Start the Streamlit frontend

In another terminal:

```powershell
streamlit run streamlit_app.py
```

The frontend will open in your browser and send requests to the FastAPI backend.

## Model Training

The training workflow is included in `Insurance_Premium.ipynb`.

The notebook covers:

- Loading the dataset
- Creating the `lifestyle_risk` feature
- Splitting data into training and testing sets
- Comparing models
- Training a Random Forest regressor
- Saving the final trained model to `model.pkl`

Note: the notebook currently references the dataset from a Colab-style path. If you want to retrain the model locally, update the dataset path inside the notebook.

## Notes

- The frontend is intentionally minimal and meant for testing the model quickly
- The backend expects the API to be running before the Streamlit form is used
- The repository includes the trained model, so you can use the app without retraining

## Future Improvements

- Better UI styling
- Model evaluation metrics in the README
- Docker support
- Deployment to Streamlit Community Cloud or Render
- Better validation and error handling

## Author

Built as a machine learning + deployment practice project using FastAPI and Streamlit.
