package Week3

trait List[T] {
  def isEmpty:Boolean
  def head:T
  def tail: List[T]
}

class Cons[T](val head:T, val tail: List[T]) extends List[T] {
  def isEmpty=false

}

class Nil[T] extends List[T] {
  def isEmpty:Boolean= true
  def head:Nothing= throw new NoSuchElementException("Nil.Head")
  def tail:Nothing= throw new NoSuchElementException("Nil.Tail")

}
//def singleton[T](elem:T)= new Cons[T](elem, new Nil[T])
//singleton[Int](3)
//singleton[Boolean](true)