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

import static java.lang.System.arraycopy;
import static java.lang.System.exit;

class TIMS {
    Stage stage;
    BorderPane bp;
    FlowPane fp;
    ArrayList<Button> buttons;

    Image originalImage;
    int[][] originalImageArray;

    public TIMS(Stage stage) {
        this.stage = stage;
        this.bp = new BorderPane();
        this.fp = new FlowPane();
        this.buttons = new ArrayList<>();

        initButtons();

        Image image = new Image(getClass().getResource("Subway.png").toExternalForm());
        PixelReader pixelReader = image.getPixelReader();

        this.originalImage = image;
        this.originalImageArray = readImage(image, pixelReader);

        ImageView finalImageView = new ImageView(image);
        finalImageView.setPreserveRatio(true);
        finalImageView.setSmooth(true);
        finalImageView.fitWidthProperty().bind(
                stage.widthProperty()
        );

        finalImageView.fitHeightProperty().bind(
                stage.heightProperty()
        );
        fp.paddingProperty().setValue(new Insets(25, 25, 25, 25));
        fp.hgapProperty().setValue(5);
        fp.getChildren().addAll(buttons);
        bp.getChildren().add(finalImageView);
        bp.setCenter(fp);
        double imageRatio = image.getWidth() / image.getHeight();
        Scene scene = new Scene(bp, 500 * imageRatio, 500);
        stage.setScene(scene);
        stage.setTitle("TIMS - The Image Manipulation Software");
        stage.show();
    }

    private void initButtons() {
        Button flipButton = new Button("Diagonal Flip");
        flipButton.setOnAction(e -> flip(originalImageArray));
        buttons.add(flipButton);

        Button grayscaleButton = new Button("Grayscale");
        grayscaleButton.setOnAction(e -> grayscale());
        buttons.add(grayscaleButton);

        Button mosaicButton = new Button("Mosaic");
        mosaicButton.setOnAction(e -> mosaic());
        buttons.add(mosaicButton);

        Button overlayButton = new Button("Add flair");
        overlayButton.setOnAction(e -> overlay());
        buttons.add(overlayButton);

        Button originalButton = new Button("Original");
        originalButton.setOnAction(e -> showOriginal());
        buttons.add(originalButton);

        Button closeButton = new Button("Exit");
        closeButton.setOnAction(e -> closeProgram());
        buttons.add(closeButton);
    }

    private void overlay() {
        Image overlay = new Image(getClass().getResource("overlay.png").toExternalForm());
        PixelReader pixelReader = overlay.getPixelReader();

        int h = (int) originalImage.getHeight();
        int w = (int) originalImage.getWidth();

        int[][] imgArr = readImage(originalImage, originalImage.getPixelReader());

        for (int i = 0; i < w; ++i) {
            for (int j = 0; j < h; ++j) {
                if (pixelReader.getColor(i, j).getRed() != 1.0 &&
                        pixelReader.getColor(i, j).getGreen() != 1.0 &&
                        pixelReader.getColor(i, j).getBlue() != 1.0)
                    imgArr[i][j] = pixelReader.getArgb(i, j);
            }
        }

        WritableImage writableImage = new WritableImage(imgArr.length, imgArr[0].length);
        PixelWriter pixelWriter = writableImage.getPixelWriter();
        writeImage(pixelWriter, imgArr);
        handleImageChange(new ImageView(writableImage));
    }

    private void grayscale() {
//        int[][] newImageArray = toGrayscale(originalImage, originalImage.getPixelReader());

        int h = (int) originalImage.getHeight();
        int w = (int) originalImage.getWidth();

        Color[][] imgArr = new Color[w][h];

        for (int i = 0; i < w; ++i) {
            for (int j = 0; j < h; ++j) {
                Color color = originalImage.getPixelReader().getColor(i, j);
                double calc = (color.getRed() + color.getGreen() + color.getBlue()) / 3;
                imgArr[i][j] = new Color(calc, calc, calc, 1);
            }
        }

        WritableImage writableImage = new WritableImage(imgArr.length, imgArr[0].length);
        PixelWriter pixelWriter = writableImage.getPixelWriter();
        writeImage(pixelWriter, imgArr);
        handleImageChange(new ImageView(writableImage));
    }

    private void mosaic() {
        int h = originalImageArray.length;
        int w = originalImageArray[0].length;

        int[][] newImageArray = new int[h][w];

        for (int i = 0; i < h / 2; ++i) {
            for (int j = 0; j < w / 2; ++j) {
                newImageArray[h / 2 + i][w / 2 + j] = originalImageArray[i][j];
            }
        }

        for (int i = 0; i < h / 2; ++i) {
            for (int j = w / 2; j < w; ++j) {
                newImageArray[(h / 2 + i) % h][(w / 2 + j) % w] = originalImageArray[i][j];
            }
        }

        for (int i = h / 2; i < h; ++i) {
            for (int j = 0; j < w / 2; ++j) {
                newImageArray[(h / 2 + i) % h][(w / 2 + j) % w] = originalImageArray[i][j];
            }
        }

        for (int i = h / 2; i < h; ++i) {
            for (int j = w / 2; j < w; ++j) {
                newImageArray[(h / 2 + i) % h][(w / 2 + j) % w] = originalImageArray[i][j];
            }
        }


        WritableImage writableImage = new WritableImage(originalImageArray.length, originalImageArray[0].length);
        PixelWriter pixelWriter = writableImage.getPixelWriter();
        writeImage(pixelWriter, newImageArray);
        handleImageChange(new ImageView(writableImage));
    }

    private void showOriginal() {
        handleImageChange(new ImageView(originalImage));
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


    /**
     * writePartialImage - helper method to write partial images on the canvas
     *
     * @param pixelWriter PixelWriter - object used to write on the canvas
     * @param imgArr      int[][] - pixel array of the image
     * @return new cursor position
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

    public void flip(int[][] imageArray) {
        int[][] newImageArray = new int[imageArray.length][imageArray[0].length];
        for (int i = 0; i < imageArray.length; ++i) {
            for (int j = 0; j < imageArray[i].length; ++j) {
                newImageArray[i][j] = imageArray[imageArray.length - 1 - i][imageArray[i].length - 1 - j];
            }
        }
        WritableImage writableImage = new WritableImage(imageArray.length, imageArray[0].length);
        PixelWriter pixelWriter = writableImage.getPixelWriter();
        writeImage(pixelWriter, newImageArray);
        handleImageChange(new ImageView(writableImage));
    }

    public void handleImageChange(ImageView image) {
        bp.getChildren().clear(); //clear the border pane
        fp.getChildren().clear();

        fp.getChildren().addAll(buttons);
        image.setPreserveRatio(true);
        image.setSmooth(true);
        image.fitWidthProperty().bind(
                stage.widthProperty()
        );

        image.fitHeightProperty().bind(
                stage.heightProperty()
        );
        bp.getChildren().add(image);
        bp.setCenter(fp);
    }
}

public class HelloApplication extends Application {
    public static void main(String[] args) {
        launch();
    }

    @Override
    public void start(Stage stage) throws IOException {
        TIMS tims = new TIMS(stage);

    }


}