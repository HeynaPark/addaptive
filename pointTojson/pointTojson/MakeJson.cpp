#include <iostream>
#include "nlohmann/json.hpp"
#include <fstream>
#include <iomanip>

using json = nlohmann::json; 

typedef enum groundtype
{
    BaseballHome,
    BaseballGround,
    BasketballHalf,
    BasketballGround,
    Boxing,
    IceLinkHalf,
    IceLink,
    SoccerHalf,
    Soccer,
    Taekwondo,
    TennisHalf,
    Tennis,
    Ufc,
    VolleyballHalf,
    VolleyballGround,
    Football
} GDT;

class WorldCoordinates4d {
    double X1 = -1.0F;
    double Y1 = -1.0F;
    double X2 = -1.0F;
    double Y2 = -1.0F;
    double X3 = -1.0F;
    double Y3 = -1.0F;
    double X4 = -1.0F;
    double Y4 = -1.0F;
};

class DscID {
    

};

void pointTojson()
{
    //SCNEN
//id
    std::string dsclist[] = { "013055","013056","013057","013058","013059","013060" };


    json jObj = json::object();
    json jArr = json::array();

    //GDT
    jObj["stadium"] = "SoccerHalf";

    //SCNEN();
    //four_fpt[i].x
    json world;
    world["X1"] = 330.0;
    world["Y1"] = 601.0;
    world["X2"] = 473.0;
    world["Y2"] = 601.0;
    world["X3"] = 490.0;
    world["Y3"] = 710.0;
    world["X4"] = 310.0;
    world["Y4"] = 709.0;

    json point2d = json::object();

    point2d["UpperPosX"] = -1.0;
    point2d["UpperPosY"] = -1.0;
    point2d["MiddlePosX"] = -1.0;
    point2d["MiddlePosX"] = -1.0;
    point2d["LowerPosX"] = -1.0;
    point2d["LowerPosX"] = -1.0;

    //sc,kpt
    json point3d;
    point3d["X1"] = 6456;
    point3d["Y1"] = 456456;
    point3d["X2"] = 456;
    point3d["Y2"] = 456;
    point3d["X3"] = 456;
    point3d["Y3"] = 456;
    point3d["X4"] = 456;
    point3d["Y4"] = 709.0;
    point3d["Y4"] = 709.0;
    point3d["Y4"] = 709.0;

    jObj["world_coords"] = world;


    auto arr = json::array();

    for (int i = 0; i < sizeof(dsclist) / sizeof(dsclist[0]); ++i)
    {
        json jDsc = json::object();

        jDsc["dsc_id"] = dsclist[i];

        jDsc["pts_2d"] = point2d;

        jDsc["pts_3d"] = point3d;


        arr.push_back(jDsc);

    }



    jObj["points"] = arr;



    std::ofstream file("../Point.pts");
    file << std::setw(4) << jObj << '\n';
    std::cout << std::setw(4) << jObj << '\n';
  
    
}

int main()
{



    pointTojson();
}