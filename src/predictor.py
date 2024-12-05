import pylab as plt
import networkx as nx

from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator, HillClimbSearch, BicScore


class Predictor(object):
    def __init__(self, data, target):
        self._data = data
        self._target = target
        self._model = None

    def _verify_model_created(self):
        if self._model is None:
            raise RuntimeError('The model is not created')

    def _generate_optimal_model_structure(self):
        hill_climb_search = HillClimbSearch(self._data)
        scoring_method = BicScore(self._data)

        return hill_climb_search.estimate(scoring_method=scoring_method)

    def _generate_model(self):
        optimal_model_structure = self._generate_optimal_model_structure()
        optimal_model_structure_edges = optimal_model_structure.edges()

        return BayesianNetwork(optimal_model_structure_edges)

    def _estimate_model_parameters(self, model):
        model.fit(self._data, estimator=MaximumLikelihoodEstimator)

    def create_model(self):
        if self._model is not None:
            return

        self._model = self._generate_model()
        self._estimate_model_parameters(self._model)

    def perform_inference(self, evidence):
        self.create_model()

        variables = [self._target]
        inference = VariableElimination(self._model)

        return inference.query(variables=variables, evidence=evidence)

    def get_model_cpds(self):
        self._verify_model_created()
        return self._model.get_cpds()

    def get_model_independencies(self):
        self._verify_model_created()
        return self._model.get_independencies()

    def save_model_structure(self, output_path='bn_structure.png'):
        self._verify_model_created()

        model_graphviz = self._model.to_graphviz()
        model_graphviz.draw(output_path, prog='dot')

    def show_model_structure(self):
        self._verify_model_created()

        nx_graph = nx.DiGraph(self._model.edges())
        nx.draw(nx_graph, with_labels=True)
        plt.show()
