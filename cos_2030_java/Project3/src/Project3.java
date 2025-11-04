import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import static java.lang.System.exit;

/**
 * This class is used for the implementation of Project 3 HW for COS2030 Java
 *
 * @author Kaloyan Doychinov
 * @version 04/11/25
 */
public class Project3 {
    private static final int SEAMSTRESSES_LIMIT = 180;
    private static final int THIEVES_LIMIT = 60;
    private static final int ASSASSINS_LIMIT = 30;

    private static final int DAYS = 30;
    private static final int MAX_DAY = 10;

    /**
     * openFile - this helper method moves the program's logic for opening files
     *
     * @param filename String - path to file
     * @return Scanner - open file stream
     */
    private static Scanner openFile(String filename) {
        try {
            File sff = new File(filename);
            return new Scanner(sff);
        } catch (FileNotFoundException e) {
            System.out.println("The file " + filename + " does not exist. Exiting...");
            exit(-1);
            return null;
        }
    }

    /**
     * stringFancyNumber - this helper method is used for formatting the fancy st/nd/rd/th numbers
     *
     * @param num int - number to be converted to fancy text
     * @return String - returns a fancy number as a text
     */
    private static String stringFancyNumber(int num) {
        String num_str = "" + num;

        if (num % 10 == 1 && num % 100 != 11) {
            num_str += "st";
        } else if (num % 10 == 2 && num % 100 != 12) {
            num_str += "nd";
        } else if (num % 10 == 3 && num % 100 != 13) {
            num_str += "rd";
        } else {
            num_str += "th";
        }

        return num_str + ":";
    }

    /**
     * _printApproved - this helper method conveys the actual logic and formatting behind printing a guild's approved credit if necessary
     *
     * @param guild      Guild - guild's credit info
     * @param crApproved int - amount of approved credit for the day
     * @param iter       int - day of the iteration
     * @param printIter  boolean - flag for printing the day (only for the first one)
     * @return nothing
     */
    private static void _printApproved(Guild guild, int crApproved, int iter, boolean printIter) {
        int totalApproved = guild.getApproved();
        boolean multiple = crApproved > 1;
        boolean maxed = false;

        String item = "";

        switch (guild.getName().toUpperCase()) {
            case "SEAMSTRESSES":
                item = multiple ? "garments" : "garment";
                if (totalApproved == SEAMSTRESSES_LIMIT) maxed = true;
                break;
            case "THIEVES":
                item = multiple ? "robberies" : "robbery";
                if (totalApproved == THIEVES_LIMIT) maxed = true;
                break;
            case "ASSASSINS":
                item = multiple ? "murders" : "murder";
                if (totalApproved == ASSASSINS_LIMIT) maxed = true;
                break;
            default:
                System.out.println("What are you doing???");
                exit(-2);
        }

        System.out.printf("%-8s%-12s %-2d %-9s approved ", (printIter ? stringFancyNumber(iter) : ""), guild.getName(), crApproved, item);
        if (maxed) {
            System.out.printf("(maxed out at %d total approved)%n", totalApproved);
        } else {
            System.out.printf("(%-3d total approved, %-2d not yet approved)%n", totalApproved, guild.getCarry());
        }
    }

    /**
     * printApproved - this helper wrapper method is used to call _printApproved for each guild
     *
     * @param seamstresses Guild - seamstresses' credit info
     * @param thieves      Guild - thieves' credit info
     * @param assassins    Guild - assassins' credit info
     * @param scrApproved  int - amount of approved credit for the day for seamstresses
     * @param tcrApproved  int - amount of approved credit for the day for thieves
     * @param acrApproved  int - amount of approved credit for the day for assassins
     * @param iter         int - day of the iteration
     * @return nothing
     */
    private static void printApproved(Guild seamstresses, Guild thieves, Guild assassins, int scrApproved, int tcrApproved, int acrApproved, int iter) {
        boolean printed = false;

        if (scrApproved > 0) {
            _printApproved(seamstresses, scrApproved, iter, !printed);
            printed = true;
        }
        if (tcrApproved > 0) {
            _printApproved(thieves, tcrApproved, iter, !printed);
            printed = true;
        }
        if (acrApproved > 0) {
            _printApproved(assassins, acrApproved, iter, !printed);
        }
    }

