# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/node_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as src_dot_ray_dot_protobuf_dot_common__pb2
from . import gcs_pb2 as src_dot_ray_dot_protobuf_dot_gcs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#src/ray/protobuf/node_manager.proto\x12\x07ray.rpc\x1a\x1dsrc/ray/protobuf/common.proto\x1a\x1asrc/ray/protobuf/gcs.proto\"p\n\x13WorkerBacklogReport\x12\x36\n\rresource_spec\x18\x01 \x01(\x0b\x32\x11.ray.rpc.TaskSpecR\x0cresourceSpec\x12!\n\x0c\x62\x61\x63klog_size\x18\x02 \x01(\x03R\x0b\x62\x61\x63klogSize\"\x80\x01\n\x1aReportWorkerBacklogRequest\x12\x1b\n\tworker_id\x18\x01 \x01(\x0cR\x08workerId\x12\x45\n\x0f\x62\x61\x63klog_reports\x18\x02 \x03(\x0b\x32\x1c.ray.rpc.WorkerBacklogReportR\x0e\x62\x61\x63klogReports\"\x1a\n\x18ReportWorkerBacklogReply\"\xe0\x01\n\x19RequestWorkerLeaseRequest\x12\x36\n\rresource_spec\x18\x01 \x01(\x0b\x32\x11.ray.rpc.TaskSpecR\x0cresourceSpec\x12!\n\x0c\x62\x61\x63klog_size\x18\x02 \x01(\x03R\x0b\x62\x61\x63klogSize\x12&\n\x0fgrant_or_reject\x18\x03 \x01(\x08R\rgrantOrReject\x12@\n\x1dis_selected_based_on_locality\x18\x04 \x01(\x08R\x19isSelectedBasedOnLocality\"\x81\x06\n\x17RequestWorkerLeaseReply\x12\x37\n\x0eworker_address\x18\x01 \x01(\x0b\x32\x10.ray.rpc.AddressR\rworkerAddress\x12G\n\x17retry_at_raylet_address\x18\x02 \x01(\x0b\x32\x10.ray.rpc.AddressR\x14retryAtRayletAddress\x12\x44\n\x10resource_mapping\x18\x03 \x03(\x0b\x32\x19.ray.rpc.ResourceMapEntryR\x0fresourceMapping\x12\x1a\n\x08\x63\x61nceled\x18\x04 \x01(\x08R\x08\x63\x61nceled\x12\x1d\n\nworker_pid\x18\x06 \x01(\rR\tworkerPid\x12\x1a\n\x08rejected\x18\x07 \x01(\x08R\x08rejected\x12=\n\x0eresources_data\x18\x08 \x01(\x0b\x32\x16.ray.rpc.ResourcesDataR\rresourcesData\x12Y\n\x0c\x66\x61ilure_type\x18\t \x01(\x0e\x32\x36.ray.rpc.RequestWorkerLeaseReply.SchedulingFailureTypeR\x0b\x66\x61ilureType\x12<\n\x1ascheduling_failure_message\x18\n \x01(\tR\x18schedulingFailureMessage\"\xee\x01\n\x15SchedulingFailureType\x12\x0e\n\nNOT_FAILED\x10\x00\x12\x15\n\x11SCHEDULING_FAILED\x10\x01\x12\x30\n,SCHEDULING_CANCELLED_PLACEMENT_GROUP_REMOVED\x10\x02\x12\x31\n-SCHEDULING_CANCELLED_RUNTIME_ENV_SETUP_FAILED\x10\x03\x12!\n\x1dSCHEDULING_CANCELLED_INTENDED\x10\x04\x12&\n\"SCHEDULING_CANCELLED_UNSCHEDULABLE\x10\x05\"S\n\x1dPrepareBundleResourcesRequest\x12\x32\n\x0c\x62undle_specs\x18\x01 \x03(\x0b\x32\x0f.ray.rpc.BundleR\x0b\x62undleSpecs\"7\n\x1bPrepareBundleResourcesReply\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\"R\n\x1c\x43ommitBundleResourcesRequest\x12\x32\n\x0c\x62undle_specs\x18\x01 \x03(\x0b\x32\x0f.ray.rpc.BundleR\x0b\x62undleSpecs\"\x1c\n\x1a\x43ommitBundleResourcesReply\"P\n\x1c\x43\x61ncelResourceReserveRequest\x12\x30\n\x0b\x62undle_spec\x18\x01 \x01(\x0b\x32\x0f.ray.rpc.BundleR\nbundleSpec\"\x1c\n\x1a\x43\x61ncelResourceReserveReply\"\xa7\x01\n\x13ReturnWorkerRequest\x12\x1f\n\x0bworker_port\x18\x01 \x01(\x05R\nworkerPort\x12\x1b\n\tworker_id\x18\x02 \x01(\x0cR\x08workerId\x12+\n\x11\x64isconnect_worker\x18\x03 \x01(\x08R\x10\x64isconnectWorker\x12%\n\x0eworker_exiting\x18\x04 \x01(\x08R\rworkerExiting\"\x13\n\x11ReturnWorkerReply\"H\n\x1bReleaseUnusedWorkersRequest\x12)\n\x11worker_ids_in_use\x18\x01 \x03(\x0cR\x0eworkerIdsInUse\"\x1b\n\x19ReleaseUnusedWorkersReply\"3\n\x15ShutdownRayletRequest\x12\x1a\n\x08graceful\x18\x01 \x01(\x08R\x08graceful\"\x15\n\x13ShutdownRayletReply\"3\n\x18\x43\x61ncelWorkerLeaseRequest\x12\x17\n\x07task_id\x18\x01 \x01(\x0cR\x06taskId\"2\n\x16\x43\x61ncelWorkerLeaseReply\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\"\xa4\x01\n\x13PinObjectIDsRequest\x12\x35\n\rowner_address\x18\x01 \x01(\x0b\x32\x10.ray.rpc.AddressR\x0cownerAddress\x12\x1d\n\nobject_ids\x18\x02 \x03(\x0cR\tobjectIds\x12&\n\x0cgenerator_id\x18\x03 \x01(\x0cH\x00R\x0bgeneratorId\x88\x01\x01\x42\x0f\n\r_generator_id\"1\n\x11PinObjectIDsReply\x12\x1c\n\tsuccesses\x18\x01 \x03(\x08R\tsuccesses\"E\n\x13GetNodeStatsRequest\x12.\n\x13include_memory_info\x18\x01 \x01(\x08R\x11includeMemoryInfo\"\xb4\x05\n\x10ObjectStoreStats\x12+\n\x12spill_time_total_s\x18\x01 \x01(\x01R\x0fspillTimeTotalS\x12.\n\x13spilled_bytes_total\x18\x02 \x01(\x03R\x11spilledBytesTotal\x12\x32\n\x15spilled_objects_total\x18\x03 \x01(\x03R\x13spilledObjectsTotal\x12/\n\x14restore_time_total_s\x18\x04 \x01(\x01R\x11restoreTimeTotalS\x12\x30\n\x14restored_bytes_total\x18\x05 \x01(\x03R\x12restoredBytesTotal\x12\x34\n\x16restored_objects_total\x18\x06 \x01(\x03R\x14restoredObjectsTotal\x12\x35\n\x17object_store_bytes_used\x18\x07 \x01(\x03R\x14objectStoreBytesUsed\x12\x37\n\x18object_store_bytes_avail\x18\x08 \x01(\x03R\x15objectStoreBytesAvail\x12\x44\n\x1fobject_store_bytes_primary_copy\x18\t \x01(\x03R\x1bobjectStoreBytesPrimaryCopy\x12=\n\x1bobject_store_bytes_fallback\x18\n \x01(\x03R\x18objectStoreBytesFallback\x12*\n\x11num_local_objects\x18\x0b \x01(\x03R\x0fnumLocalObjects\x12%\n\x0e\x63onsumed_bytes\x18\x0c \x01(\x03R\rconsumedBytes\x12.\n\x13object_pulls_queued\x18\r \x01(\x08R\x11objectPullsQueued\"\xb8\x01\n\x11GetNodeStatsReply\x12\x46\n\x12\x63ore_workers_stats\x18\x01 \x03(\x0b\x32\x18.ray.rpc.CoreWorkerStatsR\x10\x63oreWorkersStats\x12\x1f\n\x0bnum_workers\x18\x03 \x01(\rR\nnumWorkers\x12:\n\x0bstore_stats\x18\x06 \x01(\x0b\x32\x19.ray.rpc.ObjectStoreStatsR\nstoreStats\"\x11\n\x0fGlobalGCRequest\"\x0f\n\rGlobalGCReply\"O\n\x1d\x46ormatGlobalMemoryInfoRequest\x12.\n\x13include_memory_info\x18\x01 \x01(\x08R\x11includeMemoryInfo\"\x80\x01\n\x1b\x46ormatGlobalMemoryInfoReply\x12%\n\x0ememory_summary\x18\x01 \x01(\tR\rmemorySummary\x12:\n\x0bstore_stats\x18\x02 \x01(\x0b\x32\x19.ray.rpc.ObjectStoreStatsR\nstoreStats\";\n\x1cRequestObjectSpillageRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\x0cR\x08objectId\"}\n\x1aRequestObjectSpillageReply\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x1d\n\nobject_url\x18\x02 \x01(\tR\tobjectUrl\x12&\n\x0fspilled_node_id\x18\x03 \x01(\x0cR\rspilledNodeId\"T\n\x1bReleaseUnusedBundlesRequest\x12\x35\n\x0e\x62undles_in_use\x18\x01 \x03(\x0b\x32\x0f.ray.rpc.BundleR\x0c\x62undlesInUse\"\x1b\n\x19ReleaseUnusedBundlesReply\"\x18\n\x16GetSystemConfigRequest\";\n\x14GetSystemConfigReply\x12#\n\rsystem_config\x18\x01 \x01(\tR\x0csystemConfig\"\x1e\n\x1cRequestResourceReportRequest\"R\n\x1aRequestResourceReportReply\x12\x34\n\tresources\x18\x01 \x01(\x0b\x32\x16.ray.rpc.ResourcesDataR\tresources\"c\n\x1aUpdateResourceUsageRequest\x12\x45\n\x1fserialized_resource_usage_batch\x18\x01 \x01(\x0cR\x1cserializedResourceUsageBatch\"\x1a\n\x18UpdateResourceUsageReply\":\n\x13GetTasksInfoRequest\x12\x19\n\x05limit\x18\x01 \x01(\x03H\x00R\x05limit\x88\x01\x01\x42\x08\n\x06_limit\"\xa2\x01\n\x11GetTasksInfoReply\x12M\n\x17owned_task_info_entries\x18\x01 \x03(\x0b\x32\x16.ray.rpc.TaskInfoEntryR\x14ownedTaskInfoEntries\x12(\n\x10running_task_ids\x18\x02 \x03(\x0cR\x0erunningTaskIds\x12\x14\n\x05total\x18\x03 \x01(\x03R\x05total\"<\n\x15GetObjectsInfoRequest\x12\x19\n\x05limit\x18\x01 \x01(\x03H\x00R\x05limit\x88\x01\x01\x42\x08\n\x06_limit\"s\n\x13GetObjectsInfoReply\x12\x46\n\x12\x63ore_workers_stats\x18\x01 \x03(\x0b\x32\x18.ray.rpc.CoreWorkerStatsR\x10\x63oreWorkersStats\x12\x14\n\x05total\x18\x02 \x01(\x03R\x05total\"\x18\n\x16GetResourceLoadRequest\"L\n\x14GetResourceLoadReply\x12\x34\n\tresources\x18\x01 \x01(\x0b\x32\x16.ray.rpc.ResourcesDataR\tresources\"\x19\n\x17NotifyGCSRestartRequest\"\x17\n\x15NotifyGCSRestartReply\"5\n\x1aGetTaskFailureCauseRequest\x12\x17\n\x07task_id\x18\x01 \x01(\x0cR\x06taskId\"m\n\x18GetTaskFailureCauseReply\x12?\n\rfailure_cause\x18\x01 \x01(\x0b\x32\x15.ray.rpc.RayErrorInfoH\x00R\x0c\x66\x61ilureCause\x88\x01\x01\x42\x10\n\x0e_failure_cause2\x90\x10\n\x12NodeManagerService\x12]\n\x13UpdateResourceUsage\x12#.ray.rpc.UpdateResourceUsageRequest\x1a!.ray.rpc.UpdateResourceUsageReply\x12T\n\x10NotifyGCSRestart\x12 .ray.rpc.NotifyGCSRestartRequest\x1a\x1e.ray.rpc.NotifyGCSRestartReply\x12Q\n\x0fGetResourceLoad\x12\x1f.ray.rpc.GetResourceLoadRequest\x1a\x1d.ray.rpc.GetResourceLoadReply\x12\x63\n\x15RequestResourceReport\x12%.ray.rpc.RequestResourceReportRequest\x1a#.ray.rpc.RequestResourceReportReply\x12Z\n\x12RequestWorkerLease\x12\".ray.rpc.RequestWorkerLeaseRequest\x1a .ray.rpc.RequestWorkerLeaseReply\x12]\n\x13ReportWorkerBacklog\x12#.ray.rpc.ReportWorkerBacklogRequest\x1a!.ray.rpc.ReportWorkerBacklogReply\x12H\n\x0cReturnWorker\x12\x1c.ray.rpc.ReturnWorkerRequest\x1a\x1a.ray.rpc.ReturnWorkerReply\x12`\n\x14ReleaseUnusedWorkers\x12$.ray.rpc.ReleaseUnusedWorkersRequest\x1a\".ray.rpc.ReleaseUnusedWorkersReply\x12N\n\x0eShutdownRaylet\x12\x1e.ray.rpc.ShutdownRayletRequest\x1a\x1c.ray.rpc.ShutdownRayletReply\x12\x66\n\x16PrepareBundleResources\x12&.ray.rpc.PrepareBundleResourcesRequest\x1a$.ray.rpc.PrepareBundleResourcesReply\x12\x63\n\x15\x43ommitBundleResources\x12%.ray.rpc.CommitBundleResourcesRequest\x1a#.ray.rpc.CommitBundleResourcesReply\x12\x63\n\x15\x43\x61ncelResourceReserve\x12%.ray.rpc.CancelResourceReserveRequest\x1a#.ray.rpc.CancelResourceReserveReply\x12W\n\x11\x43\x61ncelWorkerLease\x12!.ray.rpc.CancelWorkerLeaseRequest\x1a\x1f.ray.rpc.CancelWorkerLeaseReply\x12H\n\x0cPinObjectIDs\x12\x1c.ray.rpc.PinObjectIDsRequest\x1a\x1a.ray.rpc.PinObjectIDsReply\x12H\n\x0cGetNodeStats\x12\x1c.ray.rpc.GetNodeStatsRequest\x1a\x1a.ray.rpc.GetNodeStatsReply\x12<\n\x08GlobalGC\x12\x18.ray.rpc.GlobalGCRequest\x1a\x16.ray.rpc.GlobalGCReply\x12\x66\n\x16\x46ormatGlobalMemoryInfo\x12&.ray.rpc.FormatGlobalMemoryInfoRequest\x1a$.ray.rpc.FormatGlobalMemoryInfoReply\x12\x63\n\x15RequestObjectSpillage\x12%.ray.rpc.RequestObjectSpillageRequest\x1a#.ray.rpc.RequestObjectSpillageReply\x12`\n\x14ReleaseUnusedBundles\x12$.ray.rpc.ReleaseUnusedBundlesRequest\x1a\".ray.rpc.ReleaseUnusedBundlesReply\x12Q\n\x0fGetSystemConfig\x12\x1f.ray.rpc.GetSystemConfigRequest\x1a\x1d.ray.rpc.GetSystemConfigReply\x12H\n\x0cGetTasksInfo\x12\x1c.ray.rpc.GetTasksInfoRequest\x1a\x1a.ray.rpc.GetTasksInfoReply\x12N\n\x0eGetObjectsInfo\x12\x1e.ray.rpc.GetObjectsInfoRequest\x1a\x1c.ray.rpc.GetObjectsInfoReply\x12]\n\x13GetTaskFailureCause\x12#.ray.rpc.GetTaskFailureCauseRequest\x1a!.ray.rpc.GetTaskFailureCauseReplyB\x03\xf8\x01\x01\x62\x06proto3')



