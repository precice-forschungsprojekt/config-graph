# Nodes

This project builds a graph based on a precice-config.xml file. The nodes in the graph correspond to the specified XML
elements and tags.<br>
The documentation for preCICE's config tags can be read
at [preCICE XML reference](https://precice.org/configuration-XML-reference.html)

> [!NOTE]
> This graph is built for the [preCICE logic checker](https://github.com/precice-forschungsprojekt/config-checker). This
> means that there may be redundancies or “inconsistencies” in the building of the graph itself.

Here you will find a list with brief explanations of each node and its parameters.

## Participant

The participant is the center of the graph. It saves references to all connected meshes, written and read data,
mappings, and more.

- `name`: The name of the participant as specified by its tag `name=""`, used in the graph debugging view to identify the
  participant.
- `write_data`: A list of all data the participant writes. This links to `WriteData` nodes to allow further references.
- `read_data`: A list of all data the participant reads. This links to `ReadData` nodes to allow further references.
- `receive_meshes`: A list of all meshes the participant receives. This links to `ReceiveMesh` nodes to allow further
  references.
- `provide_meshes`: A list of all meshes the participant provides. This links to `Mesh` nodes to allow further
  references.
- `mappings`: A list of all mappings specified by the participant. This links to `Mapping` nodes to allow further
  references.
- `exports`: A list of all exports specified by the participant. This links to `Export` nodes to allow further
  references.
- `actions`: A list of all actions the participant specifies. This links to `Action` nodes to allow further references.
- `watchpoints`: A list of all watchpoints the participant specifies. This links to `Watchpoint` nodes to allow further
  references.
- `watch_integrals`: A list of all watch integrals the participant specifies. This links to `WatchIntegral` nodes to
  allow further references.

## Mesh

Mesh nodes represent the XML elements mesh.

- `name`: The name of the mesh as specified by its tag `name=""`, used in the graph debugging view to identify the mesh.
- `use_data`: A list of all data used by the mesh. This links to `Data` nodes.
- `write_data`: A list of all data written by the mesh. This links to `Data` nodes.

## ReceiveMesh

Receive mesh nodes are used to differentiate between meshes a participant provides, and meshes a participant receives.
They are also meshes, with the additional information of who they get received by.

- `participant`: The participant the mesh gets received by.
- `mesh`: The mesh that gets received.
- `from_participant`: The participant that provides the mesh.

## Coupling

A coupling node represents a coupling-scheme element of the XML file.

- `first_participant`: The participant of the coupling scheme that gets referred to as `first=“”`.
- `second_participant`: The participant of the coupling scheme that gets referred to as `second=“”`
- `exchanges`: A list of exchanges between the participants. This links to `Exchange` nodes for further references.

## MultiCoupling

A multi-coupling node corresponds to a multi-coupling-scheme XML element. It is an extension of a regular
coupling-scheme to allow for more than two participants.

- `control_participant`: The key participant of the multi-coupling-scheme, which links to a regular `Participant` node.
- `participants`: A list of all <em>other</em> participants taking part in the multi-coupling-scheme.
- `exchanges`: A ist of all exchanges being used to exchange data in this multi-coupling-scheme.

## Data

A data node represents a data element of the XML file.

- `name`: The name of the data element as specified in `name=“”`, used in the graph debugging view to identify the data
  node.
- `data_type`: The type of the data node. Possible values are `scalar` and `vector`.

## Mapping

Mapping nodes correspond to XML subelements of participants, which specify how data gets mapped from one mesh to
another.

- `parent_participant`: This links to the participant that specifies the mapping.
- `direction`: This specifies the direction of the data mapping.
- `from_mesh`: The mesh as specified in the `from=“”` tag
- `to_mesh`: The mesh as specified in the `to=“”` tag

## WriteData

A write-data node corresponds to a subelement of a participant, specifying which data he writes.

- `participant`: The participant this write-data element belongs to.
- `data`: The data that gets written.
- `mesh`: The mesh that the data gets written to.

## ReadData

A read-data node corresponds to a subelement of a participant, specifying which data he reads.

- `participant`: The participant this read-data element belongs to.
- `data`: The data that gets read.
- `mesh`: The mesh that the data gets read from.

## Exchange

An exchange node corresponds to a subelement of a coupling-scheme. It specifies how data gets exchanged between two
participants.

- `coupling_scheme`: The coupling-scheme this exchange belongs to.
- `data`: The data that gets exchanged.
- `mesh`: The mesh through which data gets exchanged.
- `from_participant`: The participant from whom the data originates.
- `to_participant`: The participant who will receive the data.

## Export

Export nodes are another way a user can receive data from a coupled simulation using preCICE.

- `participant`: The participant whose data gets exported.

## Action

- `name`: The name of the action, as specified by `<action:…` …/>
- `participant`: The participant specifying this action.
- `mesh`: The mesh this action will operate on.
- `target_data`: The data that is being targeted by this action.
- `timing`: When this action will be executed. One value is `write-mapping-post`, the other `read-mapping-post`.

## Watchpoint

Watchpoints are a way to keep track of data development at a specified location. They correspond to a subelement of
participants.

- `name`: The name of the watchpoint.
- `participant`: The participant who the watchpoint belongs to.
- `mesh`: The mesh which gets observed 👁️👁️

## WatchIntegral

Watch-integrals are a way to keep track of data development in an entire mesh. They correspond to a subelement of
participants.

- `name`: The name of the watchpoint.
- `participant`: The participant who the watch-integral belongs to.
- `mesh`: The mesh which gets observed
