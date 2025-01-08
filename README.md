Monitoring System Application Documentation


Table of Contents


Introduction
Prerequisites
Set Up Locally
Running the Application via Docker
Configuring the Dashboard and Alerts
Example Thresholds
GitHub Repository
Docker Hub Repository
1. Introduction
The Monitoring System Application tracks system metrics and displays them in a user-friendly dashboard. The application is built using Django and is Dockerized for easy deployment. It monitors CPU, memory usage, disk space, and network activity, providing notifications based on defined thresholds.

2. Prerequisites
Before setting up the application, make sure you have the following installed:

Python (3.9 or higher)
Docker (for containerization)
Git (for cloning the repository)
Docker Hub Account (for pushing the image to Docker Hub)
3. Set Up Locally
Clone the repository:

bash
Copy code
git clone https://github.com/ARYAHARIDAS06/SeakerAlertSystem
Navigate into the project directory:

bash
Copy code
cd monitoring-system
Create a virtual environment and activate it:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate   # For Windows
source .venv/bin/activate  # For Mac/Linux
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations to set up the database:

bash
Copy code
python manage.py migrate
Run the Django development server:

bash
Copy code
python manage.py runserver
The application will be available at http://127.0.0.1:8000.

4. Running the Application via Docker
To run the application inside a Docker container, follow these steps:

Build the Docker image:

bash
Copy code
docker build -t monitoring-app .
Run the Docker container:

bash
Copy code
docker run -p 8000:8000 monitoring-app
Access the application: Open your browser and visit http://localhost:8000.

5. Configuring the Dashboard and Alerts
To configure the dashboard and alerts:

Dashboard Configuration: The dashboard shows system metrics like CPU usage, memory usage, disk space, and network activity. Ensure that the metrics collection is properly set up in the application settings.

Alerts Configuration:

Open the Django admin panel at http://localhost:8000/admin/.
Create a new alert by setting thresholds for metrics such as CPU usage, memory usage, etc.
Alerts can be set to trigger when a metric exceeds a specific threshold.
6. Example Thresholds
Here are some example thresholds to trigger notifications:

CPU Usage:

Trigger alert if CPU usage exceeds 85%.
Memory Usage:

Trigger alert if memory usage exceeds 80%.
Disk Space:

Trigger alert if disk space is less than 10% available.
Network Activity:

Trigger alert if network activity exceeds 1GB per minute.
These thresholds can be adjusted based on your monitoring requirements.

7. GitHub Repository
The source code, configurations, and other related files are available in the GitHub repository:

https://github.com/ARYAHARIDAS06/SeakerAlertSystem

8. Docker Hub Repository
The Docker image is available on Docker Hub for easy deployment. You can pull the image using:

docker tag monitoring-app aryamolvh/monitoring-app:latest
