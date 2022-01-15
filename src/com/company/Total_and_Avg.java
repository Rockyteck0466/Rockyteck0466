package com.company;

import java.util.Scanner;

public class Total_and_Avg {
    public static void main(String[] args) {
        System.out.print("Enter the First Sub Marks:");
        Scanner S1= new Scanner(System.in);
        int Maths = S1.nextInt();

        System.out.print("Enter the Second Sub Marks:");
        Scanner S2= new Scanner(System.in);
        int Physics = S2.nextInt();

        System.out.print("Enter the Third Sub Marks:");
        Scanner S3= new Scanner(System.in);
        int Chemistry = S3.nextInt();

        System.out.print("Enter the Fourth Sub Marks:");
        Scanner S4= new Scanner(System.in);
        int Hindi = S4.nextInt();

        System.out.print("Enter the Fifth Sub Marks:");
        Scanner S5= new Scanner(System.in);
        int Social = S5.nextInt();

        float Total = Maths + Physics + Chemistry + Hindi + Social;
        float Avg = Total/6;
         if (Avg<75){
             System.out.println("Current Grade:"+"C");
             System.out.print("Total Marks:"+Total);
         }
         else if(Avg<85) {
             System.out.println("Current Grade:"+"B");
             System.out.print("Total Marks:"+Total);
         }
         else if(Avg>=85) {
             System.out.println("Current Grade:"+"A");
             System.out.print("Total Marks:"+Total);
         }
    }
}