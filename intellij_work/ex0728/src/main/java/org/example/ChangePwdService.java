package org.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

public class ChangePwdService {

    @Autowired(required = false)
    @Qualifier("memberdao1")
    private MemberDao memberDao;


    public void chpwd(){
        memberDao.update();
    }
}
