package com.dip.org.entity;

// Table 정의

import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@ToString
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class FreeBoard {
    @Id
    @Column(name = "id",nullable = false)
    @GeneratedValue(strategy = GenerationType.TABLE)
    private Long id;

    private String title;
    private String content;

    private String filename;
    private int hits;

    private LocalDateTime regdate;

}
