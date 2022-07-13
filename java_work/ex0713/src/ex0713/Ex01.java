package ex0713;

/*
 * int 형 1차원 배열을 매개변수로 전달받아서 배열에 저장된 최댓값 , 최솟값을 찾아서 반환하는
 * 메소드를 각각 다음의 형태로 정의하자
 * 
 * public static int minValue(int[] arr)
 * public static int maxValue(int[] arr)
 * 
 * 단 반복문을 사용할때 minValue의 정의에서는 일반적인 for문을 사용하고 maxValue의 정의에서는
 * 새로운 for문(enhanced for문)을 사용하기로 하자.
 */
public class Ex01 {
	public static int[] ary = { 10, 20, 6, 9, 33, 5 };

	public static int minValue(int[] arr) {
		int min = ary[0];
		for (int i = 0; i < ary.length; i++) {
			if ( min > ary[i]) {
				min = ary[i];
			}
		}
		return min;
	}

	public static int maxValue(int[] arr) {
		int max = ary[0];
		for (int temp : ary) {
			if( max < temp) {
				max = temp;
			}
		}
		return max;
	}

	public static void main(String[] args) {
		int min = minValue(ary);
		int max = maxValue(ary);

		System.out.println("최솟값 = " + min);
		System.out.println("최댓값 = " + max);
	}

}
