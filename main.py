import streamlit as st
import openai 
import time

api_key = ['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','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','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']
list=[]
def get_question_topic(choice,api):

    openai.api_key=api
    messages = [{"role": "system", "content": "I'm a course suggester."}]
    message = (f'Generate the next question in simple terms to predict which is the suitable course with respect to the answer for the previous question. The answer to the previous question is "{choice}". The question should have options as "Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested". Avoid revolving the question solely around interest.')
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1)
        reply = chat.choices[0].message.content
        time.sleep(10)
    return reply

#def get_final_output(list):
    list.append('Select the most suitable course from colleges which are available in india based on the above questions with a paragrah suggesting why')
    messages=list
    client = openai(api_key='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')
    chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1)
    reply = chat.choices[0].message.content
    time.sleep(10)
    st.write(reply)
    return

st.title("Course Seeker")
interests = st.multiselect("Select your interests", ["Developer","Business","Finance and accounting","Technology","Office productivity","Personal development","Designing","Marketing","Lifestyle","Photography and video","Health and fitness","Music","Teaching and academics","Humanity","Creativity Art"])
if interests:
    #time.sleep(12)
    question=get_question_topic(interests,api_key[0])
    answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
    answer = st.radio(question, answer_options,index=None)
    choices=answer
    #list.append(f'question:{question},answer:{choices}')
    if choices:
        #time.sleep(12)
        question=get_question_topic(interests,api_key[1])
        answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
        answer = st.radio(question, answer_options,index=None)
        choices1=answer
        #list.append(f'question1:{question},answer1:{choices1}')
        if choices1:
            #time.sleep(12)
            question=get_question_topic(interests,api_key[2])
            answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
            answer = st.radio(question, answer_options,index=None)
            choices2=answer
            #list.append(f'question2:{question},answer2:{choices2}')
            if choices2:
                #time.sleep(10)
                question=get_question_topic(interests,api_key[0])
                answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
                answer = st.radio(question, answer_options,index=None)
                choices3=answer
                #list.append(f'question3:{question},answer3:{choices3}')
                if choices3:
                    #time.sleep(10)
                    question=get_question_topic(interests,api_key[1])
                    answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
                    answer = st.radio(question, answer_options,index=None)
                    choices4=answer
                    #list.append(f'question4:{question},answer4:{choices4}')
                    if choices4:
                        #time.sleep(10)
                        question=get_question_topic(interests,api_key[2])
                        answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
                        answer = st.radio(question, answer_options,index=None)
                        choices5=answer
                        #list.append(f'question5:{question},answer5:{choices5}')
                        if choices5:
                            #time.sleep(10)
                            question=get_question_topic(interests,api_key[0])
                            answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
                            answer = st.radio(question, answer_options,index=None)
                            choices6=answer
                            #list.append(f'question6:{question},answer6:{choices6}')
                            if choices6:
                                #time.sleep(10)
                                question=get_question_topic(interests,api_key[1])
                                answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
                                answer = st.radio(question, answer_options,index=None)
                                choices7=answer
                                #list.append(f'question7:{question},answer7:{choices7}')
                                if choices7:
                                        #time.sleep(10)
                                        question=get_question_topic(interests,api_key[2])
                                        answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested"]
                                        answer = st.radio(question, answer_options,index=None)
                                        choices8=answer
                                        #list.append(f'question8:{question},answer8:{choices8}')
                                        #get_final_output(list)
                                        if choices8:
                                            str1=""
                                            for i in list:
                                                str+=i
                                            messages = [{"role": "system", "content": "I'm a course suggester."}]
                                            message = ('Select the most suitable course from colleges which are available in india based on the above questions with a paragrah suggesting why')
                                            if message:
                                                messages.append({"role": "user", "content": message})
                                                chat = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1)
                                                reply = chat.choices[0].message.content
                                                st.success(reply)
    
                                            


#print(list)
#print(get_final_output(list))                                
                



