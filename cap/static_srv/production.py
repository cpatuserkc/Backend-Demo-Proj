import os

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


LINODE_BUCKET = 'simpledemos-app'
LINODE_BUCKET_REGION = 'us-east-1'
LINODE_BUCKET_ACCESS_KEY = '4S5H31GZ6580JEV0VUBX'
LINODE_BUCKET_SECRET_KEY = 'ACgPAjuCK7yz9Pc7x0MbovXMhbsTts6LQPfOEPaF'



AWS_S3_ENDPOINT_URL = f'https://{LINODE_BUCKET_REGION }.linodeobjects.com'
AWS_ACCESS_KEY_ID = LINODE_BUCKET_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = LINODE_BUCKET_SECRET_KEY
AWS_S3_REGION_NAME = LINODE_BUCKET_REGION
AWS_S3_USE_SSL = True
AWS_STORAGE_BUCKET_NAME = LINODE_BUCKET

print(f"from cpat setup folder {LINODE_BUCKET}")