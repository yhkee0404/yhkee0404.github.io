FROM python:3.12

ARG wheel=example_my_fastapi_project-0.0.1-py3-none-any.whl

# This is when using workspaces, and when exported the requirements
ARG deps=requirements.txt

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/$wheel /code/$wheel
COPY ./$deps /code/$deps

# This is adjusted to install third-party dependencies separately (the --no-deps) and install from requirements
RUN pip install --no-cache-dir --upgrade --no-deps /code/$wheel
RUN pip install -r /code/$deps

CMD ["uvicorn", "yhkee0404.example_greet_api.core:app", "--host", "0.0.0.0", "--port", "8000"]
