# Template for a FastAPI, pipenv and Docker application

This is an application template which uses Python, FastAPI, pipenv and Docker.

## What is FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.

- Fast to code: Increase the speed to develop features by about 200% to 300% *.

- Fewer bugs: Reduce about 40% of human (developer) induced errors. *

- Intuitive: Great editor support. Completion everywhere. Less time debugging.

- Easy: Designed to be easy to use and learn. Less time reading docs.

- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.

- Robust: Get production-ready code. With automatic interactive documentation.

- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

_For more details check [FastAPI on GitHub](https://github.com/tiangolo/fastapi)._

## What is pipenv

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. Windows is a first-class citizen, in our world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce deterministic builds.

The problems that Pipenv seeks to solve are multi-faceted:

- You no longer need to use ```pip``` and ```virtualenv``` separately. They work together.

- Managing a ```requirements.txt``` file can be problematic, so Pipenv uses the upcoming ```Pipfile``` and ```Pipfile.lock``` instead, which is superior for basic use cases.

- Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.

- Give you insight into your dependency graph (e.g. ```$ pipenv graph```).

- Streamline development workflow by loading ```.env``` files.

_For more details check [pipenv on GitHub](https://github.com/pypa/pipenv)_

## What is Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

_For more details check [Docker Hub](https://hub.docker.com/)_

## How to use this template

### Prerequisites

- Python 3.6+

- pipenv installed

### Installing requirements

To create the virtual environment and install all libraries and packages open the terminal in the root folder of this project (same place where the ```pipfile``` is) and type ```pipenv install```.

### Running application locally

Once the pipenv environment is installed, enter the **app** folder and type ```uvicorn main:app --host 0.0.0.0 --port 5000``` to start the web aplication on port 5000.

The application will be available on ```localhost:5000``` and the documentation (Swagger) on ```localhost:5000/docs```

### Running application as a Docker container

1. Export the requirements in a _requirements.txt_ file

    ``` cmd
    pipenv lock --requirements > requirements.txt
    ```

2. Build docker image

    ``` cmd
    docker build -t fastapitemplate .
    ```

3. Create the container

    ``` cmd
    docker run -d -p 5000:5000 fastapitemplate
    ```
