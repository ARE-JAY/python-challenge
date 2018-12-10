#Ryan Johnson
#Homework #2
# Add items to the program
import os
import csv


election_csv = os.path.join("election_data.csv")

# Open the csv file

with open(election_csv, newline="") as csvfile:

# Create csv reader 

    csvreader = csv.reader(csvfile, delimiter=",") 

# read the heading 

    csv_header = next(csvfile)
  
# * A complete list of candidates who received votes
    canidates = []   
    for row in csv.reader(csvfile):
        if row[2] not in canidates:
            canidates.append(row[2])
   # print(canidates)



with open(election_csv, newline="") as csvfile:

# Create csv reader 

    csvreader = csv.reader(csvfile, delimiter=",") 

# read the heading 

    csv_header = next(csvfile)
    votes = []   
    for row in csv.reader(csvfile):
        votes.append(row[2])
    from collections import defaultdict
    voteCount = defaultdict(int)
    for name in votes:
        voteCount[name] += 1
    
 # * The winner of the election based on popular vote.   
    winner = ""   
    winningCount = 0
    for name, value in voteCount.items():
        if int(voteCount[name]) > winningCount:
            winner = name 
            winningCount = int(voteCount[name])

 # * The total number of votes each candidate won
    khanVote = int(voteCount["Khan"])
    correyVote = int(voteCount["Correy"])
    liVote = int(voteCount["Li"])
    otooleyVote = int(voteCount["O'Tooley"])
    
 # * The total number of votes cast
    totalVotes = (khanVote + correyVote + liVote + otooleyVote)
    
    khanVote_pct = round((float(khanVote/totalVotes)* 100),3)
    correyVote_pct = round((float(correyVote/totalVotes)* 100),3)
    liVote_pct = round((float(liVote/totalVotes)* 100),3)
    otooleyVote_pct = round((float(otooleyVote/totalVotes)* 100),3)

    # print(totalVotes)
    # print(khanVote)
    # print(khanVote_pct)
    # print(correyVote)
    # print(correyVote_pct)
    # print(liVote)
    # print(liVote_pct)
    # print(otooleyVote)
    # print(otooleyVote_pct)
    # print(winner)
    # print(winningCount)

    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: ',str(totalVotes))
    print(f'-------------------------')
    print(f'{canidates[0]}: {khanVote_pct}% ({khanVote})')
    print(f'{canidates[1]}: {correyVote_pct}% ({correyVote})')
    print(f'{canidates[2]}: {liVote_pct}% ({liVote})')
    print(f'{canidates[3]}: {otooleyVote_pct}% ({otooleyVote})')
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')


    txtFile = open('PyPoll.txt', 'w')

    txtFile.write (f'Election Results' + '\n') 
    txtFile.write (f'-------------------------' + '\n')
    txtFile.write (f'Total Votes: {str(totalVotes)}' + '\n')
    txtFile.write (f'-------------------------' + '\n')
    txtFile.write (f'{canidates[0]}: {khanVote_pct}% ({khanVote})' + '\n')
    txtFile.write (f'{canidates[1]}: {correyVote_pct}% ({correyVote})' + '\n')
    txtFile.write (f'{canidates[2]}: {liVote_pct}% ({liVote})' + '\n')
    txtFile.write (f'{canidates[3]}: {otooleyVote_pct}% ({otooleyVote})' + '\n')
    txtFile.write (f'-------------------------' + '\n')
    txtFile.write (f'Winner: {winner}' + '\n')
    txtFile.write (f'-------------------------' + '\n')

txtFile.close()