_WORKERBACKLOGREPORT = DESCRIPTOR.message_types_by_name['WorkerBacklogReport']
_REPORTWORKERBACKLOGREQUEST = DESCRIPTOR.message_types_by_name['ReportWorkerBacklogRequest']
_REPORTWORKERBACKLOGREPLY = DESCRIPTOR.message_types_by_name['ReportWorkerBacklogReply']
_REQUESTWORKERLEASEREQUEST = DESCRIPTOR.message_types_by_name['RequestWorkerLeaseRequest']
_REQUESTWORKERLEASEREPLY = DESCRIPTOR.message_types_by_name['RequestWorkerLeaseReply']
_PREPAREBUNDLERESOURCESREQUEST = DESCRIPTOR.message_types_by_name['PrepareBundleResourcesRequest']
_PREPAREBUNDLERESOURCESREPLY = DESCRIPTOR.message_types_by_name['PrepareBundleResourcesReply']
_COMMITBUNDLERESOURCESREQUEST = DESCRIPTOR.message_types_by_name['CommitBundleResourcesRequest']
_COMMITBUNDLERESOURCESREPLY = DESCRIPTOR.message_types_by_name['CommitBundleResourcesReply']
_CANCELRESOURCERESERVEREQUEST = DESCRIPTOR.message_types_by_name['CancelResourceReserveRequest']
_CANCELRESOURCERESERVEREPLY = DESCRIPTOR.message_types_by_name['CancelResourceReserveReply']
_RETURNWORKERREQUEST = DESCRIPTOR.message_types_by_name['ReturnWorkerRequest']
_RETURNWORKERREPLY = DESCRIPTOR.message_types_by_name['ReturnWorkerReply']
_RELEASEUNUSEDWORKERSREQUEST = DESCRIPTOR.message_types_by_name['ReleaseUnusedWorkersRequest']
_RELEASEUNUSEDWORKERSREPLY = DESCRIPTOR.message_types_by_name['ReleaseUnusedWorkersReply']
_SHUTDOWNRAYLETREQUEST = DESCRIPTOR.message_types_by_name['ShutdownRayletRequest']
_SHUTDOWNRAYLETREPLY = DESCRIPTOR.message_types_by_name['ShutdownRayletReply']
_CANCELWORKERLEASEREQUEST = DESCRIPTOR.message_types_by_name['CancelWorkerLeaseRequest']
_CANCELWORKERLEASEREPLY = DESCRIPTOR.message_types_by_name['CancelWorkerLeaseReply']
_PINOBJECTIDSREQUEST = DESCRIPTOR.message_types_by_name['PinObjectIDsRequest']
_PINOBJECTIDSREPLY = DESCRIPTOR.message_types_by_name['PinObjectIDsReply']
_GETNODESTATSREQUEST = DESCRIPTOR.message_types_by_name['GetNodeStatsRequest']
_OBJECTSTORESTATS = DESCRIPTOR.message_types_by_name['ObjectStoreStats']
_GETNODESTATSREPLY = DESCRIPTOR.message_types_by_name['GetNodeStatsReply']
_GLOBALGCREQUEST = DESCRIPTOR.message_types_by_name['GlobalGCRequest']
_GLOBALGCREPLY = DESCRIPTOR.message_types_by_name['GlobalGCReply']
_FORMATGLOBALMEMORYINFOREQUEST = DESCRIPTOR.message_types_by_name['FormatGlobalMemoryInfoRequest']
_FORMATGLOBALMEMORYINFOREPLY = DESCRIPTOR.message_types_by_name['FormatGlobalMemoryInfoReply']
_REQUESTOBJECTSPILLAGEREQUEST = DESCRIPTOR.message_types_by_name['RequestObjectSpillageRequest']
_REQUESTOBJECTSPILLAGEREPLY = DESCRIPTOR.message_types_by_name['RequestObjectSpillageReply']
_RELEASEUNUSEDBUNDLESREQUEST = DESCRIPTOR.message_types_by_name['ReleaseUnusedBundlesRequest']
_RELEASEUNUSEDBUNDLESREPLY = DESCRIPTOR.message_types_by_name['ReleaseUnusedBundlesReply']
_GETSYSTEMCONFIGREQUEST = DESCRIPTOR.message_types_by_name['GetSystemConfigRequest']
_GETSYSTEMCONFIGREPLY = DESCRIPTOR.message_types_by_name['GetSystemConfigReply']
_REQUESTRESOURCEREPORTREQUEST = DESCRIPTOR.message_types_by_name['RequestResourceReportRequest']
_REQUESTRESOURCEREPORTREPLY = DESCRIPTOR.message_types_by_name['RequestResourceReportReply']
_UPDATERESOURCEUSAGEREQUEST = DESCRIPTOR.message_types_by_name['UpdateResourceUsageRequest']
_UPDATERESOURCEUSAGEREPLY = DESCRIPTOR.message_types_by_name['UpdateResourceUsageReply']
_GETTASKSINFOREQUEST = DESCRIPTOR.message_types_by_name['GetTasksInfoRequest']
_GETTASKSINFOREPLY = DESCRIPTOR.message_types_by_name['GetTasksInfoReply']
_GETOBJECTSINFOREQUEST = DESCRIPTOR.message_types_by_name['GetObjectsInfoRequest']
_GETOBJECTSINFOREPLY = DESCRIPTOR.message_types_by_name['GetObjectsInfoReply']
_GETRESOURCELOADREQUEST = DESCRIPTOR.message_types_by_name['GetResourceLoadRequest']
_GETRESOURCELOADREPLY = DESCRIPTOR.message_types_by_name['GetResourceLoadReply']
_NOTIFYGCSRESTARTREQUEST = DESCRIPTOR.message_types_by_name['NotifyGCSRestartRequest']
_NOTIFYGCSRESTARTREPLY = DESCRIPTOR.message_types_by_name['NotifyGCSRestartReply']
_GETTASKFAILURECAUSEREQUEST = DESCRIPTOR.message_types_by_name['GetTaskFailureCauseRequest']
_GETTASKFAILURECAUSEREPLY = DESCRIPTOR.message_types_by_name['GetTaskFailureCauseReply']
_REQUESTWORKERLEASEREPLY_SCHEDULINGFAILURETYPE = _REQUESTWORKERLEASEREPLY.enum_types_by_name['SchedulingFailureType']
WorkerBacklogReport = _reflection.GeneratedProtocolMessageType('WorkerBacklogReport', (_message.Message,), {
  'DESCRIPTOR' : _WORKERBACKLOGREPORT,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.WorkerBacklogReport)
  })
