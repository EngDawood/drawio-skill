# Draw.io Styling Reference

Complete guide to styling draw.io diagrams for professional, consistent visuals.

## Color Palettes

### Blue Scheme (Professional)
```
fillColor=#dae8fc;strokeColor=#6c8ebf
```
Use for: Primary processes, main components, information

### Green Scheme (Success/Start)
```
fillColor=#d5e8d4;strokeColor=#82b366
```
Use for: Start states, success paths, valid data

### Orange Scheme (Warning/Decision)
```
fillColor=#ffe6cc;strokeColor=#d79b00
```
Use for: Decisions, warnings, conditional logic

### Red Scheme (Error/Stop)
```
fillColor=#f8cecc;strokeColor=#b85450
```
Use for: Error states, end states, invalid data

### Gray Scheme (Neutral/Infrastructure)
```
fillColor=#f5f5f5;strokeColor=#666666
```
Use for: Infrastructure, external systems, passive elements

### Purple Scheme (Special/Authentication)
```
fillColor=#e1d5e7;strokeColor=#9673a6
```
Use for: Security, authentication, special processes

## Font Styling

### Basic Text
```xml
fontSize=12;fontColor=#333333;fontFamily=Helvetica
```

### Bold Text
```xml
fontStyle=1
```
Note: 1=bold, 2=italic, 3=bold+italic, 4=underline

### Large Headers
```xml
fontSize=16;fontStyle=1;fontColor=#000000
```

### Small Labels
```xml
fontSize=10;fontColor=#666666
```

### HTML Formatting
```xml
<mxCell value="&lt;b&gt;Bold&lt;/b&gt; and &lt;i&gt;Italic&lt;/i&gt;" style="text;html=1;"/>
```

## Alignment

### Horizontal Alignment
```
align=left    # Left align
align=center  # Center (default)
align=right   # Right align
```

### Vertical Alignment
```
verticalAlign=top     # Top
verticalAlign=middle  # Middle (default)
verticalAlign=bottom  # Bottom
```

### Combined Example
```xml
style="rounded=1;align=left;verticalAlign=top;whiteSpace=wrap;"
```

## Border Styling

### Solid Border
```
strokeColor=#6c8ebf;strokeWidth=2
```

### Dashed Border
```
strokeColor=#6c8ebf;strokeWidth=2;dashed=1
```

### Dotted Border
```
strokeColor=#6c8ebf;strokeWidth=2;dashed=1;dashPattern=1 4
```

### No Border
```
strokeColor=none
```

### Shadow
```
shadow=1
```

## Shape-Specific Styling

### Rounded Corners
```
rounded=1;arcSize=10  # arcSize controls roundness (0-50)
```

### Glass Effect
```
glass=1;fillColor=#ffffff;opacity=50
```

### Sketch Style
```
sketch=1;curveFitting=1
```

## Edge Styling

### Basic Arrow
```xml
<mxCell style="edgeStyle=orthogonalEdgeStyle;strokeColor=#6c8ebf;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Thick Arrow
```
strokeWidth=3
```

### Dashed Arrow
```
dashed=1;dashPattern=5 5
```

### Curved Arrow
```
edgeStyle=orthogonalEdgeStyle;curved=1;rounded=1
```

### Start/End Arrow Styles
```
startArrow=classic;endArrow=classic  # Both ends have arrows
startArrow=none;endArrow=classic     # Arrow at end only
endArrow=block                        # Filled arrow
endArrow=open                         # Open arrow
endArrow=diamond                      # Diamond (for aggregation)
endArrow=diamondThin                  # Hollow diamond (for composition)
```

### Arrow Size
```
startSize=6;endSize=6  # Default is 6
```

## Common Edge Styles

### Orthogonal (Right Angles)
```
edgeStyle=orthogonalEdgeStyle;rounded=1
```

### Straight Line
```
edgeStyle=none
```

### Curved Line
```
edgeStyle=orthogonalEdgeStyle;curved=1
```

### Elbow Connector
```
edgeStyle=elbowEdgeStyle
```

## Text on Edges

### Edge Label
```xml
<mxCell value="Label Text" style="edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="a" target="b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Label Position
```
labelPosition=center    # Center of edge (default)
labelPosition=source    # Near source
labelPosition=target    # Near target
```

