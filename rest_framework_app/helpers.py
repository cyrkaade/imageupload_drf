

# Helpers functions

def modify_input_for_multiple_files(pk, original, small, medium):
    dict = {}
    dict['pk'] = pk
    dict['original'] = original
    dict['small'] = small
    dict['medium'] = medium
    return dict

def delete_exp(url):
    url.delete(save=True)


