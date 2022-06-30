package ex0630;

public class Ex04 {

	public static void main(String[] args) {
		
		boolean a = true;
		for(    ;a; a = false ) {
			System.out.println("무한 루프");
		}
	}
}
