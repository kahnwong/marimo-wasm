start:
	uv run marimo edit

build:
	uv run marimo export html-wasm notebook.py -o dist --mode edit --show-code -f

serve: build
	cd dist && caddy file-server --listen :4000
