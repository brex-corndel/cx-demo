node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("j3rry99/test")
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'docker-login') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
