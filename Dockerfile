FROM python:latest as base
LABEL key="Jeremy Brex EPA Project"

# RUN pip install cx_Oracle

# Install Oracle Client
ENV ORACLE_HOME=/opt/oracle
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
RUN apt-get update && apt-get install -y libaio1 && rm -rf /var/lib/apt/lists/* \
 && wget -q https://download.oracle.com/otn_software/linux/instantclient/19600/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip \
 && unzip instantclient-*.zip \
 && mkdir -p $ORACLE_HOME \
 && mv instantclient_19_6 $ORACLE_HOME/lib \
 && rm -f instantclient-*.zip

# Add Curl

RUN apt-get update -y && apt-get install curl -y

# Install Poetry

ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# Set the working directory.
WORKDIR /app
COPY pyproject.toml /app
# COPY poetry.toml /app

# Development Docker
FROM base as development
RUN poetry install

CMD ["poetry", "run", "python", "how_long/app.py"]

# Production Docker
FROM base as production

# EXPOSE $PORT
RUN poetry config virtualenvs.create false --local && poetry install --no-dev
COPY how_long /app/how_long
CMD ["poetry", "run", "python", "how_long/app.py"]

# Testing stage
FROM base as test

RUN poetry install

# Install Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\
    rm ./chrome.deb
    
# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
    echo "Installing chromium webdriver version ${LATEST}" &&\
    curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
    apt-get install unzip -y &&\
    unzip ./chromedriver_linux64.zip

# Install Tests
COPY how_long /app/how-long
COPY tests /app/tests

ENV PATH "$PATH:/app"

ENTRYPOINT ["poetry", "run", "pytest"]
