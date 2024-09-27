 #!/bin/bash
 # White space may be messed up do to file type conversion
 strURL="https://portapi.tntech.edu/express/api/unprotected/getDirectoryInfoByAPIKey.php?apiKey=764AA90B-E06A-4A05-BE23-774DF2ECC33>
 # loop through all paramaters passed to the shell script
 for strUser in "$@"
 do
    # concatenate strURL and the current item in the loop
    strTempURL=$strURL+"$@"

    # create a new variable that contains the results of your curl statement
    arrResult=$(curl ${strTempURL})

    # debug statement to test response
    echo $arrResult

# here you need to create a new variable that will contain the length of the array from the results
    # HINT:  You should be able to pipe arrResult to jq and use its length utility to find this

    intTotal=$(echo "$arrResult" | jq 'length')

    # debug statement to test if we get the length
    echo $intTotal

# create a new variable to hold the current index number for your while loop;
    intCurrent=0

# create a while loop to allow the process to run until you are out of items to process
    while [ "$intCurrent" -lt "$intTotal" ];
    do
        # debug statement to check if we are moving through iterations
        echo $intCurrent

        # debug statemet to check that we pulled the EmailAddress
        echo $arrResult | jq -r .[${intCurrent}].EmailAddress

# establish a new variable that will contain the current Email Address and exclude or substring the value prior to the @
    strUsers=$(echo $arrResult | jq -r .[${intCurrent}].EmailAddress | cut -d '@' -f 1)

# debug statement to check that we have properly selected and stored the email address value to strUsers
    echo $strUsers

# check to see if the user exists on our VM or not
    if id "$strUsers" >/dev/null 2>&1;
    then
        echo "Error: $strUsers was not added to the system as they already exist" >> users.log
    else
        echo "Success: $strUsers was successfully added to the system" >> users.log
    fi
        intCurrent=$((intCurrent+1))
    done
done
