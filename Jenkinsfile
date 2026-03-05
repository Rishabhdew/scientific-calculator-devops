pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/username/scientific-calculator-devops.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t scientific-calculator .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker tag scientific-calculator username/scientific-calculator'
                sh 'docker push username/scientific-calculator'
            }
        }
    }
}
