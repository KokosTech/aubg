import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.image.PixelReader;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class Project4 extends Application {

    @Override
    public void start(Stage primaryStage) {
        StackPane root = new StackPane();
        //three overlapping images in the right order, width is the same, height varies
        Image image1 = new Image( "v1.png" );
        Image image2 = new Image( "v2.png" );
        Image image3 = new Image( "v3.png" );

        //set up to read image pixels
        PixelReader pixelReader1 = image1.getPixelReader();
        PixelReader pixelReader2 = image2.getPixelReader();
        PixelReader pixelReader3 = image3.getPixelReader();
        
        //read the RGB data of each image for comparison
        int[][] imageArray1 = readImage( image1, pixelReader1 );      
        int[][] imageArray2 = readImage( image2, pixelReader2 );
        int[][] imageArray3 = readImage( image3, pixelReader3 );
              
        //find out the overlapping row between image 1 and the first row of image 2 
        //that would be the last row from image 1 included in the final image
        int heightLimit1 = findOverlap( imageArray1, imageArray2 );
        //find out the overlapping row between image 2 and the first row of image 3 
        //that would be the last row from image 2 included in the final image
        int heightLimit2 = findOverlap( imageArray2, imageArray3 );
        
        //--------------DO NOT ALTER CODE ABOVE THIS LINE-----------------------
        
        //3. get width of the image (all three have the same width)
        //DO NOT CHANGE THE VARIABLE NAME
        //replace 100 with your value
        int width = 100;
        
        //4. get the height of the images
       
        
        //5. calculate the height of the combined image (replace 100 with your formula)
        //DO NOT CHANGE THE VARIABLE NAME
        int height = 100;
        
        
        //prepare to write image
        WritableImage writableImage = new WritableImage( width, height );
        PixelWriter pixelWriter = writableImage.getPixelWriter();
        
        //6. write (partial) image 1
        //you will need to use .setArgb on pixelWriter
        //figure out where to stop adding rows from image 1 to the combined image
                
        //7. write (partial) image 2
        //you will need to use .setArgb on pixelWriter
        //figure out the starting coordinates in the combined image to write image 2 
        //figure out where to stop adding rows from image 2 to the combined image
        
        //8. write (entire) image 3
        //you will need to use .setArgb on pixelWriter
        //figure out the starting coordinates in the combined image to write image 3
        
         
        //--------------DO NOT ALTER start METHOD CODE BELOW THIS LINE----------
        //show
        ImageView finalImageView = new ImageView( writableImage );
        root.getChildren().add(finalImageView);
        System.out.println( "H: " + height ); //for grading purposes
        Scene scene = new Scene(root);
        primaryStage.setTitle( "Havelock Vetinari" );
        primaryStage.setScene(scene);
        primaryStage.show();
    }
        
 
    /* readImage - read RBG data into a two dimensional integer array and return array
     * input: Image image - the Image variable to get width and height of the image from
     *        PixelReader - the PixelReader variable to get the RGB numbers from
     *                      use .getArgb( x, y ) where x and y are the pixel coordinates 
     * return: int[][] - the array with the RGB data 
     */ 
    private int[][] readImage( Image image, PixelReader pixelReader ) {
        //1. implement this method
        //get height and weight
        //create int[][] array of that size
        //read RGB data from pixelReader and add to the array
        //return the array (replace "null" with your array      
        
        return null;
    }
    
    /* findOverlap - find the overlapping row between two images using their RGB data arrays
     * input: int[][] imageArray1 - the RGB data for image 1 - a row in image 1 is the same as row 0 of image 2, 
     *                              so they have the same RGB numbers in the entire row
     *        int[][] imageArray2 - the RGB data for image 2. its row zero is an exact match to a row in image 1
     * return: int - the row number in image 1 that matches row 0 in image 2
     */
    private int findOverlap( int[][] imageArray1, int[][] imageArray2 ) {
        //2. implement this method
        //go through the array for image 1 row by row and find the row number that matched row 0 in image 2
        //return the row number (replace 0 with the row you found)
        return 0;  
    }
    
    public static void main(String[] args) {
        launch(args);
    }  
}
