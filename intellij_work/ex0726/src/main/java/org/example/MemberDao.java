package org.example;

import java.util.HashMap;
import java.util.Map;

public class MemberDao {
    public static Map<String,MemberDto> data = new HashMap<>();
    public void selectAll() {
        System.out.println(this);
        System.out.println("[data 출력 start]");
        if (data.size() ==0 ) System.out.println("data 내용없음");
        data.values().forEach(memberDto -> System.out.println(memberDto));
        System.out.println();
    }
    public void insert(MemberDto dto) {
        System.out.println(this);
        data.put(dto.getEmail(),dto);
    }

    public String getSelectByEmail(String email) {
        System.out.println(this);
        MemberDto dto = data.get(email);
        if(dto != null)
            return "have";
        else
            return "donthave";
    }
}
