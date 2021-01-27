package char6_1;

class Test{
	int ival;
	static int sval;		// 클래스 로딩 시 (프로그램 시작하자마자) 변수 할당, 언제든 사용 가능
	public void iMethod() {
		ival = 100;		// instance 메소드에서 instance 변수 접근 가능
		sval = 200;		// instance 메소드에서 static 변수 접근 가능
	}
	
	public static void sMethod() {	
//		ival = 10;				// static 메소드에서는 instance 변수 접근 불가능
		sval = 20;				// static 메소드에서 static 변수 접근 가능
//		this.sval = 40; 		// static 메소드는 this 사용 불가
	}
}

public class StaticInstanceTest {

	public static void main(String[] args) {
		Test.sval=10;			// static 변수는 객체 생성 없이 클래스명으로 접근 가능
		Test.sMethod();		// static 메소드는 객체 생성 없이 클래스명으로 호출 가능
		// Test.inval = 20;		// instance 변수는 클래스 명으로 접근 불가능
		
		Test t = new Test();	// 객체 생성
		t.ival=20;					// instance 변수는 반드시 객체 생성하여 참조변수를 통해 접근해야 함
		// Test.iMethod();		// instance 메소드는 클래스명으로 접근 불가능
		t.iMethod();				// 생성된 객체를 통해서만 호출 가능
		
	}

}
