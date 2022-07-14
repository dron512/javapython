package ex0714;

class Super{
}
class Sub extends Super{
}
class AAA{}
public class Ex05 {

	public static void main(String[] args) {
		Super super1 = new Sub();
		Sub sub1 = (Sub) super1;
//		AAA a1 = new Sub();
//		AAA a2 = new Super();
	}
}
