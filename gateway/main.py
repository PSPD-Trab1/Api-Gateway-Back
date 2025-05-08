from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from gateway.book_client import get_book, get_books

app = FastAPI()

@app.get("/books")
def list_books():
    books_response = get_books()
    return {"books": [{"book_id": b.book_id, "name": b.name, "author": b.author} for b in books_response.books]}

@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    book = get_book(book_id)
    return {"book_id": book.book_id, "name": book.name, "author": book.author}

# class ReviewInput(BaseModel):
#     rating: int
#     comment: str

# @app.post("/books/{book_id}/reviews")
# def create_review(book_id: int, review: ReviewInput):
#     try:
#         response = add_review(book_id, review.rating, review.comment)
#         if response.status != "Avaliação registrada":
#             raise HTTPException(status_code=400, detail=response.status)
#         return {"message": response.status}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/books/{book_id}/reviews")
# def list_reviews(book_id: int):
#     try:
#         response = get_reviews(book_id)
#         return {
#             "reviews": [
#                 {"book_id": r.book_id, "rating": r.rating, "comment": r.comment}
#                 for r in response.reviews
#             ]
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))