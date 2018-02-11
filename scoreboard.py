
class Scoreboard(object):

    def __init__(self, snapshot_queue):
        entries = snapshot_queue.split('\n')
        self.constant = entries.pop(0)
        self.entries = list()
        self.participants = dict()

        for entrie in entries:
            self.entries.append(self.parse_entrie(entrie))

    def parse_entrie(self, string_entrie):
        entrie = string_entrie.split(" ")
        return dict(participant = int(entrie[0]), question = int(entrie[1]), score = int(entrie[2]), type = entrie[3])
    
    def __create_participants(self):
        for entry in self.entries:
            self.participants[entry['participant']] = dict(score = 0, num_correct_question = 0)

    def get_output(self):
        self.__create_participants()

        for entry in self.entries:
            if entry['type'] == 'I':
                    self.participants[entry['participant']]['score'] += 20
            elif entry['type'] == 'C':
                    self.participants[entry['participant']]['score'] += entry['score']
                    self.participants[entry['participant']]['num_correct_question'] += 1

        result = ''
        for part in sorted(self.participants):
            result += '{} {} {} \n'.format(part, self.participants[part]['num_correct_question'], self.participants[part]['score'] )
        return result
