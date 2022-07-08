package ex0708;

public class Ex03 {

	public static void doA() {
		System.out.println("DoA 메서드");
	}
	public void doB() {
		System.out.println("DoB 메서드");
	}
	
	public static void main(String[] args) {
		Ex03.doA();
		Ex03 ex03 = new Ex03();
		ex03.doB();
		// static 메서드는 바로 호출 가능
		// staitc 메서드가 아닌것은 메모리영역에 할당 해야지만 호출 가능하다..
		
	}
}
