.PHONY: install
install:
	poetry install

.PHONY: build-clear
build-clear:
	rm -rf build dist

.PHONY: build-windows
build-windows:
	poetry run pyinstaller --onefile --distpath dist/windows --name=py_pressure_logs py_pressure_logs/main.py

.PHONY: build-mac
build-mac:
	poetry run pyinstaller --onefile --distpath dist/mac --name=py_pressure_logs py_pressure_logs/main.py

.PHONY: run-dev
run-dev:
	poetry run python py_pressure_logs/main.py

.PHONY: run-mac
run-mac:
	./dist/mac/main

.PHONY: run-windows
run-windows:
	./dist/windows/main