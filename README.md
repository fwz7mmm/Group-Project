# Group-Project WEB QUIZ

## How to start application

1. Go to the project directory in the Command Window.
2. Type "python app.py" to start the server.
3. Copy the url that display on the command prompt into the web browser to access the application.

## Design & Development of application

1. The web application is implemented by the Flask. 
2. Structure of application directory:
	> Group Project --- 
		> web
			> auth ( authentication methods including register, log in, forget password)
			
			> main ( fundamental methods used to direction between different web pages, handle user submission amd update database.)
			
			> static ( includes all the css file, image file, js file for all the web pages)
			
			> templates ( includes all the html pages, categorized by their responsibility)
			
			> user ( User and admin user methods, used to allow user reset password or admin to manage the user and access overall statistic. )
			
			> models.py ( Python file to define and initial all the necessary table for our application's database)
			> views.py ( web page error view html page)
			
		> app.db ( database which maintain all the data for our web application. )
		> app.py ( application start method )
		> requirements.txt ( includes all the packages needed for this web application. )
		
## How to use this we application

1. Click "start" button on Index page to Home page.
2. Click "sign up" or "login" button ont the right side of navigating panel to get authentication.
3. You can access admin account which was set up by developer. Username: "w: Password "w123456789".
4. Admin user are allow to manage all the users. You can click "Manage users" button on the navigating panel to veiw all the allowable behaviors. Behaviors including inactive user, view user's static, search users and reset user password.
5. 
		
		