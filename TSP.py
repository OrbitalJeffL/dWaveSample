import networkx as nx
import dwave_networkx as dnx
c5 = nx.circular_ladder_graph(5)

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = sampler = EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(c5, sampler))