pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')  // Vérifie le repo Git toutes les 5 min
    }
    stages {

        }
        stage('Installer Dépendances') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Docker') {
            steps {
                sh 'docker build -t port-scanner .'
            }
        }
        stage('Push Image Docker') {
            steps {
                sh 'docker tag port-scanner nasdas330/port-scanner:latest'
                sh 'docker push nasdas330/port-scanner:latest'
            }
        }
    }
}
