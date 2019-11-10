
#include "HuMomentsExtractor.hpp"


int main(int argc, char *argv[]){
    
    HuMomentsExtractor *huM = new HuMomentsExtractor();
    vector<string> entries = huM->listDir();
    for (int i=0;i<entries.size();i++){
        cout << entries[i] << endl;
    }
    
    bool r = huM->extractHuMoments(entries);
    
    delete huM;
    return 0;
}
