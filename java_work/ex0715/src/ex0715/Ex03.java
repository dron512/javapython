package ex0715;

interface Printable{
	int MAX_PAGE = 20;
	void print(String doc);
	default void printCMYK(String doc) {
		System.out.println("칼라 프린터");
		print(doc);
	}
}
class SPrint implements Printable{
	@Override
	public void print(String doc) {
		System.out.println("삼성프린터");
		System.out.println(doc);
	}
}
class LPrint implements Printable{
	@Override
	public void print(String doc) {
		System.out.println("엘지프린터");
		System.out.println(doc);
	}
}
public class Ex03 {
	public static void main(String[] args) {
		System.out.println(Printable.MAX_PAGE);
		//Printable.MAX_PAGE = 40;
		Printable prn = new SPrint();
		prn.print("출력하고 싶은거");
		prn = new LPrint();
		prn.print("엘지 프린터로 출력하고 싶은거");
		
		prn.printCMYK("엘지 프린터기에서 나온 칼라");
	}

}







