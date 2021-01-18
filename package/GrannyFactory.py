from package.GrannyState import GrannyState
from package.GButton import GButton
from package.GrannySynth import GrannySynth

class GrannyFactory:

    def createGrannySynth(self, config):
        stateConfig = config["stateConfig"]

        grannyStates = {}
        grannySynth = GrannySynth()

        for stateName in stateConfig:
            grannyStates[stateName] = GrannyState(stateName)
            if stateName == config["defaultState"]:
                grannySynth.currentState = grannyStates[stateName]

        for stateName in stateConfig:
            state = stateConfig[stateName]
            for i in range(len(state)):
                buttonConfig = state[i]
                buttonConfig["newState"] = grannyStates[buttonConfig["newState"]]
                grannyStates[stateName].buttons[i] = GButton(buttonConfig)
        
        return grannySynth