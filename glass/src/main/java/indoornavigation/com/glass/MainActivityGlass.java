package indoornavigation.com.glass;

import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.TextView;

import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;
import java.util.List;

import com.google.android.glass.touchpad.Gesture;
import com.google.android.glass.touchpad.GestureDetector;

public class MainActivityGlass extends Activity implements GestureDetector.BaseListener {

    int numberOfPicks = 4;
    PickPath path = new PickPath();
    List<Pick> demoPickPath = path.generateDemoPickPath();


    String currentUser;

    Long lastStartTime;
    ArrayList<Long> pickTimes = new ArrayList(numberOfPicks);

    FirebaseDatabase database = FirebaseDatabase.getInstance();

    boolean shouldProgress = true;

    GestureDetector detector;

    /* ----- UI ----- */
    View parentView;

    View aisleView;
    View[] letterViews;

    View rowView;
    // column, row
    View[][] blockViews;

    TextView locationText;
    TextView isbnText;
    TextView titleText;
    TextView authorText;
    TextView instructionText;

    enum PathView {
        AISLE,
        ROW
    }
    PathView currentView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        currentView = PathView.AISLE;

        setContentView(R.layout.activity_main);
        parentView = findViewById(R.id.parent_view);

        aisleView = findViewById(R.id.aisle_view);
        letterViews = new View[] {
                findViewById(R.id.block_a),
                findViewById(R.id.block_b),
                findViewById(R.id.block_c),
                findViewById(R.id.block_d),
                findViewById(R.id.block_e),
                findViewById(R.id.block_f)
        };

        rowView = findViewById(R.id.row_view);
        blockViews = new View[][] {
                new View[] {
                        findViewById(R.id.block_0_0),
                        findViewById(R.id.block_0_1),
                        findViewById(R.id.block_0_2),
                        findViewById(R.id.block_0_3),
                        findViewById(R.id.block_0_4),
                        findViewById(R.id.block_0_5)
                },
                new View[] {
                        findViewById(R.id.block_1_0),
                        findViewById(R.id.block_1_1),
                        findViewById(R.id.block_1_2),
                        findViewById(R.id.block_1_3),
                        findViewById(R.id.block_1_4),
                        findViewById(R.id.block_1_5)
                },
                new View[] {
                        findViewById(R.id.block_2_0),
                        findViewById(R.id.block_2_1),
                        findViewById(R.id.block_2_2),
                        findViewById(R.id.block_2_3),
                        findViewById(R.id.block_2_4),
                        findViewById(R.id.block_2_5)
                },
                new View[] {
                        findViewById(R.id.block_3_0),
                        findViewById(R.id.block_3_1),
                        findViewById(R.id.block_3_2),
                        findViewById(R.id.block_3_3),
                        findViewById(R.id.block_3_4),
                        findViewById(R.id.block_3_5)
                },
                new View[] {
                        findViewById(R.id.block_4_0),
                        findViewById(R.id.block_4_1),
                        findViewById(R.id.block_4_2),
                        findViewById(R.id.block_4_3),
                        findViewById(R.id.block_4_4),
                        findViewById(R.id.block_4_5)
                },
                new View[] {
                        findViewById(R.id.block_5_0),
                        findViewById(R.id.block_5_1),
                        findViewById(R.id.block_5_2),
                        findViewById(R.id.block_5_3),
                        findViewById(R.id.block_5_4),
                        findViewById(R.id.block_5_5)
                },
        };

        locationText = (TextView)findViewById(R.id.location_text);
        isbnText = (TextView)findViewById(R.id.isbn_text);
        titleText = (TextView)findViewById(R.id.title_text);
        authorText = (TextView)findViewById(R.id.author_text);

        instructionText = (TextView)findViewById(R.id.instruction_text);

        detector = new GestureDetector(this);
        detector.setBaseListener(this);

        //Parsing INPUTS
        InputHandler input_h = new InputHandler(this);
        //This function must later return our Data Structure that holds the data
        input_h.load_data_JSON("books.json");
        //End of Parsing Inputs

        startPicking();
    }

    @Override
    public boolean onGenericMotionEvent(MotionEvent event) {
        if (detector != null) {
            return detector.onMotionEvent(event);
        }
        return false;
    }

    // todo this needs to be called by user input
    private void startPicking() {
        // todo debug this
        currentUser = database.getReference("ar-order-picking").push().getKey();
        generateNextPick();
    }

    // todo this needs to be called when a user has picked
    private void completePick() {
        pickTimes.add(System.currentTimeMillis() - lastStartTime);
        generateNextPick();
    }

    private void generateNextPick() {
        // Reset UI dumb implementation
        if (pickTimes.size() > 0) {
            Pick previous = demoPickPath.get(pickTimes.size() - 1);
            letterViews[previous.getAisle()].setBackgroundColor(getResources().getColor(R.color.lime_green));
            if (previous.getRow() % 2 == 0) {
                blockViews[previous.getRow()][previous.getCol()].setBackgroundColor(getResources().getColor(R.color.light_red));
            } else {
                blockViews[previous.getRow()][previous.getCol()].setBackgroundColor(getResources().getColor(R.color.light_blue));
            }
        }

        // Display next pick on ui
        if (pickTimes.size() < numberOfPicks) {
            lastStartTime = System.currentTimeMillis();

            Pick book = demoPickPath.get(pickTimes.size());
            titleText.setText(book.getTitle());
            authorText.setText(book.getAuthor());
            locationText.setText(book.getLocation());
            letterViews[book.getAisle()].setBackgroundColor(getResources().getColor(R.color.red));
            blockViews[book.getRow()][book.getCol()].setBackgroundColor(getResources().getColor(R.color.red));

            displayAisleView();

        } else {
            finishPicking();
        }
    }

    private void finishPicking() {
        // todo: debug this
        database.getReference("ar-order-picking").child(currentUser).setValue(pickTimes);
    }

    @Override
    public boolean onGesture(Gesture gesture) {
        if (gesture == Gesture.TAP) {
            if (currentView == PathView.AISLE) {
                displayRowView();
            } else {
                displayAisleView();
            }
            return true;
        } else if (gesture == Gesture.SWIPE_LEFT || gesture == Gesture.SWIPE_RIGHT || gesture == Gesture.SWIPE_DOWN || gesture == Gesture.SWIPE_UP) {
            if (shouldProgress) {
                completePick();
                shouldProgress = false;
                new Handler().postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        shouldProgress = true;
                    }
                }, 1000);
            }

            return true;
        }
        return false;
    }

    private void displayRowView() {
        currentView = PathView.ROW;
        aisleView.setVisibility(View.GONE);
        rowView.setVisibility(View.VISIBLE);
        instructionText.setText("Tap for aisle view. Swipe for next book.");
    }

    private void displayAisleView() {
        currentView = PathView.AISLE;
        rowView.setVisibility(View.GONE);
        aisleView.setVisibility(View.VISIBLE);
        instructionText.setText("Tap for row view. Swipe for next book.");
    }


}
