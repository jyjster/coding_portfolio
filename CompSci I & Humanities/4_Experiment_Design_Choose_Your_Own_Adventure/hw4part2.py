'''
This program is for Hw04, Part 2: Choose Your Own Adventure.

Last modified: 02/28/19
By: Jordan Jackson
'''

### STORY INPUT DATA ###

'''
input data -- general format:

     events = list of all possible events (event variables)
          General Form: [[event_id], [event_id]]
          EX: events = [event0, event1, event2, event3]
        
     event variable: variable event# assigned to information corresponding to that event
          General form: event_id = [id, narrative text, question, choices]        
          EX: event_# = [int, 'narrative text', 'question?', [('choice 1', int), ('choice 2', int)]
          
    choices: a list of tuples
         EX: choices = [(potential choice, next_event_id), (potential choice, next_event_id)]
     
input data -- example:      
     
     # Start Event
     event0 = [0, 'At a traffic light.', 'Should you **stop** or **go**?', [('stop', 1), ('go', 2)]]
     
     event1 = [1, 'Someone cuts you off.', 'Should you **honk** or **ignore**?', [('honk', 3), ('ignore', 3)]
     event2 = [2, 'Someone cuts you off.', 'Should you **honk** or **ignore**?', [('honk', 3), ('ignore', 3)]]
     
     # Ending Event
     event3 = [3, 'You arrived home.', '**End** game or **restart**?', [('end', -1), ('restart', 0)]]
'''
text0 = "BEES ARE IMPORTANT TO THE SUSTAINABILITY OF AGRICULTURAL AND ECOLOGICAL SYSTEMS\n\n\
Almost all flowering plants, such as food crops, depend on pollinators. \n\n\
At least 1/3 of what we eat relies on animal pollinators, such as honeybees.\n\n\
MYSTERIOUSLY VANISHING BEES\n\nClint is a commercial beekeeper with healthy beehives. \
He offers the beehives’ services as pollinators to growers of a variety of crops across \n\
the United States. While his honeybees were pollinating cotton fields in Texas, they \n\
'collapsed' mysteriously—the bees abandoned their beehives and did not return.\n\n\
As the mysterious collapses persisted and intensified, bee researched termed it \n\
‘colony collapse disorder’ or CCD. By 2006, beekeepers (commercial and recreational)\n\
in the United States had lost between 15% to 75% of their beehives due to CCD.\n\n\
THE CCD CONTROVERSY\n\nStakeholders, including as researchers, beekeepers, crop growers, government\n\
regulators, and agrochemical companies, have different understandings of what CCD is, \n\
what causes it, and what should be done about it. Most agree that we do not understand\n\
why beehives become susceptible to CCD in the first place.\n\nGAME: CREATE YOUR OWN EXPERIMENT\n\n\
You are a honeybee scientist. You are interested in investigating the link between \n\
newer systemic pesticides and CCD. You need to design your next experiment."
text1 = 'Testing a direct, causal effect emphasizes precision and control, \n\
rather than reflecting nature’s complexity. Now, you need to decide \n\
the level of pesicides you will expose the bees to.'
text2 = 'You will be working in actual fields and bee yards to engage with multiple \n\
and indirect ways pesticides contribute to CCD. Such an approach takes into \n\
account the interactive and cumulative factors of the complex CCD phenomenon. Think \n\
about what sorts of measures may provide you with useful information about aspects \n\
of the hives.'
text3= 'Higher doses are more likely to produce clear and conclusive results. You \n\
may perform your study in a laboratory setting or in fields and bee yards.'
text4 = 'Low doses model the likely exposure bees have on agricultural fields. You \n\
may perform your study in a laboratory setting or in fields and bee yards.'
text5 = 'Using formal and narrowly quantitative measures is the standard among \n\
the scientific community. Next, decide on whether you will be honeybees that \n\
are chronically or acutely exposed to pesticides.'
text6 = 'ALthough informal measures are more often used by commerical beekeepers \n\
to assess hive health, than by scientists, these measures consider the \n\
multidimensional aspects of a hive, rather than splitting up a hive as isolated \n\
units. Next, decide on whether you will be honeybees that are chronically or \n\
acutely exposed to pesticides.'
text7 = 'While field studies may provide more realistic conditions, you will need \n\
to seek experimental control of all potentially confounding environmental variables.\n\
For example, consider how you might keep the honeybees in your control plot from \n\
traveling to the treated plot?'
text8 = 'Laboratory settings provide you with greater control and precision.'
text9 = text7
text10 = text8
text11 = 'Beekeepers support your choice to study the chronic effects \n\
of pesticide exposure because it considers CCD may be caused by accumulated \n\
factors over the long term. In order to conduct your study, you need to submit \n\
your experiment proposal to grant funding agencies.'
text12 = "Shorter time frames allow you to conduct multiple trials of your \n\
experiment. Plus, as the EPA's toxicity tests also focus on acute toxicity, you \n\
will be following a well-established research practice. In order to conduct \n\
your study, you need to submit your experiment proposal to grant funding agencies."
text13= text11
text14 = text12
text15 = "It has only been 1 week since you had submitted your experiment proposals \n\
and it looks like you've received serveral responses."
text16 = text15
text17 = 'All of your applications were denied. One letter mentioned that while the \n\
agency appreciated your consideration for the variety of factors that may be\n\
involved, your experiment would produce, at best, suggestive evidence. The \n\
agency was looking for experiments that could produce definitive causal evidence.'
text18 = 'A beekeeping trade association replied confirming that received \n\
your application and it is currently pending review. The other response\n\
you received rejected your use of the measures developed by \n\
beekeepers because apparently, scientists are the supposedly \n\
objective ones and are the experts here.'
text19 = 'Experiment Results: bees in the dosed group were significantly more \n\
vulnerable to infection than bees from the control group\n\
Critique from Stakeholders: the high doses you used are not field-realistic'
text20 = 'Experiment Results: Only at a particular high dosage levels does \n\
half of the treated group die within several days.\n\
Consequences: Your study was published in high-prestige scientific \n\
journals. The EPA Standard LD50 was created based on studies, \n\
including your’s, that set dosage levels below as allowed and as \n\
causing no observed adverse effects to bees.'
text21 = 'Experiment Results: no effects were observed in bee colonies exposed to \n\
field-realistic (low) dosages\n\
Critique From Stakeholders: skeptical of reliability since bees experience a \n\
vast amount of environment variability in field studies'
text22 = 'Experiment Results: honeybee colonies chronically exposed to \n\
low levels of pesticides are not harmed\n\
Critique From Stakeholders: lacks relevancy to bee colonies in natural conditions'

