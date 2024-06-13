# Image-Question-and-Answer

This repository contains a Visual Question Answering (VQA) model, based on the ViLT (Vision-and-Language Transformer) architecture, which is fine-tuned for the VQA task. The model is sourced from the Hugging Face Model Hub and is accessible through a FastAPI application. The entire application is containerized using Docker for easy deployment.

## Model Details

- **Model**: ViLT (Vision-and-Language Transformer) B32
- **Fine-tuned for**: Visual Question Answering (VQA)
- **Source**: [Hugging Face](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa/tree/main)

## Features

- **Visual Question Answering**: Provide an image and a question about the image, and the model returns an answer.
- **API**: Exposed via FastAPI for easy integration.
- **Containerization**: Dockerized for seamless deployment.

## Getting Started

### Prerequisites

- Docker installed on your machine.
- Python 3.7+ (for local development without Docker).

### Installation

#### Using Docker

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Adityasoni8898/Image-Question-and-Answer.git
    cd Image-Question-and-Answer
    ```

2. **Build the Docker image**:

    ```bash
    docker build -t vqa-model .
    ```

3. **Run the Docker container**:

    ```bash
    docker run -p 8000:8000 vqa-model
    ```

#### Local Development

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Adityasoni8898/Image-Question-and-Answer.git
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI application**:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

## Usage

Once the application is running (whether locally or via Docker), you can access the API at `http://localhost:8000`.

### API Endpoints

- **POST /predict**: Takes an image and a question as input, and returns the answer.

#### Request Example

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@path/to/your/image.jpg' \
  -F 'question=What is in the image?'
