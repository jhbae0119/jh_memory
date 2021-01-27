package char6_1;

class CardTest {
	String shape;
	char num;
	static int width = 20;
	static int height = 35;
	
	
	public String view() {
		return "["+shape+","+num+","+width+","+height+"]";
	}
}
public class Card {

	public static void main(String[] args) {
		CardTest c1 = new CardTest("하트",'A');
		
	}

}