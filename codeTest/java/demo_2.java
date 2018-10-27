import java.util.*;

interface FuncInterface 
{ 
    void abstractFun(int x); 
  
    default void normalFun() 
    { 
       System.out.println("Hello"); 
    } 
} 

class test{

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        System.out.println(a);

        FuncInterface fobj = (int x)->System.out.println(2*x);
    }
}

