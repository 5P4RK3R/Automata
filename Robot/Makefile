
PYTHON = python3
PIP = pip3
VENV = venv

# Define targets
.PHONY: all install clean run

# Default target to set up the environment and run the server
all: install run

# Install dependencies
install:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt

# Clean the project
clean:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.xml" -delete
	find . -type f -name "*.DS_Store" -delete
	find . -type d -name "__pycache__" -delete

	