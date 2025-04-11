def allowed_file(filename, allowed_extensions):
    """
    Check if the uploaded file is an allowed image type.
    
    Args:
        filename (str): Name of the uploaded file.
        allowed_extensions (set): Allowed file extensions.
    
    Returns:
        bool: True if allowed, else False.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
