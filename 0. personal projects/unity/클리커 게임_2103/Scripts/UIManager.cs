using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    public Text goldDisplayer;  //gold를 표시해주는 test component
    public Text goldPerClickDisplayer;
    // public DataController dataController;   //DataController에 대한 reference를 가져옴

    public Text goldPerSecDisplayer;

    private void Update()
    {
        goldDisplayer.text = "GOLD: " + DataController.Instance.gold;
        goldPerClickDisplayer.text = "GOLD PER CLICK: " + DataController.Instance.goldPerClick;
        goldPerSecDisplayer.text = "GOLD PER SEC: " + DataController.Instance.GetGoldPerSec();
    }

    private void Awake()
    {
        Screen.SetResolution(1920, 1080, true);
    }
}
