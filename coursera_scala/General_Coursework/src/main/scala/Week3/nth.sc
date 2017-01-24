import Week3.{List,Cons,Nil}

object nth {
  def nth[T](n:Int,xs:List[T]):T= {
    if (xs.isEmpty) throw new IndexOutOfBoundsException
    if (n == 0) xs.head
    else nth(n - 1, xs.tail)

  }
  val list=new Cons(1,new Cons(2,new Cons(3,new Nil)))
  nth(4,list)
}
