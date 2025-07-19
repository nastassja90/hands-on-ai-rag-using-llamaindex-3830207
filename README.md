# Hands-On AI: RAG using LlamaIndex

This is the repository for the LinkedIn Learning course Hands-On AI: RAG using LlamaIndex. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

<p>This course offers a deep dive into the principles and applications of retrieval-augmented generation (RAG), with a focus on the innovative LlamaIndex system. Explore how RAG enhances machine learning models by integrating external knowledge sources for more informed and accurate outputs. Instructor Harpreet Sahota
covers the architecture of retrieval systems, the mechanics of indexing vast datasets, and the integration of LlamaIndex with AI models.
 </p><p>
Gain an understanding of the theoretical underpinnings of RAG, practical skills in building and deploying LlamaIndex, and review a critical analysis of RAG applications in various industries. Topics range from the basics of data retrieval and indexing to advanced techniques in enhancing generative models with external data. By the end of the course, you’ll be prepared to design, implement, and evaluate RAG systems, positioning them at the cutting edge of AI technology implementation.

## Instructor

Harpreet SahotaLinkedIn Influencer

Deep Learning Expert, Data Scientist, Developer Relations Manager

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/harpreet-sahota?u=104).

[0]: # "Replace these placeholder URLs with actual course URLs"
[lil-course-url]: https://www.linkedin.com/learning/hands-on-ai-rag-using-llamaindex
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQEi-KCygqsEWQ/learning-public-crop_675_1200/0/1721080561320?e=2147483647&v=beta&t=KHTRqr-DMzswbaDwch90fAnYYWGIjCFF-F6e7gpW7Fc

## Additional notes

### Poetry

The original course uses `Conda` as the package manager of the project, but we chose to use **Poetry** instead.

#### Installation

**Poetry** must be used always inside an active virtual environment. Create a virtual environment with `venv` at the path _./.venv/_ of this repository and install [poetry](https://python-poetry.org/docs/#installing-manually) within that environment:

```sh
python3 -m venv ./.venv/
./.venv/bin/pip install -U pip setuptools
./.venv/bin/pip install poetry
```

Activate the environment:

```sh
source ./.venv/bin/activate
```

#### Setup

After environment activation, init the repository with poetry:

```sh
poetry init
```

Follow the instructions on the terminal.

### Install dependencies

#### Jupyter notebook

```sh
poetry add ipykernel jupyter jupyterlab
```

This will open JupyterLab in your default web browser, allowing you to create and run Jupyter notebooks.

```
jupyter lab
```

#### Llamaindex

LlamaIndex is nicely separated into numerous smaller packages.

For now, let's just install the starter package with the command:

```sh
poetry add llama-index==0.12.49 # latest version 19/07/2025
```

#### Qdrant (vector database)

We'll make use of Qdrant as our vector database through this course. Let's install the dependencies for that.

```python
poetry add qdrant-client==1.15.0 # latest version 19/07/2025
```

#### Installing LlamaIndex dependencies for Qdrant

LlamaIndex has it's dependencies nicely separated out. Let's install what we need for Qdrant:

```python
poetry add llama-index-vector-stores-qdrant==0.6.1 llama-index-readers-file==0.4.11 # latest versions 19/07/2025
```

#### Install LLM Libraries

We'll consistently make use of Cohere and OpenAI throughout the course, so let's install those dependencies as well.

```python
poetry add cohere==5.16.1 # latest version 19/07/2025
poetry add openai==1.97.0 # latest version 19/07/2025
poetry add llama-index-llms-cohere==0.5.0 # latest version 19/07/2025
poetry add llama-index-llms-openai==0.4.7 # latest version 19/07/2025
poetry add llama-index-embeddings-cohere==0.5.1 # latest version 19/07/2025
poetry add llama-index-embeddings-openai==0.3.1 # latest version 19/07/2025
poetry add llama-index-postprocessor-cohere-rerank==0.4.0 # latest version 19/07/2025
```

### Link IPython kernel to venv Environment

```python
python -m ipykernel install --user --name=lil_llama_index --display-name "LlamaIndex (LinkedIn Learning)"
```

## Documentation

Follow the rest of the documentation for this tutorial at [docs](./docs/)
