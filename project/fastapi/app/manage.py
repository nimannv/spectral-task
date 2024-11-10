import typer
# from typing import Optional
import uvicorn

app = typer.Typer()

@app.command()
def runserver(port: int):
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=False, log_level="debug")

@app.command()
def test(port: int):
    print('test')

if __name__ == "__main__":
    app()