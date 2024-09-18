# pytest
python test

## manage python version with [pyenv](https://github.com/pyenv/pyenv)

## install [suggested-build-environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

    sudo apt update
    sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl git libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

## install pyenv

    curl https://pyenv.run | bash

## intall python 3.12.6 & set to global

    pyenv install 3.12.6
    pyenv global 3.12.6

## set venv

    python -m venv venv
