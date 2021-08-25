def valid_email(email):
    """
    Check is email correct
    :param email:
    :return:
    """
    import re
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def log(file_name, text):
    """
    Write log to file
    :param file_name:
    :param text:
    :return:
    """
    with open(file_name, 'a') as f_obj:
        f_obj.write(text)


