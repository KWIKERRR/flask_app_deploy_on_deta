# Deploying Flask App with Deta and Adding Google Analytics Tags

Hello! Welcome to my repository for deploying a Flask App with Deta and integrating it with Google Analytics. Follow the steps below to set up your project:

## Step 1: Install Deta CLI

For Windows users, open PowerShell and run:

```powershell
iwr https://get.deta.dev/cli.ps1 -useb | iex
```

For Mac/Linux users, open the terminal and run:

```bash
curl -fsSL https://get.deta.dev/cli.sh | sh
```

## Step 2: Connect Deta Account

Ensure you have a Deta account and connect to it using:

```bash
deta login
```

## Step 3: Update Google Analytics Code

Navigate to the `main.py` file and replace the existing Google Analytics code with your own.

## Step 4: Deploy the App

Deploy your Flask app using the following command:

```bash
deta deploy
```

## Step 5: Check Google Analytics

Visit your Google Analytics account and navigate to the Real Time / Overview section. You should see live data reflecting the activity on your deployed Flask app.

Congratulations! You have successfully deployed a Flask app using Deta and synchronized it with your Google Analytics account.

![image](https://user-images.githubusercontent.com/119404054/205500020-757bc843-fea2-41a2-89df-891f399f23ba.png)

Feel free to explore and customize your Flask app further. If you encounter any issues or have questions, refer to the Deta and Flask documentation for additional support.

Happy coding!
