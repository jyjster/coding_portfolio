///////////// GLOBALS ///////////// 

// changes when 'simulation' tab is clicked
var simulation_status = false;
// simulation_viz_status changes from false to true at the last iteration of the simulation 
// this helps not to overload Three.js while the simulation calculations are running
var simulation_viz_status = true;

// for Three.js
var scene;
var rayset = false;
var renderer;
var canvas;
var camera;
var controls;
var pointer;
var raycaster;
var roof_group = null;
//

// location defaults correspond to a location in Palo Alto, California
var zipcode = "94301";
var timezone = "America/Los_Angeles";
var place_id = "ChIJbfq2kBe7j4ARBzf9LVIpZok";
var lat = 37.44462167;
var lon =  -122.15570614;

// TO DO: not sure if start_date is necessary
var my_date;
var start_date = "2018-07-22";
var start_date;
var date_global;
var start_time = "12:00";
initialize_now();
var altitude_global = 0;

var sunDir = new THREE.Vector3(0, 30, 0);
var sun_calcs = null;
var sunLight = null;

// units: feet
// height of columns
var roof_side_dimension = 20;

// roof length = building length
// total row width
var roof_ridge_dimension = 40;

// pitch of roof
var slope_degrees = 25;

// orientation of the roof ridge as expressed as an angle in radians in relation to North
var roof_orientation_deg = 0;

const panel = {
    type: ''
}

// Set values
// sources:
// https://news.energysage.com/average-solar-panel-size-weight/
// https://news.energysage.com/what-is-the-power-output-of-a-solar-panel/

panel['type'] = 'Residential';

panel['Residential'] = {
    size_long: 5.4,
    // 5.416667 ft (= 65 in)
    size_short: 3.2,
    // 3.25 ft (= 39 in)
    size_depth: 0.1,
    // 0.1333333 ft (= 1.6 in)
    area: 5.4 * 3.2,
    efficiency: 0.1736,
    watt_capacity: 300
}

panel['Commercial'] = {
    size_long: 6.5,
    // 6.5 ft (= 78 in)
    size_short: 3.2,
    // 3.25 ft (= 39 in)
    size_depth: 0.1,
    // 0.1333333 ft (= 1.6 in)
    area: 6.5 * 3.2,
    efficiency: 0.1923,
    watt_capacity: 400
}

var panel_type = "Residential";

var panel_size_long = panel[panel['type']]['size_long'];
var panel_size_short = panel[panel['type']]['size_short'];
var panel_size_depth = panel[panel['type']]['size_depth'];

// spacing between columns
var panel_gap_long = 1;
// spacing between rows
var panel_gap_short = 1;

var month_data_left = [0, 0,0,0,0,0,0,0,0,0,0,0,0];
var month_data_right = [0, 0,0,0,0,0,0,0,0,0,0,0,0];
var annual_left = 0;
var annual_right = 0;

///////////// FUNCTIONS ///////////// 

// TO DO: do i still need initalize_now?
function initialize_now() {
    date_global = new Date();

    var date_str = date_global.toISOString();
    var date_split = date_str.split("T");

    start_date = date_split[0];
}

// formating string in advance_hour()
function pad(num, size) {
    num = num.toString();
    while (num.length < size) num = "0" + num;
    return num;
}

// runs when "next hour" button is pressed
function advance_hour(){
    // TO DO: if 24
    // console.log(start_time);
    time_split = start_time.split(":");
    var new_hour = parseInt(time_split[0]) + 1;
    start_time = pad(new_hour,2) + ":" + time_split[1];
    // console.log('advanced start time', start_time);

    onRefreshGeometry();
} 

function format_time(hh_mm){
    output_str = 'T' + hh_mm;
    // 'T13:51:50.417-07:00'
    return output_str;
}

// converts radians to degrees
function radians_to_degrees(radians) {
    var pi = Math.PI;
    return radians * (180/pi);
  }
  
  // converts degrees to radians
  function degrees_to_radians(degrees) {
    var pi = Math.PI;
    return degrees * (pi/180);
  }  

