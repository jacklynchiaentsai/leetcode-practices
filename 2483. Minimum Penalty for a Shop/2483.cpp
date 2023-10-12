// time: O(n), space: O(1)
// simulation, note that closes at hour j so perform condition check before updating current value
// I only care about the least penalty

class Solution {
public:
    int bestClosingTime(string customers) {
        bool ally= true;
        int bestIndex = 0;
        int curpenalty = 0, bestpenalty = curpenalty;
        for(int i =0; i< customers.length(); i++){
            if (curpenalty < bestpenalty){
                bestpenalty = curpenalty;
                bestIndex = i;
            }  
            
            if (customers[i] == 'Y')
                curpenalty--;
            else{
                curpenalty++;
                ally = false;
            }
                
        }

        // checking for the last index in this case won't close until end of hours
        if (curpenalty < bestpenalty){
            bestpenalty = curpenalty;
            bestIndex = customers.length();
        }  

        return bestIndex;

    }
};
