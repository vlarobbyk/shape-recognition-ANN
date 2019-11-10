
#include "HuMomentsExtractor.hpp"



HuMomentsExtractor::HuMomentsExtractor(string srcDir, string outDir, string ext){
    this->srcDir = srcDir;
    this->outDir = outDir;
    this->ext = ext;
}

string HuMomentsExtractor::join(double d[7]){
    stringstream ss;
    for (int i=0;i<7;i++){
        if (i<6)
            ss << d[i] << ";";
        else
            ss << d[i];
    }
    return ss.str();
}

vector<string> HuMomentsExtractor::listDir(){
    vector<string> entries;
    
    DIR *pDIR = opendir(this->srcDir.c_str());
    
    struct dirent *entry;
    string name;
    
    while((entry = readdir(pDIR))!=NULL){
        name = string(entry->d_name);
        if (name.size()>3 && name.compare(name.size()-3,3,this->ext)==0)
            entries.push_back(this->srcDir+"/"+name);
    }
    
    closedir(pDIR);
    
    return entries;
}

bool HuMomentsExtractor::extractHuMoments(vector<string> entries){
    
    ofstream data;
    data.open(this->outDir+"/HuMoments.csv",ios::out);
    
    data << "f1;f2;f3;f4;f5;f6;f7;Fichero" << endl;
    
    Mat imageO;
    Mat image;
    Mat binary;
    Moments _moments;
    double huMoments[7];
    
    for (int i=0;i<entries.size();i++){
        cout << "Entry:{" << entries[i] << "}" << endl;
        Mat imageO = imread(entries[i]);
        Mat image;
        Mat binary;
        cvtColor(imageO,image,COLOR_BGR2GRAY);
        threshold(image, binary, 128, 255, THRESH_BINARY);
        
        _moments = moments(binary, true);
        
        HuMoments(_moments, huMoments);
        data << join(huMoments) << ";" << entries[i] << endl;
        
//         for (int i=0;i<7;i++)
//             cout << huMoments[i] << endl;
        
//         namedWindow("img",WINDOW_AUTOSIZE);
//         imshow("img",image);
        
//         waitKey(0);
    }
    data.close();
    return true;
}
