package ex0701;

/*
 * 자연수 1부터 시작해서 모든 홀수를 더해 나간다. 그리고 그 합이 언제 1000을 넘어서는지
 * 그리고 1000을 넘어선 값은 얼마가 되는지 계산하여 출력하는 프로그램을 작성해보자.
 */
public class Ex03 {
	public static void main(String[] args) {
		int num = 1;
		// 1,3,5,7,9
		int sum = 0;
		while (true) {
			sum = sum + num;
			num = num + 2;
			System.out.println("num = "+num);
			if (sum > 1000)
				break;
		}
		System.out.println("sum = "+ sum);
	}
}
