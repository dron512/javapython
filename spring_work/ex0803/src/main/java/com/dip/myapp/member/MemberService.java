package com.dip.myapp.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MemberService {

	@Autowired
	private MemberDao memberDao;

	public void regist(MemberDto memberDto) {
		memberDao.insert(memberDto);
	}
	
}
