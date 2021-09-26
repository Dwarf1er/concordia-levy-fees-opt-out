from datetime import datetime

def get_current_semeseter_url() -> str:
    '''Utility method to construct the URL for the levy fee opt-out form that is available every semester, the URL is constructed according to the on-going semester
    - January to April ==> winter
    - May to August ==> summer
    - September to December ==> fall
    '''
    month = datetime.now().month
    year = datetime.now().year
    semester = ""

    if (month >= 1 and month <= 4):
        semester = "winter"
    elif (month >= 5 and month <= 8):
        semester = "summer"
    else:
        semester = "fall"

    return "https://" + semester + str(year) + "optout.paperform.co"