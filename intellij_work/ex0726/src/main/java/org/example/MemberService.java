package org.example;

import org.springframework.beans.factory.annotation.Autowired;

public class MemberService {
    @Autowired
    private MemberDao memberDao;
    @Autowired
    private MemberPrinter memberPrinter;

    public void list() {
        memberDao.selectAll();
    }

    public void regist(MemberDto dto) throws Exception {
        String result = memberDao.getSelectByEmail(dto.getEmail());
        if (result.equals("have"))
            throw new Exception();
        else
            memberDao.insert(dto);
    }
}
