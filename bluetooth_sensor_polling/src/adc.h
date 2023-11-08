#ifndef ADC_H_KJJ
#define ADC_H_KJJ

struct Measurement
{
   int16_t x;
   int16_t y;
   int16_t z;
};

int initializeADC(void);
struct Measurement readADCValue(void);
void printDebugInfo(void);


#endif



