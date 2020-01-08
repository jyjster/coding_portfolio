//--------------------------------------------------------------

// *** NOTE TO PROF. LAWSON *** //

/*
I am writing to give you some context/background information about my work on this assignment.

I was/am very excited to take this class, and I am enjoying it a lot.

I have no prior experience with C++ nor OpenFrameworks, and so it is taking me signifcant time to learn them both.

During the course of this assignment, I explored several different technologies to add more interactivity, namely:
•Gesture recognition via the laptop camera
•Gesture recognition via Leap Motion
•Frequency analysis of the played sound(s) and more visually complex sound visualizers
 
Despite spending many hours on the two gesture recognition techniques, I wasn’t able to get them working for this assignment.
I also tried using classes and various add-ons, but that did not pan out either.
I finally got the FFT example integrated into my app to vary the images.

In summary, I had higher aspirations for this assignment than I was able to accomplish, and the time I spent on these other
libraries is not represented in the actual final version of the code I am submitting.

I am looking forward to increasing my mastery of additional libraries/technologies for future assignments.
 
Thanks, Jordan Jackson
*/

//--------------------------------------------------------------
// OVERVIEW: Soundscape Map with Interactive Elements
// CURRENT VERSION - BREAKDOWN:

/*
 user clicks on a cricle to play corresponding sound once (no loop)
 play sound when circle is clicked on
 overlapping sounds (can play multiple at a time)
 some of visual indication while the sound is playing
 changing cirlce color
 reactive to sound frequencies
 use fft
 do I need to use ofxFft add-on?
 */


// ORIGINAL BRAINSTORM AND VISION

// animating circles and iamges corresponding to sounds/locations
// use list/array for coordinates/locations of cirlces
// create class for circles and for images

// MAP AND SOUND LOCATIONS
// LEVEL 1: click on circle to play corresponding sound
// 1) play sound when click on circle
// 2) set background image and draw circles on top of it

// SOUNDSCAPE / SOUND
// fade in and fade out

// CIRCLES CHANGE / GET BETTER
// when you get to cirlce, it visually changes (changes size and/or color)
// circle expands to a set/particular size then stops OR grows so big/off the screen

// SOUNDSCAPE IMAGES
// corresponding image
// the whole screen changes to the corresponding image
// a smaller version of the corresponding image
// at center of screen
// near/at location of corresponding circle
// image moves towards perihpery from circle location while sound fades out
// image can scale (change depth) in doing so ^
// adding some sort of fade in/fade out for image

// SOUND VISUALIZATION
// visualizing the sound(s) while playing
// sound wave
// something more complicated/visually interesting


//--------------------------------------------------------------
// PROGRAM STARTS HERE

#include "ofApp.h"

// global declarations of variables for this file
float scalefactor;

float scaled_radius;

// const = constant integer because we don't want the size any dependent arrays to change
// 3 arrays: snd, dot_x, and dot_y
    // ideally, snd_dot would be its own class, but idk with C++
const int snd_dots = 12;

// snd is an array of SoundPlayers
ofSoundPlayer snd[snd_dots];

// 2 arrays of integers for sound circle/dot locations
int dot_x[snd_dots];

int dot_y[snd_dots];


//--------------------------------------------------------------


void ofApp::setup(){
    
    // IMAGE
        /* Map Image from Google Earth imagery, which is based on Image Landsat Copernicus imagery
           Accessed on September, 2019.*/
    
    map.load("map.jpg");
    
    // FFT
        /* FFT code based on Lewis Lepton's openFrameworks tutorial - 035 audio reactive shape
           https://youtu.be/IiTsE7P-GDs */
    
    fftSmooth = new float [8192];
    for (int i = 0; i < 8192; i++) {
        fftSmooth[i] = 0;
    }
    bands = 150;
    
    // SOUNDS
    // each are 5 seconds long, except for "09-bus.wav" which is 7.5 secs
    // all sounds are recorded by me on my iPhone, then converted from .m4a to .wav using Audacity
    
    snd[0].load("sound/01-motorbike.wav");
    dot_x[0] = 1483;
    dot_y[0] = 2309;
    
    snd[1].load("sound/02-fishing.wav");
    dot_x[1] = 735;
    dot_y[1] = 1750;
    
    snd[2].load("sound/03-highway.wav");
    dot_x[2] = 864;
    dot_y[2] = 1376;
    
    snd[3].load("sound/04-gravel.wav");
    dot_x[3] = 1037;
    dot_y[3] = 1146;
    
    snd[4].load("sound/05-bugs1.wav");
    dot_x[4] = 2283;
    dot_y[4] = 729;
    
    snd[5].load("sound/06-water1.wav");
    dot_x[5] = 2340;
    dot_y[5] = 1361;
    
    snd[6].load("sound/07-motorcycle.wav");
    dot_x[6] = 2881;
    dot_y[6] = 1179;
    
    snd[7].load("sound/08-water2.wav");
    dot_x[7] = 2936;
    dot_y[7] = 1479;
    
    snd[8].load("sound/09-busstop.wav");
    dot_x[8] = 3504;
    dot_y[8] = 1993;
    
    snd[9].load("sound/10-bugs2.wav");
    dot_x[9] = 4657;
    dot_y[9] = 1528;
    
    snd[10].load("sound/11-bugs3.wav");
    dot_x[10] = 1895;
    dot_y[10] = 420;
    
    snd[11].load("sound/12-bugs4.wav");
    dot_x[11] = 1636;
    dot_y[11] = 1391;
    
}

