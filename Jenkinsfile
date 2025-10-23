pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
        PATH = "${VENV_DIR}/bin:${env.PATH}"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
                echo "📦 Checked out code from GitHub"
            }
        }

        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo "🐍 Virtual environment ready and dependencies installed"
            }
        }

        stage('Static Code Analysis') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 src/
                '''
                echo "🔍 Linting completed"
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ --maxfail=1 --disable-warnings -q
                '''
                echo "🧪 Unit tests executed"
            }
        }

        stage('Build & Package') {
            steps {
                echo "📦 Build & Package stage (optional for Python)"
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', allowEmptyArchive: true
                echo "📂 Artifacts archived"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed! Check logs for details."
        }
    }
}
