from PIL import Image
import pillow_heif
from os import listdir
from os.path import join, splitext

# https://stackoverflow.com/questions/65045644/heic-to-jpeg-conversion-with-metadata

# def convert(input_path, output_path):
#     # Open the file
#     heif_file = pyheif.read(file_path_heic)

#     # Creation of image 
#     image = Image.frombytes(
#         heif_file.mode,
#         heif_file.size,
#         heif_file.data,
#         "raw",
#         heif_file.mode,
#         heif_file.stride,
#     )
#     # Retrive the metadata
#     for metadata in heif_file.metadata or []:
#         if metadata['type'] == 'Exif':
#             exif_dict = piexif.load(metadata['data'])

#     # PIL rotates the image according to exif info, so it's necessary to remove the orientation tag otherwise the image will be rotated again (1° time from PIL, 2° from viewer).
#     exif_dict['0th'][274] = 0
#     exif_bytes = piexif.dump(exif_dict)
#     image.save(file_path_jpeg, "JPEG", exif=exif_bytes)

path = r"C:\Users\jack\Desktop\heic"
output_folder = r"C:\Users\jack\Desktop\jpg"
pillow_heif.register_heif_opener()
for filename in listdir(path):
    full_path = join(path, filename)
    print(full_path)
    pre, ext = splitext(filename)
    full_output_path = join(output_folder, pre +".JPG")
    
    heif_file = pillow_heif.read_heif(full_path)
   
    #create the new image
    image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw",
    heif_file.mode,
    heif_file.stride,
    )

    # print(heif_file.info.keys())
    dictionary=heif_file.info
    exif_dict=dictionary['exif']
    # debug 
    # print(exif_dict)
    
    image.save(full_output_path, "JPEG", exif=exif_dict)

    # img = Image.open(full_path)
    # img.save(full_output_path)

    print(full_output_path)
    # break
