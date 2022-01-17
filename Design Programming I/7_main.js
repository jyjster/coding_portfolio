// Main.js
// Contains:
// - change time on clock graphic
// - change appliance color on 3d model


// Function onLoad is where any preliminary setup happens
function onLoad() {

  _2DView = new View2D();
  _3DView = new View3D();


  _currentElementClass = EllipseOnePointElement;


}


function on_update_time() {
    // console.log("on update time");
    _chart_data = [{
        x : _time_values,
        y : _power_values,
        mode : 'lines',
        marker: {
          color: 'rgb(255, 0, 0)'
        }
        // type: 'scatter'
    }];
    var layout = {
      xaxis : {
          range: [0, 24],
          title: {
            text: 'Time (hours)'
          }
      },
      yaxis: {
          range: [0, 50000],
          type: 'linear', 
          title: {
            text: 'Battery Capacity (watt hours)'
          }
          
      }
      // https://plotly.com/javascript/figure-labels/
    }
      // title: 'Battery Capacity by Hours',
      //   };

    // console.log(_chart_data);

    // line_chart_DIV
    // Plotly.react('line_chart_DIV', _chart_data);
    Plotly.newPlot('line_chart_DIV', _chart_data, layout);
}

function onResize() {

  var div2d = document.getElementById("Canvas2DDIV");
  _2DView.p5.resizeCanvas(div2d.clientWidth, div2d.clientHeight);
  var div3d = document.getElementById("Canvas2DDIV");
  _3DView.p5.resizeCanvas(div3d.clientWidth, div3d.clientHeight);

}

function onClassChange(aclass) {
  _currentElementClass = eval(aclass);
}


function change_appliance_color(appliance) {
  // set every appliance to the (same) default color
  for (let i = 0; i < appliance_list.length; i++) {
    appliance_list[i].current_color.r = appliance_default_color.r;
    appliance_list[i].current_color.g = appliance_default_color.g;
    appliance_list[i].current_color.b = appliance_default_color.b;

    appliance_list[i].selected = false;

    // if the appliance list item is the appliance that was called/passed in, then change that appliance's current color to its select color
    if (appliance_list[i].name == appliance) {
      appliance_list[i].selected = true;
      appliance_list[i].current_color.r = appliance_list[i].select_color.r;
      appliance_list[i].current_color.g = appliance_list[i].select_color.g;
      appliance_list[i].current_color.b = appliance_list[i].select_color.b;
    }
  }



}

function onChangeAmbientValue(aval) {
  _ambientVal = aval;

}

