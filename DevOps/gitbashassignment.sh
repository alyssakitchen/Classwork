#!/usr/bin/env bash

# Global variables, should set to the first two parameters passed to the script
strPlayer1=$1
strPlayer2=$2


# show a message to the screen asking if player 1, wtih their name
# is ready.  Include that they should type yes to begin
echo  "Ready Player 1, $strPlayer1?  Type yes to begin"

#capture the user repsonse to evaluate below
read strResponse1

# evaluate the response from player 1 and determine if
# they responded yes, if so provide a message to continue
# else provide a message that you cannot continue
# and exit with code 1
if [ "$strResponse1" = "yes" ]
then
  echo "Excellent!  Up next is a question for Player2."
else
  echo "That is too bad.  The game cannot go on without you being ready."
  exit 1
fi

# show a message to the screen asking if player 2, with their name
# is ready.  Include that they should type yes to begin
echo "Ready Player 2, $strPlayer2?  Type yes to begin"

# capture the user response to evaluate below
read strResponse2


# evaluate the response from player 2 and determine if
# they responded yes, if so provide a message to continue
# else provide a message that you cannot continue
# and exit with code 2
if [ "$strResponse2" = "yes" ]
then
  echo "Excellent!  We will begin."
else
  echo "That is too bad. The game cannot go on without you being ready."
  exit 2
fi

echo "$strPlayer1, what is your favorite number?"
read intFavNumPlay1

echo "$strPlayer2, what is your favorite number?"
read intFavNumPlay2

# this block of code should be a conditional test
# that compares player 1's response to their favorite
# number to player 2's.  If player1 has a higher number
# or equal number then a response should be shown on the
# screen indicating that player 1 (use their name passed
# as a parameter) goes first, otherwise a similar message
# indicating player 2 should go first is shown
if [ $intFavNumPlay1 -ge $intFavNumPlay2 ]
then
  echo "$strPlayer1 will go first"
else
  echo "$strPlayer2 will go first"
fi
