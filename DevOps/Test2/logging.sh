#!/usr/bin/env bash

# INSTRUCTIONS - YOU MUST READ #
# GenerativeAI, ChatGPT specifically CAN and should be used on this section of the Exam #
# You will not be able to complete this in a timely manner unless you use GenerativeAI

# There is no limitation on prompts that can be used here

# The bash script must perform the following:
# Interface with the URL below.
# Iterate across the returned results and
# append a file in your home directory when ran from anywhere
# inside the file you should create a list of PunchIDs, their Type, and the PunchDateTime on a single line
# formated similar to this:
# PunchID: 260f362c6a4d | PunchType: Clock In | DateTimeOccured: 2023-10-24 17:07:02 | RecordedToLog: 16Nov2023
# The final section on the line above shoudl be the current date in that format

strURL="https://www.thesimplehomestead.com/simpletime/time.php?SessionID=eb5a01f8-7959-47b5-ba26-fbb0884ee82b"
data=$(curl -s $strURL)

# Process the data and append the results to the temporary file
intCurrent=0
arrayResults=$(echo ${data} | jq -r '.results')
intNumPunches=$(echo ${arrayResults} | jq -r 'length')

echo "results: $arrayResults"
echo "num: $intNumPunches"

while [ "$intCurrent" -lt "intNumPunches" ]
do
  # Extract the PunchID, PunchType, and PunchDateTime from the JSON data
  punchID=$(echo $line | jq -r '.PunchID')
  punchType=$(echo $line | jq -r '.PunchType')
  punchDateTime=$(echo $line | jq -r '.DateTimeOccured')

  # Format the data and append it to the temporary file
  formattedLine="PunchID: $punchID | PunchType: $punchType | DateTimeOccured: $punchDateTime | RecordedToLog: $(date +'%d%b%Y')"
  echo "$formattedLine" >> ~/punches.log
done

# Notify the user that the file has been updated
echo "Punches log updated successfully at $(date +'%Y-%m-%d %H:%M:%S')"