---
name: drawio
description: This skill should be used when the user asks to "draw a diagram", "make a flowchart", "design a system architecture", "create an ER diagram or database schema", "draw UML, network, BPMN, org chart or mind map", or otherwise visualize a process or structure. Produces draw.io mxGraphModel XML as a .xml file or through the draw.io MCP create_diagram tool.
version: 1.1.0
---

# Draw.io Diagram Generator

Write draw.io diagrams as `mxGraphModel` XML that opens in [draw.io](https://app.diagrams.net) or the desktop app.

## Which tool to use

- **`create_diagram` available** (draw.io MCP server, in a chat that shows diagrams inline such as claude.ai): call it. The diagram appears in the conversation; write a file only when the user asks for one. Call `get_drawio_reference` once per format before the first diagram, and `search_shapes` first for AWS, Azure, GCP, Cisco, Kubernetes or brand icons.
- **Otherwise** (Claude Code, no MCP, or the user wants a file): follow Steps.

## Steps

1. Pick the nearest file in `examples/` for the requested diagram type and mirror its structure.
2. Consult the references below for the branches the diagram needs.
3. Choose positions: place nodes yourself on the grid, or hand layout to the tool (see Auto-layout).
4. Write the XML to `/mnt/user-data/outputs/<descriptive-lowercase-name>.xml` with `create_file`. The `.xml` extension keeps the content copyable in Claude's UI (the `.drawio` type is not).
5. Run the repair pass, then check the file against the Critical Rules and `references/mxfile.xsd`; done when every rule holds and the XML is well-formed.
6. Deliver per Output formats.

Diagram types covered: flowcharts, system architecture, ER, UML (class, sequence, state, activity), network, org charts, BPMN, mind maps.

## Skeleton

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
  </root>
</mxGraphModel>
```

Diagram cells go inside `<root>` with `parent="1"`.

## Auto-layout

Use it when the graph has more than about 30 shapes or coordinates are impractical to compute; only the nodes and edges (the topology) need to be right.

- **`postLayout: "elk"`** on `create_diagram`: re-lays-out every vertex as a layered flow. Set `direction` to `vertical` (default) or `horizontal`. Suits pipelines and flowcharts.
- **`routing: "libavoid"`** on `create_diagram`: keeps hand-placed coordinates and re-routes right-angle edges around shapes. Suits hand-placed architecture, swimlane, UML and floor-plan diagrams whose edges cross shapes.
- Pick one of the two. Leave both off for swimlanes, containers, grouped regions and any placement that carries meaning.
- Without the tool, place nodes yourself on the grid. Omit hand-written waypoints when `routing` is set.

## Critical Rules

1. Emit the XML with no comments: they add nothing and `--` inside one breaks parsing.
2. Give every `mxCell` a unique `id`.
3. Give every edge a geometry child: `<mxGeometry relative="1" as="geometry"/>`.
4. Escape `&amp;`, `&lt;`, `&gt;`, `&quot;` in attributes (including `R&amp;D` and HTML labels).
5. Parent the default layer to the root: `<mxCell id="1" parent="0"/>`.
6. Give cells inside a container `parent="<container_id>"` with coordinates relative to it. Parent each edge to the innermost container holding both endpoints, or `parent="1"` when an end sits outside every container.
7. Snap positions to a 10px grid; space nodes at least 200px horizontally and 120px vertically.
8. Route edges with `edgeStyle=orthogonalEdgeStyle`.
9. Write only the XML to the file, with no code fence or prose around it.

## Repair pass

Run right after writing the file, before delivery. It fixes the slips that make draw.io reject a diagram: text around the XML, a raw `<` or stray `&` in an attribute, and the default layer parented to itself.

```bash
python3 scripts/repair_xml.py /mnt/user-data/outputs/<name>.xml
```

## Output formats

- **Default**: the `.xml` file from Steps; the user opens it in draw.io.
- **Browser URL**: when the user asks for a link, print the output of the script with the local file path:

  ```bash
  python3 scripts/drawio_url.py /mnt/user-data/outputs/<name>.xml
  ```

  The script uses the `#R` form: a `#create=` hash makes draw.io warn "All changes will be lost!". Past the browser's URL length limit, deliver the file instead.
- **PNG, SVG, PDF**: tell the user to open the file in draw.io and use File, Export As.

## References

Open the one that matches the branch:

- `references/style-reference.md`: the primary guide. File structure, all style properties, shape types, edge routing, palettes, HTML labels, layers, groups. Read first for any diagram.
- `references/xml-reference.md`: containers, layers, tags, metadata, dark mode.
- `references/shapes.md`: picking a shape for a concept.
- `references/styles.md`: color palettes, fonts, borders.
- `references/edge-routing.md`: waypoints, `exitX/exitY/entryX/entryY` connection points, tangled edges.
- `references/mermaid-reference.md`: only when the user asks for Mermaid.
- `references/mxfile.xsd`: schema for validating output.
- `scripts/repair_xml.py`, `scripts/drawio_url.py`: the repair pass and URL builder above.

The upstream drawio-mcp project keeps the current versions of the shared docs. Fetch them when network access exists and a local copy looks stale:

- XML basics (skeleton, vertex and edge templates, labels, grid, containers, swimlanes): https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-essentials.md
- Full XML reference (layers, tags, metadata, tables, dark mode): https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md
- Mermaid syntax for every supported type: https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/mermaid-reference.md

## Examples

In `examples/`:

- `flowchart.drawio`: decision flow with loops.
- `architecture.drawio`: microservices with swimlane containers.
- `er-diagram.drawio`: blog database schema.
- `ER-Diagram-chen.xml`: Chen-notation ER.
- `activity-diagram.xml`: start/end states, actions, decisions, fork/join, parallel branches.
- `DFD-Context-0.xml`: level-0 data flow diagram.
- `Basic-use-case.drawio.xml`: UML use case.
