import random
from deap import base, creator, tools, algorithms

class GeneticProgrammingEngine:
    def __init__(self):
        self.toolbox = base.Toolbox()
        self._setup_toolbox()

    def _setup_toolbox(self):
        # Define primitive set and evaluation function
        pset = self._define_primitive_set()
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)
        self.toolbox.register("expr", tools.initRepeat, creator.Individual, pset.terminals[0], n=random.randint(1, 5))
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.expr)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

    def _define_primitive_set(self):
        pset = gp.PrimitiveSetTyped("MAIN", [], str)
        pset.addPrimitive(str.lower, [str], str)
        pset.addPrimitive(str.upper, [str], str)
        pset.addTerminal("import numpy as np", str)
        return pset

    def optimize(self, code):
        population = self.toolbox.population(n=50)
        hof = tools.HallOfFame(1)

        stats_fit = tools.Statistics(lambda ind: ind.fitness.values[0])
        stats_size = tools.Statistics(len)
        mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
        mstats.register("avg", np.mean)
        mstats.register("std", np.std)
        mstats.register("min", np.min)
        mstats.register("max", np.max)

        algorithms.eaSimple(population, self.toolbox, cxpb=0.5, mutpb=0.2, ngen=40, stats=mstats,
                            halloffame=hof, verbose=True)

        return hof[0]

# Example usage
if __name__ == "__main__":
    genetic_engine = GeneticProgrammingEngine()
    optimized_code = genetic_engine.optimize("import numpy as np")
    print(optimized_code)
