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
                bat 'py -m pip install --upgrade pip'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t password-checker-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f password-checker-container'
                bat 'docker run -d -p 5000:5000 --name password-checker-container password-checker-app'
            }
        }
    }
}pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -m pip install --upgrade pip'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t password-checker-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f password-checker-container'
                bat 'docker run -d -p 5000:5000 --name password-checker-container password-checker-app'
            }
        }
    }
}