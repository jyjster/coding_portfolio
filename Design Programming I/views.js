//  Views.js
// Contains:
//  - View for 3d model
//  - pie_chart
//  - clock graphic




function clock(my_hour){
  // clock code from https://github.com/Maccauhuru/Analog-Clock-JavaScript
  // console.log("hour", my_hour);

  // DIV
  const hourHand   = document.querySelector("#hour");
  const minuteHand = document.querySelector("#minute");



  //Get our local date & time
  let date = new Date();
  let currentHour = my_hour;
  let currentMinute = 0;

  //Convert Hour,Minutes & Seconds to degrees equivalents
  let hourPosition = (currentHour * 360 / 12)
  let minutePosition = (currentMinute * 360 / 60)
  // + (currentMinute * (360 / 60) / 12);    // Hour plus precise minutes
  // let minutePosition = (currentMinute * 360 / 60); // 60; // Minutes plus milliseconds


  function getCurrentTime(){
      hourPosition = hourPosition + (3 / 360)
      minutePosition = minutePosition + (6 / 60);

      hourHand.style.transform = "rotate(" + hourPosition + "deg )";
      minuteHand.style.transform = "rotate(" + minutePosition + "deg )";
  }

  // let timeInterval = setInterval(getCurrentTime, 1000);
  let time = getCurrentTime();

}

/////////////////////////////
function pie_chart(title, div, entities) {
    // console.log("pie_chart called");
    // https://plotly.com/javascript/reference/pie/

    var my_values = [];
    var my_labels = [];
    var my_colors = [];

    for (let i = 0; i < entities.length; i++) {
      var entity_loads = entities[i].get_downstream_load();
      if(entity_loads > 0){
          my_values.push(entity_loads);
          my_labels.push(entities[i].name);
          my_colors.push(entities[i].pie_color());
      }
    }

    var data = [{
      values: my_values,
      labels: my_labels,
      // marker: {colors: my_colors}
      marker: {colors: my_colors, line: {color:'#ffffff', width: 1}},
      type: 'pie',
      textinfo: 'label',
      textfont: {size: 15}
      // title: {text: title, position:"top center"}
    }];

    var layout = {
      height: 400,
      width: 400,
      showlegend: false,
      margin: {l: 50, t: 0, b: 0}
      // https://plotly.com/javascript/reference/layout/#layout-margin
      // showlegend: true
    };

    Plotly.newPlot(div, data, layout);

}


  /////////////////////   2D draw() function     ////////////////////////
  p5.draw = function() {
    // background(100);
    // background(0,255,0);
    p5.background(rect_color);
    // p5.translate(-150,0);
    // pieChart(300, current_data);

  }


