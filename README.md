# AI Code Explainer

An AI-powered application that explains code snippets, providing insights into their functionality, time complexity, and common use cases. Built with LangChain, Ollama, and Gradio.

## Features

- Code explanation with detailed analysis
- Time complexity analysis
- Common use cases identification
- User-friendly web interface
- Powered by Mistral LLM

## Prerequisites

- Python 3.9+
- Ollama installed and running
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/krish341360/Code-Explainer.git
cd Code-Explainer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Install and start Ollama:
```bash
# Install Ollama from https://ollama.ai
# Pull the Mistral model
ollama pull mistral
```

4. Create a `data` directory and add your sample files:
```bash
mkdir data
# Add your sample code and documentation files
touch data/sample_code.py
touch data/docs.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://127.0.0.1:7860)

3. Paste your code snippet in the text box and click "Submit" to get an explanation

## Project Structure

```
Code-Explainer/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── data/              # Sample code and documentation
    ├── sample_code.py
    └── docs.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
