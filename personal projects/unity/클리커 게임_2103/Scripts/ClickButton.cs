using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//카메라 상에 비치는 오브젝트를 터치했을 때 자동으로 실행해지는 함수 OnMouseDown()
public class ClickButton : MonoBehaviour
{
    public Animator anim;

    public void OnMouseDown()
    {
        DataController.Instance.gold += DataController.Instance.goldPerClick;

        anim.SetTrigger("OnClick");     // OnClick 이라는 파라미터를 발동
    }

}
