import winsound


freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

def main():
    notes_list = notes.split("-")
    iter_of_notes = iter(notes_list)

    for note in iter_of_notes:
        frequency = freqs.get(note.split(",")[0])
        duration = int(note.split(",")[1])
        winsound.Beep(frequency, duration)


if __name__ == '__main__':
    main()