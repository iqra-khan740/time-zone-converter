# ⏰ Timezone Log Converter

A simple **Flask + HTML/CSS/JS** web app to convert UTC logs into 5
timezones available in the project.

------------------------------------------------------------------------

## 🚀 Features

-   Paste logs in ``YYYY-MM-DD HH:MM:SS`` UTC format.
-   Select target timezone (e.g., Asia/Karachi, Europe/London) from dropdown menu.
-   Convert instantly with Flask backend.
-   Responsive frontend with modern dark theme.

------------------------------------------------------------------------

## 📂 Project Structure

    time-zone-converter/
    │── Backend/
    │   ├── app.py              # Flask backend
    │   ├── requirements.txt    # Dependencies
    │
    │── frontend/
    │   ├── index.html          # UI template
    │   ├── static/
    │       ├── style.css       # Stylesheet
    │       ├── script.js       # Frontend JS
    │
    │── Dockerfile              # Docker setup
    │── Procfile                # Railway process file
    │── .dockerignore
    │── README.md

------------------------------------------------------------------------

## 🛠️ Installation (Local Setup)

1.  Clone repo:

    ``` sh
    git clone https://github.com/iqra-khan740/time-zone-converter.git
    cd time-zone-converter
    ```

2.  Create virtual environment & install dependencies:

    ``` sh
    python -m venv .venv
    source .venv/bin/activate   # On Windows: .venv\Scripts\activate
    pip install -r Backend/requirements.txt
    ```

3.  Run Flask app:

    ``` sh
    cd Backend
    python app.py
    ```

4.  Open browser:

        http://127.0.0.1:5000

------------------------------------------------------------------------

## 🐳 Run with Docker

1.  Build image:

    ``` sh
    docker build -t timezone-app .
    ```

2.  Run container:

    ``` sh
    docker run -p 8080:8080 timezone-app
    ```

3.  Open:

        http://localhost:8080

------------------------------------------------------------------------