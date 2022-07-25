package org.dip.member;

import java.util.Collection;

public class MemberDAO {

    public Collection<MemberDTO> selectAll() {
        return Main.memberlist.values();
    }
}