// runs once at start
function setup() {
    setupProgram(); // set up canvas, selection / ray caster, etc.
    loadAssets();
    setupScene();
    setupGeometry();
    // initialize_now();
    requestAnimationFrame(render);
    my_date = luxon.DateTime.now().setZone(timezone);
    openTab(null, 'Setup');
    // onRefreshGeometry();
}

// runs once at start
function setupProgram() {   // Typically don't change this
    // 1. Get the canvas and create the new Renderer
    // TO DO: setupProgram 1 and 2; scene 1 and 2
    const canvas = document.getElementById("c");
    renderer = new THREE.WebGLRenderer({ canvas });
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap; // default THREE.PCFShadowMap
    raycaster = new THREE.Raycaster();
    pointer = new THREE.Vector2();
    // window.addEventListener('pointerdown', onPointerMove);
    
    scene = new THREE.Scene();
}

// runs once at start
function loadAssets() {
    var mtlLoader = new THREE.MTLLoader();
    mtlLoader.load('./assets/chair.mtl', function (materials) {

        materials.preload();
        materials.side = THREE.DoubleSide;
    });
    var tablelLoader = new THREE.MTLLoader();
    tablelLoader.load('./assets/table.mtl', function (materials) {

        materials.preload();
        materials.side = THREE.DoubleSide;
    });
}

// runs once at start
function setupScene() {

    scene.background = new THREE.Color(0x6688ff);

    // Create the Camera
    const fov = 75;
    const aspect = 2;  // the canvas default
    const near = 0.1;
    const far = 5000;
    camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
    camera.position.z =  -100;
    camera.position.x = 0;
    camera.position.y = 20;
    camera.rotation.x = degrees_to_radians(90);
    camera.rotation.z = degrees_to_radians(90);
    
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.update();

    // AXES HELPER
    // const axesHelper = new THREE.AxesHelper(10);
    // scene.add(axesHelper);

    // Add a light
    //Create a DirectionalLight and turn on shadows for the light

    // add light object as 'sun'
    sunLight = new THREE.DirectionalLight(0xffffff, 0.8);
    sunLight.position.set(sunDir.x, sunDir.y, sunDir.z); //default; light shining from top
    sunLight.target.position.set(0, 0, 0);
    sunLight.castShadow = true; // default false
    scene.add(sunLight);

    //Set up shadow properties for the sunLight
    sunLight.shadow.mapSize.width = 512; // default
    sunLight.shadow.mapSize.height = 512; // default
    sunLight.shadow.camera.near = 0.5; // default
    sunLight.shadow.camera.far = 200; // default
    sunLight.shadow.camera.left = -20;
    sunLight.shadow.camera.right = 20;
    sunLight.shadow.camera.top = 20;
    sunLight.shadow.camera.bottom = -20;
    //Create a helper for the shadow camera (optional)
    const helper = new THREE.CameraHelper(sunLight.shadow.camera);
    // scene.add(helper);

    const ambientLight = new THREE.AmbientLight(0x808080);
    scene.add(ambientLight);

    scene.add(camera);
}

// add blue line indicating north direction
function setupGeometry() {

    onRefreshGeometry();
    const material = new THREE.LineBasicMaterial( { color: 0x0000ff } );
    const NS_points = [];
    NS_points.push( new THREE.Vector3( 0, 0, 0 ) );
    NS_points.push( new THREE.Vector3( 0, 0, -100 ) );
    const geometry = new THREE.BufferGeometry().setFromPoints( NS_points);
    // NORTH LINE
    const NS_line = new THREE.Line( geometry, material );
    scene.add( NS_line );
    // scene.add(new THREE.AxesHelper( 10 ));
}

