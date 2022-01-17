// globals.js
// globally defined variables

var _elementList = [];
var _currentElementClass = null;
var _currentPointList = [];

var _xGrid = 20;
var _yGrid = 40;

var _2DView;
var _3DView;

var ess;
var _current_time = 0;
var _chart_data = [{ x: [], y: [], type: 'line'}];
var   _time_values = [];
var _power_values = [];

var _ambientVal = 50;


var appliance_default_color =
    {
        r: 214,
        g: 214,
        b: 214
    }


// Sources
var sources = [];

// Circuits
var circuits = [];

// Loads
var loads = [];
