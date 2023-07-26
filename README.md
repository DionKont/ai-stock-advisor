# AI Stock Advisor

Simple Microservice for predicting stock prices and visualing using Prophet Neural Network

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/).
* You have a `<Windows/Linux/Mac>` machine. State if OS matters.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/username/aistockadvisor
    ```

2. Change into the directory:

    ```
    cd aistockadvisor
    ```

3. Create a virtual environment (optional, but recommended):

    ```
    python -m venv env
    ```

    Activate the virtual environment (Linux/Mac):

    ```
    source env/bin/activate
    ```

    Activate the virtual environment (Windows):

    ```
    .\env\Scripts\activate
    ```

4. Install the requirements:

    ```
    pip install -r requirements.txt
    ```
5. Set Aplha Vantage API_KEY variable in env:

    ```
    e.g Windows cmd: set API_KEY="YOUR_API_KEY" or MacOs zsh: export API_KEY="YOUR_API_KEY"
    ```

## Running the application

Once you've installed, you can run the application using the Django manage.py runserver command:


Then open `http://127.0.0.1:8000/` in your web browser.

## Contributing to AI Stock Advisor

To contribute to AI Stock Advisor, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b osdev`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project>/<location>`
5. Create the pull request.

## License

This project uses the following license: [<license_name>](<link>).
