using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainSceneManager : MonoBehaviour
{
    string lastPlayTime;
    int maxHeartNum;
    int restNumOfHeart;

    DateTime dateTime_lastPlayTime;
    TimeSpan timeSpan;
    public GameObject gameContinueFailPanel;
    public Text heartText;
    public Text maxHeartText;

    // Start is called before the first frame update
    void Start()
    {
        // ��Ʈ �� ���� �� ��������
        if (PlayerPrefs.HasKey("RestNumOfHeart") == false)      // ó�� �÷����� ��
        {
            PlayerPrefs.SetInt("RestNumOfHeart", 1);
        }
        maxHeartNum = int.Parse(maxHeartText.text);
        restNumOfHeart = PlayerPrefs.GetInt("RestNumOfHeart");
        heartText.text = restNumOfHeart.ToString();

        // �÷��̾� ����ð�
        if (PlayerPrefs.HasKey("LastPlayTime") == false)
        {
            PlayerPrefs.SetString("LastPlayTime", DateTime.Now.ToString("yyyy-MM-dd-HH-mm"));
            lastPlayTime = PlayerPrefs.GetString("LastPlayTime");
        }
        else
            lastPlayTime = PlayerPrefs.GetString("LastPlayTime");

        dateTime_lastPlayTime = new DateTime(int.Parse(lastPlayTime.Split('-')[0]),
                                                        int.Parse(lastPlayTime.Split('-')[1]),
                                                        int.Parse(lastPlayTime.Split('-')[2]),
                                                        int.Parse(lastPlayTime.Split('-')[3]),
                                                        int.Parse(lastPlayTime.Split('-')[4]),
                                                        0);
        timeSpan = DateTime.Now - dateTime_lastPlayTime;
        Debug.Log(timeSpan.TotalMinutes);
    }

    // Update is called once per frame
    void Update()
    {
        //Debug.Log(DateTime.Now.ToString());
        Debug.Log(DateTime.Now.ToString("yyyy-MM-dd-HH-mm"));
    }

    void FixedUpdate()
    {
        // �����ð����� ��Ʈ �� ++
        if ( (timeSpan.TotalMinutes / 1) >= 1)
        {
            DateTime saveTime_tmp = DateTime.Now;
            saveTime_tmp = saveTime_tmp.AddMinutes(-(timeSpan.TotalMinutes % 1));      // ���� �ð�(��)�� ���ֱ�
            PlayerPrefs.SetString("LastPlayTime", saveTime_tmp.ToString("yyyy-MM-dd-HH-mm"));
            for (int i = 0; i < (int) (timeSpan.TotalMinutes - (timeSpan.TotalMinutes % 1)) / 1; i++)
            {
                if (restNumOfHeart < maxHeartNum)
                {
                    restNumOfHeart++;
                }
                else
                    break;
            }
            lastPlayTime = PlayerPrefs.GetString("LastPlayTime");
            dateTime_lastPlayTime = new DateTime(int.Parse(lastPlayTime.Split('-')[0]),
                                                        int.Parse(lastPlayTime.Split('-')[1]),
                                                        int.Parse(lastPlayTime.Split('-')[2]),
                                                        int.Parse(lastPlayTime.Split('-')[3]),
                                                        int.Parse(lastPlayTime.Split('-')[4]),
                                                        0);
            timeSpan = DateTime.Now - dateTime_lastPlayTime;
            heartText.text = restNumOfHeart.ToString();
            PlayerPrefs.SetInt("RestNumOfHeart", restNumOfHeart);
        }
    }

    public void GameContinueLoad()
    {
        if (PlayerPrefs.HasKey("StageNum"))
        {
            // ��Ʈ ����
            restNumOfHeart--;
            heartText.text = restNumOfHeart.ToString();
            PlayerPrefs.SetInt("RestNumOfHeart", restNumOfHeart);
            // �ε� ��������
            string stageNum = PlayerPrefs.GetString("StageNum");
            SceneManager.LoadScene("Stage" + stageNum);
        }
        else
            gameContinueFailPanel.SetActive(true);
    }

    public void GmaeFirstStartLoad()
    {
        // ��Ʈ ����
        restNumOfHeart--;
        heartText.text = restNumOfHeart.ToString();
        PlayerPrefs.SetInt("RestNumOfHeart", restNumOfHeart);
        // �ε� ��������
        SceneManager.LoadScene("Stage1");
    }

    public void GameQuit()
    {
        Application.Quit();
    }
}
