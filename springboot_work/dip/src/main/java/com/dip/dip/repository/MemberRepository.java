package com.dip.dip.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.dip.dip.entity.Member;

public interface MemberRepository extends JpaRepository<Member,Long> {
}
