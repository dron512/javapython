package ex0713;

class AA{
	AA(){
		System.out.println("AA 기본생성자");
	}
}
class BB extends AA{
	BB(){
		super();
		System.out.println("BB 기본생성자");
	}
}

public class Ex05 {
	public static void main(String[] args) {
		new BB();
	}
}
