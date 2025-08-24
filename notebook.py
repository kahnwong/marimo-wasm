import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo  # noqa: F401

    return


@app.cell
def _():
    print("hello")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