    //DO NOT ALTER THE MAIN METHOD
    public static void main(String[] args) {
        Guild seamstresses = new Guild("Seamstresses");
        Guild assassins = new Guild("Assassins");
        Guild thieves = new Guild("Thieves");

        //COMMENT IN AND OUT ONE CALL TO distributeCredits AT A TIME
        //read files and distribute credits
        distributeCredits(seamstresses, thieves, assassins, "seamstresses.txt", "thieves.txt", "assassins.txt");
//        distributeCredits(seamstresses, thieves, assassins, "seamstresses2.txt", "thieves2.txt", "assassins2.txt");

        //print report when all mail coaches have been dispatched
        printTotal(seamstresses, assassins, thieves);
    } //DO NOT ALTER THE MAIN METHOD

    /**
     * distributeCredits - the actual logic behind this homework, the algorithm for distributing and printing the credits
     *
     * @param seamstresses Guild - seamstresses' credit info
     * @param thieves      Guild - thieves' credit info
     * @param assassins    Guild - assassins' credit info
     * @param sFN          String - filename for the seamstresses credit requests
     * @param tFN          String - filename for the thieves credit requests
     * @param aFN          String - filename for the assassins credit requests
     * @return nothing
     */
    public static void distributeCredits(Guild seamstresses, Guild thieves, Guild assassins, String sFN, String tFN, String aFN) {
        Scanner sf = openFile(sFN);
        Scanner tf = openFile(tFN);
        Scanner af = openFile(aFN);

        for (int i = 1; i <= DAYS && (sf.hasNext() && tf.hasNext() && af.hasNext()) && (sf.hasNextInt() && tf.hasNextInt() && af.hasNextInt()); ++i) {
            if (Guild.getAllCredits() >= 270) {
                System.out.printf("%-8sNo credits.%n", stringFancyNumber(i));
                continue;
            }

            int accDayCredits = 0;
            int scr = Math.max(sf.nextInt(), 0)  + seamstresses.getCarry();
            int tcr = Math.max(tf.nextInt(), 0) + thieves.getCarry();
            int acr = Math.max(af.nextInt(), 0) + assassins.getCarry();

            int scr_approved = 0;
            int tcr_approved = 0;
            int acr_approved = 0;

            seamstresses.addCarry(-seamstresses.getCarry());
            thieves.addCarry(-thieves.getCarry());
            assassins.addCarry(-assassins.getCarry());

            if (scr + tcr + acr == 0) {
                System.out.printf("%-8sNo credits.%n", stringFancyNumber(i));
                continue;
            }

            while (accDayCredits < MAX_DAY && (scr > 0 || tcr > 0 || acr > 0)) {
                boolean cr = false;
                if (seamstresses.getApproved() < SEAMSTRESSES_LIMIT && scr > 0) {
                    seamstresses.addCredits(1);
                    ++accDayCredits;
                    ++scr_approved;
                    --scr;
                    cr = true;
                }

                if (accDayCredits < MAX_DAY && thieves.getApproved() < THIEVES_LIMIT && tcr > 0) {
                    thieves.addCredits(1);
                    ++accDayCredits;
                    ++tcr_approved;
                    --tcr;
                    cr = true;
                }

                if (accDayCredits < MAX_DAY && assassins.getApproved() < ASSASSINS_LIMIT && acr > 0) {
                    assassins.addCredits(1);
                    ++accDayCredits;
                    ++acr_approved;
                    --acr;
                    cr = true;
                }

                if (!cr) break;
            }

            seamstresses.addCarry(scr);
            thieves.addCarry(tcr);
            assassins.addCarry(acr);

            printApproved(seamstresses, thieves, assassins, scr_approved, tcr_approved, acr_approved, i);
        }

        sf.close();
        tf.close();
        af.close();
    }

    //DO NOT ALTER THE printTotal METHOD
    public static void printTotal(Guild seamstresses, Guild assassins, Guild thieves) {
        //DO NOT ALTER THIS METHOD
        System.out.printf("%nTotal credits this month: %d (%d garments, %d robberies, %d murders)%n",
                Guild.getAllCredits(), seamstresses.getApproved(), thieves.getApproved(), assassins.getApproved());

    }//DO NOT ALTER THE printTotal METHOD
}
