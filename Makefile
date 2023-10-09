APP_BACKEND_HOME = ./application/backend

.PHONY: menu lint format-code format-and-lint compile-requirements install-requirements compile-and-install-requirements setup-venv activate-venv install-pip-tools run pyclean install-ollama start-ollama run-ollama-model

menu:
	@echo "Please select an option:"
	@echo ""
	@echo "Virtual Environment Operations:"
	@echo "  1) Set up virtual environment (venv)"
	@echo "  2) Activate virtual environment (manual step)"
	@echo ""
	@echo "Dependency Management:"
	@echo "  3) Install pip-tools"
	@echo "  4) Compile dependencies"
	@echo "  5) Install compiled requirements"
	@echo "  6) Compile and Install requirements together"
	@echo ""
	@echo "Code Quality Operations:"
	@echo "  7) Format and Lint code"
	@echo ""
	@echo "Install, start and run LLM model:"
	@echo "  8) Install Ollama"
	@echo "  9) Start Ollama"
	@echo "  10) Run Model"
	@echo ""
	@echo "Run Main Script:"
	@echo " 11) Run main.py"
	@echo ""
	@echo "Clean Python Bytecode:"	
	@echo " 12) Clean Python Bytecode"
	@echo ""
	@echo " 13) Quit"	
	@read -p "Enter your choice: " choice; \
	case $$choice in \
	1) make setup-venv ;; \
	2) make activate-venv ;; \
	3) make install-pip-tools ;; \
	4) make compile-requirements ;; \
	5) make install-requirements ;; \
	6) make compile-and-install-requirements ;; \
	7) make format-and-lint ;; \
	8) make install-ollama ;; \
	9) make start-ollama ;; \
	10) make run-ollama-model ;; \
	11) make run ;; \
	12) make clean-python ;; \
	13) echo "Exiting" ;; \
	*) echo "Invalid choice" ;; \
	esac

install-pip-tools:
	python -m pip install pip-tools

lint:
	flake8 $(APP_BACKEND_HOME)

format-code:
	black $(APP_BACKEND_HOME)

format-and-lint: format-code lint

compile-requirements: install-pip-tools
	pip-compile $(APP_BACKEND_HOME)/requirements.in

install-requirements:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Error: Please activate a virtual environment first."; \
		exit 1; \
	fi
	pip install -r $(APP_BACKEND_HOME)/requirements.txt

compile-and-install-requirements: compile-requirements install-requirements

setup-venv:
	@test -d venv || python3 -m venv venv

activate-venv:
	@echo -e "\033[1;34mTo activate the virtual environment, run:\033[0m \033[1;32msource venv/bin/activate\033[0m"

install-ollama:
	curl https://ollama.ai/install.sh | sh

start-ollama:
	ollama serve

run-ollama-model:
	./run_model.sh

run:
	cd ./$(APP_BACKEND_HOME) && python3 main.py

clean-python:
	@pyclean . --verbose -i venv
