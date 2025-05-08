import grpc
from gateway import book_service_pb2, book_service_pb2_grpc

channel = grpc.insecure_channel('192.168.15.13:50051')  # endereço do serviço A
stub = book_service_pb2_grpc.BookstoreServiceStub(channel)

def get_books():
    return stub.GetBooks(book_service_pb2.Empty())

def get_book(book_id: int):
    return stub.GetBook(book_service_pb2.BookRequest(book_id=book_id))