/////////////////////      house_3D function - generates a P5 instance for the 3D view  ///////////////////////
var house_3D = function (p5) {
    var zoom = 0.60;

  //define variables for our media
    // IMAGE TEXTURES
    let wood_1;
    let wood_2;
    // OJBECTS
    let floor;
    let doors;
    let walls_int;
    let walls_ext;

    // Loads
    let fridge;
    let dryer;
    let microwave;
    let furnace;
    let water_heater;
    let stove;


    // point lights
    let light_1;
    let light_2;
    let light_3;
    let light_4;
    let light_5;

    let oven;
    let washer;

    let computer_1;
    let computer_2;
    let computer_3;

    let tv;
    let wifi;

    // let fan_1;
    // let fan_2;
    // let fan_3;

    let angle = 0;
    let furniture;
    let furniture_2;


  /////////////////////   3D preload() function     ////////////////////////

  p5.preload = function() {
      // Load model with normalise parameter set to false
      floor = p5.loadModel('media/floor.obj', false); // Imported 3D object
      doors = p5.loadModel('media/doors.obj', false); // Imported 3D object
      walls_int = p5.loadModel('media/walls_int.obj', false); // Imported 3D object
      walls_ext = p5.loadModel('media/walls_ext.obj', false); // Imported 3D object
      // stairs = p5.loadModel('media/stairs-2.obj', false); // Imported 3D object
      furniture = p5.loadModel('media/furniture.obj', false);
      furniture_2 = p5.loadModel('media/furniture-2.obj', false);
    
      // Imported 3D object
      // source: https://alquilercastilloshinchables.info/wood-floor-texture-seamless/
      wood_1 = p5.loadImage('media/wood.jpeg'); // MATERIAL #1
      // source: https://www.freecreatives.com/textures/seamless-wood-textures.html
      wood_2 = p5.loadImage('media/wood_2.png'); // MATERIAL #2

      fridge = new Fridge_load("kitchen fridge");
      fridge.preload_model(p5);

      water_heater = new Water_heater_load("hot water heater");
      water_heater.preload_model(p5);

      dryer = new Dryer_load("laundry dryer");
      dryer.preload_model(p5);

      microwave = new Microwave_load("kitchen microwave");
      microwave.preload_model(p5);

      furnace = new Furnace_load("furnace hvac");
      furnace.preload_model(p5);

      stove = new Stove_load("kitchen stove");
      stove.preload_model(p5);

      oven = new Oven_load("kitchen oven");
      oven.preload_model(p5);

      washer = new Washer_load("laundry washer");
      washer.preload_model(p5);

      light_1 = new Light_load("front bedroom light", 190, 120,  108, 200, 5);
      light_1.preload_model(p5);

      light_2 = new Light_load("office light", -180, -150, 108, 108, 5);
      light_2.preload_model(p5);

      light_3 = new Light_load("back bedroom light", 190, -150, 108, 108, 5);
      light_3.preload_model(p5);

      light_4 = new Light_load("office light", -180, 120, 108, 200, 5);
      light_4.preload_model(p5);

      light_5 = new Light_load("kitchen light", 20, 0, 108, 200, 5);
      light_5.preload_model(p5);
      

      computer_1 = new Computer_load("office computer 1", -175, -200, 36, 0);
      computer_1.preload_model(p5);

      computer_2 = new Computer_load("office computer 2", -235, -200, 36, 0);
      computer_2.preload_model(p5);

      computer_3 = new Computer_load("bedroom computer", 120, 170, 56, -90);
      computer_3.preload_model(p5);


      tv = new TV_load("television");
      tv.preload_model(p5);

      wifi = new Wifi_load("wifi router");
      wifi.preload_model(p5);


      // Assign loads to circuits
      //{r : 0, g : 0, b : 255, alpha: 255}
      // ffd166
     //  test_color = {r : 0, g : 0, b : 255, alpha: 255}
      circuits.push( new Circuit("lights", true, [light_1, light_2, light_3, light_4, light_5], {r : 242, g : 190, b : 66, alpha: 255}  ));
      circuits.push( new Circuit("computers", true, [computer_1, computer_2, computer_3], {r : 88, g : 165, b : 92, alpha: 255} ));
      // circuits.push( new Circuit("fans", true, [fan_1, fan_2, fan_3], {r : 161, g : 189, b : 243, alpha: 255}));
      circuits.push( new Circuit("fridge", true, [fridge],{r : 17, g : 85, b : 204, alpha: 255}));
      circuits.push( new Circuit("water heater", true, [water_heater], {r : 225, g : 129, b : 118, alpha: 255}  ));
      circuits.push( new Circuit("dryer", true, [dryer], {r : 238, g : 117, b : 47, alpha: 255}  ));
      circuits.push( new Circuit("microwave", true, [microwave],{r : 255, g : 101, b : 175, alpha: 255} ));
      circuits.push( new Circuit("hvac", true, [furnace],{r : 81, g : 133, b : 236, alpha: 255} ) );
      circuits.push( new Circuit("stove", true, [stove],{r : 205, g : 89, b : 247, alpha: 255} ) );
      circuits.push( new Circuit("oven", true, [oven], {r : 216, g : 67, b : 54, alpha: 255} ) );
      circuits.push( new Circuit("washer", true, [washer],{r : 104, g : 187, b : 196, alpha: 255} ) );
      circuits.push( new Circuit("living room", true, [tv, wifi],{r : 0, g : 250, b : 146, alpha: 255} ) );

      ess = new ESS("Battery Backup", circuits);
      utility_power = new UtilityPower("Utility Power", circuits, ess);

      sources = [utility_power, ess];

      // Add power sources to panel
      for (i = 0; i < sources.length; i++) sources[i].add_to_panel();

      // Add circuits to panel
      for (i = 0; i < circuits.length; i++) circuits[i].add_to_panel();

      // Add loads to panel
      for (i = 0; i < circuits.length; i++) {
	      const circuit_loads = circuits[i].get_loads();
        for (j = 0; j < circuit_loads.length; j++) {
            circuit_loads[j].add_to_panel();
            loads.push(circuit_loads[j]);  // Collect an array of all circuit loads, for pie chart
	      }
      };

      // pie_chart('Circuits', 'PieDIV', circuits);

      // Plotly.newPlot('line_chart_DIV', _chart_data);
      on_update_time();

  }
  /////////////////////   3D setup() function     ////////////////////////
  p5.setup = function () {
    var acanvas = p5.createCanvas(500, 400, p5.WEBGL);
    acanvas.parent("Canvas3DDIV");
    p5.background(_ambientVal);

  }

  
    /////////////////////   3D draw() function     ////////////////////////
  p5.draw = function () {
    // pie_chart();
    pie_chart('Circuits', 'CircuitsPieDIV', circuits);
    // pie_chart('Loads', 'LoadsPieDIV', loads);



    p5.orbitControl();
    p5.push(); // A STARTING PUSH - JUST TO BE SURE
    p5.rotateX(p5.radians(90)); // always start with this - rotates the model over so +Z is up the screen
    // p5.rotateX(-PI / 6); // this gives us a slight angle to start
    p5.rotateX(p5.radians(-65)); // this gives us a slight angle to start

    p5.background(255);
    // p5.drawAxes(30);
    // drawAxes(p5, 100); // draw ORIGIN arrows
    p5.noStroke();
    p5.scale(zoom);

    //////////////////////////////    Lights   //////////////////////

    p5.ambientLight(150, 150, 150);

    light_1.draw_point_light(p5, zoom);
    light_2.draw_point_light(p5, zoom);
    light_3.draw_point_light(p5, zoom);
    light_4.draw_point_light(p5, zoom);
    light_5.draw_point_light(p5, zoom);

    //////////////////////////////    FLOORS          //////////////////////
    p5.push();
    p5.noStroke();

    {
      // p5.texture(wood_1);
      p5.fill(236, 221, 186, 255);
      p5.model(floor);
    }
    p5.pop();
    //////////////////////////////    WALLS, INTERIOR          //////////////////////
    p5.push();
    p5.noStroke();

    {
      // p5.texture(wood_1);
      p5.fill(89, 89, 89, 200);
      p5.model(walls_int);
      p5.model(doors);
    }
    p5.pop();

    //////////////////////////////    WALLS, EXTERIOR         //////////////////////
    p5.push();
    p5.noStroke();

    {
      // p5.texture(wood_1);
      p5.fill(89, 89, 89, 255);
      p5.model(walls_ext);
    }
    p5.pop();

    //////////////////////////////    FURNITURE         //////////////////////
    p5.push();
    p5.noStroke();

    p5.fill(214);
    p5.model(furniture); // 3d model
    p5.model(furniture_2);
    // p5.model(furniture_3);
    p5.pop();

    //////////////////////////////   APPLIANCES        //////////////////////
    p5.push();
    p5.noStroke();


      // Draw loads by iterating through circuits
      for (let i = 0; i < circuits.length; i++) {
	      var circuit_loads = circuits[i].get_loads();
	      for (let j = 0; j < circuit_loads.length; j++) {
	        circuit_loads[j].draw3D(p5);
	      }
      };


    p5.pop();

  }

}




/////////////////////////////////           VIEW CLASSES    //////////////////////////////////////////////////



/////////////////////      BE Root class - mostly just an abstract placeholder  ///////////////////////
class View {
  constructor() {
    this.p5 = null;
  };
}

/////////////////////      View2D class - the view that calls P52D  ///////////////////////

class View2D extends View {
  constructor() {
    super();
    // this.p5 = new p5(pie_chart);
    // this.p5.view = this;
  };


}


/////////////////////      View3D class - the view that calls P52D  ///////////////////////

class View3D extends View {
  constructor() {
    super();
    this.p5 = new p5(house_3D);
    this.p5.view = this;
  };

}
