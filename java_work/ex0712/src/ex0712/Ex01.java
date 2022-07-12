package ex0712;

/*
 * 다음 주민등록 번호의 중간에 삽인된 - 지우고 공백으로 채워서 출력하는 프로그램을 작성해보자.
 * 990925-1012999
 * 990925-*******
 */
public class Ex01 {

	public static void main(String[] args) {

		String jumin = "990925-1012999";
		String a[] = jumin.split("-");
		System.out.println(a[0]);
		System.out.println(a[1]);
		
		System.out.println(a[0]+"-*******");
		
		
	}
	
}
