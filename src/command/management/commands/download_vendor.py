# the name of the file will be used for the command e.g. py manage.py download_vendor
from django.core.management.base import BaseCommand
from django.conf import settings
import helpers

# getting the vendors file location from django settings
STATICFILES_VENDORS = getattr(settings, 'STATICFILES_VENDORS')

# a dictionary with the links of the vendor files; the .map file is required for serving static files on whitenoise 
VENDOR_FILES = {
    'flowbite.min.js': "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
    'flowbite.min.js.map': "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js.map",
    'flowbite.min.css': "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css"
}

# this custom command uses the download function inside helpers.
class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Downloading the flowbite vendor files')
        completed_urls = []

        for name, url in VENDOR_FILES.items():
            download_path = STATICFILES_VENDORS / name
            download_result = helpers.download_flowbite_files(url, download_path)
            if download_result:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f'failed to download {url}'))

        # checking if all the vendor files were downloaded
        if set(completed_urls) == set(VENDOR_FILES.values()):
            self.stdout.write(self.style.SUCCESS('Successfully downloded all vendor files'))
        else:
            self.stdout.write(self.style.WARNING('Some files could not be downloaded'))
