/////////////////////   HTML FUNCTIONS     ////////////////////////

// FUNCTION to visualize each class on electrical panel on html
function insert_component(c_self, units) {
    // c_self = this

    // https://www.sitepoint.com/draw-rectangle-html/
    // https://www.javascripttutorial.net/dom/css/add-styles-to-an-element/
    // https://stackoverflow.com/questions/195951/how-can-i-change-an-elements-class-with-javascript

    // Implement something like this via Javascript DOM API

    // <div style="width:500px;height:100px;border:1px solid #000;">This is a rectangle!</div>

    // Need to recreate this html code using Javascript DOM
        // <label class="switch">
        //   <input type="checkbox">
        //   <span class="slider"></span>
        // </label>

    // creative Div
    const newDiv = document.createElement("div");
    // newDiv.style.cssText += 'width:100px;height:60px;border:1px solid #000;';
    // style Div
    newDiv.style.cssText += 'width:140px;border:1px solid #000;' + 'height:' + (units * 70 + 2 *(units -1)) + 'px;';
    newDiv.style.backgroundColor = c_self.get_current_color(0.25);
    // text node, // Div's label is this.name
    const newText = document.createTextNode(c_self.name);
    newDiv.appendChild(newText); // parent is the Div
    newDiv.appendChild(document.createElement("br")); // line break

    const newLabel = document.createElement("label");
    newLabel.className = 'switch'; // .className is a DOM element property

    const newInput = document.createElement("input");
    newInput.type = 'checkbox';
    // https://stackoverflow.com/questions/10436764/how-to-set-default-checkbox-status-with-javascript
    newInput.checked = c_self.status; // .checked is a boolean, sets check to default value
    c_self.my_switch = newInput;
    // https://stackoverflow.com/questions/5024056/how-to-pass-parameters-on-onchange-of-html-select
    // https://stackoverflow.com/questions/43642729/calling-a-method-from-another-method-in-the-same-class

    // onChange function for switch
    newInput.onchange = function(evt) { c_self.process_switch_event(evt) };
    const newSpan = document.createElement('span');
    newSpan.className = 'slider round';

    // fill out the html parameters
    newLabel.appendChild(newInput);
    newLabel.appendChild(newSpan);

    // put the label in the Div
    newDiv.appendChild(newLabel);

    newDiv.appendChild(document.createElement("br"));
    // if class has critical_capable = True, then add checkbox
    if (c_self.critical_capable) {
        const newCritInput = document.createElement("input");
        newCritInput.type = 'checkbox';
        newCritInput.checked = c_self.critical;
        newCritInput.onchange = function(evt) { c_self.set_critical(evt) };
        newDiv.appendChild(newCritInput);
    }

    // Display downstream
    const loadInfo = document.createTextNode(c_self.get_downstream_load() + " watts");
    c_self.load_info = loadInfo;
    newDiv.appendChild(loadInfo);
    // https://stackoverflow.com/questions/5024056/how-to-pass-parameters-on-onchange-of-html-select
    // https://stackoverflow.com/questions/43642729/calling-a-method-from-another-method-in-the-same-class
    // store reference to entire div in this.switch_div
    c_self.switch_div = newDiv;

    // put this Div code into the class's div id
    const containing_div = document.getElementById(c_self.containing_div_id);
    containing_div.appendChild(newDiv);
}

