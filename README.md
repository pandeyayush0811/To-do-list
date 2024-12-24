# To-Do List Application

A simple to-do list web application built with **Python (Flask)**, **MongoDB**, and **HTML/CSS**. This app allows users to add, mark as completed, and delete tasks.

## Features

- **Add task**: Users can add new tasks to the list.
- **Mark task as completed**: Users can mark tasks as completed.
- **Delete task**: Users can delete tasks from the list.

## Technologies Used

- **Python**: Backend language used with Flask framework.
- **Flask**: A micro web framework for Python.
- **MongoDB**: NoSQL database to store tasks.
- **HTML/CSS**: Frontend to display and interact with tasks.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pandeyayush0811/To-do-list.git
    ```

2. **Navigate to the folder**:
    ```bash
    cd to-do-list-app
    ```

3. **Activate the virtual environment**:

    - For Windows:
     ```bash
     python -m venv venv
     ```

    - Activate the environment:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up MongoDB**:

    - Make sure MongoDB is installed and running on your system.

    - Use the `config.py` file:
      If you're not using `.env` files, you can manually update the MongoDB connection in the `config.py` file.
      
      Open the `config.py` file and find the section where MongoDB URI is defined (e.g., `MONGO_URI`). Update the value of `MONGO_URI`:
      
      ```python
      class Config:
          MONGO_URI = 'mongodb://localhost:27017/todolist'  # Update this to your MongoDB connection string
      ```
      Replace `localhost:27017` with your server's address if you're connecting to a remote MongoDB instance.

6. **Run the app**:
    ```bash
    python run.py
    ```

7. **Access the app**:
    Open your browser and go to `http://127.0.0.1:5000/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to fork this repository and submit pull requests.

