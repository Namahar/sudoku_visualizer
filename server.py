from flask import Flask, render_template
import sudoku_solver

app = Flask(__name__)
board = 0

# render html
@app.route('/')
def index():
   return render_template('index.html')


@app.route('/backtrack', methods=['POST'])
def backtrack():

   # print(board)
   global board 
   board = None
   board = sudoku_solver.get_board()

   return jsonify(board)


@app.route('/solve', methods=['POST'])
def solve():
   states = sudoku_solver.solver_wrapper(board)

   jsons = {}
   count = 1

   for state in states:
      # print(state)
      # print()
      jsons[count] = jsonify(state)
      count += 1

   return jsons

def jsonify(b):
   data = {}
   count = 1

   for r in range(9):
      for c in range(9):
         data[count] = b[r][c]
         count += 1

   return data


if __name__ == '__main__':
   # run flask
   app.run(debug=True, port=8000)