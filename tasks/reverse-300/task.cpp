#include <iostream>
#include <string>

int main() {
    std::string input;

    std::cout << "Enter the flag:";
    std::cin >> input;

    if(input == "IKC{y0u_4c7u4lly_0p3n3d_7h47_w17h_n073p4d_88ff6c8a}"){
        std::cout << "Bravo!";
    }else{
        std::cout << "wr0n6 y0u l177l3 h4ck3r!";
    }

    return 0;
}