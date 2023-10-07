// since year range starts from 1971 just compare number of days passed since 1971: saves time from evalutating year, month, day
// use helper functions, avoid making repeated calculations
// time: O(1), space: O(1)

class Solution {
public:
    bool isLeapYear(int year){
        if (year % 400 == 0){
            return true;
        } else if (year % 4 == 0 && year % 100 != 0){
            return true;
        }
        return false;
    }

    int daysfrom1971(string date, unordered_map<int, int> yeardaycount){
        int year = stoi(date.substr(0,4));
        int month = stoi(date.substr(5,2));
        int day = stoi(date.substr(8,2));

        int count = yeardaycount[year];
        int months[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
        for(int i = 1; i< month; i++){
            count += months[i-1];
        }
        if (isLeapYear(year) && month >2){
            count++;
        }

        count += day;

        return count;
    }

    int daysBetweenDates(string date1, string date2) {

        // count number of days up until year from 1971
        unordered_map<int, int> yeardaycount;
        yeardaycount[1971] = 0;
        for(int i = 1972; i<=2100; i++){
            if (isLeapYear(i-1)){
                yeardaycount[i] = yeardaycount[i-1] + 366;
            } else{
                yeardaycount[i] = yeardaycount[i-1] + 365;
            }
        }

        int dateonecount = daysfrom1971(date1, yeardaycount);
        int datetwocount = daysfrom1971(date2, yeardaycount);

        return abs(dateonecount - datetwocount);

    }
};
