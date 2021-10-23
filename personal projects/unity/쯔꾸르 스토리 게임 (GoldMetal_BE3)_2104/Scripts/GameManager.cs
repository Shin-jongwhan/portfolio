using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public TalkManager talkManager;
    public QuestManager questManager;
    public Animator talkPanel;      // ó���� SetActive�� �����ٰ� ������ٰ� �̷��� ������ �ִϸ����ͷ� �ִϸ��̼� ȿ��
    //public GameObject talkPanel;
    public Animator portraitAnim;
    public Image portraitImg;
    public Sprite previousPortrait;
    //public Text talkText;     // TypeEffect.cs �ֱ� ���� ���� ��
    public TypeEffect talk;
    public Text questTalk;
    public Text TalkObjectName;
    public GameObject scanObject;
    public GameObject menuSet;
    public GameObject player;       // ���� ������ �� ������ ������
    public bool isAction;
    public int talkIndex;

    private void Start()
    {
        GameLoad();

        //Debug.Log(questManager.CheckQuest());
        questTalk.text = questManager.CheckQuest();
    }

    private void Update()
    {
        // Sub menu
        if (Input.GetButtonDown("Cancel"))
            SubMenuActive();
    }

    public void SubMenuActive()
    {
        if (menuSet.activeSelf)
            menuSet.SetActive(false);
        else
            menuSet.SetActive(true);
    }

    public void Action(GameObject scanObj, string talkObjName)
    {
        /*
        if(isAction) {      // Exit action
            isAction = false;
        }
        else
        {       // Enter action
            isAction = true;
            talkPanel.SetActive(true);
            scanObject = scanObj;
            //talkText.text = "�̰��� �̸��� " + scanObject.name + "�̶�� �Ѵ�.";

            ObjData objData = scanObject.GetComponent<ObjData>();
            Talk(objData.id, objData.inNpc);
        }
        */

        scanObject = scanObj;
        TalkObjectName.text = talkObjName;
        ObjData objData = scanObject.GetComponent<ObjData>();
        Talk(objData.id, objData.isNpc);

        // Talk(objData.id, objData.isNpc);���� ������ isAction���� true, false �Է�
        //talkPanel.SetActive(isAction);
        talkPanel.SetBool("isShow", isAction);
    }

    void Talk(int id, bool isNpc)
    {
        // Set talk data
        int questTalkIndex = 0;
        string talkData = "";

        if (talk.isAnim)
        {
            talk.SetMsg("");
            return;
        }
        else
        {
            questTalkIndex = questManager.GetQuestTalkIndex(id);
            talkData = talkManager.GetTalk(id + questTalkIndex, talkIndex);
        }

        // End talk
        if (talkData == null)
        {
            isAction = false;
            talkIndex = 0;
            questTalk.text = questManager.CheckQuest(id);
            //Debug.Log(questManager.CheckQuest(id));
            return;     // void �Լ������� return �ڿ� �ƹ� �͵� �� ���� return ���ָ� ��.
        }

        // Continue talk
        if (isNpc)
        {
            talk.SetMsg(talkData.Split(':')[0]);

            // Show portrait
            portraitImg.sprite = talkManager.GetPortrait(id, int.Parse(talkData.Split(':')[1]));        // int.Parse : ���ڿ� Ÿ���� int Ÿ������ ����ȯ
            portraitImg.color = new Color(1, 1, 1, 1);      // 1,1,1,1�� 4��° �� : ���İ�(����)
            // Animation portrait
            if (portraitImg != previousPortrait)
            {
                portraitAnim.SetTrigger("doEffect");
                previousPortrait = portraitImg.sprite;
            }
        }
        else
        {
            talk.SetMsg(talkData);

            portraitImg.color = new Color(1, 1, 1, 0);      // NPC�� ���� Image�� ���̵��� ��
        }

        isAction = true;
        talkIndex++;

    }

    public void GameSave()
    {
        // ������Ʈ���� Player�� x, y positin, QuestId, QuestActionIndex�� ������ ��Ī���� �����Ѵ�.
        PlayerPrefs.SetFloat("PlayerX", player.transform.position.x);
        PlayerPrefs.SetFloat("PlayerY", player.transform.position.y);
        PlayerPrefs.SetInt("QuestId", questManager.questId);
        PlayerPrefs.SetInt("QuestActionIndex", questManager.questActionIndex);
        PlayerPrefs.Save();

        menuSet.SetActive(false);
    }

    public void GameLoad()
    {
        if (!PlayerPrefs.HasKey("PlayerX"))
        {
            return;
        }
        float x = PlayerPrefs.GetFloat("PlayerX");
        float y = PlayerPrefs.GetFloat("PlayerY");
        int questId = PlayerPrefs.GetInt("QuestId");
        int QuestActionIndex = PlayerPrefs.GetInt("QuestActionIndex");

        player.transform.position = new Vector3(x, y, 0);
        questManager.questId = questId;
        questManager.questActionIndex = QuestActionIndex;
        questManager.ControlObject();
    }

    public void GameExit()
    {
        //DeletePlayerPrefs();
        Application.Quit();
    }

    static void DeletePlayerPrefs()     // ����Ƽ �������� ������ ���� �̿�
    {
        PlayerPrefs.DeleteAll();
        Debug.Log("All PlayerPrefs deleted");
    }

}
