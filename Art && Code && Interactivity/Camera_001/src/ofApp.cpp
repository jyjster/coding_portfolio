#include "ofApp.h"

/*
 I was able to incorporate a GUI in allowing the user to set or change the target object tracking color by either setting the color via the color slider in the GUI or by click on the object on drawn vidGrabber on screen. In the process of merging Part1 and Part2, this feature got forgotten until the end, where I did not have time to debug it so I removed this feature completely from the final version of the project I am turning in.
 
    Furthermore, although not a necessarily super "clean" or seamless solution, I added a wireless bluetooth mouse for the
    user to switch between drawing mode (see EnableDrawing) and selecting mode (via menu bar of circles/buttons on the
    right side of the screen). As this feature conflicted with the mouse clicking (mousePresssed) code of the GUI/target
    object tracking color feature described above in the previous paragraph, I prioritized the later feature.
 
    // For a working version of the user-defined target object tracking color, please see
        // Branch: turnin-1
        // Repo: CameraProj-Unfinished-Part2/
 
 I used the facetracking code we wrote in-class as the basis for my OpenCV code
         // Branch: turnin-1
         // Repo: CameraProj-Unfinished-Part2/
 
 I spent a lot of time debugg misalignment of the contours and the centroid circle when in OF_FULLSCREEN.
 I also spent a significant amount of time working to develop and debug the array I used for drawing lines.
    // Repo: CameraProj-Unfinished-Part1/
*/

//--------------------------------------------------------------
void ofApp::setup(){
    // background image
    wall.load("wall.jpg");
    
    // buttons
    picker_x[0] = 1200;
    picker_x[1] = 1200;
    picker_x[2] = 1200;
    picker_x[3] = 1200;
    picker_x[4] = 1200;
    // picker_x[5] = 1200;
    
    
    picker_y[0] = 70;
    picker_y[1] = 220;
    picker_y[2] = 370;
    picker_y[3] = 520;
    picker_y[4] = 670;
    // picker_y[5] = 820;
    
    /* picker_y[0] = 70;
     picker_y[1] = 270;
     picker_y[2] = 470;
     picker_y[3] = 670;
     picker_y[4] = 850;
     picker_y[5] = 1050;
     */
    
    picker_color[0] = ofColor::white;
    picker_color[1] = ofColor::darkSalmon;
    picker_color[2] = ofColor::mediumSlateBlue;
    picker_color[3] = ofColor::black;
    picker_color[4] = ofColor::darkGrey;
    // picker_color[5] = ofColor::darkGrey;
    
    camWidth = 640;
    camHeight = 480;
    
    // MAJOR DEBUG: 1) need to float()values 2) float() both numerator and denominator
    w_scale_cam2vid = float(ofGetWidth())/float(camWidth);
    h_scale_cam2vid = float(ofGetHeight())/float(camHeight);
    
        // w_scale_cam2vid = 1.6;
        // h_scale_cam2vid = 1.6;
    
        // camWidth = ofGetWidth();
        // camHeight = ofGetHeight();
    
    // set default object tracking color
    
    // // in classhttp://code-poetry.com/
    targetColor.setHsb(3, 126, 146);
    
    
    // at home in dorm
    // targetColor.setHsb(4, 190, 250);
    
    // findHue = 0;
    // findSat = 0;
    // findBri = 0;
    
    // connecting default color to color in opencv
    findHue = targetColor.getHue();
    findSat = targetColor.getSaturation();
    findBri = targetColor.getBrightness();
    
    vidGrabber.setDeviceID(0);
    vidGrabber.initGrabber(camWidth, camHeight);
    
    rgb.allocate(camWidth, camHeight);
    hsb.allocate(camWidth, camHeight);
    hue.allocate(camWidth, camHeight);
    sat.allocate(camWidth, camHeight);
    bri.allocate(camWidth, camHeight);
    filter1.allocate(camWidth, camHeight);
    filter2.allocate(camWidth, camHeight);
    finalImage.allocate(camWidth, camHeight);
    
    // how to boolean in c++
    // https://www.tutorialspoint.com/cplusplus/cpp_if_else_statement.htm
    EnableDrawing = false;
    
    // Feature Removed
    gui.setup();
    gui.setPosition(ofPoint(5,5));
    gui.add(color.setup("Obj. Tracking Color",
                        targetColor,
                        ofColor(0),
                        ofColor(255)));
    
    nPts[0] = 0;
    paintColor = ofColor::black;
    // black, white, darksalmon, darkblue
    lineColor[0] = paintColor;
    
    // if we want to clear the canvas we need to
    // nLns = 0
    // nPts[0] = 0;
    
    ofSetLineWidth(10);
    
    // FEATURE that did not work out: having a "DONE" button that somehow saves only the linework (painting) of the user, then makes it a texture that scaled and sized to fit the Southwest side of EMPAC.
    // isSavingPDF = false;
}