_sym_db.RegisterMessage(WorkerBacklogReport)

ReportWorkerBacklogRequest = _reflection.GeneratedProtocolMessageType('ReportWorkerBacklogRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTWORKERBACKLOGREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportWorkerBacklogRequest)
  })
_sym_db.RegisterMessage(ReportWorkerBacklogRequest)

ReportWorkerBacklogReply = _reflection.GeneratedProtocolMessageType('ReportWorkerBacklogReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTWORKERBACKLOGREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportWorkerBacklogReply)
  })
_sym_db.RegisterMessage(ReportWorkerBacklogReply)

RequestWorkerLeaseRequest = _reflection.GeneratedProtocolMessageType('RequestWorkerLeaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTWORKERLEASEREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.RequestWorkerLeaseRequest)
  })
_sym_db.RegisterMessage(RequestWorkerLeaseRequest)

RequestWorkerLeaseReply = _reflection.GeneratedProtocolMessageType('RequestWorkerLeaseReply', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTWORKERLEASEREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.RequestWorkerLeaseReply)
  })
_sym_db.RegisterMessage(RequestWorkerLeaseReply)

PrepareBundleResourcesRequest = _reflection.GeneratedProtocolMessageType('PrepareBundleResourcesRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREBUNDLERESOURCESREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PrepareBundleResourcesRequest)
  })
