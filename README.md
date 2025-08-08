# shade-python-example

This example demonstrates the available functions in the shade-agent-py package.

## Running locally

Fill out the environment variables and open Docker

Set up virtual environment and install dependencies 
```bash
python -m venv venv
source venv/bin/activate 
pip install -e .
```

Set the contract prefix to `ac-proxy.`

Install shade-agent-py
```bash
pip install shade-agent-py
```

Run the CLI 
```bash
shade-agent-cli
```

In another terminal run the tests
```bash
python src/app.py
```

## Running on Phala

Set the contract prefix to `ac-sandbox.`

Run the CLI
```bash
shade-agent-cli
```
