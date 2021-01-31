pipeline {
    agent any

    stages {
        stage('Construir') {
            steps {
                echo "          -------------CONSTRUYENDO MI SOFTWARE/CODE"
                echo "          Creando entorno virtual"
                sh 'virtualenv entorno_virtual'
                echo "          Activando el entorno_virtual"
                sh 'source entorno_virtual/bin/activate'
                // echo "          Instalando los requerimientos concretos de este proyecto"
                sh 'pip install -r requirements.txt'
                echo "          Instalando aplicación para testear"
                sh 'pip install pytest'
                echo "           Instalado aplicación/libreria necesaria para este proyecto concreto"
                sh 'pip install flask'
                echo "           Terminando de instalar requerimientos"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }   
}