pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📦 Checking out code from GitHub'
                git branch: 'main', url: 'https://github.com/Srihari5454/Automated-CI-Pipeline.git'
            }
        }

        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                echo '🐍 Setting up Python virtual environment'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Static Code Analysis') {
            steps {
                echo '🔍 Running Flake8 linting'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    # Ensure src exists, otherwise skip to avoid failure
                    if [ -d "src" ]; then
                        flake8 src/
                    else
                        echo "⚠️  src directory not found, skipping linting"
                    fi
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo '🧪 Running Pytest tests'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest --junitxml=results.xml || true
                '''
            }

            post {
                always {
                    echo '📊 Publishing test results'
                    junit 'results.xml'
                }
            }
        }

        stage('Build & Package') {
            when {
                expression { fileExists('src/app.py') }
            }
            steps {
                echo '📦 Building Flask app package'
                sh '''
                    mkdir -p build
                    cp -r src ${VENV_DIR} requirements.txt build/
                    echo "Build completed"
                '''
            }
        }

        stage('Archive Artifacts') {
            when {
                expression { fileExists('build') }
            }
            steps {
                echo '🗂️ Archiving build artifacts'
                archiveArtifacts artifacts: 'build/**/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed! Check logs for details.'
        }
    }
}
