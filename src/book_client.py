import os
import grpc
import src.protos.bookstore_pb2 as bookstore_pb2
import src.protos.bookstore_pb2_grpc as bookstore_pb2_grpc

from src.config import BOOKSTORE_SERVICE_HOST, BOOKSTORE_SERVICE_PORT

channel = grpc.insecure_channel(f"{BOOKSTORE_SERVICE_HOST}:{BOOKSTORE_SERVICE_PORT}")
stub = bookstore_pb2_grpc.BookstoreServiceStub(channel)

def get_books():
    return stub.GetBooks(bookstore_pb2.Empty())

def get_book(book_id: int):
    return stub.GetBook(bookstore_pb2.BookRequest(book_id=book_id))

def create_book(book_id: str, name:str, author:str):
    return stub.CreateBook(bookstore_pb2.Book(book_id=book_id, name=name, author=author))