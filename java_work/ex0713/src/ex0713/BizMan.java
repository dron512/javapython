package ex0713;
class Man{
	private String name;
//	public Man() {}
	// alt +shift + s-> o
	public Man(String name) {
		this.name = name;
	}
	// alt + shift + s-> s
	@Override
	public String toString() {
		return "Man [name=" + name + "]";
	}
}
// 1. 부모클래스에 기본생성자 선언
// 2. 자식클래스에 부모생성자랑 동일한 생성자를 선언
public class BizMan extends Man{

	public BizMan(String name) {
		super(name);
	}

	public static void main(String[] args) {
		BizMan biz = new BizMan("홍길동");
		System.out.println(biz);
		
	}
	
}
