# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from src.protos import review_pb2 as protos_dot_review__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protos/review_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ReviewServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddReview = channel.unary_unary(
                '/review.ReviewService/AddReview',
                request_serializer=protos_dot_review__pb2.AddReviewRequest.SerializeToString,
                response_deserializer=protos_dot_review__pb2.ReviewResponse.FromString,
                _registered_method=True)
        self.GetReviews = channel.unary_unary(
                '/review.ReviewService/GetReviews',
                request_serializer=protos_dot_review__pb2.GetReviewsRequest.SerializeToString,
                response_deserializer=protos_dot_review__pb2.ReviewList.FromString,
                _registered_method=True)


class ReviewServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddReview(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReviews(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReviewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddReview': grpc.unary_unary_rpc_method_handler(
                    servicer.AddReview,
                    request_deserializer=protos_dot_review__pb2.AddReviewRequest.FromString,
                    response_serializer=protos_dot_review__pb2.ReviewResponse.SerializeToString,
            ),
            'GetReviews': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReviews,
                    request_deserializer=protos_dot_review__pb2.GetReviewsRequest.FromString,
                    response_serializer=protos_dot_review__pb2.ReviewList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'review.ReviewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('review.ReviewService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ReviewService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddReview(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/review.ReviewService/AddReview',
            protos_dot_review__pb2.AddReviewRequest.SerializeToString,
            protos_dot_review__pb2.ReviewResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetReviews(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/review.ReviewService/GetReviews',
            protos_dot_review__pb2.GetReviewsRequest.SerializeToString,
            protos_dot_review__pb2.ReviewList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