### Label Background
```
labelBackgroundColor=#ffffff;labelBorderColor=#000000
```

## Container Styling

### Swimlane with Title
```xml
<mxCell value="Title" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
```

### Transparent Container
```
fillColor=none;strokeColor=none;pointerEvents=0
```

### Group (Invisible Container)
```
group;pointerEvents=0
```

## Opacity and Transparency

### Semi-Transparent Fill
```
opacity=50  # 0-100, where 100 is fully opaque
```

### Transparent Background
```
fillColor=none
```

## Gradients

### Vertical Gradient
```
fillColor=#dae8fc;gradientColor=#ffffff;gradientDirection=south
```

### Horizontal Gradient
```
fillColor=#dae8fc;gradientColor=#ffffff;gradientDirection=east
```

Gradient directions: `north`, `south`, `east`, `west`

## Complete Style Examples

### Professional Process Box
```xml
<mxCell value="Process Step" 
        style="rounded=1;whiteSpace=wrap;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=12;fontColor=#333333;shadow=1" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="70" as="geometry"/>
</mxCell>
```

### Important Decision Diamond
```xml
<mxCell value="Critical Decision?" 
        style="rhombus;whiteSpace=wrap;fillColor=#ffe6cc;strokeColor=#d79b00;strokeWidth=2;fontSize=12;fontStyle=1" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="140" height="100" as="geometry"/>
</mxCell>
```

### Database with Shadow
```xml
<mxCell value="User Database" 
        style="shape=cylinder3;whiteSpace=wrap;fillColor=#f5f5f5;strokeColor=#666666;shadow=1;fontSize=11" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="300" width="120" height="90" as="geometry"/>
</mxCell>
```

### Highlighted Service Container
```xml
<mxCell value="Authentication Service" 
        style="swimlane;startSize=30;fillColor=#e1d5e7;strokeColor=#9673a6;strokeWidth=2;fontSize=13;fontStyle=1" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="350" height="250" as="geometry"/>
</mxCell>
```

## Style Composition Tips

### Combine Multiple Styles
Use semicolons to separate style properties:
```
rounded=1;whiteSpace=wrap;fillColor=#dae8fc;strokeColor=#6c8ebf;shadow=1
```

### Order Doesn't Matter
These are equivalent:
```
fillColor=#dae8fc;strokeColor=#6c8ebf
strokeColor=#6c8ebf;fillColor=#dae8fc
```

### Override Defaults
Later properties override earlier ones:
```
fillColor=#dae8fc;fillColor=#ffffff  # Result: white fill
```

## Accessibility Guidelines

### High Contrast
```
fillColor=#ffffff;strokeColor=#000000;fontColor=#000000;strokeWidth=2
```

### Color-Blind Friendly Palette
- Blue: `#0072B2`
- Orange: `#E69F00`
- Green: `#009E73`
- Yellow: `#F0E442`
- Red: `#D55E00`
- Purple: `#CC79A7`
- Gray: `#999999`

### Text Readability
```
fontSize=12  # Minimum for readability
strokeWidth=2  # Ensures visibility
```

## Performance Tips

1. Reuse style strings for similar elements
2. Avoid overly complex gradients
3. Limit shadow usage to key elements
4. Keep strokeWidth reasonable (1-3 for most cases)

## Common Mistakes to Avoid

❌ Missing semicolons between properties:
```
fillColor=#dae8fc strokeColor=#6c8ebf  # WRONG
```

✅ Correct:
```
fillColor=#dae8fc;strokeColor=#6c8ebf
```

❌ Invalid color formats:
```
fillColor=blue  # WRONG (use hex)
fillColor=#dae8fc  # CORRECT
```

❌ Conflicting styles:
```
rounded=1;rounded=0  # Confusing, last one wins
```

## Official Reference

For the complete style reference:
https://www.drawio.com/doc/faq/drawio-style-reference.html
