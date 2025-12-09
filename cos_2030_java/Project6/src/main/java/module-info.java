module doychinov.kaloyan.project6 {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;


    opens doychinov.kaloyan.project6 to javafx.fxml;
    exports doychinov.kaloyan.project6;
}