// calculate instanteous power generated by a panel (mesh)
function panel_power(mesh, direction, sun_v, time){

    var panel_v = new THREE.Vector3(0, 1, 0);
    
    var z_vector = new THREE.Vector3(0, 0, 1);
    panel_v.applyAxisAngle(z_vector, mesh.rotation._z);

    var y_vector = new THREE.Vector3(0, 1, 0);
    panel_v.applyAxisAngle(y_vector, degrees_to_radians(roof_orientation_deg));

    panel_v.normalize();

    // dot product of n and d = cosine of angle a in solar radiation euqation
    var sun_factor = sun_v.dot(panel_v);
    // console.log('dot product', sun_factor);

    var panel_potential = panel[mesh.userData.type].watt_capacity;

    // var power = sun_factor * panel_factor * panel_area;
    var power =  sun_factor * panel_potential;
    // if (direction < 0) power = -power;
    if (power < 0) power = 0;
 
    mesh.userData.power = power;
    
    mesh.userData.percent_of_potential = power / panel_potential;

   if (time){

        if (mesh.userData.roof_id == "Left") {
            // month_data_left[month] += power;
            month_data_left[time.month] += (power / 1000);
        }
        else {
            month_data_right[time.month] += (power / 1000);
         }
   }

   mesh.userData.total_energy += power;

return power;
}

// draw  roof surfaces/places
function roof_planes(direction, id) {

    const geometry = new THREE.PlaneGeometry(roof_ridge_dimension, roof_side_dimension);
    var material;

    if (id == "Left"){
        material = new THREE.MeshBasicMaterial({ color: 0x88650F, side: THREE.DoubleSide });
    }
    else {
        material = new THREE.MeshBasicMaterial({ color: 0x727478, side: THREE.DoubleSide });
    }
    
    const plane = new THREE.Mesh(geometry, material);
    var slope_radians = (90 - slope_degrees) * Math.PI / 180;

    plane.position.x = direction * -roof_side_dimension / 2 * Math.sin(slope_radians);
    plane.position.y = (-roof_side_dimension / 2 * Math.cos(slope_radians)) - 0.5;
    plane.rotation.x = Math.PI / 2;
    plane.rotation.y = direction * -(Math.PI / 2 + slope_radians);
    plane.rotation.z = Math.PI / 2;

    plane.userData.type = "Roof";
    plane.userData.id = id;

    roof_group.add(plane);
}

