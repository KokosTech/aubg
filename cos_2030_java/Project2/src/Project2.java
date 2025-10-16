import java.util.Date;
import java.util.Scanner;

/**
 * This class is used for the implementation of Project 2 HW for COS2030 Java
 *
 * @author Kaloyan Doychinov
 * @version 16/10/25
 */
public class Project2 {
    private static final Scanner keyboard = new Scanner(System.in);

        public static final int TAX = 100;
        public static final int ASSASSINS_PRICE = 60;
        public static final int SEAMSTRESSES_PRICE = 12;
        public static final int THIEVES_PRICE = 25;


    /**
     * printReceipt - this method formats and prints the receipt for the given transaction
     *
     * @param data String - data to be printer
     * @return nothing
     */
    private static void printReceipt(String data) {
        Date now = new Date();
        System.out.printf("%n----- RECEIPT # %03d %s %s%n", (int) (Math.random() * 1000), now, "-".repeat(24));
        System.out.printf("  %s%n", data);
        System.out.println("-".repeat(74));
        System.out.println();
    }

    public static void main(String[] args) {
        Accounts accounts = new Accounts();

        //method will repeat calling the go() method for as long as 
        //go returns true
        //once the user wants to quit, go will return false and the program will end
        boolean go_on = true;
        while (true) {
            printTotals(accounts);
            if (!go_on) {
                System.out.println("We're closed for the day, goodbye.");
                break;
            }
            System.out.println("Next...");
            go_on = go(accounts);
        }
    } //DO NOT ALTER THE MAIN METHOD

    public static boolean go(Accounts accounts) {
        /*== guild name ==*/

        System.out.print("Which guild are you making a payment for today? ");
        String guildName = keyboard.nextLine().trim();

        char firstLetter = guildName.toUpperCase().charAt(0);
        guildName = firstLetter + guildName.substring(1).toLowerCase();

        if (firstLetter == 'Q') {
            System.out.println("We're closed for the day, goodbye.");
            return false;
        }

        /*== payment amount ==*/

        System.out.print("What was the amount of today's payment? ");
        double payment = keyboard.nextDouble();
        keyboard.nextLine();

        if (payment <= 0) {
            System.out.println("Invalid payment amount. Yell at someone. Goodbye.");
            return true;
        }

        /*== payment kind name ==*/

        System.out.print("What kind of payment - tax or donation? ");
        String paymentType = keyboard.nextLine().trim().toUpperCase();

        // check if the guild is within the valid guild - ass, seams, thief
        if (!guildName.equalsIgnoreCase("assassins") && !guildName.equalsIgnoreCase("seamstresses") && !guildName.equalsIgnoreCase("thieves")) {
            printReceipt(
                    "To register a new guild, appear in person in front of the Patrician.\n" +
                            "  We also lost your payment, so please make it again when you register."
            );
            accounts.addToDarkFund(payment);
            return true;
        }

        /*== process payment ==*/

        String receiptToBePrinted;
        switch (paymentType) {
            case "TAX":
                if (payment < TAX) {
                    accounts.addToDonationFund(payment);
                    receiptToBePrinted = String.format("$ %,.2f is not enough for tax credit.%n  " +
                            "Thank you for the donation, Guild of %s", payment, guildName);
                } else {
                    double donation = payment % TAX;
                    double taxPayment = payment - donation;
                    int months = (int) taxPayment / TAX;

                    accounts.addToTaxFund(taxPayment);
                    receiptToBePrinted = String.format("Guild of %s tax payment of $ %,.2f confirmed ", guildName, taxPayment);
                    receiptToBePrinted +=
                            "(" + ((months > 11) ? (months / 12) + " years" : "") // check if there are years in the months
                            + ((months > 11 && months % 12 != 0) ? " " : "")  // check if year and month have to be present
                            + ((months % 12 != 0) ? (months % 12) + " months" : "") + ")."; // check if there should bn run


                    if (donation > 0) {
                        accounts.addToDonationFund(donation);
                        receiptToBePrinted += String.format("%n  We're adding the residual $ %,.2f to the donation fund, thank you.", donation);
                    }
                }
                break;
            case "DONATION":
                String items = "";
                accounts.addToDonationFund(payment);
                int numberOf = 0;
                switch (guildName) {
                    case "Assassins":
                        items = "murders";
                        numberOf = (int) (payment / ASSASSINS_PRICE);
                        break;
                    case "Seamstresses":
                        items = "garments";
                        numberOf = (int) (payment / SEAMSTRESSES_PRICE);
                        break;
                    case "Thieves":
                        items = "robberies";
                        numberOf = (int) (payment / THIEVES_PRICE);
                        break;
                }

                receiptToBePrinted = String.format("Guild of %s, thank you for your donation,%n  ", guildName);
                receiptToBePrinted += numberOf < 1 ? "however, it's not enough for an item of credit."
                        : String.format("you have received credit of %d %s.", numberOf, items);
                break;
            default:
                receiptToBePrinted = String.format("Guild of %s, we're sorry, we don't take that kind of payment,%n  " +
                        "so we lost it. Please make the payment again tomorrow, goodbye.", guildName);
                accounts.addToDarkFund(payment);
        }
        if (!receiptToBePrinted.isEmpty()) printReceipt(receiptToBePrinted);
        return true;
    }

    /**
     * printTotals - prints total amounts in each accounts
     *
     * @param accounts Accounts
     */
    public static void printTotals(Accounts accounts) {
        //WRITE YOUR CODE HERE
        //finish the prints
        System.out.println("-".repeat(27));
        System.out.printf("%-15s$ %,10.2f%n", "Tax fund:", accounts.getTaxFund());
        System.out.printf("%-15s$ %,10.2f%n", "Donation fund:", accounts.getDonationFund());
        System.out.printf("%-15s$ %,10.2f%n", "Dark fund:", accounts.getDarkFund());
        System.out.printf("%-15s$ %,10.2f%n%n", "ALL FUNDS:", accounts.allFunds());
    }
}
