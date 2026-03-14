pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Rishabhdew/scientific-calculator-devops.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }

        stage('Build Docker Image') {
    steps {
        sh '/usr/local/bin/docker build -t rish9981/scientific-calculator .'
    }
}

stage('Push Docker Image') {
    steps {
        sh '/usr/local/bin/docker push rish9981/scientific-calculator'
    }
}

    }
}
