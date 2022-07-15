package ex0715;

public class Ex01 {

	public static void main(String[] args) {
		Friend[] uary = new Friend[10];
		
		uary[0] = new UniFriend("홍길동", "컴공", "010-111-1111");
		uary[1] = new UniFriend("박길동", "전자공", "010-666-556");
		
		uary[2] = new CompFriend("이길동", "구매팀", "010-222-2222");
		uary[3] = new CompFriend("김길동", "기획팀", "010-333-444");
		
		for( int i =0; i<4 ;i++) {
			uary[i].showInfo();	
		}
	}
}
