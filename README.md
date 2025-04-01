## Installation
#### Python 3 must be already installed
1. Clone the repository:
   ```bash
   git clone https://github.com/01https/task-flow-manager.git
   cd task-flow-manager
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
3. Install dependencies:
    ```bash
   pip install -r requirements.txt

4. Apply database migrations:
    ```bash
   python manage.py migrate
5. To load test data into the database, use the following command:
    ```bash
   python manage.py loaddata data.json
6. Start the development server:
    ```bash
   python manage.py runserver

## Demo
![img.png](static/assets/images/home_page.png)
![img.png](static/assets/images/tag_page.png)
