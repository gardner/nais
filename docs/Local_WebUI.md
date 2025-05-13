# Run your own local chat


## Install `uv`

- https://docs.astral.sh/uv/getting-started/installation


## Install `ollama`
<details>
<summary>Windows</summary>

Download `ollama` here: https://ollama.com/download/windows

</details>

<details>
<summary>Linux / macOS</summary>

```bash
brew install ollama
```

</details>

## Download a model

```shell
ollama pull llama3.2
```

## Run the webui

```shell
uvx open-webui serve
```

## Open a browser

Visit http://localhost:8080
