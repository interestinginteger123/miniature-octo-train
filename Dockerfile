ARG PYTHON_IMAGE
ARG POETRY_VERSION

FROM ${PYTHON_IMAGE} as build-stage

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=${POETRY_VERSION} \
    POETRY_HOME="/opt/poetry"

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential

RUN python -m venv ${POETRY_HOME}
RUN ${POETRY_HOME}/bin/pip install -U pip setuptools
RUN ${POETRY_HOME}/bin/pip install "poetry==${POETRY_VERSION}"

FROM ${PYTHON_IMAGE} as deployment-image

ENV PATH="${PATH}:/opt/poetry/bin"

COPY pyproject.toml poetry.lock ./
COPY --from=build-stage /opt/poetry/ /opt/poetry/

RUN poetry install

COPY . .

ENV PYTHONPATH="/app:${PYTHONPATH}"

CMD ["poetry", "run", "python", "./app/main.py"]