//--------------------------------------------------------------

// type: float because ofDrawCircle wants float parameters
float ofApp::scaleIt(float scale_factor, int value) {
    float result = scale_factor * value;
    return result;
}

//--------------------------------------------------------------

void ofApp::scaledCircle(int x, int y, float r, float scale) {
    float scaled_x = scaleIt( scale, x);
    float scaled_y = scaleIt( scale, y);
    // ofLog(OF_LOG_NOTICE, "scaledCircle %f %f %f %f", scaled_x, scaled_y, r, scale);
    ofDrawCircle( scaled_x, scaled_y, r);
}

//--------------------------------------------------------------

void ofApp::update(){
    
    // for FFT
    ofSoundUpdate();
    float * value = ofSoundGetSpectrum(bands);
    for (int i = 0; i < bands; i++) {
        fftSmooth[i] *= 0.2f;
        if (fftSmooth[i] < value[i]) {
            fftSmooth[i] = value[i];
        }
                    
    }
}


//--------------------------------------------------------------
void ofApp::draw(){
    
    // MAP BACKGROUND IMAGE
    
    float w_scalefactor = ofGetWidth() / map.getWidth();
    // ofLog(OF_LOG_NOTICE, "the width scale factor is %f", w_scalefactor);
    
    float h_scalefactor = ofGetHeight() / map.getHeight();
    // ofLog(OF_LOG_NOTICE, "the height scale factor is %f", h_scalefactor);
    
    // scalefactor is declared at the top of the file because other methods need to know it, now am assigning it
    scalefactor = min(w_scalefactor, h_scalefactor);
    // ofLog(OF_LOG_NOTICE, "scalefactor %f", scalefactor);
    
    int map_width = map.getWidth() * scalefactor;
    int map_height = map.getHeight() * scalefactor;
    
    map.draw(0,0, map_width, map_height);
    
    ofDrawRectangle(2, 2, 300, 75);
    ofDrawRectangle(0, map_height, 500, 20);
    
    // ofDrawRectangle(10, map_height - 20, 600, 30);
    ofPushStyle();
    ofSetColor(ofColor::black);
    ofDrawBitmapString("SOUNDSCAPE: Intersection of", 10, 30);
    ofDrawBitmapString("Poestenkill Canal and Hudson River", 10, 45);
    ofDrawBitmapString("in the City of Troy, NY", 10, 60);
    
    // ofDrawBitmapString("INSTRUCTIONS: Click on circle to play corresponding sound.", 5, map_height - 10);
    ofDrawBitmapString("INSTRUCTIONS: Click on circle to play corresponding sound.", 5, map_height + 15);
    ofPopStyle();
    
    
    
    
    float dot_radius_og = 140.0;
    // scaled_radius is declared at the top of the file, now am assigning it
    scaled_radius = dot_radius_og * scalefactor ;
    
    // push (save) the current style, the map before any dots
    ofPushStyle();
    
    // graphic settings for dots
    ofFill();

    
    // draw circles
    for(int i=0; i < snd_dots; i++) {
        // SPEED PROBLEM: sound isn't playing on time
        if (snd[i].isPlaying())
        {
            // circle radius changes size randomly
            ofSetColor(ofColor::forestGreen);
            // scaledCircle(dot_x[i], dot_y[i], ofRandom(.25 * scaled_radius, 2 * scaled_radius), scalefactor);
            
            // fft integrated into radius of green circles
            for (int j = 0; j < bands; j++){
                scaledCircle(dot_x[i], dot_y[i], -(fftSmooth[j] * 350), scalefactor);
            }
            
        }
        // else
        {
            ofSetColor(ofColor::salmon);
            scaledCircle(dot_x[i], dot_y[i], scaled_radius, scalefactor);
        }
    }
    // restoring the style form the map, prevent the map from turning the color of the circles
    ofPopStyle();
    
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){
    
}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
    
}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){
    
}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){
    
    for(int i=0; i<snd_dots; i++) {
        
        // go through all dots to identify which dot is being clicked on (i)
        if (abs(ofDist(x,y,scaleIt(scalefactor, dot_x[i]),scaleIt(scalefactor, dot_y[i]))) < scaled_radius) {
            
            // working in live time
            ofLog(OF_LOG_NOTICE, "dot[%d]", i);
            
            // not working (playing sounds) in live time
            snd[i].play();
            ofLog(OF_LOG_NOTICE, "sound[%d]", i);
            
            // test results: sounds play live, but the dot doesn't move
        }
    }
    
}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){
    
}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){
    
}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){
    
}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){
    
}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){
    
}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){
    
}
//--------------------------------------------------------------