_sym_db.RegisterMessage(PrepareBundleResourcesRequest)

PrepareBundleResourcesReply = _reflection.GeneratedProtocolMessageType('PrepareBundleResourcesReply', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREBUNDLERESOURCESREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PrepareBundleResourcesReply)
  })
_sym_db.RegisterMessage(PrepareBundleResourcesReply)

CommitBundleResourcesRequest = _reflection.GeneratedProtocolMessageType('CommitBundleResourcesRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMITBUNDLERESOURCESREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CommitBundleResourcesRequest)
  })
_sym_db.RegisterMessage(CommitBundleResourcesRequest)

CommitBundleResourcesReply = _reflection.GeneratedProtocolMessageType('CommitBundleResourcesReply', (_message.Message,), {
  'DESCRIPTOR' : _COMMITBUNDLERESOURCESREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CommitBundleResourcesReply)
  })
_sym_db.RegisterMessage(CommitBundleResourcesReply)

CancelResourceReserveRequest = _reflection.GeneratedProtocolMessageType('CancelResourceReserveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELRESOURCERESERVEREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CancelResourceReserveRequest)
  })
_sym_db.RegisterMessage(CancelResourceReserveRequest)

CancelResourceReserveReply = _reflection.GeneratedProtocolMessageType('CancelResourceReserveReply', (_message.Message,), {
  'DESCRIPTOR' : _CANCELRESOURCERESERVEREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CancelResourceReserveReply)
  })
