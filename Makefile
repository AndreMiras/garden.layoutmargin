VENV_NAME="venv"
ACTIVATE_PATH="$(VENV_NAME)/bin/activate"
PIP=`. $(ACTIVATE_PATH); which pip`
TOX=`. $(ACTIVATE_PATH); which tox`
PYTHON="$(VENV_NAME)/bin/python"
SYSTEM_DEPENDENCIES=python3-dev virtualenv build-essential libssl-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
OS=$(shell lsb_release -si)


all: system_dependencies virtualenv

virtualenv:
	test -d venv || virtualenv -p python3 venv
	. venv/bin/activate
	$(PIP) install Cython==0.26.1
	$(PIP) install -r requirements.txt

system_dependencies:
ifeq ($(OS), Ubuntu)
	sudo apt install --yes --no-install-recommends $(SYSTEM_DEPENDENCIES)
endif

clean:
	rm -rf venv/ .tox/

test:
	$(TOX)
