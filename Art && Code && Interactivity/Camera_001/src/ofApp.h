#pragma once

#include "ofMain.h"
#include "ofxOpenCv.h"
// #include "ofxCvHaarFinder.h"

#include "ofxCv.h"
#include "ofxGui.h"

#define MAXPOINTS 5000
#define MAXLINES 100
#define paintColor_count 5
#define CLEAR_index 4
#define DONE_index 5

class ofApp : public ofBaseApp{
    
public:
    void setup();
    void update();
    void draw();
    
    void keyPressed(int key);
    void keyReleased(int key);
    void mouseMoved(int x, int y );
    void mouseDragged(int x, int y, int button);
    void mousePressed(int x, int y, int button);
    void mouseReleased(int x, int y, int button);
    void mouseEntered(int x, int y);
    void mouseExited(int x, int y);
    void windowResized(int w, int h);
    void dragEvent(ofDragInfo dragInfo);
    void gotMessage(ofMessage msg);
    
    ofImage wall;
    ofColor paintColor;
    
    
    ofPoint pts[MAXLINES][MAXPOINTS];
    // pts is an array
    int nPts[MAXLINES];
    ofColor lineColor[MAXLINES];
    
    //const int paintColor_count = 4;
    // circle center pt
    
    float picker_x[paintColor_count];
    float picker_y[paintColor_count];
    ofColor picker_color[paintColor_count];
    
    int nLns = 0;
    
    int camWidth, camHeight;
    ofVideoGrabber vidGrabber;
    float w_scale_cam2vid;
    float h_scale_cam2vid;
    
    // ofxCvHaarFinder finder;
    ofxCvColorImage rgb, hsb;
    ofxCvGrayscaleImage hue, sat, bri, filter1, filter2, finalImage;
    
    ofxCvContourFinder contours;
    int findHue, findSat, findBri;
    
    float centroid_x;
    float centroid_y;
    float scaled_centroid_x;
    float scaled_centroid_y;
    
    ofxPanel gui;
    ofxColorSlider color;
    ofColor targetColor;
    
    bool EnableDrawing;
    
};
