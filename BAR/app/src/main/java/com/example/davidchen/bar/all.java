package com.example.davidchen.bar;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

public class all extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_all);
    }
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.all, menu);
        return true;
    }
    public boolean onOptionsItemSelected(MenuItem item) {
        switch(item.getItemId()){
            case R.id.cancel:
                Intent intent=new Intent(all.this,cancel.class );
                startActivity(intent);
        }
        switch(item.getItemId()){
            case R.id.select:
                Intent intent=new Intent(all.this,select.class );
                startActivity(intent);
        }
        switch(item.getItemId()){
            case R.id.main:
                Intent intent=new Intent(all.this,MainActivity.class );
                startActivity(intent);
        }
        return super.onOptionsItemSelected(item);
    }
}
