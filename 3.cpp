//try avoiding face detection

#include "cv.h"
#include "opencv2/opencv.hpp"
#include "highgui.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <float.h>
#include <limits.h>
#include <time.h>
#include <ctype.h>
#include <unistd.h>
#include <iostream>
#include <fstream>

#include "timer.hpp"
using namespace std;

using namespace cv;
//ofstream myfile;
static CvMemStorage* storage = 0;
static CvHaarClassifierCascade* cascade = 0;

void detect_and_draw( IplImage* image );
void detect_eyes(IplImage* img);
void detect_and_draw_th( IplImage* img );
void detect_eyes_th(IplImage* img);

static CvHaarClassifierCascade* cascade1 = 0;
const char* cascade_name =  "haarcascade_frontalface_alt.xml";
const char* cascade_name1 =   "haarcascade_eye.xml";


int th_o=28;
int open[10];
int n=0;
int o=1;

void tho()
{
	int min=150;
	for(n=0;n<10;n++)
	{
		if (open[n]<min&&open[n]>3)
		  min=open[n];
	}
	th_o=min;
	printf("%d",th_o);
}





int main( int argc, char** argv )
{ //myfile.open("1.dat");
  //timer time1;
  int count=0;
     cascade = (CvHaarClassifierCascade*)cvLoad( cascade_name, 0, 0, 0 );
      cascade1 = (CvHaarClassifierCascade*)cvLoad( cascade_name1, 0, 0, 0 );

   
    if( !cascade )
    {
        fprintf( stderr, "ERROR: Could not load classifier cascade\n" );
        return -1;
    }

 
    storage = cvCreateMemStorage(0);


      VideoCapture cap(0); // open the default camera
      if(!cap.isOpened())  // check if we succeeded
        return -1;

      printf("camera is on now\n");

    cap.set(CV_CAP_PROP_FRAME_WIDTH,320);
    cap.set(CV_CAP_PROP_FRAME_HEIGHT,240);
   cap.set(CV_CAP_PROP_FPS,2);
    //time1.start();
  IplImage* image2;
   Mat frame;
   IplImage ipltemp;
for(count=0,n=0;count<10;count++,n++)
    {
       
        cap >> frame;
       image2 = cvCreateImage(cvSize(frame.cols,frame.rows),8,3);
       ipltemp=frame;
       cvCopy(&ipltemp,image2);
        
     
       
    }
     for(count=0,n=0;count<10;count++,n++)
    {
       
        cap >> frame;
       image2 = cvCreateImage(cvSize(frame.cols,frame.rows),8,3);
       ipltemp=frame;
       cvCopy(&ipltemp,image2);
        detect_and_draw_th(&ipltemp);
     
       
    }

    // time1.stop();
    // printf("thresholding finished\n");
    // time1.print();


   tho();


  cvNamedWindow( "result", 1 );
   printf("\n\n\nRealtime capturing starts");


    for(;;)
    {
      //timer time2;
      //time2.start();
       
        cap >> frame; // get a new frame from camera

	 image2 = cvCreateImage(cvSize(frame.cols,frame.rows),8,3);
       ipltemp=frame;
       cvCopy(&ipltemp,image2);
        detect_and_draw(&ipltemp);
	//time2.start();
	//for(int p=0;p<25000000;p++);

	//time2.stop();
	//printf("1 frame calculated in");
	//time2.print();
    }


    return 0;
}






