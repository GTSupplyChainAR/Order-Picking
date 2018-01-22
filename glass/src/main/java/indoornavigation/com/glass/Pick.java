package indoornavigation.com.glass;

public class Pick {

    private String title;
    private String author;
    private String location;
    private int aisle;
    private int row;
    private int col;

    public Pick(String title, String author, String location, int aisle, int row, int col) {
        this.title = title;
        this.author = author;
        this.location = location;
        this.aisle = aisle;
        this.row = row;
        this.col = col;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getLocation() {
        return location;
    }

    public int getAisle() {
        return aisle;
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }

}
