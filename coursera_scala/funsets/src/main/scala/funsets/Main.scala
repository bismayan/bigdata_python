package funsets

object Main extends App {
  import FunSets._
  println(contains(singletonSet(1), 1))
  val S1=union(singletonSet(1),union(singletonSet(3),singletonSet(2)))
  val S2=union(singletonSet(1),union(singletonSet(4),singletonSet(5)))
  val S12=diff(S1,S2)
  val a:Int=5
  println("Does S12 Contain "+a+"-"+contains(S12,a))
  def gt(a:Int)(x:Int):Boolean={x>a}
  def lt(a:Int)(x:Int):Boolean={x<a}
  println(contains(filter(S2,gt(3)),4))
  println("Testing Exists "+exists(S2,lt(2)))
  println("Testing Map "+contains(map(S2,(x=>x*x+1)),26))
  printSet(map(S2,(x=>x*x)))
}
