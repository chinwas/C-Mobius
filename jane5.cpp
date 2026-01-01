#include <iostream>
#include <vector>
#include <chrono>
#include <thread>
int main(){

    std::vector<char> v_1= {'@','%','#','*','+','=','-',':','.','.','.','.'};
    std::chrono::milliseconds delay_time(32);
while(true){
    char x = v_1[0];
    for(int i=0;i<12 ; i++){
        
        v_1[i]= v_1[(i+1)%v_1.size()];
        
    }
    v_1[11]= x ;
    std::cout<<"              "<<v_1[0]<<"                             \n";
    std::cout<<"            "<<v_1[11]<<"  "<<v_1[1]<<"                \n";
    std::cout<<"         "<<v_1[10]<<"      "<<v_1[2]<<"         \n";
    std::cout<<"        "<<v_1[9]<<"        "<<v_1[3]<<"        \n";
    std::cout<<"          "<<v_1[8]<<"     "<<v_1[4]<<"        \n";
    std::cout<<"           "<<v_1[7]<<"   "<<v_1[5]<<"       \n";
    std::cout<<"             "<<v_1[6]<<"                      \n";

    std::this_thread::sleep_for(delay_time);
    std::cout << "\033[12A";
}
    return 0;























}