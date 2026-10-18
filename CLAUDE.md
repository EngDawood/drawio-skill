# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Not an application: a single Claude skill (`skills/drawio/`) that teaches Claude to emit draw.io diagrams as raw `mxGraphModel` XML. There is no build, lint, or test tooling, and no package manifest. The top-level `README.md` is a stub; the real user docs are `skills/drawio/README.md`.

Based on JGraph's official [drawio-mcp](https://github.com/jgraph/drawio-mcp). The skill works standalone (writes XML files) and defers to the draw.io MCP server's `create_diagram` tool when it is available. `.mcp.json` registers the remote server `https://mcp.draw.io/mcp`. The skill deliberately does not mention or depend on the draw.io desktop CLI; keep it that way.

## Layout

- `skills/drawio/SKILL.md` — the skill entry point (frontmatter `name`/`description` drive triggering). Sections: tool choice (MCP vs file), steps, auto-layout (`postLayout`/`routing` of `create_diagram`), Critical Rules, repair pass, output formats, references (local plus upstream `shared/` URLs), examples. Keep it short; it points into `references/`, `examples/` and `scripts/` rather than duplicating them.
- `skills/drawio/references/` — detail docs loaded on demand. `style-reference.md` is the primary one (the SKILL.md calls it the main document for generating valid files); `xml-reference.md`, `styles.md`, `shapes.md`, `edge-routing.md`, `mermaid-reference.md` supplement it. `mxfile.xsd` is the schema for validating generated output.
- `skills/drawio/scripts/` — `repair_xml.py` (fixes common XML slips in place) and `drawio_url.py` (prints an app.diagrams.net URL for a file).
- `skills/drawio/examples/` — working diagrams (flowchart, architecture, ER, activity, plus Chen ER, DFD, and use-case XML).

## Conventions to preserve when editing

- Output contract: the skill tells Claude to write diagrams to `/mnt/user-data/outputs/` with a `.xml` extension (deliberately not `.drawio`, because claude.ai's UI cannot copy DRAWIO-type files). Keep that consistent across SKILL.md and any docs you touch.
- The "Critical Rules" in SKILL.md (no XML comments, unique cell ids, every edge needs `<mxGeometry relative="1" as="geometry"/>`, escaped special chars, layer parenting, container/edge parents, 10px grid) are load-bearing for generated-file validity; examples should obey them.
- Changing a reference or example may require updating the lists that name them in `SKILL.md` and `skills/drawio/README.md`.

## Validating an example or generated diagram

No script exists. To check well-formedness and schema conformance manually (if `xmllint` is available):

```bash
xmllint --noout skills/drawio/examples/flowchart.drawio
xmllint --noout --schema skills/drawio/references/mxfile.xsd <file>
```
