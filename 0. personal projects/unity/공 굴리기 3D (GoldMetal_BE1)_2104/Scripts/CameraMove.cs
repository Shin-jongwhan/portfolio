using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMove : MonoBehaviour
{
    Transform playerTransform;
    Vector3 Offset;     // 따라가는 오브젝트와의 카메라 벡터3

    // Start is called before the first frame update
    void Awake()
    {
        playerTransform = GameObject.FindGameObjectWithTag("Player").transform;
        Offset = transform.position - playerTransform.position;
    }

    // Update is called once per frame
    void LateUpdate()       // 카메라 업데이트에 관한 것은 LateUpdate()를 쓴다.
    {
        transform.position = playerTransform.position + Offset;
    }
}
