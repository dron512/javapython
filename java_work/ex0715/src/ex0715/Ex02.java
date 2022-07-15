package ex0715;


interface A{
	public void doA();	// 재정의 해서 사용해야 된다. 오버라이드 해서 사용해야한다.
}

interface B{
	public void doB();
}

public class Ex02 implements A,B{
	public void doA() {
		
	}
	public void doB() {
		
	}
}
