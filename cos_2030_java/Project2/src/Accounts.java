/**
 * This class is used for managing the accounts of the guilds
 *
 * @author Kaloyan Doychinov
 * @version 16/10/25
 */
public class Accounts {
    private double taxFund;
    private double donationFund;
    private double darkFund;

    /**
     * Standard constructor for objects of class Guild
     */
    Accounts() {
        taxFund = 0;
        donationFund = 0;
        darkFund = 0;
    }

    /**
     * amountChecks - checks for valid amount input before adding to account
     *
     * @param amount double
     * @return boolean, weather account's been input invalid (true) or valid (false) sum
     */
    private boolean amountChecks(double amount) {
        if (amount < 0) {
            System.out.println("What are you doing? Stealing?");
            return true;
        }

        return false;
    }

    public double getTaxFund() {
        return taxFund;
    }

    public double getDonationFund() {
        return donationFund;
    }

    public double getDarkFund() {
        return darkFund;
    }

    // it feels so illegal to use $ as a variable name ;-;

    public void addToTaxFund(double $) {
        if (amountChecks($)) return;
        this.taxFund += $;
    }

    public void addToDonationFund(double $) {
        if (amountChecks($)) return;
        this.donationFund += $;
    }

    public void addToDarkFund(double $) {
        if (amountChecks($)) return;
        this.darkFund += $;
    }

    public double allFunds() {
        return this.taxFund + this.donationFund + this.darkFund;
    }
}
