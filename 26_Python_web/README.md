# 30 Days of Python – Day 26: Python Web with Flask

This is a simple text analyzer web application built using **Flask**, a lightweight Python web framework.
It allows users to input text, submit it, and view basic analysis such as character count, word count, sentence count, and the most frequently used word.

## Why I Did Not Use Heroku

I chose **not to deploy this app on Heroku** for simple, practical reasons:

- **No Account Required**: I didn't want to create another online account for something that runs perfectly locally
- **Zero Configuration Needed**: No need for additional files like `Procfile`, `requirements.txt`, or CLI tools
- **Instant Access**: Local deployment provides immediate results without internet dependency
- **Privacy First**: Keeping the project local means my data stays on my machine

✅ **This app works 100% locally** and demonstrates all Flask concepts without any external services.

---

## ✨ Features Implemented

- ✅ **Home Page** (`/`) – Welcome page with tech stack list
- ✅ **About Page** (`/about`) – Information about the course
- ✅ **Text Analyzer Page** (`/post`) – Form to input text
- ✅ **Results Page** (`/result`) – Displays analyzed text statistics
- ✅ **Template Inheritance** – Uses `layout.html` to avoid repetition
- ✅ **Static File Serving** – Includes CSS styling via Flask’s `url_for()`
- ✅ **Form Handling** – Processes user input using POST method

---

## 📁 Project Structure
```bash 
26_Python_web/
│
├── app.py
├── static/
│   └── css/
│       └── main.css
└── templates/
    ├── layout.html
    ├── home.html
    ├── about.html
    ├── post.html
    └── result.html
```

---

## 🔧 How to Run the App

1. **Install Flask** (if not already installed):
   ```bash
   pip install flask
   ```

2. Navigate to your project directory: 
    ```bash
    cd path/to/your/project
    ```

3. Run the app:
    ```bash
    python app.py
    ```

4. Open in browser:
    ```bash
    http://localhost:5000
    ```



## 📊 Text Analysis Features

The app analyzes the submitted text and displays:
- **Character Count** – Total number of characters
- **Word Count** – Number of words (split by whitespace)
- **Sentence Count** – Based on `.`, `!`, `?`
- **Most Frequent Word** – Case-insensitive, stripped of punctuation
