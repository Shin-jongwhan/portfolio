using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HideSpace : MonoBehaviour
{
    public GameObject obj;
    public int xCoordinateStart;
    public int yCoordinateStart;
    public int xArrNum;
    public int yArrNum;
    int gameObjNum;

    //int[] objArr_xCoordinate;
    //int[] objArr_yCoordinate;
    GameObject[] objArr;

    // Start is called before the first frame update
    void Start()
    {
        gameObjNum = xArrNum * yArrNum;
        Debug.Log(gameObjNum);
        //objArr_xCoordinate = new int[xArrNum];
        //objArr_yCoordinate = new int[yArrNum];
        objArr = new GameObject[gameObjNum];
        newObject();
    }

    public void newObject()
    {
        int gameObjNum = xArrNum * yArrNum;
        GameObject[] objArr = new GameObject[gameObjNum];
        int objNum = 0;
        for (int xNum = 0; xNum < xArrNum; xNum++)
            for (int yNum = 0; yNum < yArrNum; yNum++)
            {
                //Debug.Log(objNum.ToString() + " " + ((float)xCoordinateStart + (float)xNum + 0.5f).ToString() + " " + ((float)yCoordinateStart + (float)yNum - 0.5f).ToString());
                objArr[objNum] = obj;
                Instantiate(objArr[objNum], new Vector3((float) xCoordinateStart + (float) xNum + 0.5f,
                    (float) yCoordinateStart + (float) yNum + 0.5f, 0), 
                    Quaternion.identity);
                objNum++;
            }
    }

}
