pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Rishabhdew/scientific-calculator-devops.git'
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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo $DOCKER_PASS | /usr/local/bin/docker login -u $DOCKER_USER --password-stdin
                    /usr/local/bin/docker push rish9981/scientific-calculator
                    '''
                }
            }
        }

    }

    post {
        success {
            emailext (
                subject: "SUCCESS: Build ${env.BUILD_NUMBER}",
                body: "Jenkins pipeline completed successfully.",
                to: "rish9981.dewangan@gmail.com"
            )
        }

        failure {
            emailext (
                subject: "FAILED: Build ${env.BUILD_NUMBER}",
                body: "Jenkins pipeline failed.",
                to: "rish9981.dewangan@gmail.com"
            )
        }
    }
}
