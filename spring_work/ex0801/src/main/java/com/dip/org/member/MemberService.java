package com.dip.org.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Service
public class MemberService {

	@Autowired
	private MemberDao memberDao;

	public void newMember(MemberDto memberDto) {
		
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












