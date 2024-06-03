# i-am-emerge

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