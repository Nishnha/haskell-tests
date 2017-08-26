public class HelloWorld {

    private static int age = 19;

    public static void main (String[] args) {
        System.out.println("Hello World!");
        System.out.println("My age is " + age);
        System.out.println("My name is " + name("Nish", "Sinha"));
    }


    public static String name(String first, String last) {
        return first + " " + last;

        
    }

}
