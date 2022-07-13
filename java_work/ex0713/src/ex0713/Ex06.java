package ex0713;
class AAA {
	int a;
	public AAA(int a) {
		super();
		this.a = a;
	}
}
/*
 * 부모와 자식클래스에 동일한 생성자가 선언되어야 하나... 
 * 부모생성자를 임의적으로 지정시 문제없이 동작함.. 
 */
class BBB extends AAA {
	private int b;
	private int c;
	public BBB(int a, int b, int c) {
		super(a);
		this.b = b;
		this.c = c;
	}
	@Override
	public String toString() {
		return "BBB [a ="+super.a+ ", b=" + b + ", c=" + c + "]";
	}
}
public class Ex06 {
	public static void main(String[] args) {
		System.out.println(new BBB(1, 2, 3));
	}
}
