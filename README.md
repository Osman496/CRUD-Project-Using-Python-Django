# Django CRUD Project

This is a Django-based CRUD (Create, Read, Update, Delete) project that demonstrates how to manage student data. This project includes functionality to add, view, edit, and delete student records.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add new student records
- View a list of all students
- Edit student details
- Delete student records with a confirmation prompt

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python3 -m venv env
    # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    
    pip install django
  

4. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

1. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

2. **Admin interface:**

   Go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials you created.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

Distributed under the MIT License. See `LICENSE` for more information.

