class Solution {
public:
    int minimumSum(int n, int k) {
        int sum = 0;
        int sizecount = 0;
        stack<int> st;
        int i = 1;
        while (sizecount < n){
            if (i>=k){
                sum += i;
                sizecount += 1;
            } else{
                if (st.empty()){
                    sum += i;
                    st.push(k-i);
                    sizecount += 1;
                } else{
                    int cur = st.top();
                    if (i == cur){
                        st.pop();
                    }
                    else if ((i+cur) > k){
                        sum += i;
                        if ( i != (k-i))
                            st.push(k-i);
                        sizecount += 1;
                    }
                }
            }
            
            i++;
        }
        
        return sum;
        
    }
};