// FUNCTION to draw the ESS component
function insert_ess_component(c_self) {
    var units = 3;
    // c_self = this

    // https://www.sitepoint.com/draw-rectangle-html/
    // https://www.javascripttutorial.net/dom/css/add-styles-to-an-element/
    // https://stackoverflow.com/questions/195951/how-can-i-change-an-elements-class-with-javascript

    // Implement something like this via Javascript DOM API

    // <div style="width:500px;height:100px;border:1px solid #000;">This is a rectangle!</div>

    // Need to recreate this html code using Javascript DOM
    // <label for="fuel">Fuel level:</label>
    // <meter id="fuel"
    //        min="0" max="100"
    //        low="33" high="66" optimum="80"
    //        value="50">
    //     at 50/100
    // </meter>

    // creative Div
    const newDiv = document.createElement("div");
    // newDiv.style.cssText += 'width:100px;height:60px;border:1px solid #000;';
    // style Div
    newDiv.style.cssText += 'width:140px;border:1px solid #000;' + 'height:' + (units * 70) + 'px;';
    newDiv.style.backgroundColor = c_self.get_current_color(0.25);
    // text node, // Div's label is this.name
    const newText = document.createTextNode(c_self.name);
    newDiv.appendChild(newText); // parent is the Div

    // The meter, progress bar-like icon
    newDiv.appendChild(document.createElement("br")); // line break
    newDiv.appendChild(document.createElement("br")); // line break

    const meterLabel = document.createElement("label");
    meterLabel.className = 'ess_meter'; // .className is a DOM element property
    meterLabel.for = 'ess_meter';
    const labelText = document.createTextNode('Capacity:');
    meterLabel.appendChild(labelText);
    const newMeter = document.createElement("meter");
    newMeter.id = 'ess_meter';
    // 'meter' html element has default colors depending on value range, therefore to change the default colors coressponding to ranges, we just changed the ranges
    newMeter.min = 0;
    newMeter.max = c_self.capacity;
    newMeter.optimal = 0.75 * newMeter.max; // optimal is "ok" range; therefore anything (optimal, max] is green
    // newMeter.high = 0.75 * newMeter.max;
    newMeter.low  = 0.25 * newMeter.min; // 0-25% red; everything else is yellow
    newMeter.value = c_self.capacity;

    c_self.my_meter = newMeter; // my_meter is property of ESS Powersource instance
    // inserting into the DOM
    newDiv.appendChild(meterLabel);
    newDiv.appendChild(newMeter);
    newDiv.appendChild(document.createElement("br"));
    // End of meter

    // Display Configured Runtime
    // newDiv.appendChild(document.createElement("br"));
    // // const cfgRuntime = document.createTextNode(0);
    // const cfgRuntime = document.createTextNode(c_self.get_cfg_runtime());
    // const cfgRuntimeLabel = document.createElement("label");
    // const cfgRuntimeLabelText = document.createTextNode('Cfg runtime:');
    // cfgRuntimeLabel.appendChild(cfgRuntimeLabelText);
    // c_self.cfg_runtime = cfgRuntime
    // newDiv.appendChild(cfgRuntimeLabel);
    // newDiv.appendChild(cfgRuntime);

    // Display Projected Runtime
    // newDiv.appendChild(document.createElement("br"));
    // const projRuntime = document.createTextNode(c_self.get_proj_runtime());
    // const projRuntimeLabel = document.createElement("label");
    // const projRuntimeLabelText = document.createTextNode('Proj runtime:');
    // projRuntimeLabel.appendChild(projRuntimeLabelText);
    // c_self.proj_runtime = projRuntime
    // newDiv.appendChild(projRuntimeLabel);
    // newDiv.appendChild(projRuntime);

    // Display Load
    newDiv.appendChild(document.createElement("br"));
    const loadInfo = document.createTextNode(c_self.get_downstream_load() + " watts");
    const loadLabel = document.createElement("label");
    const loadLabelText = document.createTextNode('Load:');
    loadLabel.appendChild(loadLabelText);
    c_self.load_info = loadInfo;
    newDiv.appendChild(loadLabel);
    newDiv.appendChild(loadInfo);

    // Display Outage Hours
    newDiv.appendChild(document.createElement("br"));
    const outhourInfo = document.createTextNode(c_self.outage_hours);
    const outhourLabel = document.createElement("label");
    const outhourLabelText = document.createTextNode('Hours:');
    outhourLabel.appendChild(outhourLabelText);
    c_self.outhour = outhourInfo;
    newDiv.appendChild(outhourLabel);
    newDiv.appendChild(outhourInfo);

    // Advance Hours Button
    newDiv.appendChild(document.createElement("br"));
    newDiv.appendChild(document.createElement("br"));
    const advhourButton = document.createElement('button');
    const advhourButtonText = document.createTextNode('Advance 1 hour');
    advhourButton.appendChild(advhourButtonText);
    advhourButton.onclick = function(evt) { c_self.advance_time() };
    newDiv.appendChild(advhourButton);

    // store reference to entire div in this.switch_div
    c_self.switch_div = newDiv;

    // put this Div code into the class's div id
    const containing_div = document.getElementById(c_self.containing_div_id);
    containing_div.appendChild(newDiv);
}

/////////////////////   HELPER FUNCTIONS   ////////////////////////


// FUNCTION to convert minutes per day into per-hour
function mou2per_hr( mou ) {
    return (mou / (60 * 24));
}

/////////////////////   POWER SOURCE CLASSES     ////////////////////////

// CLASS
class PowerSource {
// 2 instances of PowerSource class = 1) utility power grid 2) ESS (energy storage system)
    constructor(my_name, my_circuits) {
        this.pcl_type = 'PowerSource'; // pcl = power class
        this.name = my_name;
        this.contains = my_circuits; // whom am I the parent of; can have multiple children
        this.status = true;
        this.off_color = {
            r : 255,
            g : 0,
            b : 0,
            alpha: 255
        };

        this.on_color = {
            r : 0,
            g : 0,
            b : 255,
            alpha: 255
        };
        this.containing_div_id = 'SourcesDIV';
        this.critical_capable = false;
        this.contained_by = null;  // whom am I child of, powersource isn't the child of anybody; can only have 1 parent
    }

