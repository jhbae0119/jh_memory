package char6_1;


class Product{
	int serialNum = 0;
	static int snum = 100;	// 새로 객체가 생성될때(new 할때)마다 생성되는 게 아님 + 객체가 아닌 클래스 소속--> 변하지 않음
										// 각 객체들이 공유하는 변수임
	public Product() {
		serialNum++;
		snum++;
		System.out.println("serialNum:" + serialNum + ", snum: " + snum);
	}
}
public class StaticTest {

	public static void main(String[] args) {
		Product[] prs = new Product[5];
		for (int i =0; i<prs.length; i++) {
			prs[i] = new Product();
		}

	}

}