// draws panels on roof and sets their colors (corresponding the power)
function pannelize_roof(direction, roof_id, sun_v, current_time) {

    var slope_radians = slope_degrees * Math.PI / 180;
    var row = 0;
    var column = 0;
    var axis = new THREE.Vector3(0, 0, 1);
    var upvector = new THREE.Vector3(0, 1, 0);

    if (direction == 1) upvector.applyAxisAngle(axis, slope_radians);
    else upvector.applyAxisAngle(axis, -slope_radians);

    upvector.normalize();
    dir = upvector;

    for (vPosition = panel_size_short / 2 +  panel_gap_short; Math.abs(vPosition) + panel_size_short < roof_side_dimension; vPosition = vPosition + (panel_size_short + panel_gap_short)) {
        // for loop for columns; along the roof_ridge_dimension; in the positive x direction
        row += 1; //draws first row
        // console.log("starting outer loop ", row, ", ", column);

        for (uPosition = (-roof_ridge_dimension / 2) + (panel_size_long / 2); uPosition + panel_size_long < ((roof_ridge_dimension / 2) + (panel_size_long / 2)); uPosition += panel_size_long + panel_gap_long) {
            column += 1;
            // console.log("starting inner loop ", row, ", ", column);
            var myPanelGeometry = new THREE.BoxGeometry(panel_size_short, panel_size_depth, panel_size_long);

            var sunCos = Math.abs(upvector.dot(sunDir));
            var initColor = new THREE.Color(0, 0, 0);

            const material = new THREE.MeshPhongMaterial({ color: initColor });  

            // Create the Mesh from the Geometry and a Material
            const panelMesh = new THREE.Mesh(myPanelGeometry, material);

            panelMesh.position.y = -1 * vPosition * Math.sin(slope_radians);
            panelMesh.position.x = vPosition * (-1 * direction)  * Math.cos(slope_radians);
          
            panelMesh.position.z = uPosition;
            panelMesh.rotation.z = direction * slope_radians;

            panelMesh.userData.type = panel['type'];
            panelMesh.userData.roof_id = roof_id;
            panelMesh.userData.row = row;
            panelMesh.userData.column = column;
       
            // normal vectors to panel
	        panelMesh.userData.upVector = upvector;	    
            
            var local_power = panel_power(panelMesh, direction, sun_v, current_time);
            
            if (!simulation_status){

                panel_potential = panel[panelMesh.userData.type].watt_capacity;
                panel_color = new THREE.Color(panelMesh.userData.power / panel_potential, 0, 0);
                panelMesh.material.color.set(panel_color); // updates color
                
            } else {
                // units in kwh
                max_potential = (panel[panelMesh.userData.type].watt_capacity/1000) * 4447;
		        computeAnnuals();

                if (panelMesh.userData.roof_id == "Left"){
                    left_color_r = (annual_left / (annual_left + annual_right));
                    panel_left_color = new THREE.Color(left_color_r, 0, 0);
                    panelMesh.material.color.set(panel_left_color); // updates color
                } else {
                    right_color_r = (annual_right / (annual_left + annual_right));
                    panel_right_color = new THREE.Color(right_color_r, 0 , 0);
                    panelMesh.material.color.set(panel_right_color); // updates color
                }
            }

            if (simulation_viz_status) {
                roof_group.add(panelMesh);
            }	    

            // DOT PRODUCT TROUBLESHOOTING ARROW
            const origin = new THREE.Vector3(panelMesh.position.x, panelMesh.position.y, panelMesh.position.z);
            const length = 5;
            const hex = 0xffff00;
            const arrowHelper = new THREE.ArrowHelper(dir, origin, length, hex);
            arrowHelper.userData.type = "Arrow";
            // roof_group.add(arrowHelper);

        } // inner for loop end
        column = 0;
    } // outer for loop end
} // pannelize_roof function end

// get azimuth and altitude of sun position
function sun_info(my_date){

    current_Pos = SunCalc.getPosition(my_date, lat, lon);
    
    var sun_v_std = new THREE.Vector3(
       
        // azimuth + Math.PI to correct for suncalc's azimuth in terms of South ---> get azimuth in terms of North
        Math.sin(current_Pos.azimuth + Math.PI) * Math.cos(current_Pos.altitude),
        Math.cos(current_Pos.azimuth + Math.PI) * Math.cos(current_Pos.altitude),
        Math.sin(current_Pos.altitude)
    );

    var sun_v_three = new THREE.Vector3(
        sun_v_std.x,
        sun_v_std.z,
        -sun_v_std.y
    );

    const sun_results = {};
    sun_results['sun_v_std'] =  sun_v_std;
    sun_results['SunPos'] = sun_v_std;
    sun_results['sun_v_three'] =  sun_v_three;
    sun_results['sun_v'] =  sun_v_three;
    sun_results['altitude'] = radians_to_degrees(current_Pos.altitude);
    sunDir = sun_v_three;
    sunLight.position.set(sunDir.x, sunDir.y, sunDir.z); //default; light shining from top

return sun_results;
}

