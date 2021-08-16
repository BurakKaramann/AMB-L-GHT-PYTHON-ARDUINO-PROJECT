#include <SoftwareSerial.h>

#define RxD 11
#define TxD 10

SoftwareSerial mySerial(RxD,TxD);

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}
char rxData;  
char comment[100];             // 123,123,123

String data;
String str1,str2,str3;

int x1,x2,x3;
int line;

void loop() {

    while(mySerial.available()>0){
      rxData = mySerial.read();

      if(rxData == '\r' || rxData == '\n'){
        
        data = String(comment);

        if(data.length()>0){
          
          x1=data.indexOf(",");           // 123,123,123\n
          x2=data.indexOf(",",x1+1);
          x3=data.indexOf("\n",x2+1);

          str1=data.substring(0,x1);
          str2=data.substring(x1+1,x2);
          str3=data.substring(x2+1,x3);

          analogWrite(9,str1.toInt());
          analogWrite(5,str2.toInt());
          analogWrite(3,str3.toInt());
          /*
          Serial.print("STR1 : ");
          Serial.println(str1);
          Serial.print("STR2 : ");
          Serial.println(str2);
          Serial.print("STR3 : ");
          Serial.println(str3);*/
        }

      for(int i=0; i<sizeof(comment); i++ ){
        comment[i]=char(0);
      }
      line=0;
      }
      
      else{comment[line++]=rxData;}
    } 
}
