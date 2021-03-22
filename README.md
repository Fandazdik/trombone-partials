# trombone-partials
Module with some handy trombone partial calculators

## Functions
Most of the functions handle input as a number-type, where 0 is E1 and increases by a semitone for each note (1: F1, 2: F#1, 3: G1, etc.)
For functions marked with \*, input will need to be passed as this number-type. (Refer to `to_num()`)

### `to_note(input_note, mode='#')`
Takes input as a number-type and returns it as note_type. (`to_not(0)` returns `E1` e.g.)

### `to_num(input_note)`
Takes input as a note ('D5' e.g.) and returns the note associated with it. (`to_num('E1')` returns `46` e.g.)
*Doesn't work with flats! :(*

### \*`get_note_positions(input_position, any_octave=False)`
Takes input as number-type and returns the partial and position where this note can be played in the form `(position, partial)`. `any_octave` will ignore the octave number and return the partials and positions of the note given in any octave.

### \*`get_note(input_note)`
Takes input as number-type and will return the most stable way to play the given note (with the lowest partial).
