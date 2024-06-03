# i-am-emerge



## Method 1
Deploying a Django website on an Ubuntu server using Gunicorn and Nginx involves several steps, including setting up the server environment, installing necessary software, configuring Gunicorn, setting up Nginx, and securing the installation. Below is a detailed guide to help you through the process.

### Step 1: Set Up the Server Environment

1. **Update and upgrade the server:**
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Install necessary packages:**
   ```bash
   sudo apt install python3-pip python3-dev libpq-dev nginx curl -y
   ```

3. **Install virtualenv:**
   ```bash
   sudo pip3 install virtualenv
   ```

### Step 2: Prepare the Django Application

1. **Create a directory for your project and navigate to it:**
   ```bash
   mkdir ~/myproject
   cd ~/myproject
   ```

2. **Set up a virtual environment:**
   ```bash
   virtualenv myprojectenv
   source myprojectenv/bin/activate
   ```

3. **Install Django and Gunicorn within the virtual environment:**
   ```bash
   pip install django gunicorn
   ```

4. **Create a new Django project or move your existing project to this directory:**
   ```bash
   django-admin startproject myproject .
   ```

5. **Migrate the database and create a superuser:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Test the project to ensure it runs correctly:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

### Step 3: Configure Gunicorn

1. **Create a Gunicorn systemd service file:**
   ```bash
   sudo nano /etc/systemd/system/gunicorn.service
   ```

2. **Add the following content to the file, adjusting paths and settings as necessary:**
   ```ini
   [Unit]
   Description=gunicorn daemon
   After=network.target

   [Service]
   User=yourusername
   Group=www-data
   WorkingDirectory=/home/yourusername/myproject
   ExecStart=/home/yourusername/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/yourusername/myproject/myproject.sock myproject.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. **Start and enable Gunicorn service:**
   ```bash
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn
   ```

### Step 4: Configure Nginx

1. **Create an Nginx configuration file for your project:**
   ```bash
   sudo nano /etc/nginx/sites-available/myproject
   ```

2. **Add the following content to the file, adjusting paths and settings as necessary:**
   ```nginx
   server {
       listen 80;
       server_name your_domain_or_IP;

       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
           root /home/yourusername/myproject;
       }

       location / {
           include proxy_params;
           proxy_pass http://unix:/home/yourusername/myproject/myproject.sock;
       }
   }
   ```

3. **Enable the Nginx configuration:**
   ```bash
   sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
   ```

4. **Test the Nginx configuration and restart Nginx:**
   ```bash
   sudo nginx -t
   sudo systemctl restart nginx
   ```

### Step 5: Adjust Firewall Settings

1. **Allow Nginx through the firewall:**
   ```bash
   sudo ufw allow 'Nginx Full'
   sudo ufw delete allow 'Nginx HTTP'
   ```

### Step 6: Secure Your Site (Optional but Recommended)

1. **Install Certbot and get an SSL certificate:**
   ```bash
   sudo apt install certbot python3-certbot-nginx -y
   sudo certbot --nginx -d your_domain_or_IP
   ```

2. **Follow the prompts to complete the installation and configure SSL.

### Step 7: Check Everything

1. **Ensure Gunicorn is running:**
   ```bash
   sudo systemctl status gunicorn
   ```

2. **Ensure Nginx is running:**
   ```bash
   sudo systemctl status nginx
   ```

3. **Open your web browser and navigate to your domain or IP address to verify that your Django application is up and running.

By following these steps, you should have a Django application running on an Ubuntu server with Gunicorn and Nginx. Make sure to replace placeholders like `yourusername`, `your_domain_or_IP`, and paths with your actual information.


## Method 2

Deploying a Django website on an Ubuntu server with Gunicorn, Nginx, PostgreSQL, SSL, and security configurations involves several steps. Here's a detailed guide to help you through the process:

### 1. Set Up the Ubuntu Server

1. **Update the package list and install updates:**
   ```sh
   sudo apt update
   sudo apt upgrade
   ```

2. **Install necessary packages:**
   ```sh
   sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
   ```

### 2. Set Up PostgreSQL

1. **Switch to the postgres user:**
   ```sh
   sudo -i -u postgres
   ```

2. **Open the PostgreSQL shell:**
   ```sh
   psql
   ```

3. **Create a database and user:**
   ```sql
   CREATE DATABASE your_db_name;
   CREATE USER your_user_name WITH PASSWORD 'your_password';
   ```

4. **Modify the user’s role and set the default encoding:**
   ```sql
   ALTER ROLE your_user_name SET client_encoding TO 'utf8';
   ALTER ROLE your_user_name SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_user_name SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_user_name;
   \q
   ```

5. **Exit from the postgres user:**
   ```sh
   exit
   ```

### 3. Set Up Your Django Application

1. **Create a directory for your project and navigate into it:**
   ```sh
   mkdir ~/myproject
   cd ~/myproject
   ```

2. **Set up a virtual environment and activate it:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Django and Gunicorn:**
   ```sh
   pip install django gunicorn psycopg2-binary
   ```

4. **Create a new Django project:**
   ```sh
   django-admin startproject myproject .
   ```

5. **Configure the database settings in `myproject/settings.py`:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_user_name',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '',
       }
   }
   ```