    utility_status_change() {
        for (let i = 0; i < this.contains.length; i++) {
            this.contains[i].utility_status_change(this.status);;
        }
    }

    // when you create an instance of a PowerSource, you need to tell the circuits who their parent/PowerSource is
    assign_contains_contained_by() {
        for (let i = 0; i < this.contains.length; i++) {
            this.contains[i].assign_contained_by(this);
	    }
    }

    // changes the PowerSource's status (if requested status is different from current status)
    set_status(new_status) {
        if (this.status != new_status) {
            this.status = new_status;
            this.update_load_info(); // run the method about how much power me and my children use
            this.switch_div.style.backgroundColor = this.get_current_color(0.25); // change background color of slider button box
            console.log('PowerSource/set_status:', this.name, this.status);
            return true;
        } else {
            console.log('PowerSource/set_status:', 'UNCHANGED!', this.name, this.status);
            return false;
        }
    }

    // event.target.checked, checked is a boolean
    process_switch_event(event) {
        console.log(this.pcl_type + '/process_switch_event:')
        // https://stackoverflow.com/questions/32438068/perform-an-action-on-checkbox-checked-or-unchecked-event-on-html-form
        if (this.set_status(event.target.checked)) {
            this.utility_status_change();
        }
    }

    // sync PowerSource's status with the status visualized by the button slider
        // needed because status can change without switch changing through propagation (e.g. when parent or child changes)
    sync_state() {
        if (this.status != this.my_switch.checked) {
            this.my_switch.checked = this.status;
        }
    }

    // propagate parent's status to all of its children; update_status to all my children
    propagate_status() {
        for (let i = 0; i < this.contains.length; i++) {
            this.contains[i].update_status(this.status);
        }
    }


    update_status(new_status) {
        if (this.set_status(new_status)) {
            this.sync_state();
            this.propagate_status();
        }
    }

    // displays get_downstream_load's sum on the webpage by "inserting" it into the DOM
        // changes the existing text node in the DOM
    update_load_info() {
	    // https://stackoverflow.com/questions/41384379/use-javascript-to-change-text-only-in-an-element
        console.log(this.pcl_type + '/update_load_info:')
        // textContent (pre-existing property in js API) is a property of a DOM element
        this.load_info.textContent = this.get_downstream_load();
    }

    get_downstream_load_no_status() {
        var downstream_load = 0;
        for (let i = 0; i < this.contains.length; i++) {
	        downstream_load += this.contains[i].get_downstream_load();
        }
        return downstream_load;
    }

    // find the sum of my "on" children's loads
    get_downstream_load() {
        var downstream_load = 0;
        if(this.status == true) {
	        downstream_load = this.get_downstream_load_no_status();
        }
        return downstream_load;
    }

    get_24h_downstream_load() {
        var downstream_load = 0;
        for (let i = 0; i < this.contains.length; i++) {
	        downstream_load += this.contains[i].get_24h_downstream_load();
        }
        return downstream_load;
    }

    // connects the on_color and off_color properties of the class instance to the html
    get_current_color(alpha) {
        var status_color;
        if (this.status) {
            status_color = this.on_color;
        } else {
            status_color = this.off_color;
        }
        return 'rgb(' + status_color.r + ',' + status_color.g + ',' + status_color.b + ',' + alpha + ')';
        }

        add_to_panel() {
        insert_component(this, 1); // height of class instance's box in the table (e.g. 1 unit high)
        }

        update_cfg_runtime() {
        }

}
 // SUB-CLASS
class UtilityPower extends PowerSource {
    constructor(my_name, my_circuits, my_ess) { // added my_ess
        super(my_name, my_circuits); // 'super' means call the parent class's constructor
        // Initially, the UtilityPower contains all the circuits
        this.assign_contains_contained_by();
        this.ess = my_ess;
    }

    utility_status_change() {
	    for (let i = 0; i < this.contains.length; i++) {
	        this.contains[i].utility_status_change(this.status);;
	    }
        if (!this.status) {
            // The utility power went out
            // Connect all circuits to ESS, tell utility power's children to reassign their parent to ess
            this.ess.assign_contains_contained_by();
            // Turn on the ESS
            this.ess.set_status( true );
            this.ess.sync_state();
            this.ess.update_proj_runtime();
        } else {
            // The utility power went on
            // Connect all circuits back to utility power
            this.assign_contains_contained_by();
            // Turn off the ESS
            this.ess.set_status( false );
            // Reset the ESS to initial state
            this.ess.reset();
            // With utility power back on, non-critical circuits are now re-powered, so recalculate load
            this.update_load_info();
        }
    }

    update_cfg_runtime() {
	    this.ess.update_cfg_runtime();
    }

}

