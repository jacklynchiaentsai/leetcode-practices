// time: O(n) assuming length of cpdomains[i] is fixed, space: O(n)
// use upon seeing character as way to split strings in c++
class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        unordered_map<string, int> domaincount;
        for (string cpdomain: cpdomains){
            string count = "";
            string subdomain = "";
            // reading number by encountering first white space
            for(int i=0; i<cpdomain.length(); i++){
                if (cpdomain[i] == ' ')
                    break;
                count += cpdomain[i];
            }

            int numcount = stoi(count);

            // don't need to reverse each time as long corresponds to same in map
            // starting from backwards we want to analyze upon each .
            for(int i = cpdomain.length() - 1; i>=0; i--){
                if (cpdomain[i] == ' '){
                    domaincount[subdomain] += numcount;
                    break;
                }
                    
                if (cpdomain[i] == '.'){
                    domaincount[subdomain] += numcount;
                } 
                subdomain += cpdomain[i]; // have to add . eventually
            }
        }
        vector<string> ans;
        // returning array of count-paired domains
        for(auto it: domaincount){
            string cp = to_string(it.second) + " ";
            string str = it.first;
            reverse(str.begin(), str.end());
            cp += str;
            ans.push_back(cp);
        }
        return ans;
    }
};
