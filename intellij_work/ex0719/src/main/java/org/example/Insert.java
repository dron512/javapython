package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class Insert {
    private static String dburl = "jdbc:mysql://localhost:3306/test?serverTimezone=Asia/Seoul&useSSL=false";

    Insert(){
        Connection conn;
        PreparedStatement pstmt;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");

            conn = DriverManager.getConnection(dburl,"root","1234");
            pstmt = conn.prepareStatement("insert into fish " +
                                    "(`index`,name,length,weight) " +
                                    "values " +
                                    "(?,?,?,?)");
            pstmt.setInt(1,4);
            pstmt.setString(2,"smelt");
            pstmt.setDouble(3,11.2);
            pstmt.setDouble(4,12);
            pstmt.executeUpdate();
        }catch (Exception e){
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {

        new Insert();
    }
}
