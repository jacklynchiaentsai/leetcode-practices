// time: O(1), space: O(1)
// string operations and hashmap
class Solution {
public:
    string reformatDate(string date) {
        // parsing the date string
        string parsed[3],temp;
        int index = 0;
        stringstream ss(date);
        while (ss >> temp){
            parsed[index++] = temp;
        }
        string formatted = parsed[2] + "-";

        string months[12] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        unordered_map<string, string> monthmap;
        for(int i = 1; i<=12; i++){
            if (i<=9){
                monthmap[months[i-1]] = "0" + to_string(i);
            } else{
                monthmap[months[i-1]] = to_string(i);
            }
        }

        formatted += monthmap[parsed[1]] + "-";

        if (parsed[0].length() == 3){
            formatted += "0"+ parsed[0].substr(0,1);
        } else{
            formatted += parsed[0].substr(0,2);
        }
        
        return formatted;

    }
};
