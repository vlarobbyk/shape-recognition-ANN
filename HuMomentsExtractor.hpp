#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <sstream>
#include <fstream>

#include <dirent.h>

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgcodecs/imgcodecs.hpp>


using namespace std;
using namespace cv;

class HuMomentsExtractor{
    
    private:
        string srcDir;
        string outDir;
        string ext;
        
        
    public:
        HuMomentsExtractor(string = "train", string = ".", string = "png");
        bool extractHuMoments(vector<string>);
        vector<string> listDir();
        string join(double[7]);
};
