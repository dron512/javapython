package ex0706;

/*
 * page176...
 * 생성자를 포함하는 클래스의정의
 * 밑변과 높이 정보를 지정할수 있는 Triangle클래스를 정의하자
 * 밑변과 높이 정보를 변경할수 있는 메소드와 삼각형의 넓이를 계산해서 반환하는 메소드도 정의하자
 */
class Traingle {
	int width;
	int height;
	public Traingle() {}
	public Traingle(int width, int height) {
		super();
		this.width = width;
		this.height = height;
	}
	// alt + shift + s -> o 생성자
	// alt + shift + s -> r getter setter 만들기
	public void printArea() {
		double area = this.width * this.height * 0.5d;
		System.out.println("넓이는 = " + area);
	}
	public void setWidth(int w) {
		width = w;
	}
	public void setHeight(int height) {
		this.height = height;
	}
}
public class Ex01 {
	public static void main(String[] args) {
		Traingle t1 = new Traingle();
		t1.printArea();
		t1.setHeight(50);
		t1.setWidth(50);
		t1.printArea();
		
		Traingle t2 = new Traingle(30,50);
		t2.printArea();
	}
}











