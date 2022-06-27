package ex0627;

public class Ex01 {

	public static void main(String[] args) {
	
		// num++
		// num+=1
		// num = num + 1
		
		// num = ++num
		// num = num++
		
		// 변수...선언
		// 변수의 사용 용도 에 따라... 
		// int double String boolean
		// 형변환... 자동형변환 수동형변환
		int a = 10;
		double b = a;
		
		double c = 30.44;
		int d = (int)c;
		System.out.println("b = "+b);
		System.out.println("d = "+d);
		
		System.out.println("(3+4)*5 = "+(3+4)*5);
		System.out.println("3>4 = "+(3>4));
		
		int num1 = 3;
		System.out.println("3>4 = "+(3>4 && (num1+=3)<3));
		System.out.println("num1 = "+ num1);
		System.out.println("3>4 = "+(3>4 || (num1+=3)<3));
		System.out.println("num1 = "+ num1);
		
	}
	
}
