using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ConnectionReward : MonoBehaviour
{
    public Text connectionReward;
    public CanvasGroup reward_canvasGroup;

    // Start is called before the first frame update

    void Start()
    {
        reward_canvasGroup.alpha = 1.0f;
        connectionReward.text = "미접속 보상!\n" + DataController.Instance.GetGoldPerSec() * DataController.Instance.timeAfterLastPlay;
    }
    

    public void buttonDestroy()
    {
        Object.Destroy(gameObject);
    }
}