// SUB-CLASS
class ESS extends PowerSource {
    constructor(my_name, my_circuits) {
        super(my_name, my_circuits); // 'super' means call the parent class's constructor
        this.status = false;
        this.cfg_capacity = 2 * 13500; // Watt Hours // 2 Tesla Powerwalls
        this.capacity = this.cfg_capacity;
        this.outage_hours = 0;
	_time_values.push(0);
	_power_values.push(this.cfg_capacity);
    }

    add_to_panel() {
	insert_ess_component(this);
    }

    advance_time() {
	if (this.status && (this.capacity > 0)) {
	    // Increment outage hours, and display that
	    this.outage_hours += 1;
	    this.outhour.textContent = this.outage_hours;
	    // Decrease capacity by one hour of current usage
	    console.log('advance_time, previous capacity:', this.capacity);
	    console.log('advance_time, downstream_load:', this.get_downstream_load());
	    // this.capacity = this.capacity - this.get_downstream_load();
	    this.capacity = this.capacity - mou2per_hr(this.get_24h_downstream_load());
	    if (this.capacity < 0) { this.capacity = 0 }; // Don't go negative
	    console.log('advance_time, new capacity:', this.capacity);
	    this.my_meter.value = this.capacity;
	    // Update projected runtime based on current load
	    this.update_proj_runtime();
            clock(this.outage_hours);
	    _time_values.push(this.outage_hours);
	    _power_values.push(this.capacity);
	    on_update_time();
        //clock(1+ ess.outage_hours);
        // console.log(ess.outage_hours);
	}
    }

    get_24h_downstream_load() {
        var downstream_load = 0;
        for (let i = 0; i < this.contains.length; i++) {
            downstream_load += this.contains[i].get_24h_downstream_load();
        }
        return downstream_load;
    }

    get_cfg_runtime() {
	// https://www.w3schools.com/jsref/jsref_tofixed.asp
	console.log( this.capacity);
	console.log( this.get_24h_downstream_load());
	var foo = (this.cfg_capacity / mou2per_hr(this.get_24h_downstream_load())).toFixed(1);
	console.log(foo);
	return foo;
    }

    get_proj_runtime() {
	console.log('get_proj_runtime, capacity:', this.capacity);
	console.log('get_proj_runtime, downstream_load:', this.get_downstream_load());
	var foo = (this.cfg_capacity / this.get_downstream_load_no_status()).toFixed(1);
	console.log('get_proj_runtime, projected runtime:', foo);
	return foo;
    }

    update_cfg_runtime() {
	// this.cfg_runtime.textContent = this.get_cfg_runtime();
    }

    update_proj_runtime() {
	// this.proj_runtime.textContent = this.get_proj_runtime();
    }

    process_switch_event(event) {
	// ESS has no switch, so don't do anything
    }

    sync_state() {
    }

    reset() {
	// Resets ESS to initial state
	this.capacity = this.cfg_capacity;
	this.my_meter.value = this.capacity;
	this.update_proj_runtime();
	this.outage_hours = 0;
	this.outhour.textContent = this.outage_hours;
    }

}

/////////////////////   CIRCUIT CLASS     ////////////////////////
class Circuit {

    constructor(my_name, my_critical, my_loads, my_color){
        this.pcl_type = 'Circuit';
        this.name = my_name;
        this.contains = my_loads;
        this.status = true;
        this.critical = my_critical;
        this.off_color = {
            r : 92,
            g : 61,
            b : 25,
            alpha: 255
        };
        this.on_color = {
            r : my_color.r,
            g : my_color.g,
            b : my_color.b,
            alpha: my_color.alpha
        };
	this.critical_capable = false;
	this.containing_div_id = 'CircuitsDIV';
	this.contained_by = null;
        // For each load on this circuit, set that load's circuit to this (of the circuit)
	for (let i = 0; i < my_loads.length; i++) {
	    my_loads[i].assign_contained_by(this);
	}
    }

    get_on_color() {
	return this.on_color
    }

    get_current_color(alpha) {
	var status_color;
	if (this.status) {
	    status_color = this.on_color;
	} else {
	    status_color = this.off_color;
	}
	return 'rgb(' + status_color.r + ',' + status_color.g + ',' + status_color.b + ',' + alpha + ')';
    }

    get_loads() {
	return this.contains;
    }

    get_loads_count() {
	return this.contains.length;
    }

    get_downstream_load() {
        var downstream_load = 0;
        if(this.status == true){
            for (let i = 0; i < this.contains.length; i++) {
                downstream_load += this.contains[i].get_downstream_load();
            }
        }
        return downstream_load;
    }

    get_24h_downstream_load() {
        var downstream_load = 0;
        if(this.critical == true){
            for (let i = 0; i < this.contains.length; i++) {
                downstream_load += this.contains[i].get_24h_downstream_load();
            }
        }
        return downstream_load;
    }


