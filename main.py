# from package.GrannyFactory import GrannyFactory

from package.GrannyState import GrannyState
from package.FloatKnob import FloatKnob
from package.StateKnob import StateKnob
from package.LoadKnob import LoadKnob
from package.GrannySynth import GrannySynth
from package.views.GrannyStateView import GrannyStateView
from package.views.GrannyViewManager import GrannyViewManager
from package.GrannyMediator import GrannyMediator

from package.util import clamp
import threading
import math

if __name__ == "__main__":
    debug = False


    # structure: [name of parameter, default value, increment value, name of state after click]
    #
    #
    newGrannyConfig = {

    }

    grannyConfig = {
        "defaultState": "grainParams",
        "stateConfig": {
            "grainParams": 
            [
                {
                    "name": "grain-length", 
                    "default": 75,
                    "increment": 5,
                    "min": 5, "max": 2000,
                    "newState": "filterParams"
                },
                {
                    "name": "pitch",
                    "default": 1,
                    "increment": 0.1,
                    "min": -4, "max": 4,
                    "newState": "filterParams"
                },
                {
                    "name": "playbackSpeed",
                    "default": 1,
                    "min": -4, "max": 4,
                    "increment": 0.1,
                    "newState": "filterParams"
                },
                {
                    "name": "density",
                    "default": 10,
                    "min": 1, "max": 10,
                    "increment": 1,
                    "newState": "filterParams"
                }
            ],
            "filterParams": 
            [
                {
                    "name": "frequency",
                    "default": 10000,
                    "min": 0, "max": 10000,
                    "increment": 1, "type": "exponential",
                    "newState": "grainParams"
                },
                {
                    "name": "resonance",
                    "default": 0,
                    "min": 0, "max": 4,
                    "increment": 0.1,
                    "newState": "grainParams"
                },
                {
                    "name": "filterType",
                    "default": "lowpass",
                    "type": "state",
                    "states": [ "lowpass", "highpass", "bandpass", "notch" ], 
                    "newState": "grainParams"
                },
                {
                    "name": "falloff",
                    "default": 12,
                    "min": 6, "max": 24,
                    "increment": 2,
                    "newState": "grainParams"
                },
            ]
        }
    }


    # grannyFactory = GrannyFactory()
    # grannySynth = grannyFactory.createGrannySynth(grannyConfig)

    # grannySynth.rotateButton(0, 1)
    # grannySynth.pressButton(2)
    # grannySynth.rotateButton(0, 1)
    # grannySynth.rotateButton(0, 1)
    # grannySynth.rotateButton(0, 1)
    # grannySynth.rotateButton(0, 1)
    # grannySynth.rotateButton(0, 1)
    # grannySynth.pressButton(2)
    # grannySynth.rotateButton(0, 1)

    printMsg = "hellooo"

    def func(msg):
        print(msg)

    def changeMsg():
        print("change Sample!")
        testGranny.rotateKnob(1, 1)

    # timer = threading.Timer(1, func, [printMsg])
    # timer.start()
    timer2 = threading.Timer(2, changeMsg)
    


    # val un baseVal cachen?
    # oder val nicht cachen, nur baseVal, val nur für die Callback Funktionen weiterleiten..
    # val vll in "ParameterMatrix" speichern. View guckt dann auch immer von der Matrix ab
    def changeVal(baseVal, increment):
        baseVal += increment
        val = math.exp(baseVal)
        print(val)
        return baseVal

    # baseVal = 2
    # baseVal = changeVal(baseVal, +1)
    # baseVal = changeVal(baseVal, +6)
    # baseVal = changeVal(baseVal, -0.1)

    grannyViewManager = GrannyViewManager(debug)

    grainState = GrannyState("grain", [
        FloatKnob("length", 100, [], [], 5, 2000, [1000, 100, 10, 1]),
        FloatKnob("pitch", 1, [], [], -4, 4, [1, 0.1, 0.01]),
        FloatKnob("density", 5, [], [], 0, 20, [10, 1, 0.1]),
        FloatKnob("speed", 1, [], [], -4, 4, [1, 0.1, 0.01]),
    ], grannyViewManager)    

    testState = GrannyState("filter", [
        FloatKnob("freq", 440, [], [], 0, 10000, [1000, 100, 10, 1]),
        FloatKnob("resonance", 440, [], [], 0, 10000, [1000, 100, 10, 1]),
        FloatKnob("grainLength", 440, [], [], 0, 10000, [1000, 100, 10, 1]),
        StateKnob("type", "lowpass", [], [], ["lowpass", "highpass", "bandpass", "notch"])
    ], grannyViewManager)

    masterState = GrannyState("master", [
        FloatKnob("volume", 0, [], [], 0, 15, [1, 0.1, 0.01]),
        LoadKnob("sample", [],[]),
        FloatKnob("volume", 0, [], [], 0, 15, [1, 0.1, 0.01]),
        FloatKnob("volume", 0, [], [], 0, 15, [1, 0.1, 0.01]),
    ], grannyViewManager)

    testGranny = GrannySynth([grainState, masterState, testState], masterState)
    
    grannyMediator = GrannyMediator(testGranny, grannyViewManager, debug)

    if debug:
        testGranny.rotateKnob(1, 1)
        testGranny.rotateKnob(2, 1)
        testGranny.rotateKnob(2, 1)
        testGranny.pressKnob(0)
        testGranny.pressKnob(0)

        timer2.start()
    # testGranny.pressKnob(4)

    # testGranny.pressKnob(0)
    # testGranny.rotateKnob(4,1)
    # testGranny.rotateKnob(0,1)

    

    # stateView.changeParam(1, 100)
    # stateView.changeParam(3, "hp")
    # stateView.display()


    # print(testGranny.currentState.parameters)