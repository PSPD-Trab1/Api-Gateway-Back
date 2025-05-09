import grpc
import src.protos.review_pb2 as review_pb2
import src.protos.review_pb2_grpc as review_pb2_grpc

from src.config import REVIEW_SERVICE_HOST, REVIEW_SERVICE_PORT

channel = grpc.insecure_channel(f"{REVIEW_SERVICE_HOST}:{REVIEW_SERVICE_PORT}") 
stub = review_pb2_grpc.ReviewServiceStub(channel)

def add_review(book_id: int, rating: int, comment: str):
    request = review_pb2.AddReviewRequest(
        book_id=book_id,
        rating=rating,
        comment=comment
    )
    return stub.AddReview(request)

def get_reviews(book_id: int):
    request = review_pb2.GetReviewsRequest(book_id=book_id)
    return stub.GetReviews(request)
