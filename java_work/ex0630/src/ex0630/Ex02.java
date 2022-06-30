package ex0630;

public class Ex02 {

	public static void main(String[] args) {
	
		for(int i=0; i<10; i++) {
			if( i == 5 ) {
				break;
			}
			if( i== 1 )
				continue;
			System.out.println("i = "+i);
		}
		
	}
	
}