    set_status(new_status) {
	if (this.status != new_status) {
	    this.status = new_status;
	    // this.switch_div.style.backgroundColor = this.get_current_color(0.25);
    	    this.update_load_info();
	    console.log('Circuit/set_status:', this.name, this.status);
	    return true;
	} else {
	    console.log('Circuit/set_status:', 'UNCHANGED!', this.name, this.status);
	    return false;
	}
    }

    // event.target.checked, checked is a boolean
    process_switch_event(event) {
	console.log(this.pcl_type + '/process_switch_event:')
	// https://stackoverflow.com/questions/32438068/perform-an-action-on-checkbox-checked-or-unchecked-event-on-html-form
	if (this.set_status(event.target.checked)) {
	    this.propagate_status();
	}
    }

    sync_state() {
	if (this.status != this.my_switch.checked) {
	    this.my_switch.checked = this.status;
	}
    }

    propagate_status() {
	for (let i = 0; i < this.contains.length; i++) {
	    this.contains[i].update_status(this.status);
	}
    }

    update_status(new_status) {
	if (this.set_status(new_status)) {
	    this.sync_state();
	    this.propagate_status();
	}
    }

    update_load_info() {
	// https://stackoverflow.com/questions/41384379/use-javascript-to-change-text-only-in-an-element
	this.load_info.textContent = this.get_downstream_load();
	if (this.contained_by) { this.contained_by.update_load_info() };
    }

    // only change the status of non-critical circuits when utility status changes
    utility_status_change(new_status) {
	if (!this.get_critical()) {
	    this.update_status(new_status);
	}
    }

    // 'rgb(56, 75, 126)',
    pie_color() {
        return ('rgb(' + this.on_color.r + ',' + this.on_color.g + ',' + this.on_color.b + ')')
    }

    get_status() {
	return this.status
    }

    // set the critical status to status of the html check box
    set_critical(my_switch) {
	this.critical = my_switch.target.checked;
	// When critical is changed, update the configured runtime
	this.contained_by.update_cfg_runtime();
	console.log('Circuit/set_critical:', this.name, this.critical);
    }

    assign_contained_by(my_source) {
	this.contained_by = my_source;
    }

    get_critical() {
	return this.critical;
    }

    add_to_panel() {
	insert_component(this, this.get_loads_count());
    }

}

/////////////////////   Load Class     ////////////////////////
class Load {

    constructor(my_name, my_watt, my_minute) {
        this.pcl_type = 'Load';
        this.name = my_name;
        this.watt = my_watt;  // Power used when ON in watts
        this.minute = my_minute;  // Minutes of ON usage per day
        this.status = false;
        this.off_color = {
            r : 92,
            g : 61,
            b : 25,
	        alpha: 255
	    };
        this.critical_capable = false;
        this.containing_div_id = 'LoadsDIV';
        this.contained_by = null;
        this.contains = []; // Loads don't have any children
    }

    preload_model(my_p) {
	    this.cad = my_p.loadModel(this.file, false);
    }

    get_current_color(alpha) {
	    var status_color;
        if (this.status) {
            status_color = this.contained_by.get_on_color();
        } else {
            status_color = this.off_color;
        }
        return 'rgb(' + status_color.r + ',' + status_color.g + ',' + status_color.b + ',' + alpha + ')';
    }

    pie_color() {
	var my_circuit_on_color = this.contained_by.get_on_color();
        return ('rgb(' + my_circuit_on_color.r + ',' + my_circuit_on_color.g + ',' + my_circuit_on_color.b + ')')
    }

    set_status(new_status) {
        if (this.status != new_status) {
            this.status = new_status;
            // this.switch_div.style.backgroundColor = this.get_current_color(0.25);
            this.update_load_info();
            console.log('Load/set_status:', this.name, this.status);
            return true;
        } else {
            console.log('Load/set_status:', 'UNCHANGED!', this.name, this.status);
            return false;
        }
    }

    // event.target.checked, checked is a boolean
    process_switch_event(event) {
        console.log(this.pcl_type + '/process_switch_event:')
        if (event.target.checked && this.contained_by.status) {
            // https://stackoverflow.com/questions/32438068/perform-an-action-on-checkbox-checked-or-unchecked-event-on-html-form
            this.set_status(event.target.checked);
        } else {
            this.my_switch.checked = false;
            this.set_status(false);
        }
        }

        sync_state() {
        if (this.status != this.my_switch.checked) {
            this.my_switch.checked = this.status;
        }
    }

    propagate_status() {
        for (let i = 0; i < this.contains.length; i++) {
            this.contains[i].update_status(this.status);
        }
    }

