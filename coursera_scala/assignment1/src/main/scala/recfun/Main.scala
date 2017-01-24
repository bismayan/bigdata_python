package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if(c>r)
        throw new java.util.NoSuchElementException()
      else if((c==r)||(c==0)){
        1
      }
      else
        pascal(c,r-1)+pascal(c-1,r-1)
    }


  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def balance_recur(char_temp: List[Char],num_open:Int):Boolean= {
        if (char_temp.isEmpty) {
          num_open == 0
        }
        else if(num_open<0){
          false
        }
        else if(char_temp.head=='(') {
           balance_recur(char_temp.tail, num_open + 1)
        }
        else if (char_temp.head==')') {
          balance_recur(char_temp.tail,num_open - 1)
        }
        else {
           balance_recur(char_temp.tail, num_open)
        }
      }
      balance_recur(chars,0)
    }
  
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      if(money==0) 1
      else if(coins.isEmpty) 0
      else{
        if(coins.head>money)
          countChange(money,coins.tail)
        else
          countChange(money-coins.head,coins)+countChange(money,coins.tail)
      }

    }


}



