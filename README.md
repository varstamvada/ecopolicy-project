I am using this repo to the test and research the API at Congress.gov

The objective is to pull the list of all members of the congress. This https://api.congress.gov/v3/member?api_key=[INSERT_KEY] provides a list of all congresspeople. 
The max returned value is 250 and the offset can be used to get more members

The next API endpoint is https://api.congress.gov/v3/bill/117/hr

This gives the bill but I haven't figured out the best way to get every single bill in a given congress. 

The api.congress.gov has data from 1973 but for this project, I will consider only from the year 2000

How are the Bills organized?
The bills are organized by Congress sessions. Each two-year Congress typically includes two legislative sessions, although third or special sessions were common in earlier years. But since 1973, there have been no sessions with third sessions. At this time in Jan 2024, we are in the 118 session of Congress

Bill Type values are hr (House Bills), hconres (House Concurrent Resolutions), hjres (House Joint Resolutions), hres (House Simple Resolutions), s (Senate Bills), sres (Senate Simple Resolutions), sconres (Senate Concurrent Resolutions, sjres (Senate Joint Resolutions).

GET /bill/:congress/:billType






