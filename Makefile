.PHONY: clean distclean ensure-virtualenv install-deps devenv test install docker

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache
	find . -name __pycache__ | xargs rm -rf
	find . -name '*.pyc' | xargs rm -rf

distclean: clean
	rm -rf venv
	rm -rf fastText
	rm -rf .eggs

ensure-virtualenv:
	@( \
		if [ -z "$$VIRTUAL_ENV" ]; then \
		  echo "Python virtual environment is not detected!"; \
	   	echo "Please run: python3 -mvenv venv && source venv/bin/activate"; \
		  exit 1; \
	  fi \
	)

install-deps:
	@( \
    pip3 install -r requirements.txt; \
    git clone https://github.com/facebookresearch/fastText.git; \
    cd fastText; \
	  pip3 install . \
	)

devenv: ensure-virtualenv install-deps

test:
	python3 setup.py test

install:
	python3 setup.py install

docker:
	docker build -t lucia:latest .
