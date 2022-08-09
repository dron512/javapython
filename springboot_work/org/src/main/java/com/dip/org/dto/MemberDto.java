package com.dip.org.dto;

import lombok.*;

import java.time.LocalDateTime;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class MemberDto {
    private int id;
    private String password;
    private String email;
    private String name;
    private LocalDateTime regdate;
}
