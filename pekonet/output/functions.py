from pekonet.evaluation import get_micro_macro_prf


def empty_output_function(*args, **kwargs):
    return ''


def aa_output_function(*args, **kwargs):
    data = kwargs['data']

    results = {}
    results['article'] = get_micro_macro_prf(
        data=data['article'])
    results['accusation'] = get_micro_macro_prf(
        data=data['accusation'])

    return results