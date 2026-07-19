public class Logical_Operator{
    public static void main(String[] args){
        int age=20;
        boolean hasID=true;
        if(age>=18 && hasID){
            System.out.println("Allowed");
        }else{
            System.out.println("Not allowed");
        }
    }
}

public class Logical_Operator{
    public static void main(String[] args){
        boolean isHoliday=false;
        boolean isSunday=true;
        if (isHoliday ||  isSunday){
            System.out.println("Enjoy your day!");
        }else{
            System.out.println("Go to Work");
        }
    }
}

public class Logical_Operator{
    public static void main(String[] args){
        boolean isRainy=false;
        if(!isRainy){
            System.out.println("Let's go for a walk.");
        }else{
            System.out.println("Stay at home.");
        }
    }
}

public class Logical_Operator{
    public static void main(String[] args){
        int marks=85;
        boolean attendance=true;
        if (marks>=40 && attendance){
            System.out.println("pass");
        }else{
            System.out.println("Fail");
        }
        }
    }
