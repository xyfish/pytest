# pytest
python test in wsl ubuntu 20.04

## manage python version with [pyenv](https://github.com/pyenv/pyenv)

## install [suggested-build-environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
```bash
sudo apt update
sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl git libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
## install pyenv
```bash
curl https://pyenv.run | bash
```

## add to ~/.bashrc
```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

## intall python 3.12.6 & set to global
```bash
pyenv install 3.12.6
pyenv global 3.12.6
```

## set venv
```bash
python -m venv venv
```

## auto load venv (edit .vscode/settings.json)
```json
"python.terminal.activateEnvInCurrentTerminal": true
```
## install some package
```bash
pip install pymemcache redis sqlalchemy mysql-connector-python
```

## install fastapi package
```bash
pip install fastapi uvicorn jinja2
# Successfully installed MarkupSafe-2.1.5 annotated-types-0.7.0 anyio-4.4.0 click-8.1.7 fastapi-0.115.0 h11-0.14.0 idna-3.10 jinja2-3.1.4 pydantic-2.9.2 pydantic-core-2.23.4 sniffio-1.3.1 starlette-0.38.5 uvicorn-0.30.6
pip install python-multipart
# Successfully installed python-multipart-0.0.9
```

## 使用 uvicorn 來啟動 FastAPI 應用
```bash
uvicorn your_script_name:app --reload
```
