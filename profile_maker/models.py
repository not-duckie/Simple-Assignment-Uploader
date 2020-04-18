from django.db import models


class User_Profile(models.Model):
    
    Name = models.CharField(max_length=200)
    RollNo = models.IntegerField(default = None)
    Email = models.EmailField(default = None)
    Subject = models.CharField(max_length=100,null=True,default=None)
    Time_of_Submission = models.TimeField(auto_now=True)
    Assignment = models.FileField()
    

    def __str__(self):
        return self.Name