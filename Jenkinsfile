pipeline {
    agent any
    stages
    {
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                sh "docker build -t libraryapp:v1 ."
            }
        }
        stage('Run Selenium Tests') {
            steps {
                echo "Run Selenium Tests"
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 app.py &'
                sh 'sleep 5'
                sh 'python3 -m pytest -v'
                
            }
        }
        stage('Docker Login') {
            steps {
                sh 'docker login -u shreyachundi -p Karthikeya@011'
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                sh "docker tag libraryapp:v1 shreyachundi/library-app:new"
                sh "docker push shreyachundi/library-app:new"
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml --validate=false'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}