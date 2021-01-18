from package.GrannyFactory import GrannyFactory

# structure: [name of parameter, default value, increment value, name of state after click]
#
#

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


grannyFactory = GrannyFactory()
grannySynth = grannyFactory.createGrannySynth(grannyConfig)

grannySynth.rotateButton(0, 1)
grannySynth.pressButton(2)
grannySynth.rotateButton(0, 1)
grannySynth.rotateButton(0, 1)
grannySynth.rotateButton(0, 1)
grannySynth.rotateButton(0, 1)
grannySynth.rotateButton(0, 1)
grannySynth.pressButton(2)
grannySynth.rotateButton(0, 1)