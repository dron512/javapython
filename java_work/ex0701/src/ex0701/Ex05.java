package ex0701;

public class Ex05 {

	public static void doA() {
		
	}
	
	public static void doA(int a) {
		System.out.println("doA 메서드 시작");
		System.out.println("a = "+a);
		System.out.println("doA 메서드 끝");
	}
	
	public static void main(String[] args) {
		System.out.println("시작");
		doA(13);
		doA(20);
		doA(30);
		doA(40);
		System.out.println("끝");
	}
	
}