_sym_db.RegisterMessage(CancelResourceReserveReply)

ReturnWorkerRequest = _reflection.GeneratedProtocolMessageType('ReturnWorkerRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETURNWORKERREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReturnWorkerRequest)
  })
_sym_db.RegisterMessage(ReturnWorkerRequest)

ReturnWorkerReply = _reflection.GeneratedProtocolMessageType('ReturnWorkerReply', (_message.Message,), {
  'DESCRIPTOR' : _RETURNWORKERREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReturnWorkerReply)
  })
_sym_db.RegisterMessage(ReturnWorkerReply)

ReleaseUnusedWorkersRequest = _reflection.GeneratedProtocolMessageType('ReleaseUnusedWorkersRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEUNUSEDWORKERSREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReleaseUnusedWorkersRequest)
  })
_sym_db.RegisterMessage(ReleaseUnusedWorkersRequest)

ReleaseUnusedWorkersReply = _reflection.GeneratedProtocolMessageType('ReleaseUnusedWorkersReply', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEUNUSEDWORKERSREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReleaseUnusedWorkersReply)
  })
_sym_db.RegisterMessage(ReleaseUnusedWorkersReply)

ShutdownRayletRequest = _reflection.GeneratedProtocolMessageType('ShutdownRayletRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNRAYLETREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ShutdownRayletRequest)
  })
