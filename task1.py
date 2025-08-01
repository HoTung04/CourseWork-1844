import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Station list
stations = [
    'Hyde Park Corner',
    'Green Park',
    'Piccadilly Circus',
    'Leicester Square',
    'Covent Garden',
    'Holborn'
]

edges = [
    ('Hyde Park Corner', 'Green Park', 0.8),
    ('Green Park', 'Piccadilly Circus', 0.7),
    ('Piccadilly Circus', 'Leicester Square', 0.45),
    ('Leicester Square', 'Covent Garden', 0.3),
    ('Covent Garden', 'Holborn', 0.6)
]

# Make graph
G = nx.Graph()
for u, v, d in edges:
    G.add_edge(u, v, weight=d)

# dot coordinates( x, y)
pos = {
    'Hyde Park Corner': (0, 0),
    'Green Park': (1, 1),
    'Piccadilly Circus': (2, 1),
    'Leicester Square': (3, 1),
    'Covent Garden': (4, 2),
    'Holborn': (5, 3)
}

# TOffset label position
offset = {
    'Hyde Park Corner': (0, -0.25),
    'Green Park': (0, -0.25),
    'Piccadilly Circus': (0, -0.25),
    'Leicester Square': (0, -0.25),
    'Covent Garden': (0, -0.25),
    'Holborn': (0, -0.25)
}

# Calculate new coordinates for label
offset_pos = {node: (pos[node][0] + dx, pos[node][1] + dy)
              for node, (dx, dy) in offset.items()}

# Get distance label
edge_labels = nx.get_edge_attributes(G, 'weight')

# Draw
plt.figure(figsize=(10, 5))

# Dot and Line
nx.draw_networkx_nodes(G, pos, node_color='blue', node_size=800)
nx.draw_networkx_edges(G, pos, edge_color='blue', width=2)

# line label
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={k: f"{v:.1f} km" for k, v in edge_labels.items()},
    font_size=8
)

# station label
nx.draw_networkx_labels(G, pos,
                        labels={n: "" for n in G.nodes()},
                        font_size=9)
nx.draw_networkx_labels(G, offset_pos,
                        font_size=9,
                        font_family="sans-serif")

# Line annotation
piccadilly_line = mlines.Line2D([], [], color='blue', label='Piccadilly')
plt.legend(handles=[piccadilly_line], loc='lower right',
           title="Key", frameon=True)

plt.title("Piccadilly Line – Task 1", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
