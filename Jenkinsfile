pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -e ".[dev]"'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m black --check src tests'
                sh 'python3 -m isort --check-only src tests'
                sh 'python3 -m pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Dummy deploy stage: no deployment configured.'
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}
