package ex0705;

public class Ex01 {
	public static void main(String[] args) {
		A a1 = new A();
		
		System.out.println("a1.a = "+a1.a);
		a1.a += 10;
		a1.doA();
		a1.doB();
		System.out.println(a1.doC(2.1));
		
		A a2 = new A();
		A a3 = new A();
		A a4 = new A();
		
	}
}