_sym_db.RegisterMessage(ShutdownRayletRequest)

ShutdownRayletReply = _reflection.GeneratedProtocolMessageType('ShutdownRayletReply', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNRAYLETREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ShutdownRayletReply)
  })
_sym_db.RegisterMessage(ShutdownRayletReply)

CancelWorkerLeaseRequest = _reflection.GeneratedProtocolMessageType('CancelWorkerLeaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELWORKERLEASEREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CancelWorkerLeaseRequest)
  })
_sym_db.RegisterMessage(CancelWorkerLeaseRequest)

CancelWorkerLeaseReply = _reflection.GeneratedProtocolMessageType('CancelWorkerLeaseReply', (_message.Message,), {
  'DESCRIPTOR' : _CANCELWORKERLEASEREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.CancelWorkerLeaseReply)
  })
_sym_db.RegisterMessage(CancelWorkerLeaseReply)

PinObjectIDsRequest = _reflection.GeneratedProtocolMessageType('PinObjectIDsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINOBJECTIDSREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PinObjectIDsRequest)
  })
_sym_db.RegisterMessage(PinObjectIDsRequest)

PinObjectIDsReply = _reflection.GeneratedProtocolMessageType('PinObjectIDsReply', (_message.Message,), {
  'DESCRIPTOR' : _PINOBJECTIDSREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.PinObjectIDsReply)
  })
_sym_db.RegisterMessage(PinObjectIDsReply)

GetNodeStatsRequest = _reflection.GeneratedProtocolMessageType('GetNodeStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNODESTATSREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetNodeStatsRequest)
  })
_sym_db.RegisterMessage(GetNodeStatsRequest)

ObjectStoreStats = _reflection.GeneratedProtocolMessageType('ObjectStoreStats', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTORESTATS,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ObjectStoreStats)
  })
_sym_db.RegisterMessage(ObjectStoreStats)

GetNodeStatsReply = _reflection.GeneratedProtocolMessageType('GetNodeStatsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETNODESTATSREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetNodeStatsReply)
  })
_sym_db.RegisterMessage(GetNodeStatsReply)

GlobalGCRequest = _reflection.GeneratedProtocolMessageType('GlobalGCRequest', (_message.Message,), {
  'DESCRIPTOR' : _GLOBALGCREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GlobalGCRequest)
  })
_sym_db.RegisterMessage(GlobalGCRequest)

GlobalGCReply = _reflection.GeneratedProtocolMessageType('GlobalGCReply', (_message.Message,), {
  'DESCRIPTOR' : _GLOBALGCREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GlobalGCReply)
  })
_sym_db.RegisterMessage(GlobalGCReply)

FormatGlobalMemoryInfoRequest = _reflection.GeneratedProtocolMessageType('FormatGlobalMemoryInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORMATGLOBALMEMORYINFOREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.FormatGlobalMemoryInfoRequest)
  })
_sym_db.RegisterMessage(FormatGlobalMemoryInfoRequest)

FormatGlobalMemoryInfoReply = _reflection.GeneratedProtocolMessageType('FormatGlobalMemoryInfoReply', (_message.Message,), {
  'DESCRIPTOR' : _FORMATGLOBALMEMORYINFOREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.FormatGlobalMemoryInfoReply)
  })
_sym_db.RegisterMessage(FormatGlobalMemoryInfoReply)

RequestObjectSpillageRequest = _reflection.GeneratedProtocolMessageType('RequestObjectSpillageRequest', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTOBJECTSPILLAGEREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.RequestObjectSpillageRequest)
  })
_sym_db.RegisterMessage(RequestObjectSpillageRequest)

RequestObjectSpillageReply = _reflection.GeneratedProtocolMessageType('RequestObjectSpillageReply', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTOBJECTSPILLAGEREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.RequestObjectSpillageReply)
  })
_sym_db.RegisterMessage(RequestObjectSpillageReply)

ReleaseUnusedBundlesRequest = _reflection.GeneratedProtocolMessageType('ReleaseUnusedBundlesRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEUNUSEDBUNDLESREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReleaseUnusedBundlesRequest)
  })
_sym_db.RegisterMessage(ReleaseUnusedBundlesRequest)

ReleaseUnusedBundlesReply = _reflection.GeneratedProtocolMessageType('ReleaseUnusedBundlesReply', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEUNUSEDBUNDLESREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReleaseUnusedBundlesReply)
  })
_sym_db.RegisterMessage(ReleaseUnusedBundlesReply)

GetSystemConfigRequest = _reflection.GeneratedProtocolMessageType('GetSystemConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSYSTEMCONFIGREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetSystemConfigRequest)
  })
_sym_db.RegisterMessage(GetSystemConfigRequest)

GetSystemConfigReply = _reflection.GeneratedProtocolMessageType('GetSystemConfigReply', (_message.Message,), {
  'DESCRIPTOR' : _GETSYSTEMCONFIGREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetSystemConfigReply)
  })
_sym_db.RegisterMessage(GetSystemConfigReply)

RequestResourceReportRequest = _reflection.GeneratedProtocolMessageType('RequestResourceReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTRESOURCEREPORTREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.RequestResourceReportRequest)
  })
_sym_db.RegisterMessage(RequestResourceReportRequest)

