# Edge Routing and Connection Best Practices

Advanced guide to creating clean, professional edge connections in draw.io diagrams.

## Critical Rule: Edge Geometry

**Every edge MUST have a geometry element**, even without waypoints:

❌ **WRONG** (will not render):
```xml
<mxCell id="e1" edge="1" parent="1" source="a" target="b" style="edgeStyle=orthogonalEdgeStyle;"/>
```

✅ **CORRECT**:
```xml
<mxCell id="e1" edge="1" parent="1" source="a" target="b" style="edgeStyle=orthogonalEdgeStyle;">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Edge Styles

### Orthogonal (Right Angles)
Most common for flowcharts and architecture diagrams.

```xml
<mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Straight Line
Direct connection, no bends.

```xml
<mxCell id="e2" style="edgeStyle=none;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Curved
Smooth curves for organic flows.

```xml
<mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;curved=1;rounded=1;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Elbow
Simple two-segment bend.

```xml
<mxCell id="e4" style="edgeStyle=elbowEdgeStyle;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Connection Points

Control where edges attach to shapes using exit/entry points (values 0-1):

```
exitX=0     # Left edge
exitX=0.5   # Center
exitX=1     # Right edge

exitY=0     # Top edge
exitY=0.5   # Middle
exitY=1     # Bottom edge
```

### Example: Right to Left Connection
```xml
<mxCell style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" 
        edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Example: Top to Bottom
```xml
<mxCell style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" 
        edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Waypoints (Manual Routing)

Add explicit waypoints to control edge path:

```xml
<mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="300" y="150"/>
      <mxPoint x="300" y="250"/>
    </Array>
  </mxGeometry>
</mxCell>
```

### When to Use Waypoints

1. **Avoiding overlaps**: Route around other shapes
2. **Complex flows**: Multiple connections between same nodes
3. **Aesthetic routing**: Creating specific visual paths
4. **Clearing arrow space**: Ensuring room for arrowheads

## Arrow Spacing Best Practices

### Minimum Spacing Guidelines

- **Horizontal spacing**: 200px between shapes
- **Vertical spacing**: 120px between shapes
- **Final segment**: At least 20px before arrowhead
- **Grid alignment**: Position on 10px grid

### Why Spacing Matters

Poor spacing → overlapping arrows:
```
[A] → [B]
       ↓
      [C]
```

Good spacing → clean routing:
```
[A] -----→ [B]
            |
            |
            ↓
           [C]
```

## Avoiding Edge Overlap

### Problem: Multiple edges between same shapes

❌ Bad (edges overlap):
```xml
<!-- Both edges use default routing -->
<mxCell id="e1" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="e2" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

✅ Good (different connection points and waypoints):
```xml
<!-- Top edge -->
<mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=0;entryX=0.5;entryY=0;" 
        edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="150" y="50"/>
      <mxPoint x="350" y="50"/>
    </Array>
  </mxGeometry>
</mxCell>

<!-- Bottom edge -->
<mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;entryX=0.5;entryY=1;" 
        edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="150" y="250"/>
      <mxPoint x="350" y="250"/>
    </Array>
  </mxGeometry>
</mxCell>
```

### Solution: Use Different Sides

```xml
<!-- Exit right, enter left -->
<mxCell id="e1" style="exitX=1;exitY=0.3;entryX=0;entryY=0.3;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- Exit right, enter left (lower position) -->
<mxCell id="e2" style="exitX=1;exitY=0.7;entryX=0;entryY=0.7;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Advanced Routing Techniques

### Jetty Size (Port Offset)

Controls the distance from the shape edge before the first bend:

```xml
<mxCell style="edgeStyle=orthogonalEdgeStyle;jettySize=auto;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Values:
- `jettySize=auto` - Automatic spacing (recommended)
- `jettySize=20` - Fixed 20px offset

### Entry/Exit Perimeter

For shapes that aren't rectangles:

```xml
<mxCell style="exitPerimeter=1;entryPerimeter=1;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Loop Edges (Self-Connections)

```xml
<mxCell id="loop1" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.25;entryX=1;entryY=0.75;" 
        edge="1" parent="1" source="a" target="a">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="280" y="125"/>
      <mxPoint x="280" y="175"/>
    </Array>
  </mxGeometry>
