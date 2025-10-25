from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, SlugField, TextField, DecimalField, DateTimeField, URLField, PositiveIntegerField


class Course(Model):
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='courses')
    title = CharField(max_length=255)
    slug = SlugField(unique=True)
    description = TextField()
    price = DecimalField(max_digits=8, decimal_places=2)
    instructor = ForeignKey('apps.User', on_delete=CASCADE, related_name='courses')
    image = ImageField(upload_to='courses/')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(Model):
    course = ForeignKey('apps.Course', on_delete=CASCADE, related_name='lessons')
    title = CharField(max_length=255)
    video_url = URLField(blank=True, null=True)
    content = TextField(blank=True, null=True)
    order = PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.course.title} - {self.title}"
