from django.contrib import admin

from .models import Student, Attendance, JWTPayloadTrack


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'std_name', 'std_roll', 'std_class']
    list_display_links = ['std_name']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'date', 'status']
    list_editable = ['status']
    list_display_links = ['student']\


@admin.register(JWTPayloadTrack)
class JWTPayloadTrackAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'iat']
    list_display_links = ['username']




