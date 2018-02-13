from scoreboard import Scoreboard

## read for file ##
input_file = open('example_files/input.txt','r')
string_file = input_file.read()
print(string_file)
input_file.close()

## instance scoreboard this snapshot placar ##
score = Scoreboard(string_file)
string_score_output = score.get_output()
print(string_score_output)

## write output file ##
output_file = open('example_files/output.txt','w')
output_file.write(string_score_output)
output_file.close()