"""
This graph is intended for the preCICE logical-checker https://github.com/precice-forschungsprojekt/config-checker.

You can find documentation under README.md, docs/Nodes.md and docs/Edges.md.

This graph was developed by Simon Wazynski, Alexander Hutter and Orlando Ackermann as part of https://github.com/precice-forschungsprojekt.
"""

from enum import Enum

class Edge(Enum):
    # receive mesh --> mesh
    RECEIVE_MESH__MESH = "receive-mesh_mesh"
    # receive-mesh --received-from-> participant (from)
    RECEIVE_MESH__PARTICIPANT_RECEIVED_FROM = "receive-mesh_participant-received-from"
    # The connection between receive-mesh and participant it is part of
    # receive-mesh --belongs to-> participant
    RECEIVE_MESH__PARTICIPANT__BELONGS_TO = "receive-mesh_belongs-to"

    # participant --provides-> mesh
    PROVIDE_MESH__PARTICIPANT_PROVIDES = "provide-mesh_participant-provides"

    # mapping --to-> mesh
    MAPPING__TO_MESH = "mapping_to-mesh"
    # mesh --mapped-by-> mapping
    MAPPING__FROM_MESH = "mapping_from-mesh"
    # The connection between mapping and participant it is part of
    MAPPING__PARTICIPANT__BELONGS_TO = "mapping_belongs-to"

    # participant (from) --exchanged_from--> exchange
    EXCHANGE__EXCHANGED_FROM = "exchange_exchanged-from"
    # exchange --exchanges-to--> participant (to)
    EXCHANGE__EXCHANGES_TO = "exchange_exchanges-to"
    # exchange <--> data
    EXCHANGE__DATA = "exchange_data"
    # exchange <--> mesh
    EXCHANGE__MESH = "exchange_mesh"
    # The connection between exchange and coupling scheme it is part of
    EXCHANGE__COUPLING_SCHEME__BELONGS_TO = "exchange_belongs-to"

    # The connection between acceleration and coupling scheme it is part of
    ACCELERATION__COUPLING_SCHEME__BELONGS_TO = "acceleration_belongs-to"
    # acceleration data <--> data
    ACCELERATION_DATA__DATA = "acceleration_data"
    # acceleration data <--> mesh
    ACCELERATION_DATA__MESH = "acceleration_mesh"
    # acceleration data <--> acceleration
    ACCELERATION_DATA__ACCELERATION__BELONGS_TO = "acceleration-data_belongs-to"

    # The connection between convergence-measure and coupling scheme it is part of
    CONVERGENCE_MEASURE__COUPLING_SCHEME__BELONGS_TO = "convergence-measure_belongs-to"
    # The connection between exchange and coupling scheme it is part of
    CONVERGENCE_MEASURE__EXCHANGE__BELONGS_TO = "convergence-measure_belongs-to"
    # convergence-measure <--> data
    CONVERGENCE_MEASURE__DATA = "convergence-measure_data"
    # convergence-measure <--> mesh
    CONVERGENCE_MEASURE__MESH = "convergence-measure_mesh"

    # m2n edges
    # m2n <--> acceptor
    M2N__PARTICIPANT_ACCEPTOR = "m2n_participant-acceptor"
    # m2n <--> connector
    M2N__PARTICIPANT_CONNECTOR = "m2n_participant-connector"

    # participant (first) <--> coupling-scheme
    COUPLING_SCHEME__PARTICIPANT_FIRST = "coupling-scheme_participant-first"
    # participant (second) <--> coupling-scheme
    COUPLING_SCHEME__PARTICIPANT_SECOND = "coupling-scheme_participant-second"

    # mesh --"uses"--> data
    USE_DATA = "use-data"

    # write-data --writes-to-> data
    WRITE_DATA__WRITES_TO_DATA = "write-data_writes-to-data"
    # write-data --writes-to-> mesh
    WRITE_DATA__WRITES_TO_MESH = "write-data_writes-to-mesh"
    # The connection between write-data and participant it is part of
    WRITE_DATA__PARTICIPANT__BELONGS_TO = "write-data_belongs-to"

    # data --read-by-> read-data
    READ_DATA__DATA_READ_BY = "read-data_data-read-by"
    # mesh --read-by-> read-data
    READ_DATA__MESH_READ_BY = "read-data_mesh-read-by"
    # The connection between read-data and participant it is part of
    READ_DATA__PARTICIPANT__BELONGS_TO = "read-data_belongs-to"

    # connection between participant and export node
    EXPORT__PARTICIPANT__BELONGS_TO = "export_belongs-to"

    # multi coupling: control participant
    MULTI_COUPLING_SCHEME__PARTICIPANT__CONTROL = "multi-coupling-scheme_control"
    # multi coupling: all participants (this includes regular ones, as well as control participants (they have two edges))
    MULTI_COUPLING_SCHEME__PARTICIPANT = "multi-coupling-scheme_participant"

    # connection between actions and its members
    ACTION__PARTICIPANT__BELONGS_TO = "action_belongs-to"
    ACTION__MESH = "action_mesh"
    ACTION__TARGET_DATA = "action_target-data"
    ACTION__SOURCE_DATA = "action_source-data"

    # connection between watchpoints/-integrals and their participants / meshes
    WATCH_POINT__PARTICIPANT__BELONGS_TO = "watch-point_belongs-to"
    WATCH_POINT__MESH = "watch-point_mesh"

    WATCH_INTEGRAL__PARTICIPANT__BELONGS_TO = "watch-integral_belongs-to"
    WATCH_INTEGRAL__MESH = "watch-integral_mesh"

