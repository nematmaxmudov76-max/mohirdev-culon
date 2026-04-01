from .auth import (
    UserProfileAPIView,
    UserRegisterAPIView,
    UserRegisterConfirmAPIView,
)
from .author_crud import (
    AuthorListAPIView,
    AuthorDetailAPIView,
    AuthorCreateAPIView,
    AuthorUpdateAPIView,
    AuthorDeleteAPIView,
)

from .education_crud import (
    EducationListAPIView,
    EducationDetailAPIView,
    EducationCreateAPIView,
    EducationUpdateAPIView,
    EducationDeleteAPIView,
)




__all__ = [
    "UserProfileAPIView",
    "UserRegisterAPIView",
    "UserRegisterConfirmAPIView",
    "AuthorListAPIView",
    "AuthorDetailAPIView",
    "AuthorCreateAPIView",
    "AuthorUpdateAPIView",
    "AuthorDeleteAPIView",
    "EducationListAPIView",
    "EducationDetailAPIView",
    "EducationCreateAPIView",
    "EducationUpdateAPIView",
    "EducationDeleteAPIView",
]