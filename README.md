# Biblexity

Biblexity is a natural language interface for querying and exploring biblical texts, inspired by Perplexity AI. It allows users to ask questions about the Bible in natural language and receive relevant verses and explanations.

## 🌟 Features

- Natural language queries for biblical content
- Contextual verse recommendations
- Semantic search across multiple Bible translations
- RESTful API for integration with other applications
- Modern web interface for easy interaction

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- LLM server (compatible with OpenAI API format)
- Text embedding model

### Installation

1. Clone the repository:
```bash
git clone https://github.com/username/biblexity.git
cd biblexity
```

2. Install dependencies:
```bash
pip install .
```

3. Configure the application:
```bash
# Copy the example configuration file
cp configs/app.conf.example configs/app.conf

# Edit the configuration with your settings
# Particularly the LLM and embedding model endpoints
```

4. Start the application:
```bash
python -m biblexity.main
```

## 📁 Project Structure

```
biblexity/
├── biblexity/          # Main application code
├── configs/            # Configuration files
├── notebooks/          # Jupyter notebooks for development and testing
└── resources/          # Bible texts and additional resources
```

## 🛠️ Configuration

The application can be configured through `configs/app.conf`:

```ini
[api]
context_path = "/biblexity/api/v1/"
port = 7777
description = "Biblexity an application to query bible by natural language"

[models]
llm_url = "http://localhost:1234/v1"
embedding_url = "http://localhost:1234/v1/embeddings"
api_key = ${APIKEY}
```

## 🔄 API Endpoints

- `GET /biblexity/api/v1/query`
  - Query the Bible using natural language
  - Parameters:
    - `q`: The natural language query
    - `translation`: (optional) Preferred Bible translation

- `GET /biblexity/api/v1/verse/{reference}`
  - Get a specific Bible verse by reference
  - Parameters:
    - `reference`: Bible verse reference (e.g., "John 3:16")

## 💻 Usage Examples

```python
import requests

# Query about the creation story
response = requests.get(
    "http://localhost:7777/biblexity/api/v1/query",
    params={"q": "What happened on the first day of creation?"}
)

# Get a specific verse
response = requests.get(
    "http://localhost:7777/biblexity/api/v1/verse/Genesis 1:1"
)
```

## 🧪 Development

### Running Tests

```bash
pytest tests/
```

### Adding New Features

1. Create a new branch for your feature
2. Implement the feature with appropriate tests
3. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Bible texts provided by [source]
- Inspired by Perplexity AI's interface
- Built with Python and modern NLP technologies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Project Maintainer - [@aurelSteve77](https://github.com/aurelSteve77)

Project Link: [https://github.com/username/biblexity](https://github.com/username/biblexity)