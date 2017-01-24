package funsets

object Main extends App {
  import FunSets._
  println(contains(singletonSet(1), 1))
  println(contains(intersect(singletonSet(1),singletonSet(5)), 3))
  val Set1= union(singletonSet(1),union(singletonSet(2),singletonSet(3)))
  val Set2= union(singletonSet(3),union(singletonSet(4),singletonSet(5)))
  println(contains(diff(Set1,Set2),3))

}
