import numpy as np
import rebound
import state

class Observation:
    t = None
    rv = None
    Npoints = 0
    error = 0

class FakeObservation(Observation):
    def __init__(self, state, Npoints=30, error=0., tmax=1.5):
        """
            Generates fake observations. 
        """
        self.Npoints = Npoints
        self.error = error
        sim = state.setup_sim()
        
        self.t = np.sort(np.random.uniform(0.,tmax,self.Npoints))
        self.rv = np.zeros(Npoints)
        for i, t in enumerate(self.t):
            sim.integrate(t)
            self.rv[i] = sim.particles[0].vx + np.random.normal(0.,error)