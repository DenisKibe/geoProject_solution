#output the number and number of occurrence that occurrence the most given a string

def solution(n):
    #create empty list to hold the number of count
    count_occ=[]
    #create empty list to hold the numbers
    the_number=[]
    
    #declare two variables count and first_num
    count=0
    first_num=''
    
    #declare the indexer for list
    counter_list=0
    
    #create an infinate loop to loop through the list
    #end the loop if an out of range error occurs
    while True:
        #use try catch to catch the index out of range error
        try:
            our_number=n[counter_list]
            #if count ==0 meaning it the 1st number in the list
            if count==0:
                #set our first_num variable to the this number 
                first_num=our_number
                #append our number to the_number list
                the_number.append(our_number)
                #increase count and counter_list so as to go to next
                count+=1
                counter_list+=1
            else:
                #if count is not 0
                #in this case our second number in the list
                #check if our_number is equal to the first_num
                if our_number==first_num:
                    #we increase count and indexer(counter_list)
                    count+=1
                    counter_list+=1
                else:
                    #if our_number is not equal to first_num
                    #we append the count to the count_occ
                    #reset our count to 0
                    count_occ.append(count)
                    count=0
        except:
            #End the loop if an index out of range error is encounted
            break
                
    
    
    #check the max occurrence            
    max_occ=max(count_occ)
    #find the corresponding index number in the_number list
    index_of_max=count_occ.index(max_occ)
    
    #output
    return {'max_occuring_number_is':int(the_number[index_of_max]),'number_of_occurence_is':max_occ}
    
    
n="1233999556789"
print(solution(n))
