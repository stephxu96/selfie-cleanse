package com.example.davidchen.bar;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

public class cancel extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cancel);
    }
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.cancel,menu);
        return true;
    }
    public boolean onOptionsItemSelected(MenuItem item) {
        switch(item.getItemId()){
            case R.id.select:
                Intent intent=new Intent(cancel.this,select.class );
                startActivity(intent);
        }
        switch(item.getItemId()){
            case R.id.all:
                Intent intent=new Intent(cancel.this,all.class );
                startActivity(intent);
        }
        switch(item.getItemId()){
            case R.id.main:
                Intent intent=new Intent(cancel.this,MainActivity.class );
                startActivity(intent);
        }
        return super.onOptionsItemSelected(item);
    }
}
