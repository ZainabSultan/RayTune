# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/runtime_env_agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import runtime_env_common_pb2 as src_dot_ray_dot_protobuf_dot_runtime__env__common__pb2
from . import agent_manager_pb2 as src_dot_ray_dot_protobuf_dot_agent__manager__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(src/ray/protobuf/runtime_env_agent.proto\x12\x07ray.rpc\x1a)src/ray/protobuf/runtime_env_common.proto\x1a$src/ray/protobuf/agent_manager.proto\"\xb2\x02\n\x1cGetOrCreateRuntimeEnvRequest\x12\x34\n\x16serialized_runtime_env\x18\x01 \x01(\tR\x14serializedRuntimeEnv\x12G\n\x12runtime_env_config\x18\x02 \x01(\x0b\x32\x19.ray.rpc.RuntimeEnvConfigR\x10runtimeEnvConfig\x12\x15\n\x06job_id\x18\x03 \x01(\x0cR\x05jobId\x12U\n\'serialized_allocated_resource_instances\x18\x04 \x01(\tR$serializedAllocatedResourceInstances\x12%\n\x0esource_process\x18\x05 \x01(\tR\rsourceProcess\"\xb7\x01\n\x1aGetOrCreateRuntimeEnvReply\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x17.ray.rpc.AgentRpcStatusR\x06status\x12#\n\rerror_message\x18\x02 \x01(\tR\x0c\x65rrorMessage\x12\x43\n\x1eserialized_runtime_env_context\x18\x03 \x01(\tR\x1bserializedRuntimeEnvContext\"\x80\x01\n!DeleteRuntimeEnvIfPossibleRequest\x12\x34\n\x16serialized_runtime_env\x18\x01 \x01(\tR\x14serializedRuntimeEnv\x12%\n\x0esource_process\x18\x02 \x01(\tR\rsourceProcess\"w\n\x1f\x44\x65leteRuntimeEnvIfPossibleReply\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x17.ray.rpc.AgentRpcStatusR\x06status\x12#\n\rerror_message\x18\x02 \x01(\tR\x0c\x65rrorMessage\"@\n\x19GetRuntimeEnvsInfoRequest\x12\x19\n\x05limit\x18\x01 \x01(\x03H\x00R\x05limit\x88\x01\x01\x42\x08\n\x06_limit\"w\n\x17GetRuntimeEnvsInfoReply\x12\x46\n\x12runtime_env_states\x18\x01 \x03(\x0b\x32\x18.ray.rpc.RuntimeEnvStateR\x10runtimeEnvStates\x12\x14\n\x05total\x18\x02 \x01(\x03R\x05total2\xc8\x02\n\x11RuntimeEnvService\x12\x63\n\x15GetOrCreateRuntimeEnv\x12%.ray.rpc.GetOrCreateRuntimeEnvRequest\x1a#.ray.rpc.GetOrCreateRuntimeEnvReply\x12r\n\x1a\x44\x65leteRuntimeEnvIfPossible\x12*.ray.rpc.DeleteRuntimeEnvIfPossibleRequest\x1a(.ray.rpc.DeleteRuntimeEnvIfPossibleReply\x12Z\n\x12GetRuntimeEnvsInfo\x12\".ray.rpc.GetRuntimeEnvsInfoRequest\x1a .ray.rpc.GetRuntimeEnvsInfoReplyB\x03\xf8\x01\x01\x62\x06proto3')



_GETORCREATERUNTIMEENVREQUEST = DESCRIPTOR.message_types_by_name['GetOrCreateRuntimeEnvRequest']
_GETORCREATERUNTIMEENVREPLY = DESCRIPTOR.message_types_by_name['GetOrCreateRuntimeEnvReply']
_DELETERUNTIMEENVIFPOSSIBLEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRuntimeEnvIfPossibleRequest']
_DELETERUNTIMEENVIFPOSSIBLEREPLY = DESCRIPTOR.message_types_by_name['DeleteRuntimeEnvIfPossibleReply']
_GETRUNTIMEENVSINFOREQUEST = DESCRIPTOR.message_types_by_name['GetRuntimeEnvsInfoRequest']
_GETRUNTIMEENVSINFOREPLY = DESCRIPTOR.message_types_by_name['GetRuntimeEnvsInfoReply']
GetOrCreateRuntimeEnvRequest = _reflection.GeneratedProtocolMessageType('GetOrCreateRuntimeEnvRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORCREATERUNTIMEENVREQUEST,
  '__module__' : 'src.ray.protobuf.runtime_env_agent_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetOrCreateRuntimeEnvRequest)
  })