    update_status(new_status) {
        if (this.set_status(new_status)) {
            this.sync_state();
            this.propagate_status();
        }
    }

    update_load_info() {
        // https://stackoverflow.com/questions/41384379/use-javascript-to-change-text-only-in-an-element
        this.load_info.textContent = this.get_downstream_load();
        if (this.contained_by) { this.contained_by.update_load_info() };
    }

    is_active() {  // if my status is true AND my parent's status is true, then I'm active
	    return ( this.status && this.contained_by.get_status() );
    }

    assign_contained_by(my_circuit) {
	    this.contained_by = my_circuit;
        // this.off_color = {
        //     r : my_circuit.on_color.r,
        //     g : my_circuit.on_color.g,
        //     b : my_circuit.on_color.b,
	    //     alpha: my_circuit.on_color.alpha
	    // };
    }

    add_to_panel() {
    	insert_component(this, 1);
    }

    // get_current_watts () {
    //     if (this.status == true) {
    //         return this.watt;
    //     } else {
    //         return 0;
    //     }
    // }

    get_downstream_load() {
        if (this.status == true) {
            return this.watt;
        } else {
            return 0;
        }
    }

    get_24h_downstream_load() {
        if (this.status == true) {
            return this.watt * this.minute
        } else {
            return 0;
        }
    }

    draw3D(my_p) {

        var on_color = [];
        my_p.push();
        // formatting here

        if (this.is_active()) {
            on_color = this.contained_by.get_on_color();
            my_p.fill(on_color.r, on_color.g, on_color.b, on_color.alpha);
        } else {
            my_p.fill(this.off_color.r, this.off_color.g, this.off_color.b, this.off_color.alpha);
        }
        my_p.model(this.cad);
        my_p.pop();
    }

}

///////////////////////////////// Typical Appliance Load Data  ///////////////////////////////////

// https://unboundsolar.com/solar-information/power-table
// https://www.altestore.com/diy-solar-resources/power-ratings-typical-for-common-appliances
// https://www.daftlogic.com/information-appliance-power-consumption.htm


function hr2min(hours) {
    return 60 * hours;
}

/////////////////////////////////   Fridge   ///////////////////////////////////
class Fridge_load extends Load {
    constructor(my_name) {
	super(my_name, 60, hr2min(24)); // 'super' means call the parent class's constructor
	this.status = true;
	this.load_type = "fridge";
	this.file = 'media/fridge.obj';
    }
}

/////////////////////////////////   Water Heater   ///////////////////////////////////
class Water_heater_load extends Load {
    constructor(my_name) {
        // super(my_name, 4500, hr2min(4)); // // according to usage data
        super(my_name, 4500, hr2min(6)); // runs for 15 minutes every 'advance 1 hour' 
        this.status = true;
        this.load_type = "water heater";
        this.file = 'media/water_heater.obj';
    }
}

/////////////////////////////////   Oven   ///////////////////////////////////
class Oven_load extends Load {
    constructor(my_name) {
	// super(my_name, 80, hr2min(1)); // according to usage data
    super(my_name, 80, hr2min(24)); // runs for 1 hour every 'advance 1 hour'
	this.status = true;
	this.load_type = "oven";
	this.file = 'media/oven.obj';
    }
}

/////////////////////////////////   Microwave   ///////////////////////////////////
class Microwave_load extends Load {
    constructor(my_name) {
        // super(my_name, 1000, 15); // according to usage data
        super(my_name, 1000, hr2min(6)); // runs for 15 minutes every 'advance 1 hour' c
        this.status = true;
        this.load_type = "microwave";
        this.file = 'media/microwave.obj';
    }
}


/////////////////////////////////   Dryer   ///////////////////////////////////
class Dryer_load extends Load {
    constructor(my_name) {
        // super(my_name, 3000, hr2min(1)); // according to usage data
        super(my_name, 3000, hr2min(24)); // runs for 1 hour every 'advance 1 hour'
        this.status = true;
        this.load_type = "laundry dryer";
        this.file = 'media/dryer.obj';
    }
}


/////////////////////////////////   Washer   ///////////////////////////////////
class Washer_load extends Load {
    constructor(my_name) {
	// super(my_name, 80, hr2min(1)); // according to usage data
    super(my_name, 80, hr2min(24)); // runs for 1 hour every 'advance 1 hour'
	this.status = true;
	this.load_type = "laundry washer";
	this.file = 'media/washer.obj';
    }
}
/////////////////////////////////   Furnace   ///////////////////////////////////
class Furnace_load extends Load {
    constructor(my_name) {
        // super(my_name, 5000, hr2min(12)); // according to usage data
        super(my_name, 5000, hr2min(12)); // runs for 30 minutes every 'advance 1 hour'
        this.status = true;
        this.load_type = "furnace";
        this.file = 'media/furnace.obj';
    }
}