//--------------------------------------------------------------
void ofApp::update(){
    vidGrabber.update();
    
    if (vidGrabber.isFrameNew()){
        rgb.setFromPixels(vidGrabber.getPixels());
        
        // mutating rgb, which is a copy ofvidGrabber.getPixels() that goes into OpenCV
        rgb.mirror(false, true);
        // https://openframeworks.cc/documentation/ofxOpenCv/ofxCvImage/#show_mirror
        
        hsb = rgb;
        hsb.convertRgbToHsv();
        hsb.convertToGrayscalePlanarImages(hue, sat, bri);
        
        int hueRange = 10;
        for (int i = 0; i < camWidth * camHeight; i++){
            filter1.getPixels()[i] = ofInRange(hue.getPixels()[i],
                                               findHue - hueRange,
                                               findHue + hueRange) ? 255 : 0;
        }
        filter1.flagImageChanged();
        
        int satRange = 20;
        for (int i = 0; i < camWidth * camHeight; i++){
            filter2.getPixels()[i] = ofInRange(sat.getPixels()[i],
                                               findSat - satRange,
                                               findSat + satRange) ? 255 : 0;
        }
        filter2.flagImageChanged();
        
        cvAnd(filter1.getCvImage(), filter2.getCvImage(), finalImage.getCvImage());
        finalImage.flagImageChanged();
        
        // Only look for 1 object/blob
        contours.findContours(finalImage, 1000, camWidth*camHeight/3, 1, false);
        
        for(int i=0; i<paintColor_count; i++) {
            
            // go through all dots to identify which dot is being clicked on (i)
            if (abs(ofDist(scaled_centroid_x,scaled_centroid_y, picker_x[i], picker_y[i])) < 50) {
                
                // working in live time
                // DEBUG
                // ofLog(OF_LOG_NOTICE, "DOT CLICKED [%d]", i);
                
                // paintColor = picker_color[i];
                
                if (i == 4){
                    // nLns = 0;
                    // nPts = 0;
                    nLns = 0;
                    // nPts[0] = 0;
                    for (int j = 0; j < MAXLINES; j++){
                        nPts[j] = 0;
                    }
                } else if (i == 5){
                    // TBD
                    // FEATURE attempt: "DONE" button
                } else{
                    paintColor = picker_color[i];
                }
            }
        }
        // ^ END OF paintColor for loop
        
        // moved start to draw code chunk from Part 1's mouseDragged
        if (EnableDrawing){
            if (nPts[nLns] < MAXPOINTS) {
                lineColor[nLns] = paintColor;
                pts[nLns][nPts[nLns]].x = scaled_centroid_x;
                pts[nLns][nPts[nLns]].y = scaled_centroid_y;
                nPts[nLns]++;
            }
            
        }
        
    }
}

