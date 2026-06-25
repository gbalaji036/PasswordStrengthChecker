# 🔐 PasswordStrengthChecker

A Flask-based web application that evaluates password strength and demonstrates a practical **DevOps workflow** using **Git, Jenkins, and Docker**. This project was built as an academic example of **CI/CD, containerization, and repeatable local deployment**. 

## ✨ Features

- Check password strength through a simple browser-based interface. 
- Validate passwords using basic rules such as:
  - minimum length, 
  - uppercase letters, 
  - lowercase letters, 
  - numbers, 
  - special characters. 
- Automate build and deployment workflow using Jenkins. 
- Containerize the application with Docker for consistent execution across environments.
- Maintain version history and collaboration workflow using Git and GitHub. 

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **DevOps:** Jenkins, Docker 
- **Version Control:** Git, GitHub 
- **Frontend:** HTML templates 

## 🎯 Project Objective

The aim of this project is not only to build a password checker, but also to demonstrate how a simple web application can be integrated into a complete DevOps workflow. The project shows how source control, automation, and containerization work together to improve reliability, reproducibility, and deployment consistency. 

## 📁 Project Structure

```bash
PasswordStrengthChecker/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .gitignore
└── templates/
```

## ⚙️ How It Works

1. A user enters a password in the web interface. 
2. The Flask backend processes the input and applies validation rules. 
3. The application returns a strength result such as weak, moderate, or strong. 
4. Jenkins automates the build and deployment flow after code updates. 
5. Docker packages the application and its dependencies into a reusable container. 

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/gbalaji036/PasswordStrengthChecker.git
cd PasswordStrengthChecker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in browser

```bash
http://127.0.0.1:5000
```

## 🐳 Run with Docker

### Build the image

```bash
docker build -t password-strength-checker .
```

### Run the container

```bash
docker run -p 5000:5000 password-strength-checker
```

### Open in browser

```bash
http://127.0.0.1:5000
```

## 🔁 Jenkins Pipeline

This repository includes a `Jenkinsfile` to automate the workflow. The pipeline is designed to:

- pull the latest code from GitHub, 
- build the Docker image, 
- run the containerized application. 

This reduces manual effort and ensures that the same build and deployment steps are followed consistently. 

## ✅ Evaluation

The project was considered successful when: 

- the application opened correctly in the browser, 
- password strength validation behaved as expected for different inputs, 
- the Docker container started without errors, and 
- the Jenkins pipeline completed the required automation steps. 

These checks confirmed that the application, container, and automation pipeline were working together correctly. 

## 📌 Why This Project Matters

This project shows how even a small Flask application can be turned into a complete DevOps example using the right tools. It demonstrates important software engineering ideas such as automation, portability, reproducibility, and deployment consistency. 

## 🔮 Future Improvements

- Add entropy-based password scoring. 
- Provide better password suggestions and feedback. 
- Improve the user interface. 
- Add automated testing into the Jenkins pipeline. 
- Add security checks into the CI/CD workflow. 
- Extend deployment from local hosting to a cloud platform.

## 👤 Author

**Balaji Kumar Varma G**  
B.E. Computer Science and Engineering  
BMS Institute of Technology and Management

## 📝 Note

One certificate page in the academic report contains a mismatched title, but the abstract, declaration, implementation, deployment, and evaluation sections consistently describe this project as **Password Strength Checker**. 