_sym_db.RegisterMessage(GetOrCreateRuntimeEnvRequest)

GetOrCreateRuntimeEnvReply = _reflection.GeneratedProtocolMessageType('GetOrCreateRuntimeEnvReply', (_message.Message,), {
  'DESCRIPTOR' : _GETORCREATERUNTIMEENVREPLY,
  '__module__' : 'src.ray.protobuf.runtime_env_agent_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetOrCreateRuntimeEnvReply)
  })
_sym_db.RegisterMessage(GetOrCreateRuntimeEnvReply)

DeleteRuntimeEnvIfPossibleRequest = _reflection.GeneratedProtocolMessageType('DeleteRuntimeEnvIfPossibleRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETERUNTIMEENVIFPOSSIBLEREQUEST,
  '__module__' : 'src.ray.protobuf.runtime_env_agent_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.DeleteRuntimeEnvIfPossibleRequest)
  })
_sym_db.RegisterMessage(DeleteRuntimeEnvIfPossibleRequest)

DeleteRuntimeEnvIfPossibleReply = _reflection.GeneratedProtocolMessageType('DeleteRuntimeEnvIfPossibleReply', (_message.Message,), {
  'DESCRIPTOR' : _DELETERUNTIMEENVIFPOSSIBLEREPLY,
  '__module__' : 'src.ray.protobuf.runtime_env_agent_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.DeleteRuntimeEnvIfPossibleReply)
  })
_sym_db.RegisterMessage(DeleteRuntimeEnvIfPossibleReply)

GetRuntimeEnvsInfoRequest = _reflection.GeneratedProtocolMessageType('GetRuntimeEnvsInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNTIMEENVSINFOREQUEST,
  '__module__' : 'src.ray.protobuf.runtime_env_agent_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetRuntimeEnvsInfoRequest)
  })
_sym_db.RegisterMessage(GetRuntimeEnvsInfoRequest)

GetRuntimeEnvsInfoReply = _reflection.GeneratedProtocolMessageType('GetRuntimeEnvsInfoReply', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNTIMEENVSINFOREPLY,
  '__module__' : 'src.ray.protobuf.runtime_env_agent_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetRuntimeEnvsInfoReply)
  })
_sym_db.RegisterMessage(GetRuntimeEnvsInfoReply)

_RUNTIMEENVSERVICE = DESCRIPTOR.services_by_name['RuntimeEnvService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _GETORCREATERUNTIMEENVREQUEST._serialized_start=135
  _GETORCREATERUNTIMEENVREQUEST._serialized_end=441
  _GETORCREATERUNTIMEENVREPLY._serialized_start=444
  _GETORCREATERUNTIMEENVREPLY._serialized_end=627
  _DELETERUNTIMEENVIFPOSSIBLEREQUEST._serialized_start=630
  _DELETERUNTIMEENVIFPOSSIBLEREQUEST._serialized_end=758
  _DELETERUNTIMEENVIFPOSSIBLEREPLY._serialized_start=760
  _DELETERUNTIMEENVIFPOSSIBLEREPLY._serialized_end=879
  _GETRUNTIMEENVSINFOREQUEST._serialized_start=881
  _GETRUNTIMEENVSINFOREQUEST._serialized_end=945
  _GETRUNTIMEENVSINFOREPLY._serialized_start=947
  _GETRUNTIMEENVSINFOREPLY._serialized_end=1066
  _RUNTIMEENVSERVICE._serialized_start=1069
  _RUNTIMEENVSERVICE._serialized_end=1397
# @@protoc_insertion_point(module_scope)
