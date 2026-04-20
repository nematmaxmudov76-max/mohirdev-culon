from modeltranslation.translator import TranslationOptions, register

from apps.courses.models import Category, Course, Lesson, Module, Tag

@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ["name"]

@register(Tag)
class TagTranslation(TranslationOptions):
    fields = ["name"]

@register(Course)
class CourseTranslation(TranslationOptions):
    fields = ["name"]
    
@register(Module)
class ModuleTranslation(TranslationOptions):
    fields = ["name"]

@register(Lesson)
class LessonTranslation(TranslationOptions):
    fields = ["name"]
