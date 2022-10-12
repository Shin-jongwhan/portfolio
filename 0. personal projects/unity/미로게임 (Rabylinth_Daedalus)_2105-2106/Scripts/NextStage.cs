using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class NextStage : MonoBehaviour
{
    public string nextStageNum;

    public void Goto_NextStage()
    {
        PlayerPrefs.SetString("StageNum", nextStageNum);
        SceneManager.LoadScene("Stage" + nextStageNum);
    }

}
