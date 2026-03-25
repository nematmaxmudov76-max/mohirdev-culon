We are implementing an LMS platform in Django REST Framework with @docs/mohir_dev.drawio.html schema. The flow should be in the following order:

Setup the environment
Implement models based on schema (but not makemigrations && migrate yet)
Implement Custom User Model (I'll do myself, showing 3 approaches)
Implement admin configs with proper list, edit, etc. views
Implement Authentication (Basic (custom), Session (buit-in), JWT(rest_framework_simplejwt))
and i use postgresql database don't use sqlite3