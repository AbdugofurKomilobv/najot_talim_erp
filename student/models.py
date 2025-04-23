from django.db import models

from user_auth.models import Student,GroupStudent,BaseModel

class StudentListModel(BaseModel):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)
    arribal_time = models.DateTimeField(null=True,blank=True)
    izox = models.CharField(max_length=150, blank=True,null=True)


    class Meta:
        unique_together = ('student', 'group', 'date')
        


    
    def __str__(self):
        return f"{self.student.user.full_name} - {self.date} - {'Bor' if self.is_present else 'Yo‘q'}"
