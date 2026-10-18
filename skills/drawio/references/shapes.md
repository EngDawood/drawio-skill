# Draw.io Shape Reference

Complete reference for all commonly used shapes in draw.io diagrams.

## Basic Shapes

### Rectangle
```xml
<mxCell id="rect1" value="Label" style="whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

### Rounded Rectangle
```xml
<mxCell id="rect2" value="Label" style="rounded=1;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

### Diamond (Decision)
```xml
<mxCell id="dia1" value="Decision?" style="rhombus;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="120" height="80" as="geometry"/>
</mxCell>
```

### Circle/Ellipse
```xml
<mxCell id="cir1" value="Start" style="ellipse;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="50" width="80" height="80" as="geometry"/>
</mxCell>
```

### Cylinder (Database)
```xml
<mxCell id="cyl1" value="Database" style="shape=cylinder3;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="200" y="300" width="100" height="80" as="geometry"/>
</mxCell>
```

## Flowchart Shapes

### Process
```xml
<mxCell id="proc" value="Process" style="rounded=1;whiteSpace=wrap;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

### Decision
```xml
<mxCell id="dec" value="Decision?" style="rhombus;whiteSpace=wrap;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="120" height="80" as="geometry"/>
</mxCell>
```

### Start/End (Terminator)
```xml
<mxCell id="term" value="Start" style="ellipse;whiteSpace=wrap;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="120" y="40" width="80" height="80" as="geometry"/>
</mxCell>
```

### Document
```xml
<mxCell id="doc" value="Document" style="shape=document;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="300" width="120" height="80" as="geometry"/>
</mxCell>
```

### Data Store
```xml
<mxCell id="data" value="Data" style="shape=datastore;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="400" width="100" height="60" as="geometry"/>
</mxCell>
```

### Predefined Process
```xml
<mxCell id="preproc" value="Subprocess" style="shape=process;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="500" width="120" height="60" as="geometry"/>
</mxCell>
```

## UML Shapes

### Class
```xml
<mxCell id="class1" value="&lt;b&gt;User&lt;/b&gt;&lt;hr&gt;+id: int&lt;br&gt;+name: string&lt;hr&gt;+login(): void" 
        style="whiteSpace=wrap;align=left;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="120" as="geometry"/>
</mxCell>
```

### Actor
```xml
<mxCell id="actor1" value="User" style="shape=umlActor;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="60" height="120" as="geometry"/>
</mxCell>
```

### Note
```xml
<mxCell id="note1" value="Important note" style="shape=note;whiteSpace=wrap;size=10;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="80" as="geometry"/>
</mxCell>
```

## Architecture Shapes

### Server
```xml
<mxCell id="srv1" value="Web Server" style="shape=cube;whiteSpace=wrap;boundedLbl=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="80" as="geometry"/>
</mxCell>
```

### Cloud
```xml
<mxCell id="cloud1" value="Cloud" style="ellipse;shape=cloud;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="80" as="geometry"/>
</mxCell>
```

### Queue
```xml
<mxCell id="queue1" value="Message Queue" style="shape=parallelogram;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
</mxCell>
```

## Container Shapes

### Swimlane (Horizontal)
```xml
<mxCell id="swim1" value="Service Layer" style="swimlane;startSize=30;horizontal=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="400" height="200" as="geometry"/>
</mxCell>
```

### Swimlane (Vertical)
```xml
<mxCell id="swim2" value="Component" style="swimlane;startSize=30;horizontal=0;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="200" height="300" as="geometry"/>
</mxCell>
```

### Group (Invisible)
```xml
<mxCell id="grp1" value="" style="group;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
```

## Network Shapes

### Router
```xml
<mxCell id="rtr1" value="Router" style="shape=mxgraph.network.router;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="80" height="60" as="geometry"/>
</mxCell>
```

### Firewall
```xml
<mxCell id="fw1" value="Firewall" style="shape=mxgraph.network.firewall;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="80" height="60" as="geometry"/>
</mxCell>
```

## Text and Labels

### Text Box
```xml
<mxCell id="txt1" value="Description text here" style="text;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="200" height="40" as="geometry"/>
</mxCell>
```

### Label (HTML)
```xml
<mxCell id="lbl1" value="&lt;b&gt;Bold&lt;/b&gt;&lt;br&gt;&lt;i&gt;Italic&lt;/i&gt;" 
        style="text;html=1;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

## Common Style Properties

| Property | Example | Description |
|----------|---------|-------------|
| `rounded=1` | `rounded=1` | Rounded corners |
| `whiteSpace=wrap` | `whiteSpace=wrap` | Text wrapping |
| `fillColor` | `fillColor=#dae8fc` | Background color |
| `strokeColor` | `strokeColor=#6c8ebf` | Border color |
| `fontColor` | `fontColor=#333333` | Text color |
| `fontSize` | `fontSize=14` | Font size in pixels |
| `fontStyle` | `fontStyle=1` | Bold (1), Italic (2), Bold+Italic (3) |
| `align` | `align=left` | Text alignment (left/center/right) |
| `verticalAlign` | `verticalAlign=top` | Vertical alignment (top/middle/bottom) |
| `dashed` | `dashed=1` | Dashed border |
| `strokeWidth` | `strokeWidth=2` | Border thickness |

## Shape-Specific Properties

### Cylinder
- `size`: Depth of the 3D effect (default: 15)
```xml
style="shape=cylinder3;size=20;"
```

### Document
- `size`: Size of the wave at bottom (default: 0.2)
```xml
style="shape=document;size=0.3;"
```

### Note
- `size`: Size of the folded corner (default: 10)
```xml
style="shape=note;size=15;"
```

## Complete Example

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    
    <!-- Start -->
    <mxCell id="start" value="Start" style="ellipse;whiteSpace=wrap;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
      <mxGeometry x="140" y="40" width="80" height="80" as="geometry"/>
    </mxCell>
    
    <!-- Process -->
    <mxCell id="proc1" value="Process Data" style="rounded=1;whiteSpace=wrap;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
      <mxGeometry x="120" y="160" width="120" height="60" as="geometry"/>
    </mxCell>
    
    <!-- Database -->
    <mxCell id="db1" value="Store" style="shape=cylinder3;whiteSpace=wrap;fillColor=#f5f5f5;strokeColor=#666666;" vertex="1" parent="1">
      <mxGeometry x="130" y="260" width="100" height="80" as="geometry"/>
    </mxCell>
    
    <!-- Edge -->
    <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="start" target="proc1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    
    <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="proc1" target="db1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>
```

## Finding More Shapes

For the complete shape library including cloud provider icons (AWS, Azure, GCP), network equipment, and more:
- https://www.drawio.com/doc/faq/shape-complex-create-edit
- https://www.drawio.com/blog/custom-libraries
