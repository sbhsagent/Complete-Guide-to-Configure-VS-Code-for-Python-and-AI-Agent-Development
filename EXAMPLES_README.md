# Example Files for VS Code AI Agent Development Guide

This directory contains practical example files referenced in the [Complete Guide to Configure VS Code for Python and AI Agent Development](https://sbhsagent.github.io/Complete-Guide-to-Configure-VS-Code-for-Python-and-AI-Agent-Development/).

## 📁 Project Structure

```
.
├── src/                          # Source code for AI agents
│   ├── __init__.py              # Package initialization
│   ├── hello_agent.py           # LangChain OpenAI agent example
│   ├── hello_agent_direct.py    # Direct OpenAI API example
│   ├── hello_agent_local.py     # Ollama local model example
│   ├── main.py                  # FastAPI server with AI endpoints
│   ├── main_rag_api.py          # RAG (Retrieval-Augmented Generation) API
│   ├── vector_store.py          # ChromaDB vector database setup
│   └── rag_chain.py             # RAG chain implementation
├── tests/                        # Unit tests
│   └── test_basic.py            # Basic test examples
├── .vscode/                      # VS Code configuration
│   ├── launch.json              # Debug configurations
│   └── settings.json            # Editor settings
├── .github/                      # GitHub configuration
│   └── workflows/
│       └── ci.yml               # CI/CD pipeline
├── test_setup.py                # Environment verification script
├── test_gpu.py                  # GPU/CUDA verification script
├── Dockerfile                   # Docker container configuration
├── requirements.txt             # Python dependencies (complete)
├── requirements.in              # Top-level dependencies (pip-tools)
├── pyproject.toml              # Project configuration
├── .pre-commit-config.yaml     # Pre-commit hooks
├── .env.example                # Environment variables template
└── .gitignore                  # Git ignore patterns
```

## 🚀 Quick Start

### 1. Set Up Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
# OPENAI_API_KEY=your_key_here
```

### 3. Run Examples

```bash
# Test environment setup
python test_setup.py

# Test GPU setup (if you have CUDA)
python test_gpu.py

# Run a simple AI agent
python src/hello_agent.py

# Run the FastAPI server
uvicorn src.main:app --reload

# Run the RAG API server
uvicorn src.main_rag_api:app --reload
```

## 📚 Example Descriptions

### AI Agent Examples

- **`hello_agent.py`**: Uses LangChain with OpenAI for a simple Q&A agent
- **`hello_agent_direct.py`**: Direct OpenAI API client without LangChain
- **`hello_agent_local.py`**: Uses Ollama for running local LLM models

### API Examples

- **`main.py`**: FastAPI server with rate limiting and error handling
- **`main_rag_api.py`**: Complete RAG (Retrieval-Augmented Generation) API with vector database

### RAG Components

- **`vector_store.py`**: Sets up ChromaDB for document storage and retrieval
- **`rag_chain.py`**: Implements a RAG chain using LangChain

## 🐳 Docker Usage

```bash
# Build the Docker image
docker build -t ai-agent:latest .

# Run the container
docker run -p 8000:8000 --env-file .env ai-agent:latest
```

## 🧪 Testing

```bash
# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

## 🛠️ Development Tools

### Code Formatting

```bash
# Format code with Black
black .

# Sort imports
isort .

# Lint with Ruff
ruff check .
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```

## 📝 Notes

- All Python files follow the guide's recommended practices
- YAML files are configured for CI/CD with GitHub Actions
- Dockerfile follows security best practices (non-root user, health checks)
- VS Code settings enable auto-formatting and linting

## ⚠️ Requirements

- Python 3.11 or higher (3.12 recommended)
- OpenAI API key (for cloud-based examples)
- Ollama installed (for local model examples)
- Docker (optional, for containerization)

## 🔗 Resources

- [Full Guide](https://sbhsagent.github.io/Complete-Guide-to-Configure-VS-Code-for-Python-and-AI-Agent-Development/)
- [LangChain Documentation](https://python.langchain.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)

## 📄 License

These examples are provided as educational resources for the VS Code AI development guide.
