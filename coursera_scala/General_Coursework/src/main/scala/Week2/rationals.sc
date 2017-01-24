object rationals {
  val x = new Rational(1, 3)
  x.numer
  val y= new Rational(5,7)
  x+x
  x-y
  x-x
  y+y
  val z= new Rational(6)
  x-y-z
  x<z
  x max y

  class Rational(x: Int, y: Int) {
    require(y!=0,"denominator must be non-zero")
    def this(x:Int)=this(x,1)

    private def gcd(a:Int,b:Int):Int = if (b==0) a else gcd(b,a%b)
    private val g=gcd(x,y)
    def numer = x/g
    def denom = y/g

    def +(that:Rational)=
      new Rational(
        this.numer*that.denom+that.numer*this.denom,
        this.denom*that.denom
      )
    def <(that:Rational)= this.numer*that.denom < that.numer*this.denom
    def max(that:Rational)= if(this< that) that else this
    def unary_- : Rational =new Rational(-numer,denom)
    def -(that:Rational)= this+ -that

    override def toString= {
      val g=gcd(this.numer,this.denom)
      numer+"/"+denom
    }
  }


}