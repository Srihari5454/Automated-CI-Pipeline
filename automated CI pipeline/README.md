# Automated CI Pipeline for a Web Application using Jenkins

This project showcases a fully automated **Continuous Integration (CI)** pipeline using **Jenkins** for a Flask-based web app.

### Tech Stack
- Python (Flask)
- Jenkins
- GitHub
- Pytest
- Flake8

### Pipeline Stages
1. **Checkout** – Pull latest code from GitHub.
2. **Install Dependencies** – Install Python libraries.
3. **Static Code Analysis** – Linting via Flake8.
4. **Run Tests** – Unit tests with Pytest.
5. **Build & Package** – Create `.tar.gz` artifact.
6. **Archive Artifacts** – Store build output in Jenkins.

### Setup
1. Install Jenkins on your system.
2. Connect Jenkins with your GitHub repo.
3. Add the provided `Jenkinsfile`.
4. Run the pipeline and view build/test results.

### Expected Output
- Build Artifact → `build/app.tar.gz`
- Jenkins dashboard with green stages.
- Test report under “Test Results”.

---

**Author:** Sri Hari  
**Role:** DevOps Engineer  
**Focus:** CI Automation, Testing Integration, and Artifact Management