// render with Three.js
function onRefreshGeometry() {

    // Clean out old meshes / objects
    // runs if roof_group exists
    if (roof_group) {

	for (var i = 0; i < roof_group.children.length; i++) {
            var child = roof_group.children[i];

            if (child.userData.type == "Residential" || child.userData.type == "Commercial" || child.userData.type == "Roof" || child.userData.type == "Arrow" || child.userData.type == "Sun") {
		        roof_group.remove(child)
		        i--;
            }
	}
}

    if (scene)  {

        for (var i = 0; i < scene.children.length; i++) {
            var child = scene.children[i];

            if (child.userData.type == "Sun" || child.userData.type == "Arrow" || child.userData.type == "Compass") {
                scene.remove(child)
                i--;
            }
        }
    }

    panel_size_long = panel[panel['type']]['size_long'];
    // 5.416667 ft (= 65 in)
    panel_size_short = panel[panel['type']]['size_short'];
    // 3.25 ft (= 39 in)
    panel_size_depth = panel[panel['type']]['size_depth'];
    // 0.1333333 ft (= 1.6 in)

    // if null, doesn't run
    if (!roof_group) {
        roof_group = new THREE.Group();
        scene.add(roof_group);
    }

    var date_input = start_date + format_time(start_time);
    // https://moment.github.io/luxon/index.html#/zones?id=creating-datetimes-in-a-zone
     my_date = luxon.DateTime.fromISO(date_input, { zone: timezone });

    sun_calcs = sun_info(my_date);

    sun_v = sun_calcs['sun_v_three']; // USE the flipped and mirrored sun coordinates that THREE.js expects

    // visualize sun with object
    // https://threejs.org/docs/#api/en/geometries/SphereGeometry
    const sun_distance = 50;
    const sun_rad = 5;
    const sun_diameter = 2 * sun_rad;
    const sun_sphere = new THREE.SphereGeometry( sun_rad, 32, 16 );
    const sun_material = new THREE.MeshBasicMaterial( { color: 0xffff00 } );
    const sun_mesh = new THREE.Mesh( sun_sphere, sun_material );
    sun_mesh.position.set(sun_v.x * sun_distance, sun_v.y * sun_distance, sun_v.z * sun_distance);

    sun_mesh.userData.type = "Sun";

    // don't render the sun in the 'simulation tab'
    if (!simulation_status){
        scene.add(sun_mesh);
    }

    roof_planes(1, "Left"); 
    roof_planes(-1, "Right"); 

    pannelize_roof(1, "Left", sun_v, null);
    pannelize_roof(-1, "Right", sun_v, null);

    roof_orientation_rad = degrees_to_radians(roof_orientation_deg);
    roof_group.rotation.y = roof_orientation_rad;
}

// Create the renderer loop
function render(time) {

    time *= 0.001;  // convert time to seconds

    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    // check if the size has been changed
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
        renderer.setSize(width, height, false);   // set the renderer size to the canvas size
        camera.aspect = canvas.clientWidth / canvas.clientHeight; // set the renderer aspect ratio
        camera.updateProjectionMatrix();
    }

    controls.update();
    // update the picking ray with the camera and pointer position
    if (rayset) {
        raycaster.setFromCamera(pointer, camera);

        // calculate objects intersecting the picking ray
        const intersects = raycaster.intersectObjects(scene.children);

        for (let i = 0; i < intersects.length; i++) {

            // the objects are nested so we need to ask for the selected object's parent.
            if (intersects[i].object.parent.userData.type == "Chair" || intersects[i].object.parent.userData.type == "Table") {
                var myfurniture = intersects[0].object.parent;
                var textout = "";
                textout += "<table style='border: solid' ><tr><td style='border: solid'>"
                textout += myfurniture.name;
                textout += "</td><td style='border: solid'>"
                textout += myfurniture.userData.cost;
                textout += "</td></tr></table>"

                document.getElementById("data").innerHTML = textout;
            }
        }
    }
    renderer.render(scene, camera);
    requestAnimationFrame(render);
}

function geocodeCallback(results, status) {

    if (status == google.maps.GeocoderStatus.OK) {
         lat = results[0].geometry.location.lat();
         lon = results[0].geometry.location.lng();
         place_id = results[0].place_id;

         timezone = tzlookup(lat, lon);
         console.log('timezone: ', timezone);
         
         onRefreshGeometry();
        }
       else {
        // alert("Geocode was not successful for the following reason: " + status);
        console.log('geocoder does not run');
      }
  }

// get user inputs for roof dimensions from html
function setRoofDimensions(){
    let inputVal_1 = document.getElementById("ridge_length").value;
    roof_ridge_dimension = inputVal_1;

    let inputVal_2 = document.getElementById("roof_width").value;
    roof_side_dimension = inputVal_2;
}

