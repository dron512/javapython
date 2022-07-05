package ex0705;

public class Ex05 {

	public static void doA(String str1,String str2) {
		System.out.println(str1+str2);
	}
	
	public static void main(String[] args) {
		String a = "Happy";
		String b = new String("Happy");
		
		System.out.println("a = "+a);
		System.out.println("b = "+b);
		doA(a,b);
	}
}