q0 = 'Test **one** direct causal factor or test **multiple** indirect factors?'
q1 = 'Test a **high** or **low** dose of pesticide?'
q2 = 'Record **formal** measures, such as the number of comb cells containing immature bees (or brood)\n\
and nectar and pollen stored by foraging honeybees inside each beehive,\n\
or **informal** measures, such as brood pattern and the number of frames covered with bees?'
q3 = 'Will the experiment take place in a **lab** or **field**'
q4 = q3
q5 = 'Will the study be over a **long** or **short** period of time?'
q6 = q5
q7 = 'Type **next**'
q8 = q7
q9 = q7
q10 = q7
q11 = '**Submit** your experiment design for funding.'
q12 = q11
q13= q11
q14 = q11
q15 = q7
q16 = q7
q17 = 'Do you want to **end** or **restart** game?'
q18 = q17
q19 = q17
q20 = q17
q21 = q17
q22 = q17


# Starting Event
event0 = [0, text0, q0, [('one', 1), ('multiple', 2)]]

event1 = [1, text1, q1, [('high', 3), ('low', 4)]]
event2 = [2, text2, q2, [('formal', 5), ('informal', 6)]]
event3 = [3, text3, q3, [('field', 7), ('lab', 8)]]
event4 = [4, text4, q4, [('field', 9), ('lab', 10)]]
event5 = [5, text5, q5, [('long', 11), ('short', 12)]]
event6 = [6, text6, q6, [('long', 13), ('short', 14)]]
event7 = [7, text7, q7, [('next', 19)]]
event8 = [8, text8, q8, [('next', 20)]]
event9 = [9, text9, q9, [('next', 21)]]
event10 = [10, text10, q10, [('next', 22)]]
event11 = [11, text11, q11, [('submit', 15)]]
event12 = [12, text12, q12, [('submit', 15)]]
event13 = [13, text13, q13, [('submit', 16)]]
event14 = [14, text14, q14, [('submit', 16)]]
event15 = [15, text15, q15, [('next', 17)]]
event16 = [16, text16, q16, [('next', 18)]]

