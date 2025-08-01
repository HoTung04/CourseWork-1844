import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# For Task1 + Task2

# --- Piccadilly line ---
stations1 = [
    'Hyde Park Corner',
    'Green Park',
    'Piccadilly Circus',
    'Leicester Square',
    'Covent Garden',
    'Holborn'
]

edges1 = [
    ('Hyde Park Corner', 'Green Park', 0.8),#784.36
    ('Green Park', 'Piccadilly Circus', 0.7),#696.10
    ('Piccadilly Circus', 'Leicester Square', 0.45),#445.98
    ('Leicester Square', 'Covent Garden', 0.3),#324.85
    ('Covent Garden', 'Holborn', 0.6)#570.37
]

# ---Central line ---
stations2 = [
    'Queensway',
    'Lancaster Gate',
    'Marble Arch',
    'Bond Street',
    'Oxford Circus',
    'Holborn'
]

edges2 = [
    ('Queensway', 'Lancaster Gate', 0.8),#832.66
    ('Lancaster Gate', 'Marble Arch', 1.2),#1.19
    ('Marble Arch', 'Bond Street', 0.7),#664.26
    ('Bond Street', 'Oxford Circus', 0.5),#493.74
    ('Oxford Circus', 'Holborn', 1.5)#1.53
]
# --- Metropolitan line ---
stations3 = [
    'Marylebone',
    'Baker Street',
    'Regent’s Park',
    'Oxford Circus',
    'Piccadilly Circus',
    'Charing Cross'
]

edges3 = [
    ('Marylebone', 'Baker Street', 0.4),#420.97
    ('Baker Street', 'Regent’s Park', 0.7),#703.88
    ('Regent’s Park', 'Oxford Circus', 1.0),#990.41
    ('Oxford Circus', 'Piccadilly Circus', 0.8),#777.88
    ('Piccadilly Circus', 'Charing Cross', 0.6)#602.47
]
# ---Victoria line ---
stations4 = [
    'Victoria',
    'Green Park',
    'Oxford Circus',
    'Warren Street',
    'Euston',
    'King’s Cross & St Pancras Internation'
]

edges4 = [
    ('Victoria', 'Green Park', 1.1),#1.12
    ('Green Park', 'Oxford Circus', 0.9),#924
    ('Oxford Circus', 'Warren Street', 1.1),#1.08
    ('Warren Street', 'Euston', 0.5),#503.22
    ('Euston', 'King’s Cross & St Pancras Internation', 0.7)#764.98
]


# --- Graph ---
G = nx.Graph()
for u, v, d in edges1 + edges2 + edges3 + edges4:
    G.add_edge(u, v, weight=d)

# --- Dot position( x, y) ---
pos = {
    # Piccadilly line
    'Hyde Park Corner': (-2.7, -1.6),
    'Green Park': (-1.125, -1.2),
    'Piccadilly Circus': (0.1, -1.2),
    'Leicester Square': (1.1, -1.2),
    'Covent Garden': (2, -1),
    'Holborn': (3, -0.375),
    # Central line
    'Queensway': (-6.3, -1),
    'Lancaster Gate': (-4.7, -0.8),
    'Marble Arch': (-2.3, -0.375),
    'Bond Street': (-1, 0),
    'Oxford Circus': (0, 0),
    'Holborn': (3, -0.375),
    # Metropolitan line
    'Marylebone': (-3.3, 2.3),
    'Baker Street': (-2.65, 1.875),
    'Regent’s Park': (-1.125, 1.5),
    'Oxford Circus': (0, 0),
    'Piccadilly Circus': (0.1, -1.2),
    'Charing Cross': (1.1, -1.6),
    # Victoria line
    'Victoria': (-1.125, -3.35),
    'Green Park': (-1.125, -1.2),
    'Oxford Circus': (0, 0),
    'Warren Street': (1.1, 1.875),
    'Euston': (2, 2.3),
    'King’s Cross & St Pancras Internation': (3.5, 2.3),
}

# --- Offset label position ---
offset = {
    # Piccadilly line
    'Hyde Park Corner': (-0.1, -0.4),
    'Green Park': (0, -0.4),
    'Piccadilly Circus': (0, -0.4),
    'Leicester Square': (0, 0.4),
    'Covent Garden': (0, -0.4),
    'Holborn': (0,-0.4),
    # Central line
    'Queensway': (0, -0.4),
    'Lancaster Gate': (0, -0.4),
    'Marble Arch': (0, -0.4),
    'Bond Street': (0, -0.4),
    'Oxford Circus': (0, 0.4),
    'Holborn': (0, -0.4),
    # Metropolitan line
    'Marylebone': (0, -0.4),
    'Baker Street': (0, -0.4),
    'Regent’s Park': (0, 0.4),
    'Oxford Circus': (0, 0.4),
    'Piccadilly Circus': (0, -0.4),
    'Charing Cross': (0, -0.4),
    # Victoria line
    'Victoria': (0, -0.4),
    'Green Park': (0, -0.4),
    'Oxford Circus': (0, 0.4),
    'Warren Street': (0, -0.4),
    'Euston': (0, -0.4),
    'King’s Cross & St Pancras Internation': (0, -0.4),
}

# --- Calculate new coordinates for label ---
offset_pos = {node: (pos[node][0] + dx, pos[node][1] + dy)
              for node, (dx, dy) in offset.items()}

# --- Get distance label ---
edge_labels = nx.get_edge_attributes(G, 'weight')

# --- Draw graph ---
plt.figure(figsize=(12, 6))

# Draw dot
nx.draw_networkx_nodes(G, pos,
                       nodelist=stations1,
                       node_color='darkblue',
                       node_size=800)
nx.draw_networkx_nodes(G, pos,
                       nodelist=stations2,
                       node_color='red',
                       node_size=800)
nx.draw_networkx_nodes(G, pos,
                       nodelist=stations3,
                       node_color='brown',
                       node_size=800)
nx.draw_networkx_nodes(G, pos,
                       nodelist=stations4,
                       node_color='blue',
                       node_size=800)

# draw line
nx.draw_networkx_edges(G, pos,
                       edgelist=edges1,
                       edge_color='darkblue',
                       width=2)
nx.draw_networkx_edges(G, pos,
                       edgelist=edges2,
                       edge_color='red',
                       width=2)
nx.draw_networkx_edges(G, pos,
                       edgelist=edges3,
                       edge_color='brown',
                       width=2)
nx.draw_networkx_edges(G, pos,
                       edgelist=edges4,
                       edge_color='blue',
                       width=2)

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
piccadilly_line = mlines.Line2D([], [], color='darkblue', label='Piccadilly Line')
central_line = mlines.Line2D([], [], color='red', label='Central Line')
metropolitan_line = mlines.Line2D([], [], color='brown', label='Metropolitan Line')
victoria_line = mlines.Line2D([], [], color='blue', label='Victoria Line')
plt.legend(handles=[piccadilly_line, central_line,metropolitan_line,victoria_line], loc='lower right',
           title="Lines", frameon=True)

plt.title(" Transport Map", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()

# Task 3

# Get all edge distances
edge_weights = list(nx.get_edge_attributes(G, 'weight').values())

# Total length of the network
total_length = sum(edge_weights)

# Average distance between stations
average_distance = np.mean(edge_weights)

# Standard deviation of distances
std_deviation = np.std(edge_weights)

# Print results 
print("=== Transport Network Statistics ===")
print(f"Total length of the network         : {total_length:.2f} km")
print(f"Average distance between stations  : {average_distance:.2f} km")
print(f"Standard deviation of distances    : {std_deviation:.2f} km")
