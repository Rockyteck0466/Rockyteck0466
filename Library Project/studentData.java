import java.util.ArrayList;

public class studentData {
    String name;
    int dob;
    int student_id;
    String stream;


    public void setData(String name,int dob,int student_id,String stream){
        this.name=name;
        this.dob=dob;
        this.student_id=student_id;
        this.stream=stream;
    }
    public void viewData(){
        System.out.println("Student Name:"+name);
        System.out.println("Student DOB:"+dob);
        System.out.println("Student Id:"+student_id);
        System.out.println("Student Stream:"+stream);
    }
}
