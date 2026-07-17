from whitenoise.storage import CompressedManifestStaticFilesStorage

class CustomWhiteNoiseStorage(CompressedManifestStaticFilesStorage):
    def __init__(self, *args, **kwargs):
        # We pop manifest_strict if it exists, to avoid TypeError in FileSystemStorage
        kwargs.pop('manifest_strict', None)
        super().__init__(*args, **kwargs)
        # Forcefully bypass MissingFileError
        self.manifest_strict = False
