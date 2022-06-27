package test;
/*
  int 형 변수 num1,num2,num3에 각각 10,20,30이 저장된 상태에서 다음 문장을 실행하면 변수에는
	각각 얼마가 저장되겠는가?
    num1 = num2 = num3;
	이의 	확인을 위한 코드를 작성하고 그러한 결과를 보이는 이유를 설명해보자
 */
public class Ex01 {
	public static void main(String[] args) {
		int num1 = 10;
		int num2 = 20;
		int num3 = 30;
		
		num1 = num2 = num3;
		
		System.out.println(num1);
		System.out.println(num2);
		System.out.println(num3);
	}
	
}