void detect_and_draw_th( IplImage* img )
{
    int scale = 1;

    // Create a new image based on the input image
    IplImage* temp = cvCreateImage( cvSize(img->width/scale,img->height/scale), 8, 3 );

    // Create two points to represent the face locations
    CvPoint pt1, pt2;
    int i;

    // Clear the memory storage which was used before
    cvClearMemStorage( storage );

    // Find whether the cascade is loaded, to find the faces. If yes, then:
    if( cascade )
    {

        // There can be more than one face in an image. So create a growable sequence of faces.
        // Detect the objects and store them in the sequence
        CvSeq* faces = cvHaarDetectObjects( img, cascade, storage,
                                            1.1, 2, CV_HAAR_DO_CANNY_PRUNING,
                                            cvSize(40, 40) );

        // Loop the number of faces found.
        for( i = 0; i < (faces ? faces->total : 0); i++ )
        {
           // Create a new rectangle for drawing the face
            CvRect* r = (CvRect*)cvGetSeqElem( faces, i );

			cvSetImageROI(img, *r);
			IplImage* faceSubImageLeft = cvCreateImage( cvSize(r->width, r->height), img->depth, img->nChannels );

			cvCopy(img, faceSubImageLeft);
	    detect_eyes_th(faceSubImageLeft);
            cvResetImageROI(img);
        }
    }

    //Show the image in the window named "result"
    //cvShowImage( "result", img );
//cvWaitKey(1);

    // Release the temp image created.
    cvReleaseImage( &temp );
}
// Function to detect and draw any faces that is present in an image
void detect_and_draw( IplImage* img )
{
    int scale = 1;

    // Create a new image based on the input image
    IplImage* temp = cvCreateImage( cvSize(img->width/scale,img->height/scale), 8, 3 );

    // Create two points to represent the face locations
    CvPoint pt1, pt2;
    int i;

    // Clear the memory storage which was used before
    cvClearMemStorage( storage );

    // Find whether the cascade is loaded, to find the faces. If yes, then:
    if( cascade )
    {

        // There can be more than one face in an image. So create a growable sequence of faces.
        // Detect the objects and store them in the sequence
        CvSeq* faces = cvHaarDetectObjects( img, cascade, storage,
                                            1.1, 2, CV_HAAR_DO_CANNY_PRUNING,
                                            cvSize(40, 40) );

	cvShowImage( "result", img );
	cvWaitKey(1);
        // Loop the number of faces found.
	//printf("Total faces %d\n",faces->total);
        for( i = 0; i < (faces ? faces->total : 0); i++ )
        {
           // Create a new rectangle for drawing the face
            CvRect* r = (CvRect*)cvGetSeqElem( faces, i );

			cvSetImageROI(img, *r);
			IplImage* faceSubImageLeft = cvCreateImage( cvSize(r->width, r->height), img->depth, img->nChannels );

			cvCopy(img, faceSubImageLeft);
	    detect_eyes(faceSubImageLeft);
            cvResetImageROI(img);
        }
    }

//     Show the image in the window named "result"
    cvShowImage( "result", img );
cvWaitKey(1);
    // Release the temp image created.
    cvReleaseImage( &temp );
}


/**
 * Given an image, this function will detect human eyes on the image and
 * draws green boxes around them.
 */
