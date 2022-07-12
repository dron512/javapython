package ex0711;
/*
 * 
 * page 237
 * 
 * 클래스 변수와 클래스 메서드
 * 문제
 * 다음 main 메소드와 함꼐 동작하는 Accumulator 클래스를 정의하자 그리고 Accumulator 클래스에
 * main 메소드도 넣어서 컴파일및 실행을 하자
 * 
 * 실행 결롸고 즉 showResult메소드의 호출 결과로 다음과 같은 수준의 출력을 보이면 된다.
 * sum = 45
 */
public class Ex01 {

	public static void main(String[] args) {
		System.out.println(Accumulator.MAX);
		Accumulator acc = new Accumulator();
		for(int i =0; i<10;i++) {
			acc.add(i);
		}
		acc.showResult();
	}
	
}
