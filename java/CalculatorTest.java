package char6_1;

class Calculator{
	int val1;
	int val2;

//	public Calculator() {
//		this(0,0); 		//this(): 또다른 생성자 호출, 생성자에서만 호출 가능
//	}

	// 호출되는 생성자 --> 얘만 있으면 다른데서 사용 가능
	public Calculator(int val1, int val2) {	//생성자는 매개변수의 개수나 타입이 다르면 여러개 올 수 있다(오버로드)
		this.val1 = val1;
		this.val2 = val2;
	}
	
	public int add() {
		return  val1 + val2;
	}
	
	public int sub() {
		return  val1 - val2;
	}
	
	public int mul() {
		return val1 * val2;
	}
	
	public double div() {
		return val2 == 0? 0: (double)val1/val2;
		
	}
	
}


public class CalculatorTest {

	public static void main(String[] args) {
		Calculator c1 = new Calculator(20,10);
		System.out.println(c1.add());	// 30
		System.out.println(c1.sub()); 	// 10
		System.out.println(c1.mul());	// 200
		System.out.println(c1.div()); 		// 2
		
		
	}

}
