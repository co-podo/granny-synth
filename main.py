from package.GrannyFactory import GrannyFactory
from package.GrannyState import GrannyState
from package.FloatKnob import FloatKnob
from package.StateKnob import StateKnob
from package.GrannySynth import GrannySynth

from package.util import clamp
import threading
import math


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
    timer.cancel()
    print("timer cancelled")

# timer = threading.Timer(1, func, [printMsg])
# timer.start()
# timer2 = threading.Timer(0.5, changeMsg)
# timer2.start()


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
testState = GrannyState("testState", [
    FloatKnob("freq", 440, [], [], 0, 10000, 100, 10, "linear"),
    FloatKnob("resonance", 440, [], [], 0, 10000, 100, 10, "linear"),
    FloatKnob("grainLength", 440, [], [], 0, 10000, 100, 10, "linear"),
    StateKnob("type", "lowpass", ["lowpass", "highpass", "bandpass", "notch"])
])

testState2 = GrannyState("testState2", [
    FloatKnob("freq", 440, [], [], 0, 10000, 100, 10, "linear"),
    FloatKnob("resonance", 440, [], [], 0, 10000, 100, 10, "linear"),
    FloatKnob("grainLength", 440, [], [], 0, 10000, 100, 10, "linear"),
    StateKnob("type", "lowpass", ["lowpass", "highpass", "bandpass", "notch"])
])

testGranny = GrannySynth([testState, testState2], testState)
testGranny.rotateKnob(3, 1)

print(testGranny.parameters)