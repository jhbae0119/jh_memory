package char6_1;

public class Person {
	int age;
	String name;

	public Person() {
		this("none",0); 		//this(): 또다른 생성자 호출, 생성자에서만 호출 가능
	}
	
	// 호출되는 생성자 --> 얘만 있으면 다른데서 사용 가능
	public Person(String name, int age) {	//생성자는 매개변수의 개수나 타입이 다르면 여러개 올 수 있다(오버로드)
		this.name = name;
		this.age = age;
	}
	
	public Person(String name) {
		this(name,0);
	}
	
	public Person(int age) {
		this("none",age);
	}
	
//	public Person(String id) {		// 매개변수 타입과 개수가 같은 것이 있어서 오버로드 성립 하지 않음
//
//	}
	
	public String info() {
		return "이름: " +  name +", 나이 : " + age;
	}
}
