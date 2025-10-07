import java.util.Date;
import java.util.Scanner;

/**
 * This class is used for the implementation of the Guilds in Proj1
 *
 * @author Kaloyan Doychinov
 * @version 07/10/25
 */


public class Project1 {
    public static final int MEMBER_FEE = 25;
    public static final int GUILD_FEE = 1000;
    public static final int RECEIPT_WIDTH = 40;

    public static void main(String[] args) {
        //follow the instructions in the comments EXACTLY
        //write the line of code the comment asks for UNDER the comment
        //do NOT delete the comments


        //1. print the welcome statement
        System.out.println("Welcome to the Ankh-Morpork Patrician's Office - Department of Guild Accounting");

        //2. declare a scanner object; 3. you'll have to import the Scanner class too
        Scanner keyboard = new Scanner(System.in);

        //4. on the line after this comment, create an object of type Guild, name the object guild
        //   replace the null with a call to the standard constructor
        Guild guild = new Guild();

        //5. ask the user what guild they're making a payment for
        System.out.print("What guild are you registering? ");

        //6. read the input into a variable named guildName
        String guildName = keyboard.nextLine();

        //7. trim the guildName of leading and trailing spaces
        guildName = guildName.trim();
        if (guildName.isEmpty()) {
            System.out.println("Come back when you have a valid name. Goodbye.");
            System.exit(-1);
        }

        //8. make guildName properly capitalized 
        guildName = ("" + guildName.charAt(0)).toUpperCase() + guildName.substring(1).toLowerCase();

        //9. ask the user how many members are in the guild
        System.out.print("How many members does the Guild of Seamstresses have? ");

        //10. read the input into a variable named memberNumber 
        int memberNumber = keyboard.nextInt();
        if (memberNumber < 1) {
            System.out.println("Come back when you have enough members (at least 1). Goodbye.");
            System.exit(-1);
        }

        //11. calculate the minimum amount of money the user needs to deposit to register the guild
        //    the value should be saved in a variable named minPayment 
        double minPayment = GUILD_FEE + memberNumber * MEMBER_FEE;

        //12. tell the user the minimum amount of money they have to deposit
        System.out.printf("The minimum payment to register the Guild of Seamstresses is $%,.2f%n", minPayment);

        //13. ask the user how much money they'd like to deposit
        System.out.print("How much would you like to deposit? ");

        //14. read the user input into a variable named deposit 
        double deposit = keyboard.nextDouble();

        //do NOT alter or move this code
        //if the user is not depositing enough money
        if (deposit < minPayment) {
            System.out.println("Come back when you have enough money. Goodbye.");
            System.exit(-1); // exits the program with error code -1
        }

        //15. for the guild object, set its name to guildName
        guild.setName(guildName);

        //16. for the guild object, set its members to memberNumber
        guild.setMembers(memberNumber);

        //17. for the guild object, set its balance to the deposited money minus the required fees 
        guild.setBalance(deposit - minPayment);

        //18. move to the printReceipt method below and finish it according to the directions
        printReceipt(guild); // do not alter this line of code
    }

    /* finish this method! <-----------
     *
     * printReceipt - this method prints the formatted receipt
     *
     * @param Guild guild - the Guild object with values set in the main
     * @return nothing
     */
    public static void printReceipt(Guild guild) {
        //19. all the user entered data read in the main should be in the object called guild 
        //    that is passed into this method when the method is called
        //    use getter methods from the Guild class with the mail object to print the formatted receipt
        //    the receipt is 40 characters wide
        Date now = new Date();
        System.out.println("-".repeat(RECEIPT_WIDTH));
        System.out.printf("| %-36s |%n", now);
        System.out.printf("| %-36s |%n", "");
        System.out.printf("| %-10s %-25s |%n", "NEW GUILD:", guild.getName().substring(0,25));
        System.out.printf("| %-10s %-25s |%n", "MEMBERS:", guild.getMembers());
        System.out.printf("| %-10s $ %,-23.2f |%n", "BALANCE:", guild.getBalance());
        System.out.printf("| %-36s |%n", "");
        System.out.printf("| %-36s |%n", "Approved by A-M Patrician's Office");
        System.out.println("-".repeat(RECEIPT_WIDTH));


        //20. delete the 3 instructions below when you're done
        System.out.print("Receipt is printed here. Here is what is being shipped ");
        System.out.println(guild.getName());
        System.out.println("Delete these instructions when done");

    }
}