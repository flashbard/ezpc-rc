#include <IRremote.hpp>

int IR_RECEIVE_PIN = 8;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Start the receiver
}

void loop() {
  if (IrReceiver.decode()) {
      Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
      delay(0.1);
      IrReceiver.resume();
  }
}
