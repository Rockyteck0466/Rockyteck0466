import java.awt.*;
import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException, SQLException {
        books shelf = new books();
        Scanner obj = new Scanner(System.in);
         int choice=0;
         while(choice!=7){
             System.out.println("1.Enter The Student Data\n2.View Books\n3.Add Books\n4.Issue Book\n5.Return Book\n6.Exit");
             System.out.print("Enter the Choice:");
             choice=obj.nextInt();
             if(choice==1){
                 studentData person = new studentData();
                 Scanner objname = new Scanner(System.in);
                 System.out.println("Please Enter the Student Name:");
                 person.name=objname.next();

                 Scanner objdob = new Scanner(System.in);
                 System.out.println("Please Enter the Student Dob:");
                 person.dob=objdob.nextInt();

                 Scanner objid = new Scanner(System.in);
                 System.out.println("Please Enter the Student ID:");
                 person.student_id=objname.nextInt();

                 Scanner objstream = new Scanner(System.in);
                 System.out.println("Please Enter the Student Stream:");
                 person.stream=objname.next();

                 person.setData(person.name,person.dob,person.student_id,person.stream);
                 person.viewData();
             }
             else if (choice==2){
                 Scanner SelectObj = new Scanner(System.in);
                 int choiceSelect=0;
                 while(choiceSelect!=4){
                     System.out.println("1.Electronics\n2.Computers\n3.Civil\n4.All Books\n5.Main Menu");
                     System.out.println("Select The Stream of Books to Display:");
                     choiceSelect=SelectObj.nextInt();
                     if(choiceSelect==1){
                         shelf.electronics();
                     }
                     else if (choiceSelect==2) {
                         shelf.computers();
                     }
                     else if (choiceSelect==3) {
                         shelf.civil();
                     }
                     else if (choiceSelect==4) {
                         shelf.electronics();
                         shelf.computers();
                         shelf.civil();
                     }
                     else if (choiceSelect==5){
                         break;
                     }
                 }
             }
             else if (choice==3){
                 shelf.addBooks();
             }
             else if (choice==4) {
                 shelf.issueBook();
             }
             else if (choice==5) {
                 shelf.returnBook();
             }
             else if (choice==6){
                 System.exit(0);
             }
         }
    }
}
