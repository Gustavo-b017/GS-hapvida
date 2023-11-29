#include <Adafruit_LiquidCrystal.h>
#include <Servo.h>


// iniciando lcd com o nome lcd_1
Adafruit_LiquidCrystal lcd_1(0);

// definindo portas 
const int ldr = A0; 
const int ledR = 4;
const int ledA = 5; 
const int ledV = 6; 
const int motorzinho = 3; 


// criando objeto do servo motor, basicamente definindo o servo motor
Servo motor; 

void setup(){
  
  	// definindo se e entrada ou saida de dados
 	pinMode(ledR, OUTPUT);
  	pinMode(ledA, OUTPUT);
  	pinMode(ledV, OUTPUT);
 	motor.attach(motorzinho);
  
  	// definindo tamanho do lcd
  	lcd_1.begin(16, 2);
  
  
}

void loop(){
  
    int valldr = analogRead(ldr);

  	if(valldr >= 550){ 
    digitalWrite(ledR, HIGH);
    digitalWrite(ledA, LOW); 
    digitalWrite(ledV, LOW); 
    motor.write(90); 
    lcd_1.clear();
  	lcd_1.print(valldr);
    lcd_1.print(" luz");
  	delay(1000);
    lcd_1.clear(); 
    lcd_1.print("janela aberta");
    lcd_1.setCursor(0,1);
    lcd_1.print("total");
  	delay(1000);
  	}
  	
  	else if (valldr < 550 and valldr >=300) {
    digitalWrite(ledR, LOW); 
    digitalWrite(ledA, HIGH); 
    digitalWrite(ledV, LOW); 
    motor.write(45);
    lcd_1.clear();
  	lcd_1.print(valldr);
    lcd_1.print(" luz");
  	delay(1000);
    lcd_1.clear();
    lcd_1.print("janela aberta");
    lcd_1.setCursor(0,1);
    lcd_1.print("pela metade");
  	delay(1000);
  	}
   	else {
    digitalWrite(ledR, LOW); 
    digitalWrite(ledA, LOW); 
    digitalWrite(ledV, HIGH); 
    motor.write(10); 
    lcd_1.clear();
  	lcd_1.print(valldr);
    lcd_1.print(" luz");
  	delay(1000);
    lcd_1.clear();
    lcd_1.print("janelas quase");
    lcd_1.setCursor(0,1);
    lcd_1.print("fechadas");
  	delay(1000);
	}
}