package char6_1;

class Account {
	String id;
	String name;
	int balance;
	

	public Account(String id, String name, int balance) {
		this.id=id;
		this.name = name;
		this.balance = balance;
	}
	
	public Account(String id, int balance) {
		this.id=id;
		name = "none";
		this.balance = balance;
	}
	public void deposit(int money) {
		if (money>0) {
			balance += money;
		}
	}
	
	public void withdraw(int money) {
		if (balance >=money) {
			balance -= money;
		}
		else {
			System.out.println("잔액이 부족합니다.");
		}
	}
	public String info() {
		return "계좌번호 : " + id +", 이름 : " + name + ", 잔액 : " + balance;
	}
}

public class AccountTest {

	public static void main(String[] args) {
		//Account 객체 2개 만들기
//		Account A1 = new Account();
//		A1.id = "101";
//		A1.name ="hong gil dong";
//		A1.balance = 100000;
//		
//		Account A2 = new Account();
//		A2.id = "102";
//		A2.name ="bae jae hyun";
//		A2.balance = 200000;
//		
//		System.out.println(A1.info());
//		System.out.println(A2.info());
//		
//		A1.deposit(5000);
//		A2.withdraw(10000);
//		
//		System.out.println(A1.info());
//		System.out.println(A2.info());
		
		Account A3 = new Account("103","BaeJaehyun",10000);
		System.out.println(A3.info());
		
		Account A4 = new Account("104", 200000);
		System.out.println(A4.info());
		
		
		
	}

}
