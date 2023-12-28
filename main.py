import streamlit as st
import openai 
import time

openai.api_key = 

def wait(interests,choice,i):
        time.sleep(5)
        if choice:
            question = get_question_topic(interests,choice,i)
            i=i+1
        else:
            wait(interests,choice,i)    
        return question
    

def questions(interest,choice,i):
    while True:
        
                    
        if i == 1:
            messages = [{"role": "system", "content": "you're a course suggestor"}]
            message = (f'generate a question in simple terms to predict the course suitable for the user, which will have options as "Not Interested", "Slightly Interested", "Moderately Interested", "Very Interested" and this question should be designed in a way to get the interest of the user and should be related to {interest}, do not give the options in output')
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                chat =openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1)
                reply = chat.choices[0].message.content
                
               
                
                     
                     
                
                return reply
      
def main():
    st.title("Course Seeker")

    st.write("What are your interests? Select options related to your interest.")

    # Interests related to technology
    global interests
    
    interests = st.multiselect("Select your interests", ["Developer","Business","Finance and accounting","Technology","Office productivity","Personal development","Designing","Marketing","Lifestyle","Photography and video","Health and fitness","Music","Teaching and academics","Humanity","Creativity Art"])



        # Ask 10 questions related to technology
    st.write("\nAnswer the following questions:")
    
    i=1
    global l
    l=[]
    while i<6:
        time.sleep(18)
        if i==1:
            choice="garbage_value"
            question = questions(interests,choice,i) 
            i=i+1
        else:
            question=wait(interests,choice,i)      
        answer_options = ["Not Interested", "Slightly Interested", "Moderately Interested", "Highly Interested"]
        answer = st.radio(question,answer_options,index=None,key = "<uniquevalueofsomesort>")
        choice=answer
        l=answer
        
        st.write("\nEnter submit after answering atleast 5 questions ")
        if st.button("submit"):
            st.write("\nBased on your answers, we can recommend you the desired course:")
            messages = [{"role": "system", "content": "you're a course suggestor"}]
            message = (f'the answer to the previous question is {l}, now according to the above answers, what would be the suitable course to pursue?')
            if message:
                    messages.append({"role": "user", "content": message})
                    chat = openai.chat.completions.create(
                          model="gpt-3.5-turbo", messages=messages
                    )
                    reply = chat.choices[0].message.content
                    st.write(reply)
                    break
             

    # Recommend a course based on answers
    
                

    # You can customize the recommendation logic based on the user's answers.
    #recommended_course = "Advanced Technology Course"
    #st.success(recommended_course)


main()
