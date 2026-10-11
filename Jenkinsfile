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