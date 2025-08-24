import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo  # noqa: F401

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Pandas Dataframe""")
    return


@app.cell
def _():
    from string import ascii_uppercase as letters

    import numpy as np
    import pandas as pd

    df = pd.DataFrame(
        np.random.randint(0, 100, size=(100, len(letters))), columns=list(letters)
    )
    df
    return (df,)


@app.cell
def _(df):
    df["A"].hist()
    return


@app.cell
def _(mo):
    mo.md(r"""# Display JSON""")
    return


@app.cell
def _():
    json_data = ["foo", {"bar": ("baz", None, 1.0, 2)}]
    json_data
    return


@app.cell
def _(mo):
    mo.md(r"""# pydantic""")
    return


@app.cell
def _():
    from pydantic import BaseModel

    class MeetingInfo(BaseModel):
        attendees: int = 5
        meeting_duration_minutes: int = 30
        times_per_week: int = 1
        avg_salary: int = 100000

    meeting = MeetingInfo()
    print(meeting)
    print()
    print(f"Meeting duration (m): {meeting.meeting_duration_minutes}")
    return


@app.cell
def _(mo):
    mo.md(r"""# BeautifulSoup""")
    return


@app.cell
def _():
    import requests
    from bs4 import BeautifulSoup

    r = requests.get("https://example.com")
    print(f"status code: {r.status_code}")

    soup = BeautifulSoup(r.content, features="lxml")
    content = soup.get_text()
    print(f"content: {content}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
