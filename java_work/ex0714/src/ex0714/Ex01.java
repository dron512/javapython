package ex0714;

/*
  page 309
  [    1 2 3 4 5     ]
  문제1
  위 메소드를 호출하는 형태로, int형 2차원 배열에 저장된 값 전부를 두번째 매개 변수로 전달된 값의 크기만큼 증가시키는 메소드를
  다음의 형태로 정의하자
  public static void addTwoDArr(int[][] arr,int add){
  	// 이안에서 addOneDArr 메소드를 호출한다.
  }
  문제 2
  다음 형태로 표현된 2차원 배열이 존재한다고 가정해보자
  1	2	3	1행
  4	5	6	2행
  7	8	9	3행
  
  이러한 형태를 갖는 int 형 2차원 배열이 인자로 전달되면, 다음의 형태로 배열의 구조를 변경시키는 메소드를 정의하자
  7	8	9	3행이 1행으로
  1	2	3	1행이 2행으로
  4	5	6	2행이 3행으로
  물론 배열의 가로와 세로 길이에 상관없이 위와 깉이 동작하도록 메소드를 정의해야 한다.
 */
public class Ex01 {
	public static void printoneArr(int [] arr) {
		for (int i = 0; i < arr.length; i++)
			System.out.printf("arr[%d] = %d\n", i, arr[i]);
	}
	
	public static void printtwoArr(int [][] arr) {
		for (int i = 0; i < arr.length; i++) {
			printoneArr(arr[i]);
			System.out.println();
		}
	}
	
	public static void addOneDArr(int[] arr, int add) {
		for (int i = 0; i < arr.length; i++)
			arr[i] += add;
	}

	public static void addTwoDArr(int[][] arr, int add) {
		for (int i = 0; i < arr.length; i++) 
			addOneDArr(arr[i], add);
	}

	public static void main(String[] args) {
		int a[][] = {           
				{11},
				{11,22},
				{11,22,33}
		};
		
		printtwoArr(a);
		addTwoDArr(a, 3);
		printtwoArr(a);
		
	}
}










