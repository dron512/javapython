package org.example;

public class MemberService {

    private MemberDao memberDao;
    private MemberPrinter memberPrinter;

    public void setMemberPrinter(MemberPrinter memberPrinter) {
        this.memberPrinter = memberPrinter;
    }

    public MemberService(){}

    public MemberService(MemberDao memberDao) {
        this.memberDao = memberDao;
    }

    public void setMemberDao(MemberDao memberDao) {
        this.memberDao = memberDao;
    }

    public void list(){
//        memberDao = new MemberDao();
        memberDao.selectAll();
    }

    /*
        만약에...
        datamap 안에 같은 이메일이 있으면...
        저장할수 없다..
        아니면...
        data 저장을 해야 합니다.
     */
    public void regist(MemberDto dto) throws Exception {
//        System.out.println(dto);
//        memberDao = new MemberDao();

        String result = memberDao.getSelectByEmail(dto.getEmail());
        if(result.equals("have"))
            throw new Exception();
        else
            memberDao.insert(dto);


    }
}
