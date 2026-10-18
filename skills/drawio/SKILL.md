---
name: drawio
description: Generate draw.io diagrams as .xml files for flowcharts, architecture diagrams, ER diagrams, UML, network diagrams, and more. Use whenever the user mentions diagrams, flowcharts, visual representations, system architecture, database schemas, or asks to visualize any process or structure. Works in claude.ai for free users without external dependencies.
---

# Draw.io Diagram Generator

Generate professional draw.io diagrams as `.xml` files (mxGraphModel format) that can be opened in [draw.io](https://app.diagrams.net) or the draw.io desktop app. Using `.xml` extension ensures users can copy and inspect the file content directly in Claude's UI.

## Quick Start

When the user requests a diagram:

1. **Generate mxGraphModel XML** for the requested diagram type
2. **Write to `/mnt/user-data/outputs/`** using `create_file` tool with `.xml` extension
3. **Share with user** using `present_files` tool

## Supported Diagram Types

- **Flowcharts** - Process flows, decision trees, workflows
- **System Architecture** - Microservices, cloud infrastructure, component diagrams
- **ER Diagrams** - Database schemas, entity relationships
- **UML** - Class diagrams, sequence diagrams, state machines
- **Network Diagrams** - Network topology, infrastructure
- **Org Charts** - Team structures, hierarchies
- **BPMN** - Business process modeling
- **Mind Maps** - Concept mapping, brainstorming
- **Activity Diagrams** - UML activity flows with start/end states, actions, decisions, and parallel branches

## Format Selection

For claude.ai users, we generate XML directly (no server-side conversion needed):

- **XML (our approach)**: Direct file generation, works offline, full control
- ~~Mermaid/CSV~~: Requires server conversion (not available for free users)

## File Naming

- Descriptive, lowercase with hyphens: `user-login-flow.xml`
- Always use `.xml` extension (NOT `.drawio` — the DRAWIO type in Claude's UI cannot be copied)
- Save to `/mnt/user-data/outputs/`

## XML Structure

### Basic Template

Every diagram follows this structure:

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <!-- Your diagram elements here with parent="1" -->
  </root>
</mxGraphModel>
```

## Reference

See `references/style-reference.md` : A comprehensive guide covering the complete .drawio file structure, all style properties, shape types, edge routing, color palettes, HTML labels, layers, groups, and complete examples. This is the primary document an AI system needs to generate valid draw.io files.
See `references/mxfile.xsd` — An XML Schema Definition (XSD) for validating the structure of .drawio files. Use this to validate AI-generated output before saving or delivering it to users.
See `references/mermaid-reference.md` : Short hints for generating Mermaid diagrams that render correctly in draw.io. draw.io's Mermaid parser covers 26 diagram types — the header keyword on the first non-directive line selects the type.
See `references/xml-reference.md`: Detailed reference for styles, edge routing, containers, layers, tags, metadata, and dark mode. Consult this when generating draw.io XML diagrams.

### Shape Library

See `references/shapes.md` for complete shape reference.

Common shapes:
- **Rectangle**: `style="rounded=1;whiteSpace=wrap;"`
- **Diamond**: `style="rhombus;whiteSpace=wrap;"`
- **Circle**: `style="ellipse;whiteSpace=wrap;"`
- **Cylinder**: `style="shape=cylinder3;whiteSpace=wrap;"`

### Edge Routing

**CRITICAL**: Every edge MUST have a geometry child element:

```xml
<mxCell id="e1" edge="1" parent="1" source="a" target="b" style="edgeStyle=orthogonalEdgeStyle;">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Key practices:
- Space nodes 200px horizontal / 120px vertical minimum
- Use `edgeStyle=orthogonalEdgeStyle` for right angles
- Control connection points with `exitX/exitY/entryX/entryY` (0-1 values)
- Add waypoints for complex routing (see `references/edge-routing.md`)

### Styling

See `references/styles.md` for complete style reference.

Quick reference:
- Colors: `fillColor=#dae8fc;strokeColor=#6c8ebf`
- Fonts: `fontSize=12;fontColor=#333333`
- Borders: `strokeWidth=2;dashed=1`

## Containers

For nested elements (architecture diagrams, groupings):

**Swimlane** (visible container):
```xml
<mxCell id="svc1" value="User Service" style="swimlane;startSize=30;fillColor=#dae8fc;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
<mxCell id="api1" value="API" style="rounded=1;" vertex="1" parent="svc1">
  <mxGeometry x="20" y="40" width="120" height="60" as="geometry"/>
</mxCell>
```

**Group** (invisible container):
```xml
<mxCell id="grp1" style="group;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
```

## Examples

See the `examples/` directory for complete working diagrams:
- `examples/flowchart.xml` - Simple decision flow
- `examples/architecture.xml` - Microservices architecture
- `examples/er-diagram.xml` - Database schema
- `examples/activity-diagram.xml` - Activity diagram (admin dashboard login flow with start/end states, actions, decisions, fork/join, and parallel branches)

## Resources

- **References**: Detailed guides in `references/` directory
- **Shapes**: `references/shapes.md` - All available shapes
- **Styles**: `references/styles.md` - Complete styling options
- **Edge Routing**: `references/edge-routing.md` - Advanced routing techniques
- **Official Docs**: https://www.drawio.com/doc/faq/drawio-style-reference.html

## Critical Rules

1. **No double hyphens in XML comments**: `--` breaks XML parsing
2. **Unique IDs**: Each `mxCell` needs unique `id` attribute
3. **Edge geometry**: Always include `<mxGeometry relative="1" as="geometry"/>`
4. **Escape special chars**: Use `&amp;`, `&lt;`, `&gt;`, `&quot;` in attributes
5. **Grid alignment**: Position nodes on 10px grid for clean layouts
