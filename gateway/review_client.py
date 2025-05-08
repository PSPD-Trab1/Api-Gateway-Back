import grpc
from . import review_pb2, review_pb2_grpc


channel = grpc.insecure_channel('192.168.15.12:50052') 
stub = review_pb2_grpc.ReviewServiceStub(channel)

def add_review(book_id: int, rating: int, comment: str):
    request = review_pb2.ReviewRequest(
        book_id=book_id,
        rating=rating,
        comment=comment
    )
    return stub.AddReview(request)

def get_reviews(book_id: int):
    request = review_pb2.BookReviewRequest(book_id=book_id)
    return stub.GetReviews(request)
