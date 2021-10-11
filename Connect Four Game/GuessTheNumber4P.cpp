
#include<bits/stdc++.h>

using namespace std;
//Rights reserved for DEVSTRONS'
int HID_no=rand();

int main(){
    //Here size of array represents the number of players
    int player[4];
    int i=0;
    cout<<"There will be 4 players in the game with 10 attempts each : "<<endl;
    //This loop will help us controle the flow for number of attempts 
    while(i<10){
        //Now It's time to take input form players
        cout<<endl<<10-i<<" Attempts left "<<endl;
        cout<<endl<<"Player 1 : ";
        cin>>player[0];
        cout<<endl<<"Player 2 : ";
        cin>>player[1];
        cout<<endl<<"Player 3 : ";
        cin>>player[2];
        cout<<endl<<"Player 4 : ";
        cin>>player[3];
      //Now let's check the results 
        for(int j=0;j<4;j++){
            if (player[j]==HID_no){
              //player won 
                cout<<endl<<"Player "<<j+1<<" won the match ! "<<endl; 
                return 0;
            }
            else{
              //Better luck next time
                cout<<endl<<"Player "<<j+1<<" better luck next time ! "<<endl;
            }
        }    
      //attempt value updation
        i++;
    }
    return 0;
}
