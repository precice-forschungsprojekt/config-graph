import networkx as nx

from precice_config_graph import graph, xml_processing
from precice_config_graph import nodes as n
from precice_config_graph.edges import Edge
from precice_config_graph.nodes import DataType, Direction, TimingType, CouplingSchemeType, ActionType

xml = xml_processing.parse_file("tests/example-configs/actions/precice-config.xml")
G_actual = graph.get_graph(xml)


edges = []

# Data
n_color = n.DataNode("Color", DataType.SCALAR)


# Generator
n_generator_mesh = n.MeshNode("Generator-Mesh", [n_color])

n_generator_participant = n.ParticipantNode("Generator", provide_meshes=[n_generator_mesh])

n_generator_write_data = n.WriteDataNode(n_generator_participant, n_color, n_generator_mesh)
n_generator_participant.write_data.append(n_generator_write_data)

edges += [
    (n_generator_mesh, n_color, Edge.USE_DATA),
    (n_generator_mesh, n_generator_participant, Edge.PROVIDE_MESH__PARTICIPANT_PROVIDES),

    (n_generator_write_data, n_generator_participant, Edge.WRITE_DATA__PARTICIPANT__BELONGS_TO),
    (n_generator_write_data, n_generator_mesh, Edge.WRITE_DATA__WRITES_TO_MESH),
    (n_generator_write_data, n_color, Edge.WRITE_DATA__WRITES_TO_DATA),
]


# Propagator
n_propagator_mesh = n.MeshNode("Propagator-Mesh", [n_color])

n_propagator_participant = n.ParticipantNode("Propagator", provide_meshes=[n_propagator_mesh])

n_propagator_receive_mesh = n.ReceiveMeshNode(
    n_propagator_participant, from_participant=n_generator_participant, mesh=n_generator_mesh
)

n_mapping = n.MappingNode(
    n_propagator_participant, Direction.READ, from_mesh=n_generator_mesh, to_mesh=n_propagator_mesh
)
n_propagator_participant.mappings.append(n_mapping)

n_read_data = n.ReadDataNode(n_propagator_participant, data=n_color, mesh=n_propagator_mesh)
n_propagator_participant.read_data.append(n_read_data)

n_action = n.ActionNode(
    n_propagator_participant, type=ActionType.MULTIPLY_BY_AREA, mesh=n_propagator_mesh,
    timing=TimingType.WRITE_MAPPING_POST, target_data=n_color, source_data=[],
)
n_propagator_participant.actions.append(n_action)

edges += [
    (n_propagator_mesh, n_color, Edge.USE_DATA),
    (n_propagator_mesh, n_propagator_participant, Edge.PROVIDE_MESH__PARTICIPANT_PROVIDES),

    (n_propagator_receive_mesh, n_propagator_participant, Edge.RECEIVE_MESH__PARTICIPANT__BELONGS_TO),
    (n_propagator_receive_mesh, n_generator_participant, Edge.RECEIVE_MESH__PARTICIPANT_RECEIVED_FROM),
    (n_propagator_receive_mesh, n_generator_mesh, Edge.RECEIVE_MESH__MESH),

    (n_mapping, n_propagator_participant, Edge.MAPPING__PARTICIPANT__BELONGS_TO),
    (n_mapping, n_generator_mesh, Edge.MAPPING__FROM_MESH),
    (n_mapping, n_propagator_mesh, Edge.MAPPING__TO_MESH),

    (n_read_data, n_propagator_participant, Edge.READ_DATA__PARTICIPANT__BELONGS_TO),
    (n_read_data, n_color, Edge.READ_DATA__DATA_READ_BY),
    (n_read_data, n_propagator_mesh, Edge.READ_DATA__MESH_READ_BY),

    (n_action, n_propagator_participant, Edge.ACTION__PARTICIPANT__BELONGS_TO),
    (n_action, n_propagator_mesh, Edge.ACTION__MESH),
    (n_action, n_color, Edge.ACTION__TARGET_DATA),
]


# M2N Sockets edge
edges += [
    (n_generator_participant, n_propagator_participant, Edge.SOCKET)
]

# Couping scheme
n_coupling_scheme = n.CouplingSchemeNode(
    CouplingSchemeType.SERIAL_EXPLICIT, first_participant=n_generator_participant,
    second_participant=n_propagator_participant, exchanges=[]
)

n_exchange = n.ExchangeNode(
    coupling_scheme=n_coupling_scheme, data=n_color, mesh=n_generator_mesh, from_participant=n_generator_participant,
    to_participant=n_propagator_participant,
)
n_coupling_scheme.exchanges.append(n_exchange)

edges += [
    (n_coupling_scheme, n_generator_participant, Edge.COUPLING_SCHEME__PARTICIPANT_FIRST),
    (n_coupling_scheme, n_propagator_participant, Edge.COUPLING_SCHEME__PARTICIPANT_SECOND),

    (n_exchange, n_coupling_scheme, Edge.EXCHANGE__COUPLING_SCHEME__BELONGS_TO),
    (n_exchange, n_color, Edge.EXCHANGE__DATA),
    (n_exchange, n_generator_mesh,Edge.EXCHANGE__MESH),
    (n_exchange, n_generator_participant,Edge.EXCHANGE__PARTICIPANT_EXCHANGED_BY),
    (n_exchange, n_propagator_participant, Edge.EXCHANGE__EXCHANGES_TO),
]

G_expected = nx.Graph()
for (node_a, node_b, attr) in edges:
    G_expected.add_edge(node_a, node_b, attr=attr)

assert nx.is_isomorphic(G_expected, G_actual),\
    f"Graphs did not match: {nx.to_dict_of_dicts(G_actual)}, {nx.to_dict_of_dicts(G_expected)}"
