package ex0715;

public class Ex04 {
	public static void main(String[] args) {
		Printable print = new Printable() {
			@Override
			public void print(String doc) {
				System.out.println("인터페이스 객체 생성");
				System.out.println(doc);
			}
		};
		print.print("내용");
		
		Printable print1 = (doc)->{
			System.out.println("임터페이스 람다 생성");
			System.out.println(doc);
		};
		print1.print("새로운... 내용..");
	}
}
