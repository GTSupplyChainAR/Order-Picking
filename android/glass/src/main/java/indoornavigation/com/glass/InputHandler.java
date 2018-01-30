package indoornavigation.com.glass;

import android.content.Context;
import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;

public class InputHandler {
    private final static String TAG = "AR-OP:InputHandler:";
    private Context mContext;

    public InputHandler(Context context){
        mContext = context;
    }

    public void load_data_JSON(String json_input_fname) {

        //Read File
        String json_str = null;
        try {
            InputStream is = mContext.getAssets().open(json_input_fname);
            int size = is.available();
            byte[] buffer = new byte[size];
            is.read(buffer);
            is.close();
            json_str = new String(buffer, "UTF-8");
        } catch (IOException e) {
            e.printStackTrace();
        }

        ArrayList<HashMap<String, String>> bookList = new ArrayList<HashMap<String, String>>();

        convertDataJSON(json_str, bookList);
    }

    private void convertDataJSON(String json_str, ArrayList<HashMap<String, String>> bookList) {
        try {
            JSONObject obj = new JSONObject(json_str);
            JSONArray m_jArry = obj.getJSONArray("Books");

            for(int i = 0 ; i < m_jArry.length(); i++){
                JSONObject json_obj_i = m_jArry.getJSONObject(i);
                String title_in = json_obj_i.getString("Title");
                String author_in = json_obj_i.getString("Author");
                String location_in = json_obj_i.getString("Location");

                HashMap<String,String> book_i = new HashMap<String, String>();
                book_i.put("Title", title_in);
                book_i.put("Author", author_in);
                book_i.put("Location", location_in);

                bookList.add(book_i);
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    //Convert to JSONObject


        //UNCOMMENT TO PRIN INPUT
        //Log.d(TAG, "The JSON file has "+bookList.size()+" entries.");
        //for(int i = 0 ; i < bookList.size() ; i++){
        //    HashMap<String, String> book_i = bookList.get(i);
        //    Log.d(TAG, "=== Book "+i + "===");
        //    Log.d(TAG, "Title: " + book_i.get("Title"));
        //    Log.d(TAG, "Author: " + book_i.get("Author"));
        //    Log.d(TAG, "Location: " + book_i.get("Location"));
        //}
}
