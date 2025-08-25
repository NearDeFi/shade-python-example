# shade-python-example

This example demonstrates the available functions in the shade-agent-py package.

## Running locally

Fill out the environment variables and open Docker

Set up a virtual environment and install dependencies 
```bash
python -m venv venv
source venv/bin/activate 
pip install -e .
```

Set the contract prefix to `ac-proxy.`

Run the CLI 
```bash
shade-agent-cli
```

In another terminal, run the app
```bash
python src/app.py
```

## Running on Phala

Set the contract prefix to `ac-sandbox.`

Run the CLI
```bash
shade-agent-cli
```