void detect_eyes(IplImage* img)
{
      cvClearMemStorage( storage );
	  CvRect EyeCenter;
	  CvFont font;
	  IplImage* img1;
	  img1 = cvCreateImage( cvSize(img->width,img->height),
                                            IPL_DEPTH_8U, img->nChannels );

    cvInitFont(&font, CV_FONT_HERSHEY_SIMPLEX, 1.0, 1.0, 0, 1, CV_AA);

	  CvScalar s,s1,s2,s3;
	  cvCopy(img,img1,0);
 
  /* Load the face detector and create empty memory storage */
  if (cascade1) {
    

  /* Detect objects */
  CvSeq* eyes = cvHaarDetectObjects(
    img,
    cascade1,
    storage,
    1.1,
    3,
    CV_HAAR_DO_CANNY_PRUNING,
    cvSize(40, 20)
  );

  int i,j,max=0;

  /* Draw green boxes around the eyes found */
  for( i = 0; i < (eyes ? eyes->total : 0); i++ ) {
    CvRect* r = (CvRect*)cvGetSeqElem(eyes, i);
	   cvRectangle(
      img,
      cvPoint(r->x, r->y),
      cvPoint(r->x + r->width, r->y + r->height),
      CV_RGB(0, 255, 0),
      2, 8, 0
    );

	
  }//printf("Total eyes %d\n",eyes->total);
  for( i = 0; i < (eyes ? eyes->total : 0); i++ ) 
  {
    CvRect* r = (CvRect*)cvGetSeqElem(eyes, i);
	EyeCenter.x = r->x + (r->width/2) - 10;
	EyeCenter.y = r->y + (r->height/2) - 10;

	EyeCenter.width = 20;
	EyeCenter.height = 20;

	//Eye SubImage Creation for Left,
	cvSetImageROI(img,EyeCenter);
	IplImage* EyeSubImageLeft = cvCreateImage( cvSize(EyeCenter.width, EyeCenter.height), img->depth, img->nChannels );
	cvCopy(img,EyeSubImageLeft);

	int width=EyeSubImageLeft->width;
	int height=EyeSubImageLeft->height;
    //Convert RGB to GRAY Image
	IplImage* LeftGray = cvCreateImage( cvSize( width,height ), IPL_DEPTH_8U, 1 );
	cvCvtColor( EyeSubImageLeft, LeftGray, CV_RGB2GRAY );

	for (i = 1; i<width - 1; i++)
	{
		for(j = 1; j<height - 1; j++)
		{
			s=cvGet2D(LeftGray,i,j);
			s1=cvGet2D(LeftGray,i-1,j+1);
			s2=cvGet2D(LeftGray,i,j+1);
			s3=cvGet2D(LeftGray,i+1,j+1);

			s.val[0] = (s.val[0] - (s1.val[0] + s2.val[0] + s3.val[0])/3);

			if (s.val[0] > max)
				max = s.val[0];

		}
	}
printf("intensity=%d\n",max);
printf("threshold=%d\n",th_o);
if (max>th_o){
	 
	o=0;
	
}
else{
o++;
if(o==2)printf("EYE CLOSED",o);
//myfile<<"1"<<endl;
}
printf("\n");
//myfile<<"0"<<endl;
cvShowImage( "result", img1 );
	cvWaitKey(1);

  }
      
  }
		

}
void detect_eyes_th(IplImage* img)
{
      cvClearMemStorage( storage );
	  CvRect EyeCenter;
	  CvFont font;
	  IplImage* img1;
	  img1 = cvCreateImage( cvSize(img->width,img->height),
                                            IPL_DEPTH_8U, img->nChannels );

    cvInitFont(&font, CV_FONT_HERSHEY_SIMPLEX, 1.0, 1.0, 0, 1, CV_AA);

	  CvScalar s,s1,s2,s3;
	  cvCopy(img,img1,0);
 
  /* Load the face detector and create empty memory storage */
  if (cascade1) {
    

  /* Detect objects */
  CvSeq* eyes = cvHaarDetectObjects(
    img,
    cascade1,
    storage,
    1.1,
    3,
    CV_HAAR_DO_CANNY_PRUNING,
    cvSize(40, 20)
  );

  int i,j,max=0;

  /* Draw green boxes around the eyes found */
  for( i = 0; i < (eyes ? eyes->total : 0); i++ ) {
    CvRect* r = (CvRect*)cvGetSeqElem(eyes, i);
	   cvRectangle(
      img,
      cvPoint(r->x, r->y),
      cvPoint(r->x + r->width, r->y + r->height),
      CV_RGB(0, 255, 0),
      2, 8, 0
    );

	
  }
  for( i = 0; i < (eyes ? eyes->total : 0); i++ ) 
  {
    CvRect* r = (CvRect*)cvGetSeqElem(eyes, i);
	EyeCenter.x = r->x + (r->width/2) - 10;
	EyeCenter.y = r->y + (r->height/2) - 10;

	EyeCenter.width = 20;
	EyeCenter.height = 20;

	//Eye SubImage Creation for Left,
	cvSetImageROI(img,EyeCenter);
	IplImage* EyeSubImageLeft = cvCreateImage( cvSize(EyeCenter.width, EyeCenter.height), img->depth, img->nChannels );
	cvCopy(img,EyeSubImageLeft);

	int width=EyeSubImageLeft->width;
	int height=EyeSubImageLeft->height;
    //Convert RGB to GRAY Image
	IplImage* LeftGray = cvCreateImage( cvSize( width,height ), IPL_DEPTH_8U, 1 );
	cvCvtColor( EyeSubImageLeft, LeftGray, CV_RGB2GRAY );

	for (i = 1; i<width - 1; i++)
	{
		for(j = 1; j<height - 1; j++)
		{
			s=cvGet2D(LeftGray,i,j);
			s1=cvGet2D(LeftGray,i-1,j+1);
			s2=cvGet2D(LeftGray,i,j+1);
			s3=cvGet2D(LeftGray,i+1,j+1);

			s.val[0] = (s.val[0] - (s1.val[0] + s2.val[0] + s3.val[0])/3);

			if (s.val[0] > max)
				max = s.val[0];

		}
	}

	open[n]=max;

  }
      
  }
		

}

