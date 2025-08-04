import numpy as np
import networkx as nwx
import matplotlib.pyplot as matplt
import matplotlib.lines as matline

# For Task1 + Task2

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

# ---Central Route ---
stations2 = [
    'Holborn Station',
    'Oxford Circus Station',
    'Bond Street Station',
    'Marble Arch Station',
    'Lancaster Gate Station',
    'Queensway Station'
]

edges2 = [
    ('Bond Street Station', 'Oxford Circus Station', 0.5),#493.74
    ('Marble Arch Station', 'Bond Street Station', 0.7),#664.26
    ('Queensway Station', 'Lancaster Gate Station', 0.8),#832.66
    ('Lancaster Gate Station', 'Marble Arch Station', 1.2),#1.19
    ('Oxford Circus Station', 'Holborn Station', 1.5)#1.53
]
# --- Metropolitan Route ---
stations3 = [
    'Charing Cross Station',
    'Piccadilly Circus Station',
    'Oxford Circus Station',
    'Regent’s Park Station',
    'Baker Street Station',
    'Marylebone Station',
]

edges3 = [
    ('Marylebone Station', 'Baker Street Station', 0.4),#420.97
    ('Piccadilly Circus Station', 'Charing Cross Station', 0.6),#602.47
    ('Baker Street Station', 'Regent’s Park Station', 0.7),#703.88
    ('Oxford Circus Station', 'Piccadilly Circus Station', 0.8),#777.88
    ('Regent’s Park Station', 'Oxford Circus Station', 1.0),#990.41
]
# ---Victoria Route ---
stations4 = [
    'King’s Cross & St Pancras Internation Station',
    'Euston Station',
    'Victoria Station',
    'Green Park Station',
    'Oxford Circus Station',
    'Warren Street Station',
]

edges4 = [
    ('Warren Street Station', 'Euston Station', 0.5),#503.22
    ('Euston Station', 'King’s Cross & St Pancras Internation Station', 0.7),#764.98
    ('Green Park Station', 'Oxford Circus Station', 0.9),#924
    ('Oxford Circus Station', 'Warren Street Station', 1.1),#1.08
    ('Victoria Station', 'Green Park Station', 1.1),#1.12
]


# --- Graph ---
Graph = nwx.Graph()
for x, y, z in edges1 + edges2 + edges3 + edges4:
    Graph.add_edge(x, y, weight=z)

# --- Dot position( x, y) ---
dot = {
    # Piccadilly Route
    'Holborn Station': (3, -0.375),
    'Covent Garden Station': (2, -1),
    'Leicester Square Station': (1.1, -1.2),
    'Piccadilly Circus Station': (0.1, -1.2),
    'Green Park Station': (-1.125, -1.2),
    'Hyde Park Corner Station': (-2.7, -1.6),
    # Central Route
    'Holborn Station': (3, -0.375),
    'Oxford Circus Station': (0, 0),
    'Bond Street Station': (-1, 0),
    'Marble Arch Station': (-2.3, -0.375),
    'Lancaster Gate Station': (-4.7, -0.8),
    'Queensway Station': (-6.3, -1),
    # Metropolitan Route
    'Charing Cross Station': (1.1, -1.6),
    'Piccadilly Circus Station': (0.1, -1.2),
    'Oxford Circus Station': (0, 0),
    'Regent’s Park Station': (-1.125, 1.5),
    'Baker Street Station': (-2.65, 1.875),
    'Marylebone Station': (-3.3, 2.3),
    # Victoria Route
    'King’s Cross & St Pancras Internation Station': (3.5, 2.3),
    'Euston Station': (2, 2.3),
    'Warren Street Station': (1.1, 1.875),
    'Green Park Station': (-1.125, -1.2),
    'Victoria Station': (-1.125, -3.35),
    'Oxford Circus Station': (0, 0),
}

# --- Offset label position ---
offset = {
    # Piccadilly Route
    'Green Park Station': (0, -0.4),
    'Covent Garden Station': (0, -0.4),
    'Hyde Park Corner Station': (-0.1, -0.4),
    'Piccadilly Circus Station': (0, -0.4),
    'Leicester Square Station': (0, 0.4),
    'Holborn Station': (0,-0.4),
    # Central Route
    'Lancaster Gate Station': (0, -0.4),
    'Bond Street Station': (0, -0.4),
    'Holborn Station': (0, -0.4),
    'Queensway Station': (0, -0.4),
    'Marble Arch Station': (0, -0.4),
    'Oxford Circus Station': (0, 0.4),
    # Metropolitan Route
    'Baker Street Station': (0, -0.4),
    'Oxford Circus Station': (0, 0.4),
    'Charing Cross Station': (0, -0.4),
    'Marylebone Station': (0, -0.4),
    'Regent’s Park Station': (0, 0.4),
    'Piccadilly Circus Station': (0, -0.4),
    # Victoria Route
    'Green Park Station': (0, -0.4),
    'Warren Street Station': (0, -0.4),
    'King’s Cross & St Pancras Internation Station': (0, -0.4),
    'Victoria Station': (0, -0.4),
    'Oxford Circus Station': (0, 0.4),
    'Euston Station': (0, -0.4),
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
nwx.draw_networkx_nodes(Graph, dot,
                       nodelist=stations2,
                       node_size=800,
                       node_color='red')
nwx.draw_networkx_nodes(Graph, dot,
                       nodelist=stations3,
                       node_size=800,
                       node_color='brown')
nwx.draw_networkx_nodes(Graph, dot,
                       nodelist=stations4,
                       node_size=800,
                       node_color='blue')

# draw Route
nwx.draw_networkx_edges(Graph, dot,
                       edgelist=edges1,
                       width=2,
                       edge_color='darkblue')
nwx.draw_networkx_edges(Graph, dot,
                       edgelist=edges2, 
                       width=2,
                       edge_color='red')
nwx.draw_networkx_edges(Graph, dot,
                       edgelist=edges3,
                       width=2,
                       edge_color='brown')
nwx.draw_networkx_edges(Graph, dot,
                       edgelist=edges4,
                       width=2,
                       edge_color='blue')

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
central_route = matline.Line2D([], [], color='red', label='Central Route')
metropolitan_route = matline.Line2D([], [], color='brown', label='Metropolitan Route')
victoria_route = matline.Line2D([], [], color='blue', label='Victoria Route')
matplt.legend(handles=[piccadilly_route, central_route,metropolitan_route,victoria_route], loc='lower left',
           title="Routes", frameon=True)

matplt.title(" Map of The transportation system", fontsize=14)
matplt.show()

# Task 3

# Acquire all edge values(distance)
edge_weights = list(nwx.get_edge_attributes(Graph, 'weight').values())

# Total network length
nw_total_length = sum(edge_weights)

# Average separation between stations
stt_average_distance = np.mean(edge_weights)

# The gap standard deviation
stt_std_deviation = np.std(edge_weights)

# Print results 
print("=== Metrics from Transport Networks ===")
print(f"Total network length : {nw_total_length} kilometer")
print(f"Average separation between stations(distance) : {stt_average_distance} kilometer")
print(f"The gap standard deviation : {stt_std_deviation} kilometer")
