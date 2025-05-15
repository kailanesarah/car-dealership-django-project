<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>🚗💻 Car Dealership - Django Project</h1>
    <p><strong>Developed by:</strong> Kailane Sarah — Project created during the PyCode BR course.</p>

<h2>🚀 Project Overview</h2>

<h3>🏞️ Situation</h3>
    <p>Many car dealerships lack a streamlined online system for managing vehicle listings efficiently. Users need a platform to register, update, and remove listings seamlessly while improving engagement and user experience.</p>

<h3>🎯 Task</h3>
    <p>The goal was to develop a web system using Django that allows users to register, authenticate, and manage vehicle listings while integrating AI-based car description generation to enhance usability.</p>

<h3>🏃‍♂️ Action</h3>
    <ul>
        <li>Developed a Django-based web application for user authentication and car management.</li>
        <li>Implemented full CRUD functionality for vehicle listings.</li>
        <li>Integrated <strong>OpenAI</strong> to auto-generate car descriptions, saving users time.</li>
        <li>Designed a clean, user-friendly interface with custom templates for smooth navigation.</li>
    </ul>

<h3>🎯 Result</h3>
    <ul>
        <li>A fully functional web system enabling effortless vehicle management.</li>
        <li>Enhanced user experience with AI-powered descriptions.</li>
        <li>Secure authentication for users, ensuring data integrity.</li>
        <li>A scalable solution with planned future improvements, such as search filters and payment integration.</li>
    </ul>

<h2>📌 How to Set Up the Project</h2>

<h3>🔧 Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>Django</li>
        <li>Additional libraries listed in <code>requirements.txt</code></li>
    </ul>

<h3>📥 Installation Steps</h3>
<ol>
<li>Clone this repository:</li>
        <pre><code>git clone https://github.com/kailanesarah/car-dealership-django-project.git</code></pre>

<li>Navigate to the project folder:</li>
    <pre><code>cd car-dealership-django-project</code></pre>

<li>Install the required dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>

<li>Configure your environment variables in a <code>.env</code> file:</li>
    <pre><code>DJANGO_SECRET_KEY='your_secret_key_here'
DB_NAME='database_name'
DB_USER='database_user'
DB_PASSWORD='database_password'</code></pre>

<li>Run database migrations:</li>
    <pre><code>python manage.py migrate</code></pre>

<li>(Optional) Create a superuser to access the admin panel:</li>
    <pre><code>python manage.py createsuperuser</code></pre>

<li>Start the development server:</li>
    <pre><code>python manage.py runserver</code></pre>

<li>Open your browser and access the project at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.</li>
</ol>
<h2>🌍 Project Endpoints</h2>

 <h3>🔹 Car Management Routes</h3>
    <table>
        <tr>
            <th>Method</th>
            <th>Endpoint</th>
            <th>Description</th>
        </tr>
        <tr><td>GET</td><td>/project/listCars/</td><td>Lists all registered cars</td></tr>
        <tr><td>GET</td><td>/project/detailCars/&lt;pk&gt;/</td><td>Shows details of a specific car</td></tr>
        <tr><td>POST</td><td>/project/registerCars/</td><td>Adds a new car</td></tr>
        <tr><td>PUT</td><td>/project/updateCars/&lt;pk&gt;/</td><td>Updates an existing car</td></tr>
        <tr><td>DELETE</td><td>/project/deleteCars/&lt;pk&gt;/</td><td>Deletes a car</td></tr>
    </table>
<h3>🔹 User Account Routes</h3>
    <table>
        <tr>
            <th>Method</th>
            <th>Endpoint</th>
            <th>Description</th>
        </tr>
        <tr><td>POST</td><td>/account/registerAccount/</td><td>Registers a new user</td></tr>
        <tr><td>POST</td><td>/account/loginAccount/</td><td>User login</td></tr>
        <tr><td>POST</td><td>/account/logoutAccount/</td><td>User logout</td></tr>
    </table>
<h2>🔮 Future Improvements</h2>
    <ul>
        <li>Advanced filters for car search (price, brand, model, etc.).</li>
        <li>User reviews and ratings for vehicles.</li>
        <li>Modernized UI with Bootstrap or Tailwind CSS.</li>
        <li>Integration with payment systems for online purchases.</li>
    </ul>

 <h2>📩 Contact</h2>
    <p>If you have any questions or suggestions, feel free to reach out!</p>
    <p>📧 Email: <a href="mailto:kailanesarahpro@gmail.com">kailanesarahpro@gmail.com</a></p>
    <p>🔗 GitHub: <a href="https://github.com/kailanesarah">https://github.com/kailanesarah</a></p>

<p>⭐ If you liked the project, please leave a star on the repository! 🚀</p>

</body>
</html>
