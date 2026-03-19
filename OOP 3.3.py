def draw_grid():
    do_ngang = '+ - - - - '
    do_doc = '|         '
    def print_row():
        print(do_ngang * 2 + '+')
        print(do_doc * 2 + '|')
        print(do_doc * 2 + '|')
        print(do_doc * 2 + '|')
        print(do_doc * 2 + '|')
    print_row() 
    print_row() 
    print(do_ngang * 2 + '+') 
draw_grid()

def draw_big_grid():
  ngang= '+ - - - - '
  doc= '|         '
  def mot_tang():
      print(ngang * 4 + '+')
      print(doc * 4 +'|')
      print(doc * 4 +'|')
      print(doc * 4 +'|')
      print(doc * 4 +'|')
  mot_tang()
  mot_tang()
  mot_tang()
  mot_tang()
  print(ngang * 4 +'+')
draw_big_grid()
      
