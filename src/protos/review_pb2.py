# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/review.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'protos/review.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protos/review.proto\x12\x06review\"D\n\x10\x41\x64\x64ReviewRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\x05\x12\x0e\n\x06rating\x18\x02 \x01(\x05\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\" \n\x0eReviewResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"$\n\x11GetReviewsRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\x05\":\n\x06Review\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\x05\x12\x0e\n\x06rating\x18\x02 \x01(\x05\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\"-\n\nReviewList\x12\x1f\n\x07reviews\x18\x01 \x03(\x0b\x32\x0e.review.Review2\x8b\x01\n\rReviewService\x12=\n\tAddReview\x12\x18.review.AddReviewRequest\x1a\x16.review.ReviewResponse\x12;\n\nGetReviews\x12\x19.review.GetReviewsRequest\x1a\x12.review.ReviewListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.review_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDREVIEWREQUEST']._serialized_start=31
  _globals['_ADDREVIEWREQUEST']._serialized_end=99
  _globals['_REVIEWRESPONSE']._serialized_start=101
  _globals['_REVIEWRESPONSE']._serialized_end=133
  _globals['_GETREVIEWSREQUEST']._serialized_start=135
  _globals['_GETREVIEWSREQUEST']._serialized_end=171
  _globals['_REVIEW']._serialized_start=173
  _globals['_REVIEW']._serialized_end=231
  _globals['_REVIEWLIST']._serialized_start=233
  _globals['_REVIEWLIST']._serialized_end=278
  _globals['_REVIEWSERVICE']._serialized_start=281
  _globals['_REVIEWSERVICE']._serialized_end=420
# @@protoc_insertion_point(module_scope)
