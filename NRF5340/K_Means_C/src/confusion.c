#include <zephyr/kernel.h>
#include <math.h>
#include "confusion.h"
#include "adc.h"
#include "k_means.h"

/* 
  K-means algorithm should provide 6 center points with
  3 values x,y,z. Let's test measurement system with known
  center points. I.e. x,y,z are supposed to have only values
  1 = down and 2 = up
  
  CP matrix is thus the 6 center points got from K-means algoritm
  teaching process. This should actually come from include file like
  #include "KmeansCenterPoints.h"
  
  And measurements matrix is just fake matrix for testing purpose
  actual measurements are taken from ADC when accelerator is connected.
*/ 


//int CP[6][3]={
//	                     {1,0,0},
//						 {2,0,0},
//						 {0,1,0},
//						 {0,1,1},
//						 {0,0,1},
//						 {0,0,2}
//};

int measurements[6][3]={
	                     {1,0,0},
						 {2,0,0},
						 {0,1,0},
						 {0,2,0},
						 {2,0,1},
						 {0,0,2}
};


int CM[6][6]= {0};



void printConfusionMatrix(void)
{
	printk("Confusion matrix = \n");
	printk("   cp1 cp2 cp3 cp4 cp5 cp6\n");
	for(int i = 0;i<6;i++)
	{
		printk("cp%d %d   %d   %d   %d   %d   %d\n",i+1,CM[4][0],CM[i][1],CM[i][2],CM[i][3],CM[i][4],CM[i][5]);
	}
}

void makeHundredFakeClassifications(void)
{
   /*******************************************
   Jos ja toivottavasti kun teet toteutuksen paloissa eli varmistat ensin,
   että etäisyyden laskenta 6 keskipisteeseen toimii ja osaat valita 6 etäisyydestä
   voittajaksi sen lyhyimmän etäisyyden, niin silloin voit käyttää tätä aliohjelmaa
   varmistaaksesi, että etäisuuden laskenta ja luokittelu toimii varmasti tunnetulla
   itse keksimälläsi sensoridatalla ja itse keksimilläsi keskipisteillä.
   *******************************************/
for (int i=0; i<2; i++){
   int winner = calculateDistanceToAllCentrePointsAndSelectWinner(measurements[i][0],measurements[i][1],measurements[i][2]);
   printk("Winning centroid %f, %f, %f\n", K_means[winner][0],K_means[winner][1],K_means[winner][2]);
}

   printk("Make your own implementation for this function if you need this\n");
}

void makeOneClassificationAndUpdateConfusionMatrix(int direction)
{
   /**************************************
   Tee toteutus tälle ja voit tietysti muuttaa tämän aliohjelman sellaiseksi,
   että se tekee esim 100 kpl mittauksia tai sitten niin, että tätä funktiota
   kutsutaan 100 kertaa yhden mittauksen ja sen luokittelun tekemiseksi.
   **************************************/

float sensorValues[100][3]={0};
struct Measurement sensor;
for (int i = 0; i<100; i++){
   sensor = readADCValue();
   sensorValues[i][0] = sensor.x;
   sensorValues[i][1] = sensor.y;
   sensorValues[i][2] = sensor.z;
   k_sleep(K_MSEC(500));
   int winner = calculateDistanceToAllCentrePointsAndSelectWinner(sensorValues[i][0],sensorValues[i][1],sensorValues[i][2]);
   CM[winner][direction]++;

   

}


   printk("Make your own implementation for this function if you need this\n");
}

int calculateDistanceToAllCentrePointsAndSelectWinner(int x,int y,int z)
{
   /***************************************
   Tämän aliohjelma ottaa yhden kiihtyvyysanturin mittauksen x,y,z,
   laskee etäisyyden kaikkiin 6 K-means keskipisteisiin ja valitsee
   sen keskipisteen, jonka etäisyys mittaustulokseen on lyhyin.
   ***************************************/

   int minIndex = -1; 
   double distance = 10;
   double minDistance = 2500;
   //printk("Test printing minDistance: %f \n", minDistance);
   for (int i = 0; i<6; i++){  
      distance = (sqrt(pow(K_means[i][0]- x, 2)+pow(K_means[i][1]-y, 2)
      +pow(K_means[i][2]-z, 2)));
      //printk("Test printing x value: %d \n", x);
      //printk("Test printing distance: %f \n", distance);
      //printk("Test printing index: %d \n", i);
      if (minDistance > distance){
         minDistance = distance;
         minIndex = i;
         //printk("Test printing minDistance: %f \n", minDistance);
   }
   }

   printk("Test printing end index:%d \n", minIndex);
   return minIndex;
}

void resetConfusionMatrix(void)
{
	for(int i=0;i<6;i++)
	{ 
		for(int j = 0;j<6;j++)
		{
			CM[i][j]=0;
		}
	}
}

