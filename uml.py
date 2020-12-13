print(
    '''
     ,------------.                            
     |ChatBot     |                            
     |------------|                            
     |#name       |                            
     |------------|                            
     |+init_bot() |                            
     |+start_bot()|                            
     |+bot_end()  |                            
     `------------'                            
            |                                  
            |                                  
            |           ,------------------.   
            |           |ManagePhones      |   
  ,------------------.  |------------------|   
  |TextInput         |  |------------------|   
  |------------------|  |+print_list()     |   
  |#text             |  |+print_name()     |   
  |------------------|  |+reinit()         |   
  |+change_input()   |  |+filter()         |   
  |+remove_punc()    |  |+filter_by_os()   |   
  |+text_initiation()|  |+filter_by_price()|   
  `------------------'  |+sort()           |   
            |           |+sort_price()     |   
            |           |+recommend_phone()|   
            |           `------------------'   
            |                     |            
,----------------------.          |            
|ManageIntent          |          |            
|----------------------|          |            
|#intentObj            |          |            
|----------------------|          |            
|+extractIntent()      |          |            
|+check_second_intent()|          |            
|+get_response()       |          |            
`----------------------'          |            
            |                     |            
            |                     |           
            |         ,-----------------------.
            |         |Phone                  |
            |         |-----------------------|
    ,-------------.   |#id                    |
    |Intent       |   |#name                  |
    |-------------|   |#brand                 |
    |#db          |   |#os                    |
    |-------------|   |#price                 |
    |+set_intent()|   |#size                  |
    |+get_all()   |   |#color                 |
    `-------------'   |#recommend_score       |
                      |-----------------------|
                      |+get_phone(phone_num)  |
                      |+get_number_of_phones()|
                      `-----------------------'
                                               
              ,----------------.               
              |dbHandle        |               
              |----------------|               
              |#memory         |               
              |----------------|               
              |+read(json_file)|               
              `----------------'               
    '''
)