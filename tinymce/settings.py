import os
import warnings
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.functional import lazy
from tinymce.utils import baseurl

OLD_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', False)
if OLD_CONFIG:
    warnings.warn("TINYMCE_DEFAULT_CONFIG is deprecated, check docs for instructions.", DeprecationWarning)
DEFAULT_CONFIG = OLD_CONFIG or {'theme': "modern", 'relative_urls': False}

if getattr(settings, 'TINYMCE_JS_URL', False):
    raise RuntimeError("TINYMCE_JS_URL is not supported anymore, check docs for instructions.")

# added laziness to support django.contrib.staticfiles.storage.ManifestStaticFilesStorage
# and other storages that needs post-processing
staticfiles_storage_url_lazy = lazy(staticfiles_storage.url, str)
JS_URL = staticfiles_storage_url_lazy('tinymce/tinymce.min.js')
JS_ROOT = staticfiles_storage_url_lazy('tinymce')
JS_BASE_URL = lazy(baseurl, str)(JS_URL)

if getattr(settings, 'TINYMCE_SPELLCHECKER', False):
    raise NotImplementedError("TINYMCE_SPELLCHECKER is not implemented yet.")
USE_SPELLCHECKER = False

if getattr(settings, 'TINYMCE_COMPRESSOR', False):
    raise NotImplementedError("TINYMCE_COMPRESSOR is not implemented yet.")
USE_COMPRESSOR = False

if getattr(settings, 'TINYMCE_FILEBROWSER', False):
    raise RuntimeError("TINYMCE_FILEBROWSER is not supported anymore, check docs for instructions.")
USE_FILEBROWSER = False
