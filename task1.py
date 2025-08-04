import networkx as nwx
import matplotlib.pyplot as matplt
import matplotlib.lines as matline


# --- Piccadilly Route ---
stations1 = [
    'Holborn Station',
    'Covent Garden Station',
    'Leicester Square Station',
    'Piccadilly Circus Station',
    'Green Park Station',
    'Hyde Park Corner Station'
]

edges1 = [
    ('Leicester Square Station', 'Covent Garden Station', 0.3),#324.85
    ('Piccadilly Circus Station', 'Leicester Square Station', 0.45),#445.98
    ('Covent Garden Station', 'Holborn Station', 0.6),#570.37
    ('Green Park Station', 'Piccadilly Circus Station', 0.7),#696.10
    ('Hyde Park Corner Station', 'Green Park Station', 0.8),#784.36
]

# --- Graph ---
Graph = nwx.Graph()
for x, y, z in edges1:
    Graph.add_edge(x, y, weight=z)

# --- Dot position( x, y) ---
dot = {
    # Piccadilly Route
    'Holborn Station': (5, 3),
    'Covent Garden Station': (4, 2),
    'Leicester Square Station':  (3, 1),
    'Piccadilly Circus Station': (2, 1),
    'Green Park Station': (1, 1),
    'Hyde Park Corner Station': (0, 0),
}

# --- Offset label position ---
offset = {
    # Piccadilly Route
    'Green Park Station': (0, -0.25),
    'Covent Garden Station': (0, -0.25),
    'Hyde Park Corner Station': (-0.1, -0.25),
    'Piccadilly Circus Station': (0, -0.25),
    'Leicester Square Station': (0, -0.25),
    'Holborn Station': (0,-0.25),
}
# --- Calculate new coordinates for label ---
offset_dot = {nd: (dot[nd][0] + dx, dot[nd][1] + dy)
              for nd, (dx, dy) in offset.items()}

# --- Get distance label ---
edge_labels = nwx.get_edge_attributes(Graph, 'weight')

# --- Draw graph ---
matplt.figure(figsize=(12, 6))

# Draw dot
nwx.draw_networkx_nodes(Graph, dot,
                       nodelist=stations1,
                       node_size=800,
                       node_color='darkblue')
# draw Route
nwx.draw_networkx_edges(Graph, dot,
                       edgelist=edges1,
                       width=2,
                       edge_color='darkblue')
# Route label
nwx.draw_networkx_edge_labels(
    Graph, dot,
    edge_labels={a: f"{y:.1f} km" for a, y in edge_labels.items()},
    font_size=7
)

# station label
nwx.draw_networkx_labels(Graph, dot,
                        labels={n: "" for n in Graph.nodes()},
                        font_size=8)
nwx.draw_networkx_labels(Graph, offset_dot,
                        font_size=8,
                        font_family="arial")

# Route annotation
piccadilly_route = matline.Line2D([], [], color='darkblue', label='Piccadilly Route')
matplt.legend(handles=[piccadilly_route], loc='upper left',
           title="Routes", frameon=True)

matplt.title(" Map of The transportation system", fontsize=14)
matplt.show()

