from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticSotrage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    file_overwrite = True


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    file_overwrite = False

