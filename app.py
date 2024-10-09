from tkinter import *
from mydb import database
from tkinter import messagebox
from mynlp import code_nlp

class NLPApp :
    def __init__(self):
        

        #create db object

        self.dbo=database()
        self.nlpo=code_nlp()
        #load login page
        self.root=Tk()   # Creating object
        self.root.title("NLP App")  # Giving Title
        self.root.iconbitmap('resources/favicon.ico')  # Adding Icon
        self.root.geometry('350x600') # Changing the size of window
        self.root.configure(bg='#dfe3e3')  # Background color
        self.login_gui()  # Calling login page


        self.root.mainloop()  # Needed to hold the window else it will diappear

    def login_gui (self):
        self.clear()
        heading=Label(self.root,text='NLP App',bg='#dfe3e3',fg='black') #heading of page
        heading.pack(pady=(30,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading.configure(font=('verdana',24,'bold')) #changing font of heading
        label1=Label(self.root,text='Enter your Email') #adding level 
        label1.pack(pady=(5,5))

        self.email_input=Entry(self.root,width=30) #box to take user email
        self.email_input.pack(pady=(5,5),ipady=4)

        #same steps to take user password

        label2=Label(self.root,text='Enter your Password') #adding level 
        label2.pack(pady=(5,5))

        self.password_input=Entry(self.root,width=30,show="*") #box to take user email
        self.password_input.pack(pady=(5,5),ipady=4)
        
        #login Button
        ''' command option is used to tell which function to call if button is clicked'''
        login_btn=Button(self.root,text='Login',width=20,height=1,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        #adding text if not registered
        label3=Label(self.root,text="Not a Member?")
        label3.pack(pady=(5,5))

        #adding Button to redirect to registration page

        redirect_btn=Button(self.root,text='Register here',command=self.register_gui)
        redirect_btn.pack(pady=(5,5))

    def register_gui(self):
        ''' this function is to create registeration page'''
        #clear the existing gui
        self.clear()
        heading=Label(self.root,text='NLP App',bg='#dfe3e3',fg='black') #heading of page
        heading.pack(pady=(30,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading.configure(font=('verdana',24,'bold')) #changing font of heading
        label0=Label(self.root,text='Enter your Name') #adding level 
        label0.pack(pady=(5,5))
        self.name_input=Entry(self.root,width=30) #box to take user email
        self.name_input.pack(pady=(5,5),ipady=4)

        label1=Label(self.root,text='Enter your email') #adding level 
        label1.pack(pady=(5,5))

        self.email_input=Entry(self.root,width=30) #box to take user email
        self.email_input.pack(pady=(5,5),ipady=4)

        #same steps to take user password

        label2=Label(self.root,text='Enter your Password') #adding level 
        label2.pack(pady=(5,5))

        self.password_input=Entry(self.root,width=30,show="*") #box to take user email
        self.password_input.pack(pady=(5,5),ipady=4)
        
        #register Button
        register_btn=Button(self.root,text='Register',width=20,height=1,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        #adding text if not registered
        label3=Label(self.root,text="Already a Member?")
        label3.pack(pady=(5,5))

        #adding Button to redirect to registration page

        redirect_btn=Button(self.root,text='Login Now',command=self.login_gui)
        redirect_btn.pack(pady=(5,5))


    def clear(self):
        ''' this function is responssible to clear the existing options available on GUI. Using it at every function.'''    
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        ''' this function is to perform registration. Capturing the data provided by user and sending the same inputs 
        to function add_data which is defined in mydb.py'''
        #fetch data from GUI
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        response=self.dbo.add_data(name,email,password)

        if response :
            messagebox.showinfo('Success','Registration Sucessful, you can Login Now')
        else:
            messagebox.showerror('Error','Email Already Exists')

    def perform_login(self):
        ''' this function is to perform login. Capturing the data provided by user and sending the same inputs 
        to function search which is defined in mydb.py'''
        email=self.email_input.get()
        password = self.password_input.get()

        response= self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','Login Successful')
            self.home_gui()
        else :
            messagebox.showerror('Error', 'Email/Passowrd Incorrect')
    

    def home_gui(self):
        ''' this function is to create profile page'''
        self.clear()

        heading=Label(self.root,text='NLP App',bg='#dfe3e3',fg='black') #heading of page
        heading.pack(pady=(30,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading.configure(font=('verdana',24,'bold')) #changing font of heading 

        langdet_btn=Button(self.root,text='Language Detection',width=20,height=2,command=self.langdet_gui)
        langdet_btn.pack(pady=(20,20))
        translation_btn=Button(self.root,text='Language Translation',width=20,height=2,command=self.translation_gui)
        translation_btn.pack(pady=(20,20))
        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=20,height=2,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20,20))

        logout_btn=Button(self.root,text='Logout',width=10,height=1,command=self.login_gui)
        logout_btn.pack(pady=(20,20))

    def langdet_gui(self):
        ''' This function is creating a GUI page for Language detection'''
        self.clear()
        heading=Label(self.root,text='NLP App',bg='#dfe3e3',fg='black') #heading of page
        heading.pack(pady=(30,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading.configure(font=('verdana',24,'bold')) #changing font of heading 

        heading2=Label(self.root,text='Language Detection',bg='#dfe3e3',fg='black') #heading of page
        heading2.pack(pady=(10,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading2.configure(font=('verdana',15)) #changing font of heading 

        label1=Label(self.root,text="Enter your Text")
        label1.pack(pady=(5,5))
        self.langdet_input=Entry(self.root,width=50)
        self.langdet_input.pack(pady=(5,5),ipady=4)


        langdet_btn=Button(self.root,text='Detect Language',width=15,height=1,command=self.do_lang_detection)
        langdet_btn.pack(pady=(10,10))

        self.langdet_result=Label(self.root,text="",bg='#dfe3e3',fg='black')
        self.langdet_result.pack(pady=(5,5))
        self.langdet_result.configure(font=('verdana',16))

        goback_btn=Button(self.root,text='Back to Home',width=15,height=1,command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_lang_detection(self):
        ''' This function is performing language detection task. capturing the text provide by user and sending the same to mynlp.py'''
        text=self.langdet_input.get()
        result=self.nlpo.lang_detect(text)
        self.langdet_result['text']=result
    
    def translation_gui(self):
        '''this function is creating a GUI for translation task'''
        self.clear()
        heading=Label(self.root,text='NLP App',bg='#dfe3e3',fg='black') #heading of page
        heading.pack(pady=(30,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading.configure(font=('verdana',24,'bold')) #changing font of heading 

        heading2=Label(self.root,text='Language Translation',bg='#dfe3e3',fg='black') #heading of page
        heading2.pack(pady=(10,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading2.configure(font=('verdana',15)) #changing font of heading 

        label1=Label(self.root,text="Enter your Text")
        label1.pack(pady=(5,5))
        self.translation_input=Entry(self.root,width=50)
        self.translation_input.pack(pady=(5,5),ipady=4)

        label2=Label(self.root,text="Language to Translate?")
        label2.pack(pady=(5,5))
        self.translation_language_input=Entry(self.root,width=10)
        self.translation_language_input.pack(pady=(5,5),ipady=1)


        translation_btn=Button(self.root,text='Translate',width=15,height=1,command=self.do_translation)
        translation_btn.pack(pady=(10,10))

        self.translation_result=Label(self.root,text="",bg='#dfe3e3',fg='black')
        self.translation_result.pack(pady=(5,5))
        self.translation_result.configure(font=('verdana',16))

        goback_btn=Button(self.root,text='Back to Home',width=15,height=1,command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_translation(self):
        ''' This function is taking input and doing translation using function in mynlp.py'''
        text=self.translation_input.get()
        dest=self.translation_language_input.get()
        result=self.nlpo.translation(text,dest)
        self.translation_result['text']=result

    def sentiment_gui(self):
        ''' This function is creating a page for sentiment analysis'''
        self.clear()
        heading=Label(self.root,text='NLP App',bg='#dfe3e3',fg='black') #heading of page
        heading.pack(pady=(30,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading.configure(font=('verdana',24,'bold')) #changing font of heading 

        heading2=Label(self.root,text='Sentiment Analysis',bg='#dfe3e3',fg='black') #heading of page
        heading2.pack(pady=(10,30)) # to show on HTML we must pack, pady to give space from up and bottom
        heading2.configure(font=('verdana',15)) #changing font of heading 

        label1=Label(self.root,text="Enter your Text")
        label1.pack(pady=(5,5))
        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,5),ipady=4)

        

        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=15,height=1,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result=Label(self.root,text="",bg='#dfe3e3',fg='black')
        self.sentiment_result.pack(pady=(5,5))
        self.sentiment_result.configure(font=('verdana',16))

        goback_btn=Button(self.root,text='Back to Home',width=15,height=1,command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_sentiment_analysis(self):
        ''' This function is doing sentiment analysis'''
        text=self.sentiment_input.get()
        
        result=self.nlpo.sentiment(text)
        self.sentiment_result['text']=result
   

nlp=NLPApp()
