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

    public static void main(String[] args) {
        launch(args);
    }

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
        int[][] imageArray1 = readImage(image1, pixelReader1);
        int[][] imageArray2 = readImage(image2, pixelReader2);
        int[][] imageArray3 = readImage(image3, pixelReader3);

        //find out the overlapping row between image 1 and the first row of image 2
        //that would be the last row from image 1 included in the final image
        int heightLimit1 = findOverlap(imageArray1, imageArray2);

        if (heightLimit1 < 0) {
            outputError(primaryStage, root, "Image 1 & 2 don't have an overlap");
            return;
        }

        //find out the overlapping row between image 2 and the first row of image 3
        //that would be the last row from image 2 included in the final image
        int heightLimit2 = findOverlap(imageArray2, imageArray3);

        if (heightLimit2 < 0) {
            outputError(primaryStage, root, "Image 2 & 3 don't have an overlap");
            return;
        }

        //--------------DO NOT ALTER CODE ABOVE THIS LINE-----------------------

        //3. get width of the image (all three have the same width)
        //DO NOT CHANGE THE VARIABLE NAME
        //replace 100 with your value
        if (imageArray1.length != imageArray2.length && imageArray2.length != imageArray3.length) {
            outputError(primaryStage, root, "Images must have the same width!");
            return;
        }

        int width = imageArray1.length;

        //4. get the height of the images - i don't see a reason for that
        int cursorHeight = 0;
        int img3h = imageArray3[0].length;

        //5. calculate the height of the combined image (replace 100 with your formula)
        //DO NOT CHANGE THE VARIABLE NAME
        int height = heightLimit1 + heightLimit2 + img3h;

        //prepare to write image
        WritableImage writableImage = new WritableImage(width, height);
        PixelWriter pixelWriter = writableImage.getPixelWriter();

        //6. write (partial) image 1
        //you will need to use .setArgb on pixelWriter
        //figure out where to stop adding rows from image 1 to the combined image
        cursorHeight = writePartialImage(pixelWriter, imageArray1, cursorHeight, heightLimit1);

        //7. write (partial) image 2
        //you will need to use .setArgb on pixelWriter
        //figure out the starting coordinates in the combined image to write image 2
        //figure out where to stop adding rows from image 2 to the combined image
        cursorHeight = writePartialImage(pixelWriter, imageArray2, cursorHeight, heightLimit2);

        //8. write (entire) image 3
        //you will need to use .setArgb on pixelWriter
        //figure out the starting coordinates in the combined image to write image 3
        writePartialImage(pixelWriter, imageArray3, cursorHeight, img3h);

        //--------------DO NOT ALTER start METHOD CODE BELOW THIS LINE----------
        //show
        ImageView finalImageView = new ImageView(writableImage);
        root.getChildren().add(finalImageView);
        System.out.println("H: " + height); //for grading purposes
        Scene scene = new Scene(root);
        primaryStage.setTitle("Havelock Vetinari");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * writePartialImage - helper method to write partial images on the canvas
     *
     * @param pixelWriter   PixelWriter - object used to write on the canvas
     * @param imgArr        int[][] - pixel array of the image
     * @param startPos      int - starting position on canvas
     * @param partialHeight int - cut the image at given row
     * @return new cursor position
     */
    private int writePartialImage(PixelWriter pixelWriter, int[][] imgArr, int startPos, int partialHeight) {
        for (int i = 0; i < imgArr.length; ++i) {
            for (int j = 0; j < partialHeight; ++j) {
                pixelWriter.setArgb(i, j + startPos, imgArr[i][j]);
            }
        }

        return startPos + partialHeight;
    }

    /**
     * outputError - helper method to print error ui
     *
     * @param primaryStage - Stage
     * @param root         - StackPane
     * @param err          - String - error message
     */
    private void outputError(Stage primaryStage, StackPane root, String err) {
        Text text = new Text(err);
        root.getChildren().add(text);
        Scene scene = new Scene(root);
        primaryStage.setTitle("Critical Error");
        primaryStage.setScene(scene);
        primaryStage.setHeight(200);
        primaryStage.setWidth(400);
        primaryStage.show();
    }

    /* readImage - read RBG data into a two dimensional integer array and return array
     * input: Image image - the Image variable to get width and height of the image from
     *        PixelReader - the PixelReader variable to get the RGB numbers from
     *                      use .getArgb( x, y ) where x and y are the pixel coordinates
     * return: int[][] - the array with the RGB data
     */
    private int[][] readImage(Image image, PixelReader pixelReader) {
        //1. implement this method
        //get height and weight
        //create int[][] array of that size
        //read RGB data from pixelReader and add to the array
        //return the array (replace "null" with your array
        int h = (int) image.getHeight();
        int w = (int) image.getWidth();

        int[][] imgArr = new int[w][h];

        for (int i = 0; i < w; ++i) {
            for (int j = 0; j < h; ++j) {
                imgArr[i][j] = pixelReader.getArgb(i, j);
            }
        }

        return imgArr;
    }

    /* findOverlap - find the overlapping row between two images using their RGB data arrays
     * input: int[][] imageArray1 - the RGB data for image 1 - a row in image 1 is the same as row 0 of image 2,
     *                              so they have the same RGB numbers in the entire row
     *        int[][] imageArray2 - the RGB data for image 2. its row zero is an exact match to a row in image 1
     * return: int - the row number in image 1 that matches row 0 in image 2
     */
    private int findOverlap(int[][] imageArray1, int[][] imageArray2) {
        //2. implement this method
        //go through the array for image 1 row by row and find the row number that matched row 0 in image 2
        //return the row number (replace 0 with the row you found)

        for (int j = 0; j < imageArray1[0].length; ++j) {
            for (int i = 0; i < imageArray1.length; ++i) {
                if (imageArray1[i][j] != imageArray2[i][0]) break;
                else if (i == imageArray1.length - 1 && imageArray1[i][j] == imageArray2[i][0])
                    return j;
            }
        }

        return -1;
    }
}
