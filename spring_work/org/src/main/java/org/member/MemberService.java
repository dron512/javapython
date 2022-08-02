package org.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Service
public class MemberService {

	@Autowired
	private MemberDao memberDao;

	public void newMember(MemberDto memberDto) {
		
		// 해당되는 email 이 존재하는확인
		// 없으면 data추가
		// 있으면 data넣을수없다 이미중복...
		
		// 있는지 확인 메서드
//		memberDao.getSelectByEmail(memberDto.getEmail());
		// 추가 하는 메서드
		memberDao.insert(memberDto);
		
	}
	
	public void printMember() {
		memberDao.selectall()
				.forEach(m -> System.out.println(m));
	}
	
	
}