</mxCell>
```

## Arrowhead Styles

### Standard Arrow
```xml
<mxCell style="endArrow=classic;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Both Ends
```xml
<mxCell style="startArrow=classic;endArrow=classic;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### No Arrow
```xml
<mxCell style="endArrow=none;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Block Arrow (Filled)
```xml
<mxCell style="endArrow=block;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Diamond (UML Aggregation)
```xml
<mxCell style="endArrow=diamond;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Hollow Diamond (UML Composition)
```xml
<mxCell style="endArrow=diamondThin;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Edge Labels

### Simple Label
```xml
<mxCell value="Success" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Positioned Label
```xml
<mxCell value="Error" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="a" target="b">
  <mxGeometry x="0.2" y="10" relative="1" as="geometry">
    <mxPoint as="offset"/>
  </mxGeometry>
</mxCell>
```

- `x` value: Position along edge (-1 to 1, where 0 is center)
- `y` value: Offset perpendicular to edge

### Label with Background
```xml
<mxCell value="Important" 
        style="edgeStyle=orthogonalEdgeStyle;labelBackgroundColor=#ffffff;labelBorderColor=#000000;" 
        edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Common Edge Patterns

### Flowchart Decision Branches
```xml
<!-- Decision diamond -->
<mxCell id="dec" value="Valid?" style="rhombus;whiteSpace=wrap;" vertex="1" parent="1">
  <mxGeometry x="150" y="100" width="100" height="80" as="geometry"/>
</mxCell>

<!-- Yes path (right) -->
<mxCell id="yes" value="Yes" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;" 
        edge="1" parent="1" source="dec" target="success">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- No path (down) -->
<mxCell id="no" value="No" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;" 
        edge="1" parent="1" source="dec" target="error">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Architecture Component Communication
```xml
<!-- Bidirectional data flow -->
<mxCell id="api_to_db" value="Query" 
        style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;entryX=0.5;entryY=0;startArrow=classic;endArrow=classic;" 
        edge="1" parent="1" source="api" target="database">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Sequence Diagram Messages
```xml
<!-- Synchronous message -->
<mxCell id="msg1" value="login()" 
        style="edgeStyle=none;endArrow=block;strokeWidth=1.5;" 
        edge="1" parent="1" source="user" target="system">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- Return message (dashed) -->
<mxCell id="ret1" value="success" 
        style="edgeStyle=none;endArrow=open;dashed=1;" 
        edge="1" parent="1" source="system" target="user">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Troubleshooting

### Problem: Arrow overlaps bend

**Cause**: Final segment too short for arrowhead

**Solution**: Increase spacing or add waypoint
```xml
<mxCell style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="250" y="150"/>  <!-- Add waypoint for longer final segment -->
    </Array>
  </mxGeometry>
</mxCell>
```

### Problem: Edges overlap each other

**Cause**: Multiple edges using same path

**Solution**: Use different exit/entry points or waypoints

### Problem: Edge doesn't connect

**Cause**: Missing geometry element or invalid source/target

**Solution**: Always include `<mxGeometry relative="1" as="geometry"/>`

## Layout Tips

1. **Start with spacing**: Position nodes 200px apart horizontally
2. **Grid alignment**: Snap to 10px grid for clean look
3. **Test connections**: Add edges after positioning all nodes
4. **Adjust waypoints last**: Fine-tune routing after basic layout
5. **Use rounded edges**: Add `rounded=1` for professional appearance

## Complete Example: Complex Routing

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    
    <!-- Nodes -->
    <mxCell id="a" value="Start" style="ellipse;whiteSpace=wrap;" vertex="1" parent="1">
      <mxGeometry x="40" y="100" width="80" height="80" as="geometry"/>
    </mxCell>
    
    <mxCell id="b" value="Process" style="rounded=1;whiteSpace=wrap;" vertex="1" parent="1">
      <mxGeometry x="200" y="110" width="120" height="60" as="geometry"/>
    </mxCell>
    
    <mxCell id="c" value="Decision" style="rhombus;whiteSpace=wrap;" vertex="1" parent="1">
      <mxGeometry x="210" y="230" width="100" height="80" as="geometry"/>
    </mxCell>
    
    <mxCell id="d" value="End" style="ellipse;whiteSpace=wrap;" vertex="1" parent="1">
      <mxGeometry x="220" y="370" width="80" height="80" as="geometry"/>
    </mxCell>
    
    <!-- Edges with proper routing -->
    <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="a" target="b">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    
    <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="b" target="c">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    
    <mxCell id="e3" value="Yes" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=1;" 
            edge="1" parent="1" source="c" target="d">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    
    <!-- Loop back with waypoints -->
    <mxCell id="e4" value="No" 
            style="edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.5;entryX=0;entryY=0.5;rounded=1;" 
            edge="1" parent="1" source="c" target="b">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="160" y="270"/>
          <mxPoint x="160" y="140"/>
        </Array>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>
```
