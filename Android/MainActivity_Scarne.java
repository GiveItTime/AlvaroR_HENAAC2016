// Author: Alvaro Rivas
// Date: 9/11/2016
// Description:
//      Scarne’s dice is an android app implementation of the turn-based dice game where players score points by rolling a die.
//      User is playing against the computers artificial intelligence by taking turns rolling a dice. The winner is whomever
//      reaches or exceeds 100 total points. If either player rolls a one accumulated score and turn is lost. Computer AI
//      and player choose when to add running total to current score by holding.

package com.dice.alvaro.scarnesdice;

import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.Random;

public class MainActivity_Scarne extends AppCompatActivity {
    private int overallScorePlayer = 0; // Stores overall player score
    private int overallScorePC = 0; // Stores overall PC score
    private int currentPlayerScore = 0; // Stores current player score
    private int currentPCScore = 0; // Stores current PC score
    private int playerCompareScore =0 ; // Stores score for PC to compare current score against
    private Button rollButton;
    private Button holdButton;
    private Button resetButton;
    private TextView playerText;
    private TextView pcText;
    private ImageView image;
    Handler handle = new Handler(); // event handler
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_activity__scarne);

        rollButton = (Button) findViewById(R.id.rollButton); // Roll Button
        holdButton = (Button) findViewById(R.id.holdButton); // Hold Button
        resetButton = (Button) findViewById(R.id.restartButton); // Restart Button
        playerText = (TextView) findViewById(R.id.playerTextView); // Shows current player score and overall score
        pcText = (TextView) findViewById(R.id.pcTextView); // Shows current PC score and overall score
        image = (ImageView) findViewById(R.id.imageView); // Displays different Images

//  Rolls dice and displays image of dice roll. Adds up each consecutive roll for total current player score.
//  If roll is one player looses turn and current score is not added to total.
        rollButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Random diceRoll = new Random();//New Instance of dice roll
                int rollNum = diceRoll.nextInt(6) + 1;// rolls dice
                // Displays image based on roll; player dice
                switch (rollNum){
                    case 1:
                        image.setImageResource(R.drawable.dice1);
                        break;
                    case 2:
                        image.setImageResource(R.drawable.dice2);
                        break;
                    case 3:
                        image.setImageResource(R.drawable.dice3);
                        break;
                    case 4:
                        image.setImageResource(R.drawable.dice4);
                        break;
                    case 5:
                        image.setImageResource(R.drawable.dice5);
                        break;
                    case 6:
                        image.setImageResource(R.drawable.dice6);
                        break;
                }
                // User rolled a one: looses turn and current accumulated points
                if(rollNum == 1){
                    currentPlayerScore = 0;
                    // Delay between computer turns allows user to see PC take its turn
                    handle.postDelayed(
                            new Runnable() {
                                @Override
                                public void run() {
                                    //PC logic- PC Turn
                                    computerTurnAI();
                                }
                            }, 2000);// two second delay
                    overallScorePC += currentPCScore;
                    currentPCScore = 0;
                    // Ends Game if Player Wins; disables roll and hold
                    if(overallScorePlayer >= 100){
                        playerText.setText("You WIN!!!");
                        disableButtons();
                    }
                    // Ends Game if Player looses; disables roll and hold
                    else if(overallScorePC >= 100){
                        playerText.setText("You LOSE!!!");
                        disableButtons();
                    }
                    // Displays PC current turn
                    else{
                        playerText.setText("Your Total Score: " + Integer.toString(overallScorePlayer));
                        pcText.setText(" PC Total Score: " + Integer.toString(overallScorePC) + " PC current Score: "
                                + Integer.toString(currentPCScore));
                    }
                }
                // Displays Player current turn
                else {
                    currentPlayerScore += rollNum;
                    playerText.setText("Your current total: " + Integer.toString(currentPlayerScore) +" Your Total Score: "
                            + Integer.toString(overallScorePlayer));
                    pcText.setText(" PC Total Score: " + Integer.toString(overallScorePC));
                }
            }// End of onClick

        });// End of rollButton

        // Saves current player cumulative score.
        // Computer takes its turn
        holdButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                playerCompareScore = currentPlayerScore;
                overallScorePlayer += currentPlayerScore;
                handle.postDelayed(
                        new Runnable() {
                            @Override
                            public void run() {
                                computerTurnAI();
                            }
                        }, 2000);// two second delay
                // adds pc current score to pc total score
                overallScorePC += currentPCScore;
                currentPCScore = 0;
                // Ends Game if Player Wins
                if(overallScorePlayer >= 100){
                    playerText.setText("You WIN!!!");
                    disableButtons();
                }
                // Ends Game if Player looses
                else if(overallScorePC >= 100){
                    playerText.setText("You LOSE!!!");
                    disableButtons();
                }
                // Displays Player current turn
                else{
                    playerText.setText("Your Total Score: " + Integer.toString(overallScorePlayer));
                    pcText.setText("PC Total Score: " + Integer.toString(overallScorePC) + " PC current Score: "
                            + Integer.toString(currentPCScore));
                }
                currentPlayerScore = 0; // resets players current total
            }
        });// End of holdButton
        // Restarts Game
        resetButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // resets all scores
                currentPCScore = 0;
                currentPlayerScore = 0;
                overallScorePC = 0;
                overallScorePlayer = 0;
                image.setImageResource(R.drawable.scarne);// starting image
                playerText.setText("Welcome");
                pcText.setText("Game On!!!");
                enableButtons();
            }
        });// End of resetButton
    }// End of onCreate

    // Computer turn logic
    public void computerTurnAI(){

        Random diceRoll = new Random();//New Instance of dice roll
        // if no one has won yet
        if((overallScorePlayer <= 100) && (overallScorePC <=100)) {
            int pcRoll = diceRoll.nextInt(6) + 1;
            // Displays image based on roll; pc dice
            switch (pcRoll) {
                case 1:
                    image.setImageResource(R.drawable.dicepc1);
                    break;
                case 2:
                    image.setImageResource(R.drawable.dicepc2);
                    break;
                case 3:
                    image.setImageResource(R.drawable.dicepc3);
                    break;
                case 4:
                    image.setImageResource(R.drawable.dicepc4);
                    break;
                case 5:
                    image.setImageResource(R.drawable.dicepc5);
                    break;
                case 6:
                    image.setImageResource(R.drawable.dicepc6);
                    break;
            }
            currentPCScore += pcRoll;
            // Computer rolled a one: looses turn and current accumulated points
            if (pcRoll == 1) {
                currentPCScore = 0;
                enableButtons();
                // If current pc score is less than players
                // last score computer continues rolling
            }
            else if (currentPCScore < playerCompareScore) {
                // Delay between computer turns allows user to see PC take its turn
                handle.postDelayed(
                        new Runnable() {
                            @Override
                            public void run() {
                                computerTurnAI();
                            }
                        }, 2000);// two second delay
            }

        }

    }// end of ComputerAI
    public void disableButtons(){
        rollButton.setEnabled(false);
        holdButton.setEnabled(false);
    }// End of disable button
    // Enables Button
    public void enableButtons(){
        rollButton.setEnabled(true);
        holdButton.setEnabled(true);
    }// End of enable button
}
