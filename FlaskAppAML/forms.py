from wtforms import Form, StringField, TextAreaField, validators, SelectField

option1=[(0,"0"),(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6")]
option2=[("Lyft","Lyft"), ("Uber","Uber")]
option3=[("Lux","Lux"),("Lux Black","Lux Black"),("Lux Black XL","Lux Black XL"),("Lyft","Lyft"),("Lyft XL","Lyft XL"),("Shared","Shared")]
option4=[("Black","Black"),("Black SUV","Black SUV"),("Taxi","Taxi"),("UberPool","UberPool"),("UberX","UberX"),("UberXL","UberXL"),("WAV","WAV")]
option5=[(0,"0"),(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8"),(9,"9"),(10,"10"),(11,"11"),(12,"12"),(13,"13"),(14,"14"),(15,"15"),(16,"16"),(17,"17"),(18,"18"),(19,"19"),(20,"20"),(21,"21"),(22,"22"),(23,"23"),(24,"24")]
class SubmissionForm(Form):
    #title = StringField('Title', [validators.Length(min=2, max=30)])
    #category = StringField('Category', [validators.Length(min=0, max=30)])
    #text = TextAreaField('Text', [validators.Length(min=1, max=500)])
    dayWeek=SelectField('dayWeek', choices=option1)
    cabName=SelectField('cabName', choices=option2)
    cabType=SelectField('cabType')
    
    hourDay=SelectField('hourDay', choices=option5)
    distance=StringField('distance',[validators.Length(min=2, max=30)])
    rain=StringField('rain',[validators.Length(min=2, max=30)])
    temperature=StringField('temperature',[validators.Length(min=2, max=30)])
