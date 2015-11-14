# -*- coding: utf-8 -*-

import Tkinter as tk
import time
import csv
import sys

BERNIE_SPEECH = """Now is the time for millions of working families to come together. to revitalize American democracy. to end the collapse of the American middle class and to make certain that our children and grandchildren are able to enjoy a quality of life that brings them health, prosperity, security and joy . and that once again makes the United States the leader in the world in the fight for economic and social justice, for environmental sanity and for a world of peace. My fellow Americans: This country faces more serious problems today than at any time since the Great Depression and, if you include the planetary crisis of climate change. it may well be that the challenges we face now are direr than any time in our modern history. Here is my promise to you for this campaign. Not only will I fight to protect the working families of this country. but we're going to build a movement of millions of Americans who are prepared to stand up and fight back. We're going to take this campaign directly to the people – in town meetings, door to door conversations, on street corners and in social media – and that’s BernieSanders.com by the way. This week we will be in New Hampshire, Iowa and Minnesota – and that’s just the start of a vigorous grassroots campaign. Let's be clear. This campaign is not about Bernie Sanders. It is not about Hillary Clinton. It is not about Jeb Bush or anyone else. This campaign is about the needs of the American people, and the ideas and proposals that effectively address those needs. As someone who has never run a negative political ad in his life, my campaign will be driven by issues and serious debate; not political gossip, not reckless personal attacks or character assassination. This is what I believe the American people want and deserve. I hope other candidates agree, and I hope the media allows that to happen. Politics in a democratic society should not be treated like a baseball game, a game show or a soap opera. The times are too serious for that. Let me take a minute to touch on some of the issues that I will be focusing on in the coming months, and then give you an outline of an Agenda for America which will, in fact, deal with these problems and lead us to a better future""".split('.')

def onKeyPress(event):
        text.insert('end', 'You pressed %s\n' % (event.char, ))

def main():
    file_name = 'data_' + str(time.time()) + '_keylog.csv'
    with open(file_name, 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=' ')

        root = tk.Tk()
        root.geometry('500x200')
        text = tk.Text(root, background='black', foreground='white', font=('Helvetica', 12))
        text.pack()

        current_presses = 0
        current_sentence = 0
        text.insert('end', '\n\n\n' + BERNIE_SPEECH[current_sentence] + '\n\n\n')

        def onKeyPress(event, state=[current_presses, current_sentence, data_writer, text]):
            print state, len(BERNIE_SPEECH[state[1]]), event.char
            state[0] += 1
            state[2].writerow([time.time(), event.char])
            if state[1] >= len(BERNIE_SPEECH):
                state[3].insert('end', 'Thanks! Saving Data and Exiting!')
                sys.exit()
            if state[0] >= len(BERNIE_SPEECH[state[1]]):
                state[1] += 1
                state[0] = 0
                state[3].insert('end', '\n\n\n' + BERNIE_SPEECH[state[1]] + '\n\n\n')

        root.bind('<KeyPress>', onKeyPress)
        root.mainloop()

if __name__ == '__main__':
    main()
