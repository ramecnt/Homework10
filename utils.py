import json

def get_all():
    with open("candidates.json ", "r", encoding = 'utf-8') as file:
        return json.load(file)

def get_by_pk(pk):
    file = get_all()
    for i in file:
        if i['pk'] == pk:
            return i

def get_by_skill(skill_name):
    result = []
    file = get_all()
    for i in file:
        if skill_name in i['skills'].lower().split(', '):
            result.append(i)
    return result

def format_candidates(candidates):
    result = '<pre>'
    for candidate in candidates:
        result += f'{candidate["name"]}\n' \
                  f'{candidate["position"]}\n' \
                  f'{candidate["skills"]}\n' \
                  f'<pre>'
    return result
