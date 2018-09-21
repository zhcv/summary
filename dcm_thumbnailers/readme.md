using your sudo rights, create a file nii.thumbnailer in /usr/share/thumbnailers/ with the following text;
script: https://github.com/kevin-keraudren/ubuntu-medical-imagingts 


[Thumbnailer Entry]
TryExec=/home/zhang/.local/ubuntu-medical-imaging/scripts/nii_thumbnailer.py
Exec=/home/zhang/.local/ubuntu-medical-imaging/scripts/nii_thumbnailer.py %s %i %o
MimeType=image/nii;image/gznii;application/dicom;
