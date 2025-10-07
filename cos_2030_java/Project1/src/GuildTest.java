/** This class tests your Guild class - execute its main method
 *  
 *  @author  E.Lovellette
 *  @version 1/22/2023
 */ 
public class GuildTest {
    public static void main( String[] args ) {
        Guild g = new Guild();
        assert g.getName().equals( "" ) : "standard constructor name value fail";
        assert g.getMembers() - 0 == 0 : "standard constructor members value fail";
        assert g.getBalance() - 0.0 < 0.001 : "standard constructor balance value fail";
        System.out.println( "standard constructor is correct" );
        
        g.setName( "Thieves" );
        g.setMembers( 5 );
        g.setBalance( 1234.56 - 1000 - 5 * 25 );
        
        assert g.getName().equals( "Thieves" ) : "get or set name fail";
        System.out.println( "getter and setter for name instance variable are correct" );

        assert g.getMembers() - 5 == 0 : "get or set members fail";
        System.out.println( "getter and setter for members instance variable are correct" );
        
        assert g.getBalance() - 109.56 < 0.001 : "get or set balance fail";
        System.out.println( "getter and setter for balance instance variable are correct" );
        
        System.out.println( "All tests passed." );
    }
}
