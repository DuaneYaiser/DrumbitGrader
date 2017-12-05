import os, json

drumbit_dict = {}

os.chdir('drumbits/')
drumbit_files = os.listdir('.')

score = 0
hihathits = 0

four_floor_flag = False
backbeat_flag = False
hihat_flag = False
tempo_flag = False
other_tracks_flag = False
vol_pan_flag = False


''' Check for 'Four on the Floor' pattern in bass drum (track8) and backbeats in snare (track7). Add Two Points to score for each if correct '''
def fouronfloor_check(drumbeat):
    global score,four_floor_flag
    bassdrum = drumbeat['pattern1']['track8']['steps']
    fouronthefloor = [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
    if bassdrum == fouronthefloor:
        score += 2
        four_floor_flag = True
        return score
    else:
        return score


def backbeat_check(drumbeat):
    global score,backbeat_flag
    snaredrum = drumbeat['pattern1']['track7']['steps']
    backbeat = [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
    if snaredrum == backbeat:
        score += 2
        backbeat_flag = True
        return score
    else:
        return score


    ''' Check for closed hihat (track6) having minimum of four hits. Add one point if True '''
def check_hihat_num(drumbeat):
    global score,hihathits,hihat_flag
    hihat =  drumbeat['pattern1']['track6']['steps']
    hihathits = 0
    for num in hihat:
        if num == 1:
            hihathits += 1
    if hihathits < 4:
        return None
    else:
        score += 1
        hihat_flag = True
        return score


    ''' Check that at least one other instrument (tracks 1-5) gets used at least once '''
def check_other_instrument_used(drumbeat):
    global score,other_tracks_flag
    none_flag = True
    other_tracks = [drumbeat['pattern1']['track1']['steps'],
    drumbeat['pattern1']['track2']['steps'],
    drumbeat['pattern1']['track3']['steps'],
    drumbeat['pattern1']['track4']['steps'],
    drumbeat['pattern1']['track5']['steps']]

    for track in other_tracks:
        if none_flag == False:
            break
        for bit in track:
            if bit == 1:
                none_flag = False
                score += 1
                other_tracks_flag = True
                return score
            else:
                continue
    if none_flag:
        return None
    ''' Check that tempo is within required range between 70 and 150 BPM. Add one point if True '''

def check_tempo_range(drumbeat):
    global score,tempo,tempo_flag
    tempo = drumbeat['options']['tempo']

    if tempo >= 70 and tempo <= 150:
        score += 1
        tempo_flag = True
        return score
    else:
        return None

    ''' Check that at least one volume and one panning position has been changed '''

def check_volume_and_pan(drumbeat):
    global score,vol_pan_flag
    all_tracks_vol = [drumbeat['pattern1']['track1']['vol'],
    drumbeat['pattern1']['track2']['vol'],
    drumbeat['pattern1']['track3']['vol'],
    drumbeat['pattern1']['track4']['vol'],
    drumbeat['pattern1']['track5']['vol'],
    drumbeat['pattern1']['track6']['vol'],
    drumbeat['pattern1']['track7']['vol'],
    drumbeat['pattern1']['track8']['vol']]

    all_tracks_pan = [drumbeat['pattern1']['track1']['pan'],
    drumbeat['pattern1']['track2']['pan'],
    drumbeat['pattern1']['track3']['pan'],
    drumbeat['pattern1']['track4']['pan'],
    drumbeat['pattern1']['track5']['pan'],
    drumbeat['pattern1']['track6']['pan'],
    drumbeat['pattern1']['track7']['pan'],
    drumbeat['pattern1']['track8']['pan']]

    volume_flag = False
    panning_flag = False

    for track in all_tracks_vol:
        if track != 1:
            volume_flag = True
        else:
            continue

    for track in all_tracks_pan:
        if track != 1:
            panning_flag = True
        else:
            continue

    if volume_flag and panning_flag:
        score += 1
        vol_pan_flag = True
        return score
    else:
        return None


def print_score():
    global score,team_num
    print('Team{}: {}, {} : {} / 8'.format(team_num,last_name,first_name,score))


def print_score_for_csv(current_file):
    global score,team_num

    team_num = str(current_file[0])

    fullname_underscore = current_file[1:-5]
    fullname_as_list = fullname_underscore.split('_')
    first_name = fullname_as_list[1]
    last_name = fullname_as_list[0]

    print('Team' + team_num, ',', last_name + ',', first_name, ',', score)


def grade_one(drumbeat):
    global score,hihathits,tempo,four_floor_flag,backbeat_flag,hihat_flag,tempo_flag,other_tracks_flag,vol_pan_flag
    score = 0
    hihathits = 0
    four_floor_flag = False
    backbeat_flag = False
    hihat_flag = False
    tempo_flag = False
    other_tracks_flag = False
    vol_pan_flag = False
    fouronfloor_check(drumbeat)
    backbeat_check(drumbeat)
    check_hihat_num(drumbeat)
    check_other_instrument_used(drumbeat)
    check_tempo_range(drumbeat)
    check_volume_and_pan(drumbeat)



def print_names(list_names):
    for name in list_names:
        team_num = name[0]
        fullname_underscore = name[1:-5]
        fullname_as_list = fullname_underscore.split('_')
        first_name = fullname_as_list[1]
        last_name = fullname_as_list[0]
        print("Team" + team_num + ":", last_name + ",", first_name + ": ", score)


def student_grade_report(current_file):
    global score, hihathits, tempo

    team_num = str(current_file[0])

    fullname_underscore = current_file[1:-5]
    fullname_as_list = fullname_underscore.split('_')
    first_name = fullname_as_list[1]
    last_name = fullname_as_list[0]

    print('Your Drumbit pattern has been reviewed against the standards of your "Drumbit" rubric. '
    'Below are the results.\n')
    print('Drumbit grade report for {0} {1} :'.format(first_name,last_name))
    if four_floor_flag == True:
        print("'Four On the Floor' pattern found in the bass/kick drum track. Two points earned!")
    else:
        print("*Your bass/kick drum track does not contain exactly the 'Four on the Floor' pattern. Minus 2 points.*")
    if backbeat_flag == True:
        print("Backbeats in snare drum on beats two and four. 2 points earned!")
    else:
        print("*Your snare drum does not have exactly backbeats on beats two and four. Minus 2 points.*")
    if hihat_flag == True:
        print("You have at least the minimum required number of closed hihat hits. "
        "{} hits found. 1 point earned!".format(hihathits))
    else:
        print("*You do not have the minimum required closed hihat hits. {} hits found. Minus 1 point.*".format(hihathits))
    if other_tracks_flag == True:
        print("You have used at least one instrument other than kick, snare, and closed hihat. 1 point earned!")
    else:
        print("*You did not use any instruments other than kick, snare, and closed hihat. Minus 1 point.*")
    if tempo_flag == True:
        print("Your tempo of {} BPM is in the acceptable range between 70-150 BPM. "
        "1 point earned!".format(tempo))
    else:
        print("*Your tempo of {} BPM is outside the acceptable range between 70-150 BPM."
        "Minus 1 point.*".format(tempo))
    if vol_pan_flag == True:
        print("You have adjusted at least one volume and one panning position. "
        "1 point earned!")
    else:
        print("*Either all volume positions and/or all panning positions remain unadjusted. "
        "Minus 1 point.*")
    print("Total Score: {} / 8".format(score))
    if score == 8:
        print("Congratulations {}, you got a perfect score!".format(first_name))

    print('\n' + '\n')


def create_dict(files):
    global drumbit_dict,drumbeat

    for file in files:
        if file.endswith('.json'):
            with open(file,'r') as fh:
                data = fh.read()
                json_file = json.loads(data)
                drumbit_dict[file] = json_file
                drumbeat = drumbit_dict[file]

def main():
    create_dict(drumbit_files)

    for key in drumbit_dict:
        grade_one(drumbit_dict[key])
        # student_grade_report(key)
        print_score_for_csv(key)


if __name__ == "__main__":

    main()