/////////////////////////////////   Stove   ///////////////////////////////////
class Stove_load extends Load {
    constructor(my_name) {
        // super(my_name, 4000, 30); // according to usage data
        super(my_name, 4000, hr2min(12)); // run for 30 minutes every 'advance 1 hour' 
        
        this.status = true;
        this.load_type = "stove";
        this.file = 'media/stove.obj';
    }
}

/////////////////////////////////   TV   ///////////////////////////////////
class TV_load extends Load {
    constructor(my_name) {
        // super(my_name, 150, hr2min(2.5)); // according to usage data
        super(my_name, 150, hr2min(24)); // runs for 1 hour every 'advance 1 hour'
        this.status = true;
        this.load_type = "tv";
        // https://www.bls.gov/opub/btn/volume-7/television-capturing-americas-attention.htm
        this.file = 'media/tv.obj';
    }
}

/////////////////////////////////   Wifi Router   ///////////////////////////////////
class Wifi_load extends Load {
    constructor(my_name) {
        super(my_name, 7, hr2min(24)); // according to usage data // runs for 1 hour every 'advance 1 hour'
        this.status = true;
        this.load_type = "router";
        this.file = 'media/wifi.obj';
    }
}


/////////////////////////////////   Lights   ///////////////////////////////////
class Light_load extends Load {
    constructor(my_name, my_x, my_y, my_z, my_z_light) {
        // super(my_name, 18, hr2min(6)); // according to usage data
        super(my_name, 18, hr2min(24)); // runs for 1 hour every 'advance 1 hour'
        this.status = true;
        this.location = {
            x : my_x,
            y : my_y,
            z : my_z, 
            z_light: my_z_light
            
	};

	this.load_type = "light";
	this.file = 'media/light.obj';
    }

    // light has own draw3D function because there are multiple instances of its class, each with a different location
    draw3D(my_p) {
	    var on_color = [];

	my_p.push();
        // formatting here
        my_p.translate(this.location.x, this.location.y, this.location.z);
        if (this.is_active()) {
            on_color = this.contained_by.get_on_color();
            my_p.fill(on_color.r, on_color.g, on_color.b, on_color.alpha);
        } else {
            my_p.fill(this.off_color.r, this.off_color.g, this.off_color.b, this.off_color.alpha);
        }
        my_p.model(this.cad);
        my_p.pop();
    }

     // A maximum of 5 pointLight can be active at one time
     draw_point_light(my_p, my_zoom){
        // my_p.push();

        if (this.is_active()) {
            // my_p.pointLight(255, 249, 164, this.location.x, this.location.y, 108);
            // my_p.pointLight(255, 249, 164, 0, 0, 108);
            // my_p.pointLight(255, 249, 164, 120, 120, 120);
            //my_p.box(50, 50, 50);
            my_p.spotLight(255, 249, 164, this.location.x * my_zoom, this.location.y * my_zoom, this.location.z_light * my_zoom, 0, 0, -1, Math.PI/3, 5);
            // console.log(this.location.x, this.location.y, this.location.z);
           //  my_p.push();
            // my_p.translate(120, 120, 120);
             // my_p.translate(this.location.x, this.location.y, this.location.z );
            // my_p.box(50, 50, 50)

            // QUESTION: why isn't light in same location as the box?
            // QUESTION: how to control intensity of light?
           //  my_p.pop();
        }
        // my_p.pop();
    }

}

/////////////////////////////////   Computers   ///////////////////////////////////
class Computer_load extends Load {
    constructor(my_name, my_x, my_y, my_z, my_a) {
        // super(my_name, 80, hr2min(8)); // according to usage data
        super(my_name, 80, hr2min(24)); // runs for 1 hour every 'advance 1 hour'
        this.status = true;
        this.angle = my_a;
        this.location = {
            x : my_x,
            y : my_y,
            z : my_z
        };

	this.load_type = "computer";
	this.file = 'media/computer.obj';
    }
    // light has own draw3D function because there are multiple instances of its class, each with a different location
    draw3D(my_p) {
	var on_color = [];

    // my_p.pointLight(255, 249, 164, this.location.x, this.location.y, 108);
    // my_p.pointLight(255, 249, 164, 0, 0, 108);
	my_p.push();
    // my_p.pointLight(255, 249, 164, this.location.x, this.location.y, 108);
	// formatting here
	my_p.translate(this.location.x, this.location.y, this.location.z);
    my_p.rotateZ(my_p.radians(this.angle));

    // my_p.box(50, 50, 50)
	if (this.is_active()) {
        on_color = this.contained_by.get_on_color();
	    my_p.fill(on_color.r, on_color.g, on_color.b, on_color.alpha);

	} else {
	    my_p.fill(this.off_color.r, this.off_color.g, this.off_color.b, this.off_color.alpha);
	}
	my_p.model(this.cad);
	my_p.pop();
    }
}

