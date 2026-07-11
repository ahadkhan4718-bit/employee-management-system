<p align="center">
  <img src="banner.png" width="100%" alt="Employee Management System Banner">
</p>
# 🚀 Employee Management System

A production-ready Employee Management System built with **Flask** and **MySQL**, deployed on **AWS EC2** with **Amazon RDS**, **Gunicorn**, **Nginx**, **Docker**, **Docker Compose**, and **GitHub Actions CI/CD**.

---

## 📌 Features

- ➕ Add Employee
- ✏️ Update Employee
- ❌ Delete Employee
- 🔍 Search Employee
- 📋 View All Employees
- 🗄️ MySQL Database Integration
- 🐳 Docker Containerization
- ⚙️ Docker Compose Support
- 🌐 Production Deployment using Nginx + Gunicorn
- ☁️ AWS EC2 + Amazon RDS
- 🚀 GitHub Actions CI Pipeline

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Flask (Python) |
| Database | MySQL (Amazon RDS) |
| Web Server | Nginx |
| WSGI Server | Gunicorn |
| Containerization | Docker |
| Multi-Container | Docker Compose |
| Cloud | AWS EC2 |
| Version Control | Git & GitHub |
| CI | GitHub Actions |
| OS | Ubuntu Linux |

---

# 📂 Project Structure

```text
employee-management-system/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
│
├── templates/
│
├── static/
│
└── .github/
    └── workflows/
        ├── ci.yml
        └── deploy.yml
```

---

# 🏗️ Architecture

```text
                User
                  │
                  ▼
             Web Browser
                  │
                  ▼
               Nginx
                  │
                  ▼
              Gunicorn
                  │
                  ▼
              Flask App
                  │
                  ▼
          Amazon RDS (MySQL)
```

---

# 🚀 Deployment Architecture

```text
Developer
     │
git push
     │
     ▼
GitHub
     │
     ▼
GitHub Actions
     │
     ▼
CI Pipeline
     │
     ▼
Docker Build
     │
     ▼
EC2 Deployment
     │
     ▼
Docker Compose
     │
     ▼
Nginx
     │
     ▼
Gunicorn
     │
     ▼
Flask
     │
     ▼
Amazon RDS
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/ahadkhan4718-bit/employee-management-system.git

cd employee-management-system
```

---

## Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t employee-app:v1 .
```

## Run Container

```bash
docker run -d -p 8001:8000 --name employee employee-app:v1
```

---

# 🐳 Docker Compose

Start Application

```bash
docker compose up -d
```

Rebuild Application

```bash
docker compose up -d --build
```

Stop Application

```bash
docker compose down
```

---

# ☁️ AWS Deployment

The application is deployed using:

- Amazon EC2
- Amazon RDS
- Nginx
- Gunicorn
- Docker
- Docker Compose

---

# 🔄 CI Pipeline

GitHub Actions automatically performs:

- Checkout Repository
- Setup Python
- Install Dependencies
- Python Syntax Check
- Build Docker Image

---

# 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/
├── home.png
├── add-employee.png
├── search.png
└── docker.png
```

---

# 📚 What I Learned

Through this project I learned:

- Linux Commands
- Git & GitHub
- Flask Development
- MySQL Database
- Amazon EC2
- Amazon RDS
- Docker
- Docker Compose
- Gunicorn
- Nginx
- Systemd
- GitHub Actions (CI)
- Production Deployment
- Troubleshooting Production Servers

---

# 🔮 Future Improvements

- Continuous Deployment (CD)
- Terraform
- CloudWatch Monitoring
- Elastic IP
- Load Balancer
- Auto Scaling
- HTTPS using SSL
- Domain Name Integration

---

# 👨‍💻 Author

**Ahad Khan**

GitHub:
https://github.com/ahadkhan4718-bit

LinkedIn:
https://linkedin.com/in/ahad-khan-ak

---

⭐ If you found this project useful, consider giving it a Star.
