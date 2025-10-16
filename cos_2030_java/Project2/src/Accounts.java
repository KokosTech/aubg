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
        taxFund = 0.0;
        donationFund = 0.0;
        darkFund = 0.0;
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

    /**
     * getTaxFund - this method returns the current amount of money in the Tax Fund
     *
     * @return double taxFund
     */
    public double getTaxFund() {
        return taxFund;
    }

    /**
     * getDonationFund - this method returns the current amount of money in the Donation Fund
     *
     * @return double donationFund
     */
    public double getDonationFund() {
        return donationFund;
    }

    /**
     * getDarkFund - this method returns the current amount of money in the Dark Fund
     *
     * @return double darkFund
     */
    public double getDarkFund() {
        return darkFund;
    }

    // it feels so illegal to use $ as a variable name ;-;

    /**
     * addToTaxFund - this method adds a specified amount to the Tax Fund
     *
     * @param $ double - amount to add to the Tax Fund
     * @return nothing
     */
    public void addToTaxFund(double $) {
        if (amountChecks($)) return;
        this.taxFund += $;
    }

    /**
     * addToDonationFund - this method adds a specified amount to the Donation Fund
     *
     * @param $ double - amount to add to the Donation Fund
     * @return nothing
     */
    public void addToDonationFund(double $) {
        if (amountChecks($)) return;
        this.donationFund += $;
    }

    /**
     * addToDarkFund - this method adds a specified amount to the Dark Fund
     *
     * @param $ double - amount to add to the Dark Fund
     * @return nothing
     */
    public void addToDarkFund(double $) {
        if (amountChecks($)) return;
        this.darkFund += $;
    }


    /**
     * allFunds - this method returns a sum of all funds
     *
     * @return double - sum of all funds
     */
    public double allFunds() {
        return this.taxFund + this.donationFund + this.darkFund;
    }
}
