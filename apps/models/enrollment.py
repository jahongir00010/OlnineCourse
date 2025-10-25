from django.db.models import Model, ForeignKey, DateTimeField, CASCADE


class Enrollment(Model):
    user = ForeignKey("apps.User", on_delete=CASCADE, related_name="enrollments")
    course = ForeignKey("apps.Course", on_delete=CASCADE, related_name="enrollments")
    enrolled_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} -> {self.course.title}"
