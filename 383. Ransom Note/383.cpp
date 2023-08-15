class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> magazinedict;
        // iterate through magazine
        for (int i = 0; i< magazine.length(); i++){
            char alpha = magazine[i];
            if (magazinedict.count(alpha)) {
                magazinedict[alpha] += 1;
            }
            else {
                magazinedict[alpha] = 1;
            }
        }

        // iterate through ransomnote
        for (int i = 0; i< ransomNote.length(); i++){
            char alpha = ransomNote[i];
            if (magazinedict.count(alpha)){
                magazinedict[alpha] -= 1;
                if (magazinedict[alpha] < 0){
                    return false;
                }
            } else{
                return false;
            }
        }

        return true;
    }
};
