pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t password-checker-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f password-checker-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name password-checker-container password-checker-app'
            }
        }
    }
}