6. **Migrate the database:**
   ```sh
   python manage.py migrate
   ```

7. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

8. **Collect static files:**
   ```sh
   python manage.py collectstatic
   ```

### 4. Configure Gunicorn

1. **Create a Gunicorn systemd service file:**
   ```sh
   sudo nano /etc/systemd/system/gunicorn.service
   ```

2. **Add the following configuration:**
   ```ini
   [Unit]
   Description=gunicorn daemon
   After=network.target

   [Service]
   User=your_username
   Group=www-data
   WorkingDirectory=/home/your_username/myproject
   ExecStart=/home/your_username/myproject/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/your_username/myproject/myproject.sock myproject.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. **Start and enable Gunicorn:**
   ```sh
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn
   ```

### 5. Configure Nginx

1. **Create an Nginx configuration file for your site:**
   ```sh
   sudo nano /etc/nginx/sites-available/myproject
   ```

2. **Add the following configuration:**
   ```nginx
   server {
       listen 80;
       server_name your_domain_or_IP;

       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
           root /home/your_username/myproject;
       }

       location / {
           include proxy_params;
           proxy_pass http://unix:/home/your_username/myproject/myproject.sock;
       }
   }
   ```

3. **Enable the Nginx configuration:**
   ```sh
   sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
   ```

4. **Test the Nginx configuration:**
   ```sh
   sudo nginx -t
   ```

5. **Restart Nginx:**
   ```sh
   sudo systemctl restart nginx
   ```

### 6. Secure Your Site with SSL

1. **Install Certbot:**
   ```sh
   sudo apt install certbot python3-certbot-nginx
   ```

2. **Obtain an SSL certificate:**
   ```sh
   sudo certbot --nginx -d your_domain_or_IP
   ```

3. **Automatically renew the SSL certificate:**
   ```sh
   sudo systemctl status certbot.timer
   ```

### 7. Enhance Security

1. **Set up a firewall:**
   ```sh
   sudo ufw allow OpenSSH
   sudo ufw allow 'Nginx Full'
   sudo ufw enable
   ```

2. **Ensure your database is not exposed to the outside world:**
   - Edit PostgreSQL configuration to listen only on localhost:
     ```sh
     sudo nano /etc/postgresql/12/main/postgresql.conf
     ```
   - Set `listen_addresses = 'localhost'`.

3. **Configure Django security settings in `settings.py`:**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['your_domain_or_IP']

   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

### 8. Monitoring and Maintenance

1. **Monitor Gunicorn and Nginx logs for errors:**
   ```sh
   sudo journalctl -u gunicorn
   sudo tail -F /var/log/nginx/error.log
   ```

2. **Keep your system and packages up to date:**
   ```sh
   sudo apt update
   sudo apt upgrade
   ```

By following these steps, you should have a robust, secure, and well-performing Django application deployed on an Ubuntu server using Gunicorn, Nginx, PostgreSQL, and SSL.