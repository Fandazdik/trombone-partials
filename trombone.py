import random

notes = {
    0: ('E'),
    1: ('F'),
    2: ('F#', 'Gb'),
    3: ('G'),
    4: ('G#', 'Ab'),
    5: ('A'),
    6: ('A#', 'Bb'),
    7: ('B'),
    8: ('C'),
    9: ('C#', 'Db'),
    10: ('D'),
    11: ('D#', 'Eb')
}

def get_note_positions(input_position, any_octave = False):
    final_position_list = []
    for position in range(1, 8):
        root_number = 7 - position
        for add_interval in [(0, 1), (7, 2), (12, 3), (16, 4), (19, 5)]:
            unmodded_note = root_number + add_interval[0]
            if any_octave:
                if unmodded_note % 12 == input_position:
                    final_position_list.append((position, add_interval[1]))
            else:
                if unmodded_note == input_position:
                    final_position_list.append((position, add_interval[1]))
    return final_position_list #Returns (position, partial)

def get_note(input_note):
    for position in range(1, 8):
        root_number = 7 - position
        for add_interval in [(0, 1), (7, 2), (12, 3), (16, 4), (19, 5)]:
            unmodded_note = root_number + add_interval[0]
            if unmodded_note == input_note:
                return position, add_interval[1]
    
def to_note(input_note, mode = '#'): # or 'b'
    global notes
    black_notes = [2, 4, 6, 9, 11]
    res = divmod(input_note, 12)
    # dividend + 2
    # remainder use notes dict
    octave = res[0] + 2
    if res[1] in black_notes:
        if mode == '#':
            note = notes[res[1]][0]
        elif mode == 'b':
            note = notes[res[1]][1]
    else:
        note = notes[res[1]]
    
    return note + str(octave)

def to_num(input_note): # inverse of to_note
    note = input_note[:-1]
    octave = input_note[-1:]
    
    counter = 0
    for note_names in notes.values(): # To deal with tuples
        if note in note_names:
            remainder = counter
            break
        counter += 1
    
    octave = (int(octave) - 2) * 12
    
    
    return octave + remainder

def random_note(oct_range, black_notes = False, mode = '#'):
    global notes
    octave = random.choice(range(oct_range[0], oct_range[1]+1))
    note_choice = [0, 1, 3, 5, 7, 8, 10] if not black_notes else range(0, 12)
    note = notes[random.choice(note_choice)]
    if len(note) == 2:
        if mode == '#':
            note = note[0]
        elif mode == 'b':
            note = note[1]
    return note + str(octave)
    
    
