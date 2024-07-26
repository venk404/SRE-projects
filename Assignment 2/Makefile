.ONESHELL:
VENV := venv

all: install Schema-creation run


install: $(VENV)/Scripts/activate

$(VENV)/Scripts/activate: requirements.txt
	python -m venv $(VENV)

ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\activate.ps1
	$(VENV)\Scripts\python -m pip install --upgrade pip
	$(VENV)\Scripts\pip install -r requirements.txt
else
	chmod +x $(VENV)/bin/activate
	$(VENV)/bin/activate
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
endif



Schema-creation:
ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\python DB\Schemas\Create_Student.py
else
	$(VENV)/bin/python DB/Schemas/Create_Student.py
endif

# Define the run step
run:
ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\uvicorn Main:app --reload --host 0.0.0.0 --port 8000
else
	$(VENV)/bin/uvicorn Main:app --reload --host 0.0.0.0 --port 8000
endif

# Define a clean step
clean:
ifeq ($(OS),Windows_NT)
	@powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
	@powershell -Command "Get-ChildItem -Recurse -Directory -Filter 'data' | Remove-Item -Recurse -Force"
else
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "data" -exec rm -rf {} +
endif

test:
ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\python test.py
else
	$(VENV)/bin/python test.py
endif

.PHONY: install run clean reinstall
