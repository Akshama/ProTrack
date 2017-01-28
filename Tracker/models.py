from django.db import models

#Groups
class group(models.Model):
    gname = models.CharField(max_length=100)

    def __str__(self):
        return self.gname

#Registration and Login
class member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username


#Members associated with a Group
class group_member(models.Model):                                                           
     group = models.ForeignKey(group, on_delete=models.CASCADE)
     members = models.CharField(max_length=100)   #Members to be mapped here from member model

#Projects associated with a Group
class project(models.Model):                                                                 
    pgroup = models.ForeignKey(group, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    pdesc = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.pname
#........................................
Status_Choices = (
    ('red','Red'),('yellow','Yellow'),('green','Green'),
)
Priority_Choices = (
    ('high','High'),('medium','Medium'),('low','Low'),
)

#Tasks associated with a Project
class task(models.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    tname = models.CharField(max_length=100)
    desc = models.CharField(max_length=200,blank=True)
    due_date = models.DateField('due date')
    risk = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=50,default='Yellow',choices=Status_Choices)
    priority = models.CharField(max_length=50,choices=Priority_Choices)
    state = models.CharField(max_length=50)
    assign = models.CharField(max_length=100)
    remainder = models.CharField(max_length=200,blank=True)
    heading = models.CharField(max_length=200,blank=True)
    dep_task = models.CharField(max_length=100,blank=True)
    cur_sprint = models.CharField(max_length=100,blank=True,null=True)
    tp = models.IntegerField(default=1)

    def __str__(self):
        return self.tname

# Task's associated tags
class tag(models.Model):
     task = models.ForeignKey(task, on_delete=models.CASCADE)
     tag = models.CharField(max_length=100)

# Task's associated comments
class comment(models.Model):
     task = models.ForeignKey(task, on_delete=models.CASCADE)
     comment = models.CharField(max_length=500)

# Task's associated subtasks
class subtask(models.Model):
     task = models.ForeignKey(task, on_delete=models.CASCADE)
     subtask = models.CharField(max_length=100)  # Add attributes required for subtask

     def __str__(self):
        return self.subtask

# Sprints for a Project
class sprint(models.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    sname = models.CharField(max_length=100,verbose_name='Sprint Name')
    start_date =models.DateField('start date')
    end_date =models.DateField('end date')
    def __str__(self):
        return self.sname
