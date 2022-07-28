package org.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

public class MemberService {

    @Autowired(required = false)
    @Qualifier("memberdao1")
    private MemberDao memberDao;

    //저장
    public void regist(){
        memberDao.insert();
    }
    // 보기
    public void getall(){
        memberDao.selectall();
    }

    //삭제
    //변경


}
