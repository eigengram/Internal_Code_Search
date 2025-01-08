from fastapi import FastAPI
from app.routes import code_router
from app.database import create_tables

app = FastAPI(title="Internal Code Repository")

# Initialize database tables
create_tables()

# Include routes
app.include_router(code_router)
for route in app.routes:
    print(route.path, route.methods)


# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Code Repository API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
