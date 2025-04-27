import os

# Define the folder structure
folders = [
    "data/characters",
    "data/knowledge_base",
    "src",
    "notebooks",
    "models",
    "docs",
    "ui"
]

# Define the files to create
files = {
    "README.md": "# Harry Potter AI Agent\n\nAn open-source intelligent Harry Potter character agent with memory, retrieval, and planning.",
    "LICENSE": "MIT License",  # You can later replace with full text
    "requirements.txt": "# Add Python packages here\ntransformers\nsentence-transformers\nstreamlit\nchromadb\nfaiss-cpu",
    ".gitignore": "__pycache__/\nvenv/\n*.pyc\n.ipynb_checkpoints/\nmodels/\n",
    "src/__init__.py": "",
    "src/main.py": "# Entry point for the Harry Potter AI Agent",
    "src/memory.py": "# Memory system for characters",
    "src/retrieval.py": "# Knowledge base retrieval system",
    "src/character_agent.py": "# Character personalities and response logic",
    "src/utils.py": "# Helper functions",
    "ui/app.py": "# Streamlit or Gradio app for the AI agent",
    "notebooks/01_experiments.ipynb": "",  # Empty Jupyter notebooks
    "notebooks/02_model_tests.ipynb": ""
}

def create_project_structure():
    print("Setting up project structure...")

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create files
    for filepath, content in files.items():
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {filepath}")

    print("\nProject structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
