from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import CodeBlock
from app.schemas import CodeBlockCreate, CodeBlockResponse

code_router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@code_router.post("/codeblocks", response_model=CodeBlockResponse)
def add_code_block(code_block: CodeBlockCreate, db: Session = Depends(get_db)):
    db_code = CodeBlock(**code_block.dict())
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code

@code_router.get("/codeblocks/{code_id}", response_model=CodeBlockResponse)
def get_code_block(code_id: int, db: Session = Depends(get_db)):
    db_code = db.query(CodeBlock).filter(CodeBlock.id == code_id).first()
    if not db_code:
        raise HTTPException(status_code=404, detail="Code block not found")
    return db_code

@code_router.get("/codeblocks")
def search_code_blocks(query: str = "", db: Session = Depends(get_db)):
    codes = db.query(CodeBlock).filter(
        CodeBlock.title.contains(query) | CodeBlock.tags.contains(query)
    ).all()
    return codes

# Placeholder login route
@code_router.get("/login")
def login():
    return {"message": "This is a placeholder for the login page"}

@code_router.delete("/codeblocks/{code_id}")
def delete_code_block(code_id: int, db: Session = Depends(get_db)):
    db_code = db.query(CodeBlock).filter(CodeBlock.id == code_id).first()
    if not db_code:
        raise HTTPException(status_code=404, detail="Code block not found")
    db.delete(db_code)
    db.commit()
    return {"message": "Code block deleted successfully"}

@code_router.put("/codeblocks/{code_id}")
def update_code_block(code_id: int, code_block: CodeBlockCreate, db: Session = Depends(get_db)):
    db_code = db.query(CodeBlock).filter(CodeBlock.id == code_id).first()
    if not db_code:
        raise HTTPException(status_code=404, detail="Code block not found")
    
    db_code.title = code_block.title
    db_code.description = code_block.description
    db_code.tags = code_block.tags
    db_code.code = code_block.code
    db.commit()
    db.refresh(db_code)
    return {"message": "Code block updated successfully", "code_block": db_code}
