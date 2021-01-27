package char6_1;

class MyClass{
		final int num = 20; 		// class 변수 내 final 변수는 딱 한번 선언과 동시에 초기값 지정, 
											// 변경 불가능한 값이므로 static으로 선언하는 것이 합리적
		public MyClass(int num) {
//			this.num = num;		// 생성자에서 final 변수 수정 불가능
		}
		
}
public class FinalTest {

	public static void main(String[] args) {
		final int num =10;		// 상수 : 변경할 수 없다. 그래서 반드시 선언과 동시에 초기화 필요
		int num2 =30;
		num2 = 50;
//		num =20;					//final 변수 변경 불가능
		final int num3;
		num3 =20;	// 초기화
//		num3 =60;	// 초기화 후 다시 변경 불가능

	}

}
