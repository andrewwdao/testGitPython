/* TRANSFERING DATA FROM SERIAL TO PARALLEL USING SPI PROTOCOL AND IC 74HC595
 *  
 *  ------74HC595
 *  1 - QB      16 - VCC
 *  2 - QC      15 - QA
 *  3 - QD      14 - SER    - connect to DS_PIN - DATA_PIN  or to QH' of the previous 74HC595
 *  4 - QE      13 - !OE    - connect to GND  
 *  5 - QF      12 - RCLK   - connect to STCP_PIN - LATCH_PIN (even when get data from a 74HC595 not a MCU)
 *  6 - QG      11 - SRCLK  - connect to SHCP_PIN - CLOCK_PIN (even when get data from a 74HC595 not a MCU)
 *  7 - QH      10 - !SRCLR - connect to VCC
 *  8 - GND     9  - QH'    - left floated when using only 1 74HC595, connect to pin 14 (SER) of the next 74HC595 if using multiple ones.
 * 
 */
#include <stdio.h>
#include <stdlib.h>     /* atof */
#include <wiringPi.h>
#include <wiringShift.h>

//WE ARE USING Raspberry Pi -  EVERY PIN IS ABLE TO CREATE PWM SIGNAL, CLOCK PIN AND DATA PIN ARE REQUIRED TO HAVE PWN PRODUCE CAPABILITY
#define DS_PIN  	0 //Pin connected to SER - DATA PIN (or Pin14 - DS) of 74HC595 - pin 0 of wiringPi, GPIO17
#define STCP_PIN 	2 //Pin connected to RCLK - LATCH_PIN (or Pin12 - ST_CP) of 74HC595 - pin 2 of wiringPi, GPIO 27
#define SHCP_PIN 	3 //Pin connected to SRCLK - CLOCK_PIN (or Pin11 - SH_CP) of 74HC595 - pin 3 of wiringPi, GPIO 22



char DATA1 = 0b00000001; //THIS IS THE DATA YOU WANT TO SEND, formated in byte, only send a byte each time
char DATA2 = 0b01000010; //THIS IS THE DATA YOU WANT TO SEND, formated in byte, only send a byte each time
char DATA3 = 0b00000111; //THIS IS THE DATA YOU WANT TO SEND, formated in byte, only send a byte each time

//byte DATA2 = 123;

void HC595_init() {
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print message to the screen
		printf("setup wiringPi failed !");
		return; 
	}//end if
	//shiftSetup(1);
	//set pins to output so you can control the shift register
	pinMode(DS_PIN, OUTPUT);
	pinMode(STCP_PIN, OUTPUT);
	pinMode(SHCP_PIN, OUTPUT);

}//end stepper_init
//--------------------------------

int main(void) {
	HC595_init();
	while(1) {
		
	digitalWrite(STCP_PIN, LOW); // LATCH_PIN low, make sure the LEDs don't change while you're sending in bits
    shiftOut(DS_PIN, SHCP_PIN, MSBFIRST, DATA1); //DATA to the last 74HC595 in the chain
    //shiftOut(DS_PIN, SHCP_PIN, MSBFIRST, DATA2); //DATA to the next 74HC595 in the chain
  //shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, DATA3); //continue to transfer
  //shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, DATA4); //DATA to the FIRST 74HC595 in the chain (connected with MCU)
    digitalWrite(STCP_PIN, HIGH);//take the latch pin high so the LEDs will light up   
	delay(5000);
	digitalWrite(STCP_PIN, LOW); // LATCH_PIN low, make sure the LEDs don't change while you're sending in bits
    shiftOut(DS_PIN, SHCP_PIN, MSBFIRST, DATA2); //DATA to the last 74HC595 in the chain
    //shiftOut(DS_PIN, SHCP_PIN, MSBFIRST, DATA2); //DATA to the next 74HC595 in the chain
  //shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, DATA3); //continue to transfer
  //shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, DATA4); //DATA to the FIRST 74HC595 in the chain (connected with MCU)
    digitalWrite(STCP_PIN, HIGH);//take the latch pin high so the LEDs will light up   
	delay(5000);
	digitalWrite(STCP_PIN, LOW); // LATCH_PIN low, make sure the LEDs don't change while you're sending in bits
    shiftOut(DS_PIN, SHCP_PIN, MSBFIRST, DATA3); //DATA to the last 74HC595 in the chain
    //shiftOut(DS_PIN, SHCP_PIN, MSBFIRST, DATA2); //DATA to the next 74HC595 in the chain
  //shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, DATA3); //continue to transfer
  //shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, DATA4); //DATA to the FIRST 74HC595 in the chain (connected with MCU)
    digitalWrite(STCP_PIN, HIGH);//take the latch pin high so the LEDs will light up   
	delay(5000);
	}
}