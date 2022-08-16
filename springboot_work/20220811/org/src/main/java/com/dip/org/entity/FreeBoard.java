package com.dip.org.entity;

// Table 정의

import lombok.*;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
@Getter
@Setter
@ToString
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class FreeBoard {
    @Id
    @Column(name = "id", nullable = false)
    private Long id;

    private String title;
    private String content;

    private String regdate;

}