// get user location input via zipcode then find lat lon via google geocoder
function getInputLocation() {
    // Selecting the input element and get its value
    let inputVal = document.getElementById("zipcode").value;
    zipcode = inputVal;
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': zipcode}, geocodeCallback);
  }

  // Code for tabs from https://www.w3schools.com/howto/howto_js_tabs.asp
  function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    if (tabName == "Simulation") {
        simulation_status = true;
    }
    else { 
        simulation_status = false;
    }

    onRefreshGeometry();

    console.log('simulation status: ', simulation_status);

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    if (evt){
        evt.currentTarget.className += " active";
    }
  } 

  function create_graph(left, right){

    // need to slice because january starts at index 1 and index 0 is just a filler
    console.log('slice: ', month_data_left.slice(1));

    var trace1 = {
        x: ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
        y: left,
        name: "Brown Roof's Panels",
        marker: {color: 'rgb(136, 101, 15)'},
        type: 'bar'
    };
    
    var trace2 = {
        x: ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
        y: right,
        name: "Grey Roof's Panels",
        marker: {color: 'rgb(114, 116, 120)'},
        type: 'bar'
    };
    
    var data = [trace1, trace2];
    
    var layout = {
        barmode: 'stack',
        width: '100%',
        title: {
            text:'Total Monthly Solar Energy Production in 2021'},
        yaxis: {
            title: 'Energy (kwh)'
        }, 
        xaxis: {
            title: 'Month'
        }
      }
    
    Plotly.newPlot('bar_chart_DIV', data, layout);
  }

function computeAnnuals() {
    annual_left = 0;
    annual_right = 0;
    for (let i = 1; i < 13; i++) {
        annual_left += month_data_left[i];
        annual_right += month_data_right[i];
    }
}

function runAnnualSimulation(){
    
    var start_dt = luxon.DateTime.fromObject({year: 2021, month: 1, day: 1}, { zone: timezone});
    console.log('simulation date: ', start_dt.toString());

    var dt = luxon.DateTime.fromObject({year: 2021, month: 1, day: 1}, { zone: timezone});

    var times;
    simulation_viz_status = false;

    while (dt.hasSame(start_dt, 'year')) {
   
        times = SunCalc.getTimes(dt, lat, lon);

        if ((dt >= times.sunrise) && (dt <= times.sunset)){
             // so january is month_data[1]

             sun_calcs = sun_info(dt);
             sun_v = sun_calcs['sun_v'];
             pannelize_roof(1, "Left", sun_v, dt);
             pannelize_roof(-1, "Right", sun_v, dt);
        }
        // increments DateTime by 1 hour
        dt = dt.plus({ hours: 1 });
     
    }
    
    console.log('simulation end date: ', dt.toString());

    simulation_viz_status = true;

    create_graph(month_data_left.slice(1), month_data_right.slice(1));

    computeAnnuals();

    console.log(annual_left);
    console.log(annual_right);

    const annual_placeholder = document.getElementById("annual_left_DIV");
    annual_placeholder.innerHTML = "The panels on the grey roof generate " + Math.trunc(annual_right).toLocaleString("en-US") + " kwh in 2021, "
    const annual_placeholder_2 = document.getElementById("annual_right_DIV");
    annual_placeholder_2.innerHTML =  "while the panels on the brown roof generate " + Math.trunc(annual_right).toLocaleString("en-US") + " kwh for that year."

    onRefreshGeometry();
  }

// show user roof slope selection in html
  function onSlopePicker(){
    var slider = document.getElementById("slope");
    var output = document.getElementById("slope_output");
    output.innerHTML = "roof pitch angle: " + slider.value + "°"; 
  }

  // show user orientation selection in html
  function onOrientationPicker() {
    var slider = document.getElementById("orientation");
    var output = document.getElementById("orient_output");
    output.innerHTML = "roof orientation: " + slider.value + "°" + "counterclockwise from "; 
    var output_2 = document.getElementById("orient_output_2");
    output_2.innerHTML = "North"; 
  }