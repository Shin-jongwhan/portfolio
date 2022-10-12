using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public float limitTime;
    public bool isLimitTimeStage;

    public GameObject cancelPanel;
    public GameObject ExitQuestionPanel;
    public GameObject exitButton;
    public GameObject LimitTimePanel;
    public GameObject player;
    public GameObject startLine;
    public GameObject finishLine;
    public Text TimerText;

    HideSpace hideSpace;

    // Start is called before the first frame update
    void Start()
    {
        if (isLimitTimeStage == false)
        {
            LimitTimePanel.SetActive(false);
            limitTime = 9999.0f;
        }
        TimerText.text = ((limitTime - (limitTime % 60)) / 60).ToString() + ":" + (limitTime % 60).ToString();
        limitTime += 1;     // 바로 1초가 없어지는 것 방지

        player.transform.position = new Vector3(-1.5f, 2.5f);
        startLine.transform.position = new Vector3(-1.5f, 2.5f);
        finishLine.transform.position = new Vector3(2.5f, -4.5f);

        hideSpace = GetComponent<HideSpace>();
        hideSpace.xCoordinateStart = -5;
        hideSpace.yCoordinateStart = -6;
        hideSpace.xArrNum = 10;
        hideSpace.yArrNum = 12;
        hideSpace.newObject();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetButtonDown("Cancel"))
            CancelPanelActive();

        if (limitTime > 0)
            limitTime -= Time.deltaTime;
        TimerText.text = ((int) (limitTime - (limitTime % 60)) / 60).ToString() + ":" + ((int)limitTime % 60).ToString();
    }

    void FixedUpdate()
    {
        LimitTimeOut();
    }

    public void CancelPanelActive()
    {
        if (cancelPanel.activeSelf)
        {
            ExitQuestionPanel.SetActive(false);
            cancelPanel.SetActive(false);
        }
        else
        {
            cancelPanel.SetActive(true);
        }
    }

    public void GoMainScene()
    {
        SceneManager.LoadScene("MainScene");
    }

    void LimitTimeOut()
    {
        if ((int) limitTime == 0)
        {
            Debug.Log("제한 시간이 초과되었습니다.");
        }
    }

}
