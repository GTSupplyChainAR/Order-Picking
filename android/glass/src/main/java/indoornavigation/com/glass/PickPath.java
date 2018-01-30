package indoornavigation.com.glass;

import java.util.ArrayList;
import java.util.List;

public class PickPath {

    private List<Pick> picks;

    public PickPath() {
        picks = new ArrayList();
    }

    public List<Pick> generateDemoPickPath() {
        picks = new ArrayList();
        String [] titles = {
                "The Name of the Wind",
                "Lord of the Rings",
                "A WIzard of Earthsea",
                "Left Hand of Darkness"
        };
        String [] authors = {
                "Patrick K. Rothfuss",
                "J.R.R. Tolkien",
                "Ursula K. LeGuin",
                "Ursula K. LeGuin"
        };
        int [] aisles = {
                1,
                2,
                3,
                3,
        };
        int [] rows = {
                2,
                3,
                1,
                4,
        };
        int [] cols = {
                1,
                2,
                1,
                1,
        };

        for (int i = 0; i < titles.length; i++) {
            picks.add(new Pick(titles[i], authors[i], Integer.toString(i), aisles[i], rows[i], cols[i]));
        }
        return picks;
    }
}
