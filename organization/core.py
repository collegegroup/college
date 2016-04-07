__author__ = "ravi"


def handle_uploaded_file(file_obj, image_name):
    try:
        destination = open(image_name, 'wb+')
        for chunk in file_obj.chunks():
            destination.write(chunk)
        destination.close()
    except:
        raise