//--------------------------------------------------------------
void ofApp::draw(){
    
    // vidGrabber.draw(0,0);
    
    // display it backwards on the screen, it does not mutated/change vidGrabber (contents) itself
    // vidGrabber.draw(camWidth,0,-camWidth,camHeight);
    // vidGrabber.draw(ofGetWidth(),0,-ofGetWidth(),ofGetHeight());
    // horizontally flip image, attempt 1
    // hsb.mirror(false, true);
    // https://openframeworks.cc/documentation/ofxOpenCv/ofxCvImage/#!show_mirror
    

    // hsb.draw(0, camHeight, 320, 240);
    
    // hue.draw(camWidth, 0, 320, 240);
    // sat.draw(camWidth, 240, 320, 240);
    // bri.draw(camWidth, 480, 320, 240);
    
    // filter1.draw(camWidth+320, 0, 320, 240);
    // filter2.draw(camWidth+320, 240, 320, 240);
    // finalImage.draw(camWidth+320, 480, 320, 240);
    
    // finder.draw(0,0);
    
    
    float scalefactor;
    float w_scalefactor = ofGetWidth() / wall.getWidth();
    // ofLog(OF_LOG_NOTICE, "the width scale factor is %f", w_scalefactor);
    
    float h_scalefactor = ofGetHeight() / wall.getHeight();
    // ofLog(OF_LOG_NOTICE, "the height scale factor is %f", h_scalefactor);
    
    // scalefactor is declared at the top of the file because other methods need to know it, now am assigning it
    scalefactor = min(w_scalefactor, h_scalefactor);
    // ofLog(OF_LOG_NOTICE, "scalefactor %f", scalefactor);
    
    int wall_width = wall.getWidth() * w_scalefactor;
    int wall_height = wall.getHeight() * h_scalefactor;
    
    wall.draw(0,0, wall_width, wall_height);
    
    // ofDrawCircle(1200, 110, 50);
    for (int c = 0; c < paintColor_count; c++) {
        ofPushStyle();
        ofSetColor(picker_color[c]);
        ofDrawCircle(picker_x[c], picker_y[c], 50);
        ofPopStyle();
    }
    
    // Text
    ofDrawBitmapString("CLEAR", 1180, 675);
    // ofDrawBitmapString("DONE", 1185, 825);
    
    // gui.draw();
    
    // contours.draw(0,0);
    
    for(int i =0; i < contours.nBlobs; i++){
        cout << "blob " << i << ":" <<  contours.blobs[i].centroid << endl;
        
        // ofDrawCircle(contours.blobs[i]::x, contours.blobs[i]::y, 50);
        // ofLog(OF_LOG_NOTICE, "test %f", contours.blobs[i].centroid);
        
        cout << "TEST X " << i << ":" <<  contours.blobs[i].centroid.x << endl;
        
        centroid_x = contours.blobs[i].centroid.x;
        centroid_y = contours.blobs[i].centroid.y;
        
        scaled_centroid_x = centroid_x * w_scale_cam2vid;
        scaled_centroid_y = centroid_y * h_scale_cam2vid;
        
        
        // centroid_x = contours.blobs[i].centroid.x * w_scale_cam2vid;
        // centroid_y = contours.blobs[i].centroid.y * h_scale_cam2vid;
        
        // ofLog(OF_LOG_NOTICE, "TEST | centroid %f, %f | scale %f, %f", centroid_x, centroid_y, w_scale_cam2vid, h_scale_cam2vid);
        
        // ofPushMatrix();
        // ofScale(w_scale_cam2vid, h_scale_cam2vid);
        // ofDrawCircle(centroid_x, centroid_y, 25);
        
        ofDrawCircle(centroid_x * w_scale_cam2vid, centroid_y * h_scale_cam2vid, 25);
        
        // ofPopMatrix();
    }
    
    ofPushStyle();
    //for every draw line
    
    for (int j = 0; j <= nLns; j++) {
        ofSetColor(lineColor[j]);
        
        if (nPts[j] > 1) {
            for (int i = 0; i < nPts[j] - 1; i++) {
                // I think ofSetLineWidth only accepts values up to 10
                // ofSetLineWidth(100);
                ofDrawLine(pts[j][i].x, pts[j][i].y, pts[j][i + 1].x, pts[j][i + 1].y);
            }
        }
    }
    
    ofPopStyle();
 
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    // ofLog(OF_LOG_NOTICE, "key %d", key);
    // key for number 1 is "key 49"
    
    // from Part 1 to test how/if to change drawing line color
    // if (key == 49){
        // paintColor = ofColor::white;
    // }
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){
    
}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
    
}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){
    
    // moved to in update()
    
    /*
    if (nPts[nLns] < MAXPOINTS) {
        lineColor[nLns] = paintColor;
        pts[nLns][nPts[nLns]].x = x;
        pts[nLns][nPts[nLns]].y = y;
        nPts[nLns]++;
    }
    */
}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){
    EnableDrawing = true;
    
    // PREVIOUS LEFT-OUT FEATURE: GUI OR USER CLICKING --> SET OR CHANGE TARGET OBJECT TRACKING COLOR
    /*
    int mx = x % camWidth;
    int my = y % camHeight;
    
    findHue = hue.getPixels()[my * camWidth + mx];
    findSat = sat.getPixels()[my * camWidth + mx];
    findBri = bri.getPixels()[my * camWidth + mx];
    */
    
    // DEBUG OBJECT TRACKING TARGET COLOR
     ofLog(OF_LOG_NOTICE, "color %d %d %d", findHue, findSat, findBri);
    
    /*
    // gui.add(color.setup("Obj. Tracking Target Color", ofColor(findHue, findSat));
    
    // color = findHue, findSat;
    // color.setup(findHue, findSat);
    
    
    // ofColor targetColor = ofColor(0);
    targetColor.setHsb(findHue, findSat, findBri);
    // https://openframeworks.cc/documentation/types/ofColor/#show_setHsb
    
    // SHAWN GUI
    // color.setup("Obj. Tracking Color", targetColor, ofColor(0), ofColor(255));
    

     // color.setup("Target Color",
                // targetColor,
                // ofColor(0),
                // ofColor(255));
     */
}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){
    EnableDrawing = false;
    
    // create a new line
    nLns++;
    // ofLog(OF_LOG_NOTICE, "nLns = %d", nLns);
    
    nPts[nLns] = 0;
    // reset so can draw again, BUT wipes canvas
    
    
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
