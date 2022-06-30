package ex0630;

public class SwitchBreak {
	public static void main(String[] args) {
		int n = 2;
		/*
		switch (n) {
		case 1:
			System.out.println("Simple java");
			break;
		case 2:
			System.out.println("Funny java");
		case 3:
			System.out.println("Fatastic java");
			break;
		default:
			System.out.println("The best programming Laguage");
			break;
		}
		*/
		if( n==1 ) {
			System.out.println("Simple java");
		}
		else if( n==2 ) {
			System.out.println("Funny java");
		}
		else if( n==3 ) {
			System.out.println("Fatastic java");
		}
		else {
			System.out.println("The best programming Laguage");
		}
		System.out.println("Do you like java?");
	}
}








