package doychinov.kaloyan.project6;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.*;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.FlowPane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

import static java.lang.System.exit;


public class TIMSApplication extends Application {
    private Stage stage;
    private BorderPane bp;
    private FlowPane fp;
    private ArrayList<Button> buttons;

    private Image originalImage;
    private int[][] originalImageArray;

    private int h = 0;
    private int w = 0;

    public static void main(String[] args) {
        launch();
    }

    private void initButtons() {
        Button flipButton = new Button("Diagonal Flip");
        flipButton.setOnAction(e -> flip(originalImageArray));
        this.buttons.add(flipButton);

        Button grayscaleButton = new Button("Grayscale");
        grayscaleButton.setOnAction(e -> grayscale());
        this.buttons.add(grayscaleButton);

        Button mosaicButton = new Button("Mosaic");
        mosaicButton.setOnAction(e -> mosaic());
        this.buttons.add(mosaicButton);

        Button overlayButton = new Button("Add flair");
        overlayButton.setOnAction(e -> overlay());
        this.buttons.add(overlayButton);

        Button originalButton = new Button("Original");
        originalButton.setOnAction(e -> showOriginal());
        this.buttons.add(originalButton);

        Button closeButton = new Button("Exit");
        closeButton.setOnAction(e -> closeProgram());
        this.buttons.add(closeButton);
    }

    private void overlay() {
        Image overlay = new Image(getClass().getResource("overlay.png").toExternalForm());
        PixelReader pixelReader = overlay.getPixelReader();

        int[][] newImageArray = readImage(originalImage, originalImage.getPixelReader());

        for (int i = 0; i < this.w; ++i) {
            for (int j = 0; j < this.h; ++j) {
                Color color = pixelReader.getColor(i, j);

                if (color.getRed() != 1.0 && color.getGreen() != 1.0 && color.getBlue() != 1.0) {
                    newImageArray[i][j] = pixelReader.getArgb(i, j);
                }
            }
        }

        handleImageChange(newImageArray);
    }

    private void grayscale() {
        Color[][] newImageArray = new Color[this.w][this.h];

        for (int i = 0; i < this.w; ++i) {
            for (int j = 0; j < this.h; ++j) {
                Color color = originalImage.getPixelReader().getColor(i, j);
                double calc = (color.getRed() + color.getGreen() + color.getBlue()) / 3;
                newImageArray[i][j] = new Color(calc, calc, calc, 1);
            }
        }

        handleImageChange(newImageArray);
    }

    private void mosaic() {
        int[][] newImageArray = new int[this.w][this.h];

        for (int i = 0; i < this.w; ++i) {
            for (int j = 0; j < this.h; ++j) {
                newImageArray[(this.w / 2 + i) % this.w][(this.h / 2 + j) % this.h] = originalImageArray[i][j];
            }
        }

        handleImageChange(newImageArray);
    }

    public void flip(int[][] imageArray) {
        int[][] newImageArray = new int[this.w][this.h];
        for (int i = 0; i < this.w; ++i) {
            for (int j = 0; j < this.h; ++j) {
                newImageArray[i][j] = imageArray[this.w - 1 - i][this.h - 1 - j];
            }
        }

        handleImageChange(newImageArray);
    }

    private void showOriginal() {
        handleImageChange(originalImageArray);
    }


    private void closeProgram() {
        exit(0);
    }

    /**
     * readImage - read RBG data into a two dimensional integer array and return array
     * input: Image image - the Image variable to get width and height of the image from
     * PixelReader - the PixelReader variable to get the RGB numbers from
     * use .getArgb( x, y ) where x and y are the pixel coordinates
     * return: int[][] - the array with the RGB data
     */
    private int[][] readImage(Image image, PixelReader pixelReader) {
        int nh = (int) image.getHeight();
        int nw = (int) image.getWidth();

        int[][] imgArr = new int[nw][nh];

        for (int i = 0; i < nw; ++i) {
            for (int j = 0; j < nh; ++j) {
                imgArr[i][j] = pixelReader.getArgb(i, j);
            }
        }

        return imgArr;
    }


    /**
     * writePartialImage - helper method to write partial images on the canvas
     *
     * @param pixelWriter PixelWriter - object used to write on the canvas
     * @param imgArr      int[][] - pixel array of the image
     */
    private void writeImage(PixelWriter pixelWriter, int[][] imgArr) {
        for (int i = 0; i < imgArr.length; ++i) {
            for (int j = 0; j < imgArr[i].length; ++j) {
                pixelWriter.setArgb(i, j, imgArr[i][j]);
            }
        }
    }

    private void writeImage(PixelWriter pixelWriter, Color[][] imgArr) {
        for (int i = 0; i < imgArr.length; ++i) {
            for (int j = 0; j < imgArr[i].length; ++j) {
                pixelWriter.setColor(i, j, imgArr[i][j]);
            }
        }
    }

    private void handleImageDisplay(ImageView image) {
        this.bp.getChildren().clear(); //clear the border pane
        this.fp.getChildren().clear();

        this.fp.getChildren().addAll(this.buttons);
        image.setPreserveRatio(true);
        image.setSmooth(true);

        image.fitWidthProperty().bind(
                this.stage.widthProperty()
        );
        image.fitHeightProperty().bind(
                this.stage.heightProperty()
        );

        this.bp.getChildren().add(image);
        this.bp.setCenter(this.fp);
    }

    private void handleImageChange(int[][] newImageArray) {
        WritableImage writableImage = new WritableImage(newImageArray.length, newImageArray[0].length);
        PixelWriter pixelWriter = writableImage.getPixelWriter();
        writeImage(pixelWriter, newImageArray);
        handleImageDisplay(new ImageView(writableImage));
    }

    private void handleImageChange(Color[][] newImageArray) {
        WritableImage writableImage = new WritableImage(newImageArray.length, newImageArray[0].length);
        PixelWriter pixelWriter = writableImage.getPixelWriter();
        writeImage(pixelWriter, newImageArray);
        handleImageDisplay(new ImageView(writableImage));
    }

    @Override
    public void start(Stage stage) throws IOException {
        this.stage = stage;
        this.bp = new BorderPane();
        this.fp = new FlowPane();
        this.buttons = new ArrayList<>();

        initButtons();

        Image image = new Image(getClass().getResource("Subway.png").toExternalForm());
        PixelReader pixelReader = image.getPixelReader();

        this.originalImage = image;
        this.originalImageArray = readImage(image, pixelReader);
        this.h = (int) originalImage.getHeight();
        this.w = (int) originalImage.getWidth();

        // display image
        ImageView finalImageView = new ImageView(image);
        finalImageView.setPreserveRatio(true);
        finalImageView.setSmooth(true);

        // set aspect concrete ratio
        finalImageView.fitWidthProperty().bind(
                stage.widthProperty()
        );
        finalImageView.fitHeightProperty().bind(
                stage.heightProperty()
        );

        // display buttons
        this.fp.paddingProperty().setValue(new Insets(25, 25, 25, 25));
        this.fp.hgapProperty().setValue(5);
        this.fp.getChildren().addAll(this.buttons);
        this.bp.getChildren().add(finalImageView);
        this.bp.setCenter(fp);

        // window properties (same aspect ratio as the image - only initially)
        double imageRatio = image.getWidth() / image.getHeight();
        Scene scene = new Scene(bp, 500 * imageRatio, 500);
        stage.setScene(scene);
        stage.setTitle("TIMS - The Image Manipulation Software");
        stage.show();

    }
}