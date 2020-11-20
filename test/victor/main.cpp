#include <iostream>
#include <vector>

using std::vector;

int main()
{
    std::cout << "Hello World!\n";

    std::vector<int> back_point;
    back_point.resize(3);

    // back_point.push_back(1);
    // back_point.push_back(1);
    back_point[1] = 1;

    
    for (int i = 0; i < back_point.size(); i++)
    {
        std::cout << i << ":" << back_point[i] << "\n";
    }

    return 0;
}