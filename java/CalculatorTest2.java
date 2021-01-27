package char6_1;

class Calculator2{
	public static int add(int x, int y) {
		return x+y;
	}
	
	public static int sub(int x, int y) {
		return x-y;
	}
	public static int mul(int x, int y) {
		return x*y;
	}
	public static double div(int x, int y) {
		return y == 0? 0: (double)x/y;
	}
	
}

public class CalculatorTest2 {

	public static void main(String[] args) {
//		Calculator2 c1 = new Calculator2();
//		System.out.println(c1.add(10,20));	// 30
//		System.out.println(c1.sub(20,8)); 	// 12
//		System.out.println(c1.mul(2,3));	// 6
//		System.out.println(c1.div(6,3)); 		// 2
		
		System.out.println(Calculator2.add(10,20));	// 30
		System.out.println(Calculator2.sub(20,8)); 	// 12
		System.out.println(Calculator2.mul(2,3));	// 6
		System.out.println(Calculator2.div(6,3)); 		// 2

	}

}
