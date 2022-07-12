package ex0711;

public class Ex03 {
	
	public Ex03() {
		System.out.println("기본생성자");
	}
	public Ex03(int a) {
		System.out.println("파라메타 1개 a = "+a);
	}
	public Ex03(int a,int b) {
		System.out.println("파라메타 2개 a = "+a);
		System.out.println("파라메타 2개 b = "+b);
	}
	public static void main(String[] args) {
		new Ex03();
		new Ex03(10);
		new Ex03(10,20);
	}
}
