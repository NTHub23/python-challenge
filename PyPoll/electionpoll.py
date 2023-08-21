#!/usr/bin/env python
# coding: utf-8

# In[70]:


import csv
import os

Election_I_Data = os.path.join(".", "Resources", "election_data.csv")

Election_Result = os.path.join(".", "Election_Analysis.txt")


Total_Votes = 0
List_of_Candidate = []

#{} indicates dictionary
Total_Votes_Candidate= {}

Candidate_winner = ""
Winning_Candi_Count = 0



with open(Election_I_Data) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)
    
        
    for voter in reader:
        Total_Votes = Total_Votes + 1
        
        Candidate_Name = voter[2]
        
        if Candidate_Name not in List_of_Candidate:
            
            List_of_Candidate.append(Candidate_Name)
            
            Total_Votes_Candidate[Candidate_Name] = 0
            
        Total_Votes_Candidate[Candidate_Name] +=1
        
        
               
        
with open(Election_Result,  "w") as txt_file:
    Election_Results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes : {Total_Votes}\n"        
        f"-------------------------\n")
    print(Election_Results)
    txt_file.write(Election_Results)

    

#To Calculate Percentage of votes for each candidate  
    for Each_Candidate in Total_Votes_Candidate:
            Total_Cand_Votes = Total_Votes_Candidate[Each_Candidate]
            Voter_Percentage = float(Total_Cand_Votes)/float(Total_Votes) * 100
            

#To find the winning candidate
            
            if(Total_Cand_Votes > Winning_Candi_Count):
                Winning_Candi_Count = Total_Cand_Votes
                Winning_Candidate = Each_Candidate
                
            Final_Result = f"{Each_Candidate}: {Voter_Percentage:.3f}% ({Total_Cand_Votes})\n"
            
            print(Final_Result, end="")
            txt_file.write(Final_Result)
      
    
    
    Election_Results_Summary = (
        f"-------------------------\n"
        f"Winner: {Winning_Candidate}\n"
        f"-------------------------")
    
    print(Election_Results_Summary)
    
    
    txt_file.write(Election_Results_Summary)
    

