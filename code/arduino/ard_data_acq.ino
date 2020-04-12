#include <Wire.h>
#include <Adafruit_ADS1015.h>

const int SWEEP_LENGTH = 9; // in seconds
const int SAMP_FREQ = 125;   // sps per channel
const int NUM_CHANNELS = 8;
const int mux_0 = 7;
const int mux_1 = 8;
const int mux_2 = 9;
const int sigPin = 10;
const int ledPin = 11;

Adafruit_ADS1015 ads;

#define serialPi Serial

void setup() 
{ 
  /* Set up MUX control pins */
  pinMode(mux_0, OUTPUT);
  pinMode(mux_1, OUTPUT);
  pinMode(mux_2, OUTPUT);

  /* Set up signal, acknowledge, and led pins */
  pinMode(sigPin, INPUT);
  pinMode(ledPin, OUTPUT);

  /* Set parameters for ADC */
  ads.setGain(GAIN_ONE);
  ads.begin();

  /* Set up communication with Raspbery Pi */
  serialPi.begin(115200);
}

void loop() 
{
  uint8_t state = digitalRead(sigPin);
  int sample_length = NUM_CHANNELS * 15;
  int16_t sample;//[sample_length];
  
  /* check for signal from Raspberry Pi */
  if (state == HIGH) {
    digitalWrite(ledPin, HIGH);

    /* Start data acquisition */
    //serialPi.print("Recording Start!\n");
    for (int i = 0; i < SWEEP_LENGTH * SAMP_FREQ; ++i) {
      for (int j = 0; j < NUM_CHANNELS; ++j) {
        mux_ctrl(j);
        sample = ads.readADC_SingleEnded(0);
        serialPi.print(sample);
        serialPi.print(",");
      }
    }
    serialPi.print("\n");
    //serialPi.print("Recording Stop!\n");
    
    
  } else {
    /* Stop data collection */
    digitalWrite(ledPin, LOW);
    mux_ctrl(0);
  }
  
}

void mux_ctrl(int count) {
  switch (count) {
    case 0:
      digitalWrite(mux_0, LOW);
      digitalWrite(mux_1, LOW);
      digitalWrite(mux_2, LOW);
      break;
    case 1:
      digitalWrite(mux_0, HIGH);
      digitalWrite(mux_1, LOW);
      digitalWrite(mux_2, LOW);
      break;
    case 2:
      digitalWrite(mux_0, LOW);
      digitalWrite(mux_1, HIGH);
      digitalWrite(mux_2, LOW);
      break;
    case 3:
      digitalWrite(mux_0, HIGH);
      digitalWrite(mux_1, HIGH);
      digitalWrite(mux_2, LOW);
      break;
    case 4:
      digitalWrite(mux_0, LOW);
      digitalWrite(mux_1, LOW);
      digitalWrite(mux_2, HIGH);
      break;
    case 5:
      digitalWrite(mux_0, HIGH);
      digitalWrite(mux_1, LOW);
      digitalWrite(mux_2, HIGH);
      break;
    case 6:
      digitalWrite(mux_0, LOW);
      digitalWrite(mux_1, HIGH);
      digitalWrite(mux_2, HIGH);
      break;
    case 7:
      digitalWrite(mux_0, HIGH);
      digitalWrite(mux_1, HIGH);
      digitalWrite(mux_2, HIGH);
      break;
  }
 
}
