
/*****************************************************************************
*                                                                            *
*                            Extractor      								 *
*                                                                            *
*   Copyright (C) 2021 By 4dreplay, Incoporated. All Rights Reserved.        *
******************************************************************************

    File Name       : Extractor.Hpp
    Author(S)       : Me Eunkyung
    Created         : 17 Sep 2021

    Description     : Extractor.Hpp
    Notes           : Feature Extractor From Image.
*/
#include <filesystem>
#include <fstream>
#include <vector>
#include <cmath>
#include "../util/DefData.hpp"
#include "../util/Pip.hpp"


using namespace std;
using namespace cv;

class Extractor {

public :
    Extractor(string& imgset, int cnt , int* roi);
    ~Extractor();
    int Execute();
    int VerifyNumeric();
    void DrawInfo();
    PARAM* p;

    vector<Mat> imgs;
    vector<SCENE> cal_group;


private :

    bool is_first;
    bool verify_mode = false;

    SCENE* cur_train = 0;
    SCENE* cur_query = 0;

    vector<Mat>LoadImages(const string& path);
    void SaveImageSet(vector<Mat>& images);
    void InitializeData(int cnt, int* roi);
    int UpdateConfig();
    void NormalizePoint(SCENE* sc, int maxrange);
    int CalculateCenter(SCENE* sc1, SCENE* sc2);
    int DecomposeHomography();
    int FindHomographyP2P(); 

    Mat ProcessImages(Mat& img);
    int GetFeature(SCENE* sc);
    vector<KeyPoint> MaskKeypointWithROI(vector<KeyPoint>* oip);
    void SetCurTrainScene(SCENE* sc) { cur_train = sc; };
    void SetCurQueryScene(SCENE* sc) { cur_query = sc; };
    int MakeMatchPair();
    int PostProcess();
    int CalVirtualRod();
    int SolvePnP();
    int SolveRnRbyH();
    ADJST CalAdjustData();
    int Warping();
    int WarpingStep1();
    int WarpingStep2();
    int AdjustImage(ADJST adj);

    Point2f GetRotatePoint(Point2f ptCenter, Point2f ptRot, double dbAngle);
    Mat GetRotationMatrix(float rad, float cx, float cy);    
    Mat GetScaleMatrix(float scalex, float scaley, float cx, float cy);    
    Mat GetScaleMatrix(float scalex, float scaley);        
    Mat GetTranslationMatrix(float tx, float ty);

    Mat GetRotationMatrix(float rad);    
    Mat GetMarginMatrix(int width, int height, int marginx, int marginy, int marginw, int marginh);
};
