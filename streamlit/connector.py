import os
import pathlib

from PIL.Image import QUAD
import genesis as gn

   
class Handler(object):
    instance = None
    data = None

    @staticmethod
    def getInstance():
        if Handler.instance == None :
            Handler.instance = Handler()
        return Handler.instance


    class ParamHolder():
        instance = None
        ground = None
        imageset = None
        region = []
        
        def setGround(self, ground):
            self.ground = ground
            print("setGround is called ", self.ground)

        def setRegionData(self, imageset, region):
            self.imageset = imageset
            self.region = region
            print("setRegionData is called ", self.region)
            #gn.Calibrator.getInstance()


    class BaseData() : 
        cur_path = os.getcwd() +'/'
        os.chdir('../')
        prj_path = os.getcwd() +'/'
        img_path = prj_path + 'image/'
        libname = prj_path + 'libgenesis.dylib'
        print(cur_path, prj_path, img_path)

        def getImageList(self):
            newlist = []
            imglist = os.listdir(self.img_path)
            imglist.sort()
            for i in imglist :
                if i == '.DS_Store':
                    continue
                newlist.append(self.img_path + i)

            return newlist

        def getGroundType(self):
            gr_type = { "BaseballHome" : 1,
                        "BaseballGround" : 2,
                        "BasketballHalf" : 3,
                        "BasketballGround" : 4,
                        "Boxing" : 5,
                        "IceLinkHalf" : 6,
                        "IceLink" : 7,
                        "SoccerHalf" : 8,
                        "Soccer" : 9,
                        "Taekwondo" : 10,
                        "TennisHalf" : 11 ,
                        "Tennis" : 12,
                        "Ufc" : 13,
                        "VolleyballHalf" : 14,
                        "VolleyballGround" : 15,
                        "Football" : 16 }
            return gr_type

