# Draw.io Skill for Claude.ai

Generate professional draw.io diagrams directly in claude.ai. Creates native `.drawio` files that work with [draw.io web app](https://app.diagrams.net) and [draw.io desktop](https://github.com/jgraph/drawio-desktop).

## Features

✅ **No setup required** - Works immediately in claude.ai  
✅ **Free tier compatible** - Works with no external services or API keys; uses the draw.io MCP server when available  
✅ **Native .drawio files** - Full compatibility with draw.io ecosystem  
✅ **Rich shape library** - Flowcharts, UML, architecture, networks, and more  
✅ **Professional styling** - Color schemes, fonts, and layout guidelines  
✅ **Comprehensive examples** - Working diagrams you can learn from  

## Quick Start

### For claude.ai Users

1. Upload `SKILL.md` to your conversation or reference it in your project
2. Ask Claude to create a diagram:
   ```
   Create a flowchart for user authentication
   ```
3. Download the generated `.drawio` file
4. Open in [draw.io](https://app.diagrams.net)

### For Claude Code Users

1. Copy the entire skill directory to your skills folder
2. Use `/drawio` or mention diagrams in your request

## Supported Diagram Types

| Type | Use Cases |
|------|-----------|
| **Flowcharts** | Process flows, decision trees, algorithms |
| **Architecture** | Microservices, system design, cloud infrastructure |
| **ER Diagrams** | Database schemas, entity relationships |
| **UML** | Class diagrams, sequence diagrams, state machines |
| **Network** | Network topology, infrastructure diagrams |
| **BPMN** | Business process modeling |
| **Org Charts** | Team structures, hierarchies |
| **Mind Maps** | Brainstorming, concept mapping |

## What's Included

```
drawio/
├── SKILL.md              # Main skill file
├── README.md             # This file
├── examples/             # Working diagram examples
│   ├── flowchart.drawio
│   ├── architecture.drawio
│   ├── er-diagram.drawio
│   ├── ER-Diagram-chen.xml
│   ├── activity-diagram.xml
│   ├── DFD-Context-0.xml
│   └── Basic-use-case.drawio.xml
└── references/           # Detailed documentation
    ├── style-reference.md   # Primary guide for valid files
    ├── xml-reference.md     # Containers, layers, tags, dark mode
    ├── shapes.md            # Shape library
    ├── styles.md            # Styling guide
    ├── edge-routing.md      # Advanced connection techniques
    ├── mermaid-reference.md # Mermaid hints
    └── mxfile.xsd           # Schema for validating output
```

## Usage Examples

### Simple Request
```
Draw a flowchart for a login process with email validation
```

### Detailed Request
```
Create an architecture diagram showing:
- API Gateway
- 3 microservices (User, Product, Order)
- Each service has its own database
- Services communicate via message queue
Use blue for services, gray for databases
```

### ER Diagram
```
Design a database schema for a blog with:
- Users (id, email, name)
- Posts (id, user_id, title, content)
- Comments (id, post_id, user_id, content)
Show relationships with cardinality
```

## Relationship to the official draw.io MCP

This skill is based on the official [draw.io-mcp](https://github.com/jgraph/drawio-mcp) project. The repo's `.mcp.json` registers the remote server at `https://mcp.draw.io/mcp`.

| Situation | What the skill does |
|-----------|---------------------|
| `create_diagram` tool available in a chat that shows diagrams inline (claude.ai) | Calls it; the diagram appears in the conversation |
| No MCP server, Claude Code, or a file is wanted | Writes `.xml` to `/mnt/user-data/outputs/`, repairs and validates it, optionally builds a browser URL |

For large or flow-style diagrams the MCP tool can auto-position nodes (`postLayout: "elk"`) or re-route edges (`routing: "libavoid"`). Without it, place nodes on a 10px grid.

## Opening Your Diagrams

### Option 1: Web App (Easiest)
1. Go to https://app.diagrams.net
2. Click "Open Existing Diagram"
3. Upload your `.drawio` file

### Option 2: Desktop App
1. Download [draw.io desktop](https://github.com/jgraph/drawio-desktop/releases)
2. Install and open the app
3. Open your `.drawio` file

### Option 3: Edit Inline
The `.drawio` files are XML - you can edit them directly if needed!

## Learning Resources

### Included Documentation
- `references/style-reference.md` - Primary guide: structure, styles, shapes, edges, palettes
- `references/shapes.md` - Every shape type with examples
- `references/styles.md` - Color palettes, fonts, styling
- `references/edge-routing.md` - Connection techniques

### Examples
- `examples/flowchart.drawio` - Decision flow with loops
- `examples/architecture.drawio` - Microservices setup
- `examples/er-diagram.drawio` - Blog database schema
- `examples/activity-diagram.xml` - Activity diagram with fork/join
- `examples/ER-Diagram-chen.xml`, `DFD-Context-0.xml`, `Basic-use-case.drawio.xml` - Chen ER, data flow, use case

### Official draw.io Resources
- [Style Reference](https://www.drawio.com/doc/faq/drawio-style-reference.html)
- [XML Schema](https://www.drawio.com/assets/mxfile.xsd)
- [Shape Libraries](https://www.drawio.com/blog/custom-libraries)

## How It Works

1. **You request a diagram** → Claude analyzes the requirements
2. **Claude picks a route** → the MCP `create_diagram` tool if available, otherwise XML written to a file
3. **Repair and validate** → a short Python repair pass, then the Critical Rules and `references/mxfile.xsd`
4. **Deliver** → `.xml` in `/mnt/user-data/outputs/`, or a browser URL on request
5. **Export** → open in draw.io and use File → Export As for PNG, SVG or PDF

## Advanced Tips

### Reusing Diagrams
1. Download your diagram
2. In future conversations, upload it and ask Claude to modify it
3. Claude can read the XML and make changes

### Custom Styling
You can specify colors in your request:
```
Use navy blue for database components (#1a1f5c)
Use light green for API services (#d5e8d4)
```

### Complex Layouts
For large diagrams, request iterative building:
```
First create the high-level architecture
Then add details to the User Service
Then add the database connections
```

## Troubleshooting

**Problem**: Edges don't appear  
**Solution**: Make sure each edge has `<mxGeometry relative="1" as="geometry"/>`

**Problem**: Shapes overlap  
**Solution**: Request more spacing or specific coordinates

**Problem**: Can't open file in draw.io  
**Solution**: Verify the XML is well-formed (no `--` in comments)

**Problem**: Want to export to PNG/PDF  
**Solution**: Open in draw.io desktop → File → Export As → PNG/PDF

## Contributing

Found an issue? Have an example to share?

This skill is based on the official draw.io-mcp project. For the full-featured version:
https://github.com/jgraph/drawio-mcp

## License

MIT License - Based on draw.io-mcp by JGraph

## Credits

- **Original Project**: [draw.io-mcp](https://github.com/jgraph/drawio-mcp) by JGraph
- **Adaptation**: Simplified for claude.ai free tier users
- **draw.io**: © JGraph Ltd

Not affiliated with JGraph or draw.io

## Version

**v1.1.0**
- MCP-aware tool choice, auto-layout options, repair pass, browser URL output
- Stricter XML rules (no comments, container and edge parenting)

**v1.0.0** - Initial release
- Complete mxGraphModel XML generation
- Comprehensive shape library
- Professional styling guides
- Working examples
- Zero external dependencies
