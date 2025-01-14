from __future__ import annotations

from enum import Enum


class Direction(Enum):
    READ = "read"
    WRITE = "write"


class DataType(Enum):
    SCALAR = "scalar"
    VECTOR = "vector"


class TimingType(Enum):
    WRITE_MAPPING_POST = "write-mapping-post"
    READ_MAPPING_POST = "read-mapping-post"


class ParticipantNode:
    def __init__(
            self, name: str,
            write_data: list[WriteDataNode] = None, read_data: list[ReadDataNode] = None,
            receive_meshes: list[ReceiveMeshNode] = None, provide_meshes: list[MeshNode] = None,
            mappings: list[MappingNode] = None,
            exports: list[ExportNode] = None,
            actions: list[ActionNode] = None,
            watchpoints: list[WatchpointNode] = None,
            watch_integrals: list[WatchIntegralNode] = None
    ):
        self.name = name

        if write_data is None:
            self.write_data = []
        else:
            self.write_data = write_data

        if read_data is None:
            self.read_data = []
        else:
            self.read_data = read_data

        if receive_meshes is None:
            self.receive_meshes = []
        else:
            self.receive_meshes = receive_meshes

        if provide_meshes is None:
            self.provide_meshes = []
        else:
            self.provide_meshes = provide_meshes

        if mappings is None:
            self.mappings = []
        else:
            self.mappings = mappings

        if exports is None:
            self.exports = []
        else:
            self.exports = exports

        if actions is None:
            self.actions = []
        else:
            self.actions = actions

        if watchpoints is None:
            self.watchpoints = []
        else:
            self.watchpoints = watchpoints

        if watch_integrals is None:
            self.watch_integrals = []
        else:
            self.watch_integrals = watch_integrals


class MeshNode:
    def __init__(self, name: str, use_data: list[DataNode] = None):
        self.name = name

        if use_data is None:
            self.use_data = []
        else:
            self.use_data = use_data


class ReceiveMeshNode:
    def __init__(self, participant: ParticipantNode, mesh: MeshNode, from_participant: ParticipantNode):
        self.participant = participant
        self.mesh = mesh
        self.from_participant = from_participant


class CouplingNode:
    def __init__(
            self,
            first_participant: ParticipantNode, second_participant: ParticipantNode,
            exchanges: list[ExchangeNode] = None
    ):
        self.first_participant = first_participant
        self.second_participant = second_participant

        if exchanges is None:
            self.exchanges = []
        else:
            self.exchanges = exchanges


class MultiCouplingNode:
    def __init__(self, control_participant: ParticipantNode, participants: list[ParticipantNode] = None,
                 exchanges: list[ExchangeNode] = None):
        # TODO control participant as first entry of participants[] ?
        self.control_participant = control_participant

        if participants is None:
            self.participants = []
        else:
            self.participants = participants

        if exchanges is None:
            self.exchanges = []
        else:
            self.exchanges = exchanges


class DataNode:
    def __init__(self, name: str, data_type: DataType):
        self.name = name
        self.data_type = data_type


class MappingNode:
    def __init__(self, parent_participant: ParticipantNode, direction: Direction,
                 from_mesh: MeshNode, to_mesh: MeshNode):
        self.parent_participant = parent_participant
        self.direction = direction
        self.from_mesh = from_mesh
        self.to_mesh = to_mesh


class WriteDataNode:
    def __init__(self, participant: ParticipantNode, data: DataNode, mesh: MeshNode):
        self.participant = participant
        self.data = data
        self.mesh = mesh


class ReadDataNode:
    def __init__(self, participant: ParticipantNode, data: DataNode, mesh: MeshNode):
        self.participant = participant
        self.data = data
        self.mesh = mesh


class ExchangeNode:
    def __init__(self, coupling_scheme: CouplingNode | MultiCouplingNode, data: DataNode, mesh: MeshNode,
                 from_participant: ParticipantNode,
                 to_participant: ParticipantNode):
        self.coupling_scheme = coupling_scheme
        self.data = data
        self.mesh = mesh
        self.from_participant = from_participant
        self.to_participant = to_participant


# TODO is a node for logging (https://precice.org/configuration-logging.html) needed? For me it does not make sense,
#  as it is not used/connected to anything else


# TODO is export a “valid” node? Maybe good for info, but as stated in precice: "great feature for debugging", so not
#  really a good way to use coupling data
class ExportNode:
    def __init__(self, participant: ParticipantNode):
        self.participant = participant


class ActionNode:
    def __init__(self, name: str, participant: ParticipantNode, mesh: MeshNode, target_data: DataNode,
                 timing: TimingType):
        self.name = name
        self.participant = participant
        self.mesh = mesh
        self.target_data = target_data
        self.timing = timing


class WatchpointNode:
    def __init__(self, name: str, participant: ParticipantNode, mesh: MeshNode):
        self.name = name
        self.participant = participant

        self.mesh = mesh


class WatchIntegralNode:
    def __init__(self, name: str, participant: ParticipantNode, mesh: MeshNode):
        self.name = name
        self.participant = participant
        self.mesh = mesh
