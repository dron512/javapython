package ex0707;

public class Ex01 {

	public static void main(String[] args) {
		Person p1 = new Person();
//		p1.name = "자바";
		p1.setName("자바");
		System.out.println(p1);
		System.out.println(p1.toString());
		
		Person p2 = new Person("한글");
		System.out.println(p2);
	}
	
}
