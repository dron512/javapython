package com.dip.dip.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.dip.dip.entity.Customer;

import java.util.List;

public interface CustomerRepository extends JpaRepository<Customer,Long> {
    // select * from customer where lasename =?
    List<Customer> findByLastName(String lastName);
    // select * from customer where id = ?
    Customer findById(long id);
}
