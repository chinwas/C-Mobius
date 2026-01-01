#include <iostream>
#include <vector>
int main(){

    std::vector<char> v_1= {'H','e','l','l','o',',','j','a','n','e','4','!'};
    
while(true){
    char x = v_1[0];
    for(int i=0;i<12 ; i++){
        
        v_1[i]= v_1[(i+1)%v_1.size()];
        
    }
    v_1[11]= x ;
    std::cout<<"                         "<<v_1[0]<<"                             \n";
    std::cout<<"            "<<v_1[1]<<"                         "<<v_1[2]<<"                \n";
    std::cout<<"         "<<v_1[3]<<"                             "<<v_1[4]<<"         \n";
    std::cout<<"        "<<v_1[5]<<"                               "<<v_1[6]<<"        \n";
    std::cout<<"          "<<v_1[7]<<"                             "<<v_1[8]<<"        \n";
    std::cout<<"           "<<v_1[9]<<"                           "<<v_1[10]<<"       \n";
    std::cout<<"                         "<<v_1[11]<<"                      \n";














}
    return 0;




}