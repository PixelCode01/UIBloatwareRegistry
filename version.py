__version__ = "1.4.0"
__author__ = "PixelCode01"
__description__ = "Android Bloatware Remover - Remove unwanted pre-installed apps"
__url__ = "https://github.com/PixelCode01/UIBloatwareRegistry"

def get_version():
    return __version__

def get_version_info():
    return {
        "version": __version__,
        "author": __author__,
        "description": __description__,
        "url": __url__
    }