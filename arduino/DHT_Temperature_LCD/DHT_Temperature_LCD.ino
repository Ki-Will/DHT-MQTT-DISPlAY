#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define LCD_ADDR 0x27
#define LCD_COLS 16
#define LCD_ROWS 2

DHT dht(DHTPIN, DHTTYPE);

LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLS, LCD_ROWS);

String candidateName = "IRAKOZE Prince Bonheur";
int nameLength = candidateName.length();
int scrollPosition = 0;
unsigned long previousMillis = 0;
const long scrollInterval = 300;

void setup() {
  lcd.init();
  lcd.backlight();
  dht.begin();
  Serial.begin(9600);
}

void loop() {
  float temperature = dht.readTemperature();
  
  if (isnan(temperature)) {
    temperature = 0.0;
  }

  updateLCD(temperature);
  Serial.println(temperature);
  
  delay(500);
}

void updateLCD(float temp) {
  lcd.clear();
  
  if (nameLength <= 16) {
    lcd.setCursor(0, 0);
    lcd.print(candidateName);
  } else {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= scrollInterval) {
      previousMillis = currentMillis;
      scrollPosition++;
      if (scrollPosition > nameLength) {
        scrollPosition = 0;
      }
    }
    
    String displayName = candidateName + " " + candidateName;
    lcd.setCursor(0, 0);
    lcd.print(displayName.substring(scrollPosition, scrollPosition + 16));
  }
  
  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(temp);
  lcd.print(" C");
}
