package ex0704;
/*
 * 문제1
 * 인자로 정수 n을 전달 받아서 2의 n승을 계산하여 반환하는 메소드를 재귀의 형태로 정의하고,
 * 이를 호출하는 main 메소드를 정의해보자
 * 
 * 2^3 = 2*2*2*1
 * 2^4 = 2*2*2*2*1
 * 2^5 = 2*2*2*2*2*1
 */
public class Ex03 {

	public static void main(String[] args) {
		int result = doA(3);
		System.out.println("result = "+result);
		result = doA(5);
		System.out.println("result = "+result);
	}
	/*
	 * doA(3)
	 * 2*doA(2)
	 * 2*2*doA(1)
	 * 2*2*2*doA(0)
	 * return 2*2*2*1
	 */
	public static int doA(int n) {
		if(n==1)
			return 2;
		else
			return 2*doA(n-1);
	}
}












