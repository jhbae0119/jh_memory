package char6_1;

public class Pesrson_ex {

	public static void main(String[] args) {
		Person p1 = new Person();
		p1.age = 20;
		p1.name = "BAE JAE HYUN";
		System.out.println(p1.info());
		
		Person p2 = new Person();
		p2.age = 40;
		p2.name = "KIM JAE HYUN";
		System.out.println(p2.info());
		
		Person p4 = new Person("KIM JAE HYUN22", 50);
		System.out.println(p4.info());
		
		Person p5 = new Person("KIM JAE HYUN5");
		System.out.println(p5.info());
		
		Person p6 = new Person(50);
		System.out.println(p6.info());

	}

}
