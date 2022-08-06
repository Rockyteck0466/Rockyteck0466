import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.sql.*;

public class books {

        ArrayList<String> ece = new ArrayList<>();
        ArrayList<String> cse = new ArrayList<>();
        ArrayList<String> civl = new ArrayList<>();

        ArrayList<String> issuedBookCollection = new ArrayList<>();

    public void electronics(){
        try {
            String urlDb = "jdbc:oracle:thin:@localhost:1521:orcl";
            String userDb = "system";
            String passwordDb = "oracle";
            Class.forName("java.sql.Driver");
            Connection con = DriverManager.getConnection(urlDb,userDb,passwordDb);
            Statement stmt = con.createStatement();
            ResultSet qres=stmt.executeQuery("Select * from ELECTRONICS_BOOKS");
            int count = 1;
            System.out.println("------------Electronics------------");
            while(qres.next()){
                int bookid = qres.getInt(1);
                String bookName=qres.getString(2);
                String bookAuthor =qres.getString(3);
                int bookVolume=qres.getInt(4);
                int bookStock =qres.getInt(5);
                System.out.println("BOOK NO:"+count);
                System.out.println("Book Id:"+bookid+" "+"\nBook Name:"+" "+bookName+" "+"\nBook Author:"+" "+bookAuthor+" "+"\nBook Volume:"+" "+bookVolume+" "+"\nBook Stock:"+" "+bookStock);
                System.out.println("-------------------------------------");
                count=count+1;
            }
            stmt.close();
            con.close();

        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    public void computers(){
        try {
            String urlDb = "jdbc:oracle:thin:@localhost:1521:orcl";
            String userDb = "system";
            String passwordDb = "oracle";
            Class.forName("java.sql.Driver");
            Connection con = DriverManager.getConnection(urlDb,userDb,passwordDb);
            Statement stmt = con.createStatement();
            ResultSet qres=stmt.executeQuery("Select * from COMPUTERS_BOOKS");
            int count = 1;
            System.out.println("------------Computers------------");
            while(qres.next()){
                int bookid = qres.getInt(1);
                String bookName=qres.getString(2);
                String bookAuthor =qres.getString(3);
                int bookVolume=qres.getInt(4);
                int bookStock =qres.getInt(5);
                System.out.println("BOOK NO:"+count);
                System.out.println("Book Id:"+bookid+" "+"\nBook Name:"+" "+bookName+" "+"\nBook Author:"+" "+bookAuthor+" "+"\nBook Volume:"+" "+bookVolume+" "+"\nBook Stock:"+" "+bookStock);
                System.out.println("-------------------------------------");
                count=count+1;
            }
            stmt.close();
            con.close();

        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    public void civil(){
        try {
            String urlDb = "jdbc:oracle:thin:@localhost:1521:orcl";
            String userDb = "system";
            String passwordDb = "oracle";
            Class.forName("java.sql.Driver");
            Connection con = DriverManager.getConnection(urlDb,userDb,passwordDb);
            Statement stmt = con.createStatement();
            ResultSet qres=stmt.executeQuery("Select * from CIVIL_BOOKS");
            int count = 1;
            System.out.println("------------Civil------------");
            while(qres.next()){
                int bookid = qres.getInt(1);
                String bookName=qres.getString(2);
                String bookAuthor =qres.getString(3);
                int bookVolume=qres.getInt(4);
                int bookStock =qres.getInt(5);
                System.out.println("BOOK NO:"+count);
                System.out.println("Book Id:"+bookid+" "+"\nBook Name:"+" "+bookName+" "+"\nBook Author:"+" "+bookAuthor+" "+"\nBook Volume:"+" "+bookVolume+" "+"\nBook Stock:"+" "+bookStock);
                System.out.println("-------------------------------------");
                count=count+1;
            }
            stmt.close();
            con.close();

        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    public void addBooks() throws IOException, SQLException {
        Scanner obj = new Scanner(System.in);
        int choice = 0;
        System.out.println("Choice: "+choice);
        while (choice!=4){
            System.out.println("1.Electronics\n2.Computers\n3.Civil\n4.Main Menu");
            System.out.print("Please Enter the department to Add the Book:");
            choice=obj.nextInt();
            if(choice==1) {
                BufferedReader reader = null;
                Statement stmt = null;
                Connection con = null;
                try {
                    String urlDb = "jdbc:oracle:thin:@localhost:1521:orcl";
                    String userDb = "system";
                    String passwordDb = "oracle";
                    Class.forName("java.sql.Driver");
                    con = DriverManager.getConnection(urlDb, userDb, passwordDb);
                    stmt = con.createStatement();

                    int CurrentStock = 0;
                    reader = new BufferedReader(new InputStreamReader(System.in));

                    System.out.println("Enter the Book#: ");
                    int bookid1 = Integer.parseInt(reader.readLine());

                    System.out.println("Enter the BookName: ");
                    String bookname = reader.readLine();

                    System.out.println("Enter the Author Name: ");
                    String authorname = reader.readLine();

                    System.out.println("Enter the Volume: ");
                    int bookvolume = Integer.parseInt(reader.readLine());

                    int bookstock1 = 1;

                    //Using prepared Statement to insert the values to the table.
                    PreparedStatement pstmt = con.prepareStatement("INSERT INTO ELECTRONICS_BOOKS (BOOK#,BOOK_NAME,AUTHOR,VOLUME,STOCK) VALUES (?,?,?,?,?)");

                    pstmt.setObject(1, bookid1);
                    pstmt.setObject(2, bookname);
                    pstmt.setObject(3, authorname);
                    pstmt.setObject(4, bookvolume);
                    pstmt.setObject(5, bookstock1);

                    int count = pstmt.executeUpdate();
                    System.out.println(count + " Row Updated");

                } catch (ClassNotFoundException e) {
                    throw new RuntimeException(e);
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                } catch (NoSuchElementException e) {
                    throw new RuntimeException(e);
                } finally {
                    reader.close();
                    stmt.close();
                    con.close();
                }
            }
            else if (choice==2){
                Scanner objBook = new Scanner(System.in);
                System.out.println("Enter the Book Name To add:");
                cse.add(objBook.next().toLowerCase());

            }
            else if (choice==3){
                Scanner objBook = new Scanner(System.in);
                System.out.println("Enter the Book Name To add:");
                civl.add(objBook.next().toLowerCase());

            }
            else if (choice==4) {
                break;
            }
        }
    }
    public void issueBook() {
        Scanner objIssueBook = new Scanner(System.in);
        int issueSelection = 0;
        while (issueSelection!=4) {
            System.out.println("1.Electronics\n2.Computers\n3.Civil\n4.Main Menu");
            System.out.print("Please Enter the department to Issue the Book:");
            issueSelection = objIssueBook.nextInt();
            if (issueSelection == 1) {
                Scanner issueBookName = new Scanner(System.in);
                System.out.println("Enter The Book Name:");
                ece.remove(ece.indexOf(issueBookName.next()));
                issuedBookCollection.add(issueBookName.next());

            } else if (issueSelection == 2) {
                Scanner issueBookName = new Scanner(System.in);
                System.out.println("Enter The Book Name:");
                int index=cse.indexOf(issueBookName.next().toLowerCase());
                cse.remove(index);
                issuedBookCollection.add(issueBookName.next().toLowerCase());

            } else if (issueSelection == 3) {
                Scanner issueBookName = new Scanner(System.in);
                System.out.println("Enter The Book Name:");
                int index=civl.indexOf(issueBookName.next().toLowerCase());
                civl.remove(index);
                issuedBookCollection.add(issueBookName.next().toLowerCase());

            } else if (issueSelection == 4) {
                break;
            }
        }
    }

    public void returnBook(){
        Scanner objReturnBook = new Scanner(System.in);
        int returnSelection = 0;
        while (returnSelection!=4){
            System.out.println("1.Electronics\n2.Computers\n3.Civil\n4.Main Menu");
            System.out.print("Please Enter the department to Return the Book:");
            returnSelection = objReturnBook.nextInt();
            if (returnSelection==1){
                Scanner returnBookName = new Scanner(System.in);
                System.out.println("Enter The Book Name To Return:");
                ece.add(returnBookName.next().toLowerCase());
                issuedBookCollection.remove(returnBookName.next().toLowerCase());

            } else if (returnSelection==2) {
                System.out.println("Enter The Book Name To Return:");
                Scanner returnBookName = new Scanner(System.in);
                cse.add(returnBookName.next().toLowerCase());
                issuedBookCollection.remove(returnBookName.next().toLowerCase());

            } else if (returnSelection==3) {
                System.out.println("Enter The Book Name To Return:");
                Scanner returnBookName = new Scanner(System.in);
                civl.add(returnBookName.next().toLowerCase());
                issuedBookCollection.remove(returnBookName.next().toLowerCase());

            }
                else if (returnSelection==4){
                    break;
            }
        }
        }
    }