RequestResourceReportReply = _reflection.GeneratedProtocolMessageType('RequestResourceReportReply', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTRESOURCEREPORTREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.RequestResourceReportReply)
  })
_sym_db.RegisterMessage(RequestResourceReportReply)

UpdateResourceUsageRequest = _reflection.GeneratedProtocolMessageType('UpdateResourceUsageRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESOURCEUSAGEREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.UpdateResourceUsageRequest)
  })
_sym_db.RegisterMessage(UpdateResourceUsageRequest)

UpdateResourceUsageReply = _reflection.GeneratedProtocolMessageType('UpdateResourceUsageReply', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESOURCEUSAGEREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.UpdateResourceUsageReply)
  })
_sym_db.RegisterMessage(UpdateResourceUsageReply)

GetTasksInfoRequest = _reflection.GeneratedProtocolMessageType('GetTasksInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKSINFOREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetTasksInfoRequest)
  })
_sym_db.RegisterMessage(GetTasksInfoRequest)

GetTasksInfoReply = _reflection.GeneratedProtocolMessageType('GetTasksInfoReply', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKSINFOREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetTasksInfoReply)
  })
_sym_db.RegisterMessage(GetTasksInfoReply)

GetObjectsInfoRequest = _reflection.GeneratedProtocolMessageType('GetObjectsInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTSINFOREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetObjectsInfoRequest)
  })
_sym_db.RegisterMessage(GetObjectsInfoRequest)

GetObjectsInfoReply = _reflection.GeneratedProtocolMessageType('GetObjectsInfoReply', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTSINFOREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetObjectsInfoReply)
  })
_sym_db.RegisterMessage(GetObjectsInfoReply)

GetResourceLoadRequest = _reflection.GeneratedProtocolMessageType('GetResourceLoadRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRESOURCELOADREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetResourceLoadRequest)
  })
_sym_db.RegisterMessage(GetResourceLoadRequest)

GetResourceLoadReply = _reflection.GeneratedProtocolMessageType('GetResourceLoadReply', (_message.Message,), {
  'DESCRIPTOR' : _GETRESOURCELOADREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetResourceLoadReply)
  })
_sym_db.RegisterMessage(GetResourceLoadReply)

NotifyGCSRestartRequest = _reflection.GeneratedProtocolMessageType('NotifyGCSRestartRequest', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFYGCSRESTARTREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.NotifyGCSRestartRequest)
  })
_sym_db.RegisterMessage(NotifyGCSRestartRequest)

NotifyGCSRestartReply = _reflection.GeneratedProtocolMessageType('NotifyGCSRestartReply', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFYGCSRESTARTREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.NotifyGCSRestartReply)
  })
_sym_db.RegisterMessage(NotifyGCSRestartReply)

GetTaskFailureCauseRequest = _reflection.GeneratedProtocolMessageType('GetTaskFailureCauseRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKFAILURECAUSEREQUEST,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetTaskFailureCauseRequest)
  })
_sym_db.RegisterMessage(GetTaskFailureCauseRequest)

GetTaskFailureCauseReply = _reflection.GeneratedProtocolMessageType('GetTaskFailureCauseReply', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKFAILURECAUSEREPLY,
  '__module__' : 'src.ray.protobuf.node_manager_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetTaskFailureCauseReply)
  })
_sym_db.RegisterMessage(GetTaskFailureCauseReply)

