# FASTAPI

# Setting Up Python Environment in Visual Studio Code

This guide will help you set up a Python development environment in Visual Studio Code (VS Code) and install FastAPI for building web applications and APIs.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

1. **Python**: You should have Python installed on your system. If not, you can install it using the package manager appropriate for your platform. For macOS, you can use Homebrew:

    ```
    brew install python
    ```

## Steps to Set Up Python Environment

1. **Create a Python Virtual Environment**:

    Create a virtual environment to isolate your Python project dependencies. Replace `myenv` with the name you prefer for your environment:

    ```shell
    python3.9 -m venv myenv
    ```

2. **Activate the Virtual Environment**:

    Activate the virtual environment to work within it. You need to activate it every time you open VS Code or work on your project:

    - On macOS/Linux:

        ```shell
        source myenv/bin/activate
        ```

3. **Install FastAPI and Uvicorn**:

    Inside your activated virtual environment, you can install FastAPI and Uvicorn using `pip`:

    ```shell
    pip install fastapi uvicorn
    ```

    These libraries will allow you to build high-performance web applications and APIs with Python.

4. **Develop Your FastAPI Application**:

    Now, you can start building your FastAPI application in Visual Studio Code. Create your Python files, define routes, and write your FastAPI code.

5. **Run Your FastAPI Application**:

    To run your FastAPI application, use Uvicorn from the command line. Replace `main` with the name of your Python file containing your FastAPI app and `app` with the name of your FastAPI application instance:

    ```shell
    uvicorn main:app --reload
    ```

    This command will start the development server, and your FastAPI application will be accessible at `http://localhost:8000/` by default.

Remember to deactivate your virtual environment when you're done working on your project:

```shell
deactivate