# Ending Events
event17 = [17, text17, q17, [('end', -1), ('restart', 0)]]
event18 = [18, text18, q18, [('end', -1), ('restart', 0)]]
event19 = [19, text19, q19, [('end', -1), ('restart', 0)]]
event20 = [20, text20, q20, [('end', -1), ('restart', 0)]]
event21 = [21, text21, q21, [('end', -1), ('restart', 0)]]
event22 = [22, text22, q22, [('end', -1), ('restart', 0)]]
                
events = [event0, event1, event2, event3, event4, event5,\
          event6, event7, event8, event9, event10, event11,\
          event12, event13, event14, event15, event16, event17,\
          event18, event19, event20, event21, event22]
    
### FUNCTION DEFINITIONS ###

def q_and_a(question):
    
    '''
    This function asks the user a question and takes their inputed answer.
    
    Input parameters:
    question: string from corresponding eventID list
    
    Return value:
    string: user's answer in lowercase
    '''    
    print()
    # Print question and assign user's input as 'answer'.
    answer = input('{}\n'.format(question))
    # Make input lowercase for processing.
    answer = answer.lower()
    return answer


def process_choices(question, choices, record):
    
    '''
    This function proccesses the user's answer. It checks the validity \
         of the input based on the possible answer choices.
    
    Input parameters:
    question: string
    choices: list of tuples (string, event_ID)
    record: list of user's decisions
    
    Return value:
    next_event_id: int corresponding to event_id of next event
    '''
    
    # Keep asking the question until the user answers it correctly.
    while True:
        answer = q_and_a(question)
        record.append(answer)
        # Test if input is valid.
        for c in choices:
            if answer == c[0]:
                print('You chose {}.\n'.format(answer))
                # Returns event_id based on user's answer.
                return c[1]
        # Input is invalid. Need to redirect to ask for the input.
        print('Invalid input. Please try again.')

def process_event(event_data, record_list):
    
    '''
    This function is executed for each event. It prints an event's \
         narrative text, prints the question, takes and tests the user's \
         input, and figures out which event to go to next \
         given the user's answer. 
    
    Input parameters:
    event_data: list of information for 1 event list includes ints, strings, and a nested list
         event_data = [ID, narrative_text, question, [(choice1, event_ID), (choice2, event_ID)]]
    
    Return value:
    next_event_id: integer for next event to redirect user to
    '''
    
    print(event_data[1])
    question = event_data[2]
    choices = event_data[3]
    # Returns next_event_id.
    return process_choices(question, choices, record_list)


### PROGRAM STARTS HERE ###

# At the beginning of each game, the 'record' list needs to be empty/reset.
record = []
# Starting event_id = 0
next_event_id = 0

while True:
    # Tell the computer which event_id to process now.
    event = events[next_event_id]
    # process_event function returns next_event_ID
    next_event_id = process_event(event, record)
    # In the case the user chooses to end the game.
    if next_event_id == -1:
        break
    # In the case the user chooses to restart the game.
    elif next_event_id == 0:
        # 'record' list needs to be reset to an empty list.
        record = []
        # An extra line helps the user visually distinguish among each game play.
        print()

# Executes at the end of the game.
print('Game over.')
print('Here are your methodological choices:\n\n{}'.format(record))
print()
print("This game was based on and inspired by the book 'Vanishing Bees: \n\
Science, Politics, and Honeybee Health' by Suryanarayanan and Kleinman.")