/////////////////////////////////   Fans   ///////////////////////////////////
class Fan_load extends Load {
    constructor(my_name, my_x, my_y, my_z) {
        // super(my_name, 80, hr2min(6)); // according to usage data
        super(my_name, 80, hr2min(24)); // runs for 1 hour every 'advance 1 hour'
        this.status = true;
        this.location = {
            x : my_x,
            y : my_y,
            z : my_z
	    };

	this.load_type = "fan";
	this.file = 'media/fan.obj';
    // this.angle = 0;
    }

    // light has own draw3D function because there are multiple instances of its class, each with a different location
    draw3D(my_p) {
        var on_color = [];

        // my_p.pointLight(255, 249, 164, this.location.x, this.location.y, 108);
        // my_p.pointLight(255, 249, 164, 0, 0, 108);
        my_p.push();
        // my_p.pointLight(255, 249, 164, this.location.x, this.location.y, 108);
        // formatting here
        my_p.translate(this.location.x, this.location.y, this.location.z);
        // my_p.box(50, 50, 50)
        if (this.is_active()) {
            on_color = this.contained_by.get_on_color();
            my_p.fill(on_color.r, on_color.g, on_color.b, on_color.alpha);
            // my_p.rotateX(this.angle);
        } else {
            my_p.fill(this.off_color.r, this.off_color.g, this.off_color.b, this.off_color.alpha);
        }
        my_p.model(this.cad);
        my_p.pop();
        // angle += 0.025;
        }
}

/////////////////////////////////   Element   ///////////////////////////////////
class Element {
  constructor() {
    // These are system parameters, be careful changing or overwriting these in your classes
    this.class = this.constructor.name;
    this.children = [];
    this.points = [];
    this.selected = false;

    // feel free to modifty these in the base class or subclasses
    this.size = { "x": 10, "y": 10, "z": 10 };
    this.color = "#888888";
    this.rotation = 0;
    this.opacity = 1;


  }
  draw2D(ap5) { };
  draw3D(ap5) { };
  mouseClicked3D(ap5) {
    return false;
  };
  mouseClicked2D(ap5) {
    if (Math.abs(ap5.mouseX - this.points[0].x) <= this.size.x  / 2 && Math.abs(ap5.mouseY - this.points[0].y) <= this.size.y / 2)  {
      this.selected = !this.selected;
      return true;
    }
    else return false;
  };

  mouseDragged(pdelta) {
    for (var j = 0; j < this.points.length; j++) {
      this.points[j].x += pdelta.x;
      this.points[j].y += pdelta.y;
    }
  }

  getColorOpacitySelect(ap5) {
    // creates an color with alpha from the current color text string and opacity number (0<1)
    var acolor;
    if (ap5) {
    if (this.selected) acolor = ap5.color("#ff7777"); else acolor = ap5.color(this.color);
    }
    else {
      if (this.selected) acolor = color("#ff7777"); else acolor = color(this.color);
    }
    acolor.setAlpha(this.opacity * 255);
    return acolor;

  }

}

/////////////////////////////////   OnePointElement   ///////////////////////////////////

class OnePointElement extends Element {
  constructor(pts) {
    super();
    this.points = pts;
  }
}
OnePointElement.createType = "onePoint";



/////////////////////////////////   TwoPointElement   ///////////////////////////////////


class TwoPointElement extends Element {
  constructor(pts, asize, angle) {
    super();
    this.points = pts;

    this.closed = false;
  }


  mouseClicked2D(ap5) {
    var mousePoint = { "x": ap5.mouseX, "y": ap5.mouseY, "z": 0 };
    for (var i = 0; i < this.points.length; i++) {

      if (closePoints(this.points[i], mousePoint)) {
        this.selected = !this.selected;
        return true;
      }
    }
    return false;
  };

}
TwoPointElement.createType = "twoPoint";

class MultiPointElement extends Element {
  constructor(pts, asize, angle) {
    super();
    this.points = pts;
    // Now fix the start - end point situation
    // if the start and end points are close, get rid of the end point and close the walls
    if (this.points && closePoints(this.points[0], this.points[this.points.length - 1])) {
      this.points.pop();
      this.closed = true;
    }
    //otherwise the shape is open
    else this.closed = false;
  }


  mouseClicked2D(ap5) {
    var mousePoint = { "x": ap5.mouseX, "y": ap5.mouseY, "z": 0 };
    for (var i = 0; i < this.points.length; i++) {

      if (closePoints(this.points[i], mousePoint)) {
        this.selected = !this.selected;
        return true;
      }
    }
    return false;
  };

}
MultiPointElement.createType = "multiPoint";
