from tkinter import *
from mydb import Database
from myapi import API
from tkinter import messagebox

class NLPApp:

    def __init__(self):
        # creating database object
        self.db=Database()
        self.api=API()

        # load the gui login page
        self.root = Tk()
        self.root.title('NLP App')
        self.root.iconbitmap('resources/nlpapp_logo.ico')
        self.root.geometry('400x600')
        self.root.configure(bg='#2E4053')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP APP', bg='#2E4053', fg='#F4D03F')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana', 24, 'bold'))

        # Email
        label1=Label(self.root, text='Enter Email', bg='#2E4053', fg='#F4D03F')
        label1.pack(pady=(10,10))
        label1.configure(font=('Comic Sans MS',14))

        self.email_input=Entry(self.root,width=40)
        self.email_input.pack(pady=(10,10),ipady=4)

        # Password
        label2=Label(self.root, text='Enter Password', bg='#2E4053', fg='#F4D03F')
        label2.pack(pady=(10,10))
        label2.configure(font=('Comic Sans MS',14))

        self.password_input=Entry(self.root,width=40,show='*')
        self.password_input.pack(pady=(10,10),ipady=4)

        #Login Button
        login_btn=Button(self.root,text='Login',width=20,height=2,bg='#F4D03F',borderwidth=0,command=self.perform_login)
        login_btn.pack(pady=(20,20))

        # Register option
        label3 = Label(self.root, text='Not a member? Register', bg='#2E4053', fg='#F4D03F')
        label3.pack(pady=(10,10))
        label3.configure(font=('Comic Sans MS',10))

        redirect_btn = Button(self.root, text='Register Now', width=20, height=2, bg='#F4D03F', borderwidth=0,command=self.register_gui)
        redirect_btn.pack(pady=(20,20))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP APP', bg='#2E4053', fg='#F4D03F')
        heading.pack(pady=(20, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        # Name
        label0 = Label(self.root, text='Enter your Name', bg='#2E4053', fg='#2ECC71')
        label0.pack(pady=(10, 10))
        label0.configure(font=('Comic Sans MS', 14))

        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(10, 10), ipady=4)

        # Email
        label1 = Label(self.root, text='Enter your Email', bg='#2E4053', fg='#2ECC71')
        label1.pack(pady=(10, 10))
        label1.configure(font=('Comic Sans MS', 14))

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(10, 10), ipady=4)

        # Password
        label2 = Label(self.root, text='Enter your Password', bg='#2E4053', fg='#2ECC71')
        label2.pack(pady=(10, 10))
        label2.configure(font=('Comic Sans MS', 14))

        self.password_input = Entry(self.root, width=40)
        self.password_input.pack(pady=(10, 10), ipady=4)

        # Register Button
        register_btn = Button(self.root, text='Register', width=20, height=2, bg='#2ECC71', borderwidth=0,command=self.perform_registration)
        register_btn.pack(pady=(20, 20))

        # Register option
        label3 = Label(self.root, text='Already a member?', bg='#2E4053', fg='#2ECC71')
        label3.pack(pady=(10, 10))
        label3.configure(font=('Comic Sans MS', 10))

        redirect_btn = Button(self.root, text='Login Now', width=20, height=2, bg='#2ECC71', borderwidth=0,
                              command=self.login_gui)
        redirect_btn.pack(pady=(20, 20))

    def clear(self):
        # clear the existing gui
        for widget in self.root.pack_slaves():
            widget.destroy()

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        response=self.db.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration Successful')
        else:
            messagebox.showinfo('Error','Email Already Registered')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.db.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showinfo('Error', 'Incorrect Email/Password')


    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP APP', bg='#2E4053', fg='#F4D03F')
        heading.pack(pady=(20, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        # Sentiment Analysis
        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=3, bg='#F4D03F', borderwidth=0,
                              command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20, 20))

        # Named Entity Recognition
        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=3, bg='#F4D03F', borderwidth=0,
                               command=self.ner_gui)
        ner_btn.pack(pady=(20, 20))

        # Emotion Detection
        emotion_btn = Button(self.root, text='Emotion Detection', width=30, height=3, bg='#F4D03F', borderwidth=0,
                               command=self.emotion_gui)
        emotion_btn.pack(pady=(20, 20))

        # Logout
        logout_btn = Button(self.root, text='Logout', width=16, height=2, bg='#2ECC71', borderwidth=0,
                              command=self.login_gui)
        logout_btn.pack(pady=(50, 20))

    # Sentiment Analysis GUI
    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP APP', bg='#2E4053', fg='#F4D03F')
        heading.pack(pady=(20, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#2E4053', fg='#2ECC71')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 16))

        label1 = Label(self.root, text='Enter the Text', bg='#2E4053', fg='#2ECC71')
        label1.pack(pady=(10, 10))
        label1.configure(font=('Comic Sans MS', 12))

        self.sentiment_input = Entry(self.root, width=60)
        self.sentiment_input.pack(pady=(5, 10), ipady=6)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', width=20, height=2, bg='#F4D03F', borderwidth=0,
                               command=self.perform_sentiment_analysis)
        sentiment_btn.pack(pady=(20, 20))

        self.sentiment_result = Label(self.root, text='', bg='#2E4053', fg='#2ECC71')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('Comic Sans MS', 14))

        goback_btn = Button(self.root, text='Go Back', width=20, height=2, bg='#F4D03F', borderwidth=0,
                               command=self.home_gui)
        goback_btn.pack(pady=(50, 20))


    def perform_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.api.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt += i+' -> '+str(result['sentiment'][i])+'\n'

        self.sentiment_result['text'] = txt

    # Named Entity Recognition GUI
    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP APP', bg='#2E4053', fg='#F4D03F')
        heading.pack(pady=(20, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#2E4053', fg='#2ECC71')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 16))

        label1 = Label(self.root, text='Enter the Text', bg='#2E4053', fg='#2ECC71')
        label1.pack(pady=(10, 10))
        label1.configure(font=('Comic Sans MS', 12))

        self.ner_input = Entry(self.root, width=60)
        self.ner_input.pack(pady=(5, 10), ipady=6)

        ner_btn = Button(self.root, text='Perform NER', width=20, height=2, bg='#F4D03F', borderwidth=0,
                               command=self.perform_ner)
        ner_btn.pack(pady=(20, 20))

        self.ner_result = Label(self.root, text='', bg='#2E4053', fg='#2ECC71')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('Comic Sans MS', 14))

        goback_btn = Button(self.root, text='Go Back', width=20, height=2, bg='#F4D03F', borderwidth=0,
                            command=self.home_gui)
        goback_btn.pack(pady=(20, 20))


    def perform_ner(self):
        text = self.ner_input.get()
        result = self.api.ner(text)

        txt = ''
        for i in result['entities']:
            for j in i:
                if j == 'confidence_score':
                    continue
                txt += j + ' -> ' + str(i[j]) + '\n'
            txt += '\n'

        self.ner_result['text'] = txt

    # Emotion Detection GUI
    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP APP', bg='#2E4053', fg='#F4D03F')
        heading.pack(pady=(20, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Detection', bg='#2E4053', fg='#2ECC71')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 16))

        label1 = Label(self.root, text='Enter the Text', bg='#2E4053', fg='#2ECC71')
        label1.pack(pady=(10, 10))
        label1.configure(font=('Comic Sans MS', 12))

        self.emotion_input = Entry(self.root, width=60)
        self.emotion_input.pack(pady=(5, 10), ipady=6)

        ner_btn = Button(self.root, text='Detect Emotion', width=20, height=2, bg='#F4D03F', borderwidth=0,
                               command=self.perform_emotion_detection)
        ner_btn.pack(pady=(20, 20))

        self.emotion_result = Label(self.root, text='', bg='#2E4053', fg='#2ECC71')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('Comic Sans MS', 14))

        goback_btn = Button(self.root, text='Go Back', width=20, height=2, bg='#F4D03F', borderwidth=0,
                            command=self.home_gui)
        goback_btn.pack(pady=(20, 20))


    def perform_emotion_detection(self):
        text = self.emotion_input.get()
        result = self.api.emotion_detection(text)

        txt = ''
        for i in result['emotion']:
            txt += i + ' -> ' + str(result['emotion'][i]) + '\n'

        self.emotion_result['text'] = txt

# NLP Object
nlp = NLPApp()
