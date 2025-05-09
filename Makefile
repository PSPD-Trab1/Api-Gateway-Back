load_env:
	export $(cat .env | grep -v '^#' | xargs)

grpc:
	uv run python -m grpc_tools.protoc -I. --python_out=src/ --grpc_python_out=src/ protos/bookstore.proto
	uv run python -m grpc_tools.protoc -I. --python_out=src/ --grpc_python_out=src/ protos/review.proto

# Define the start command for the uvicorn server
start:
	$(MAKE) load_env
	uv run uvicorn src.main:app --host 0.0.0.0 --port 50053
