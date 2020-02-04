from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Main function of the web application
    
    Returns:
        List -- Hello World
    """
    return {"Hello": "World"}