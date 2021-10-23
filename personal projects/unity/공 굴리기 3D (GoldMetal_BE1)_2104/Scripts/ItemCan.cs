using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ItemCan : MonoBehaviour
{

    public float rotateSpeed;

    // Update is called once per frame
    void Update()
    {
        //Space.World : 회전을 도는 기준은 월드 좌표계와 Local 좌표계(게임 오브젝트)가 있다.
        transform.Rotate(Vector3.up * rotateSpeed * Time.deltaTime, Space.World);
    }

}
