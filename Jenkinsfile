pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')  // Vérifie les mises à jour Git toutes les 5 minutes
    }
    stages {
        stage('Installer Dépendances') {
            steps {
               sh 'python -m pip install -r requirements.txt'
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
                sh 'docker tag port-scanner error-413/port-scanner:latest'
                sh 'docker push error-413/port-scanner:latest'
            }
        }
    }
}