_NODEMANAGERSERVICE = DESCRIPTOR.services_by_name['NodeManagerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _WORKERBACKLOGREPORT._serialized_start=107
  _WORKERBACKLOGREPORT._serialized_end=219
  _REPORTWORKERBACKLOGREQUEST._serialized_start=222
  _REPORTWORKERBACKLOGREQUEST._serialized_end=350
  _REPORTWORKERBACKLOGREPLY._serialized_start=352
  _REPORTWORKERBACKLOGREPLY._serialized_end=378
  _REQUESTWORKERLEASEREQUEST._serialized_start=381
  _REQUESTWORKERLEASEREQUEST._serialized_end=605
  _REQUESTWORKERLEASEREPLY._serialized_start=608
  _REQUESTWORKERLEASEREPLY._serialized_end=1377
  _REQUESTWORKERLEASEREPLY_SCHEDULINGFAILURETYPE._serialized_start=1139
  _REQUESTWORKERLEASEREPLY_SCHEDULINGFAILURETYPE._serialized_end=1377
  _PREPAREBUNDLERESOURCESREQUEST._serialized_start=1379
  _PREPAREBUNDLERESOURCESREQUEST._serialized_end=1462
  _PREPAREBUNDLERESOURCESREPLY._serialized_start=1464
  _PREPAREBUNDLERESOURCESREPLY._serialized_end=1519
  _COMMITBUNDLERESOURCESREQUEST._serialized_start=1521
  _COMMITBUNDLERESOURCESREQUEST._serialized_end=1603
  _COMMITBUNDLERESOURCESREPLY._serialized_start=1605
  _COMMITBUNDLERESOURCESREPLY._serialized_end=1633
  _CANCELRESOURCERESERVEREQUEST._serialized_start=1635
  _CANCELRESOURCERESERVEREQUEST._serialized_end=1715
  _CANCELRESOURCERESERVEREPLY._serialized_start=1717
  _CANCELRESOURCERESERVEREPLY._serialized_end=1745
  _RETURNWORKERREQUEST._serialized_start=1748
  _RETURNWORKERREQUEST._serialized_end=1915
  _RETURNWORKERREPLY._serialized_start=1917
  _RETURNWORKERREPLY._serialized_end=1936
  _RELEASEUNUSEDWORKERSREQUEST._serialized_start=1938
  _RELEASEUNUSEDWORKERSREQUEST._serialized_end=2010
  _RELEASEUNUSEDWORKERSREPLY._serialized_start=2012
  _RELEASEUNUSEDWORKERSREPLY._serialized_end=2039
  _SHUTDOWNRAYLETREQUEST._serialized_start=2041
  _SHUTDOWNRAYLETREQUEST._serialized_end=2092
  _SHUTDOWNRAYLETREPLY._serialized_start=2094
  _SHUTDOWNRAYLETREPLY._serialized_end=2115
  _CANCELWORKERLEASEREQUEST._serialized_start=2117
  _CANCELWORKERLEASEREQUEST._serialized_end=2168
  _CANCELWORKERLEASEREPLY._serialized_start=2170
  _CANCELWORKERLEASEREPLY._serialized_end=2220
  _PINOBJECTIDSREQUEST._serialized_start=2223
  _PINOBJECTIDSREQUEST._serialized_end=2387
  _PINOBJECTIDSREPLY._serialized_start=2389
  _PINOBJECTIDSREPLY._serialized_end=2438
  _GETNODESTATSREQUEST._serialized_start=2440
  _GETNODESTATSREQUEST._serialized_end=2509
  _OBJECTSTORESTATS._serialized_start=2512
  _OBJECTSTORESTATS._serialized_end=3204
  _GETNODESTATSREPLY._serialized_start=3207
  _GETNODESTATSREPLY._serialized_end=3391
  _GLOBALGCREQUEST._serialized_start=3393
  _GLOBALGCREQUEST._serialized_end=3410
  _GLOBALGCREPLY._serialized_start=3412
  _GLOBALGCREPLY._serialized_end=3427
  _FORMATGLOBALMEMORYINFOREQUEST._serialized_start=3429
  _FORMATGLOBALMEMORYINFOREQUEST._serialized_end=3508
  _FORMATGLOBALMEMORYINFOREPLY._serialized_start=3511
  _FORMATGLOBALMEMORYINFOREPLY._serialized_end=3639
  _REQUESTOBJECTSPILLAGEREQUEST._serialized_start=3641
  _REQUESTOBJECTSPILLAGEREQUEST._serialized_end=3700
  _REQUESTOBJECTSPILLAGEREPLY._serialized_start=3702
  _REQUESTOBJECTSPILLAGEREPLY._serialized_end=3827
  _RELEASEUNUSEDBUNDLESREQUEST._serialized_start=3829
  _RELEASEUNUSEDBUNDLESREQUEST._serialized_end=3913
  _RELEASEUNUSEDBUNDLESREPLY._serialized_start=3915
  _RELEASEUNUSEDBUNDLESREPLY._serialized_end=3942
  _GETSYSTEMCONFIGREQUEST._serialized_start=3944
  _GETSYSTEMCONFIGREQUEST._serialized_end=3968
  _GETSYSTEMCONFIGREPLY._serialized_start=3970
  _GETSYSTEMCONFIGREPLY._serialized_end=4029
  _REQUESTRESOURCEREPORTREQUEST._serialized_start=4031
  _REQUESTRESOURCEREPORTREQUEST._serialized_end=4061
  _REQUESTRESOURCEREPORTREPLY._serialized_start=4063
  _REQUESTRESOURCEREPORTREPLY._serialized_end=4145
  _UPDATERESOURCEUSAGEREQUEST._serialized_start=4147
  _UPDATERESOURCEUSAGEREQUEST._serialized_end=4246
  _UPDATERESOURCEUSAGEREPLY._serialized_start=4248
  _UPDATERESOURCEUSAGEREPLY._serialized_end=4274
  _GETTASKSINFOREQUEST._serialized_start=4276
  _GETTASKSINFOREQUEST._serialized_end=4334
  _GETTASKSINFOREPLY._serialized_start=4337
  _GETTASKSINFOREPLY._serialized_end=4499
  _GETOBJECTSINFOREQUEST._serialized_start=4501
  _GETOBJECTSINFOREQUEST._serialized_end=4561
  _GETOBJECTSINFOREPLY._serialized_start=4563
  _GETOBJECTSINFOREPLY._serialized_end=4678
  _GETRESOURCELOADREQUEST._serialized_start=4680
  _GETRESOURCELOADREQUEST._serialized_end=4704
  _GETRESOURCELOADREPLY._serialized_start=4706
  _GETRESOURCELOADREPLY._serialized_end=4782
  _NOTIFYGCSRESTARTREQUEST._serialized_start=4784
  _NOTIFYGCSRESTARTREQUEST._serialized_end=4809
  _NOTIFYGCSRESTARTREPLY._serialized_start=4811
  _NOTIFYGCSRESTARTREPLY._serialized_end=4834
  _GETTASKFAILURECAUSEREQUEST._serialized_start=4836
  _GETTASKFAILURECAUSEREQUEST._serialized_end=4889
  _GETTASKFAILURECAUSEREPLY._serialized_start=4891
  _GETTASKFAILURECAUSEREPLY._serialized_end=5000
  _NODEMANAGERSERVICE._serialized_start=5003
  _NODEMANAGERSERVICE._serialized_end=7067
# @@protoc_insertion_point(module_scope)
