/*
when saving both way relationships, make sure mark the key and its reverse in recursion as visited to avoid infinite recursion looping
n = number of equations, m = number of queries
time: O(m * n^2)
space: O(m+n)
*/

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        vector<double> responses;
        unordered_map<string, double> eq_map;
        unordered_set<string> ele_set;
        unordered_set<string> eq_set;

        for(int i =0; i< equations.size(); i++){
            vector<string> equation_pair = equations[i];
            double value = values[i];

            string equation = equation_pair[0] + "/" + equation_pair[1];
            string rev_equation = equation_pair[1] + "/" + equation_pair[0];
            eq_map[equation] = value;
            eq_map[rev_equation] = 1.0 / value;

            ele_set.insert(equation_pair[0]);
            ele_set.insert(equation_pair[1]);
        }

        for(vector<string> query: queries){
            string first = query[0];
            string second = query[1];

            if (ele_set.find(first) == ele_set.end() || ele_set.find(second) == ele_set.end()){
                responses.push_back(-1.0);
            } else if (first == second){
                responses.push_back(1.0);
            } else{
                eq_set.clear();
                responses.push_back(findVal(first, second, eq_map, eq_set));
            }
        }

        return responses;
    }

    double findVal(string start, string end, unordered_map<string, double>& eq_map, unordered_set<string>& eq_set){
        string equation = start + "/" + end;
        if (eq_map.find(equation) != eq_map.end()){
            return eq_map[equation];
        }

        for(auto it: eq_map){
            string eq = it.first;
            double val = it.second;

            if (eq.find(start+ "/") == 0){
                if (eq_set.find(eq) != eq_set.end()){
                    continue;
                }
                
                int divindex = eq.find("/");
                string newstart = eq.substr(divindex+1);
                // mark as visited to avoid infinite loop
                eq_set.insert(eq);
                eq_set.insert(newstart + "/" + start); // reverse equation

                double inter_ans = findVal(newstart, end, eq_map, eq_set);
                if (inter_ans != -1.0){
                    eq_map[equation] = val * inter_ans;
                    return eq_map[equation];
                }
            }
        }

        return -1.0;
    }
};

/*
eq_map = {"a/b": 2.0, "b/e": 3.0}

*/
