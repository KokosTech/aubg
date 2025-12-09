module doychinov.kaloyan.project4jfx {
    requires javafx.controls;
    requires javafx.fxml;


    opens doychinov.kaloyan.project4jfx to javafx.fxml;
    exports doychinov.kaloyan.project4jfx;
}